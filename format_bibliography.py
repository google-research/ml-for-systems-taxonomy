# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Formats the bibliography as a markdown file for inclusion in the repo.

Usage: python format_bibtex.py <INPUT_FILE >OUTPUT_FILE

"""

import re
import sys

bibtex = []

entry = {}
for line in sys.stdin:
  if not line.strip():
    continue

  m = re.match(r'@\S+{(.*),$', line)
  if m:
    entry['citekey'] = m.group(1)
    continue

  if line.strip() == '}':
    bibtex.append(entry)
    entry = {}
    continue

  m = re.match(r'\s*(\S+)\s*=\s*{(.*)},?$', line)
  if m:
    entry[m.group(1)] = m.group(2)
    continue

  print('WARNING: Unknown bibtex: ' + line)

for b in bibtex:
  for kv in b['annote'].split(';'):
    e = kv.split('=')
    b[e[0]] = e[1].split(',')


def print_category(entries, level):
  """Recursively prints categories and entries."""
  categories = set([b['CATEGORY'][level] for b in entries])
  for c in categories:
    print('%s %s\n' % ('#' * (level+2), c))
    subentries = [b for b in entries if b['CATEGORY'][level] == c]
    for se in subentries:
      if len(se['CATEGORY']) > level + 1:
        print_category(subentries, level+1)
        break
      else:
        if not 'booktitle' in se:
          if 'archivePrefix' in se and 'eprint' in se:
            se['booktitle'] = '%s:%s' % (se['archivePrefix'], se['eprint'])

        print('* **%s**, %s, *%s*\n' %
              (se['title'], se['author'], se['booktitle']))
        print('  * Taxonomy Category: %s\n' % ', '.join(se['TYPE']))
        print('  * ML Strategies: %s\n' % ', '.join(se['STRATEGIES']))

print('# ML for Systems Bibliography\n')
print('''This file contains a formatted version of the ML for Systems
bibliography associated with the article "A Taxonomy of ML for Systems Problems"
in IEEE Micro. For the full annotated bibliography in bibtex format, see
`bibliography.bib`. To cite, please use:\n''')

print('```')
print('''@article{maas2020_ml_taxonomy,
  author={Martin Maas},
  journal={IEEE Micro},
  title={A Taxonomy of ML for Systems Problems},
  year={2020},
  number={3},
}''')
print('```\n')
print_category(bibtex, 0)
