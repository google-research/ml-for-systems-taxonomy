# ML for Systems Bibliography

This file contains a formatted version of the ML for Systems
bibliography associated with the article "A Taxonomy of ML for Systems Problems"
in IEEE Micro. For the full annotated bibliography in bibtex format, see
`bibliography.bib`. To cite, please use:

```
@article{maas2020_ml_taxonomy,
  author={Martin Maas},
  journal={IEEE Micro},
  title={A Taxonomy of ML for Systems Problems},
  year={2020},
  number={3},
}
```

## Language Runtime Systems

### Memory Management

* **Learning-Based Memory Allocation for C++ Server Workloads**, Maas, Martin and Andersen, David G. and Isard, Michael and Javanmard, Mohammad Mahdi and McKinley, Kathryn S. and Raffel, Colin, *Proceedings of the Twenty-Fifth International Conference on Architectural Support for Programming Languages and Operating Systems*

  * Taxonomy Category: Extrapolation, Forecasting

  * ML Strategies: Supervised learning, LSTMs

## Computer Systems

### Scheduling

* **Paragon: QoS-Aware Scheduling for Heterogeneous Datacenters**, Delimitrou, Christina and Kozyrakis, Christos, *Proceedings of the Eighteenth International Conference on Architectural Support for Programming Languages and Operating Systems*

  * Taxonomy Category: Extrapolation

  * ML Strategies: Collaborative Filtering

* **Quasar: Resource-Efficient and QoS-Aware Cluster Management**, Delimitrou, Christina and Kozyrakis, Christos, *Proceedings of the 19th International Conference on Architectural Support for Programming Languages and Operating Systems*

  * Taxonomy Category: Extrapolation

  * ML Strategies: Collaborative Filtering

* **Learning Scheduling Algorithms for Data Processing Clusters**, Mao, Hongzi and Schwarzkopf, Malte and Venkatakrishnan, Shaileshh Bojja and Meng, Zili and Alizadeh, Mohammad, *Proceedings of the ACM Special Interest Group on Data Communication*

  * Taxonomy Category: Discovery

  * ML Strategies: Reinforcement Learning

* **Device Placement Optimization with Reinforcement Learning**, Mirhoseini, Azalia and Pham, Hieu and Le, Quoc V. and Steiner, Benoit and Larsen, Rasmus and Zhou, Yuefeng and Kumar, Naveen and Norouzi, Mohammad and Bengio, Samy and Dean, Jeff, *Proceedings of the 34th International Conference on Machine Learning - Volume 70*

  * Taxonomy Category: Optimization

  * ML Strategies: Reinforcement Learning, LSTMs

### Distributed Systems

* **Seer: Leveraging Big Data to Navigate the Complexity of Performance Debugging in Cloud Microservices**, Gan, Yu and Zhang, Yanqi and Hu, Kelvin and Cheng, Dailun and He, Yuan and Pancholi, Meghna and Delimitrou, Christina, *Proceedings of the Twenty-Fourth International Conference on Architectural Support for Programming Languages and Operating Systems*

  * Taxonomy Category: Anomaly Detection

  * ML Strategies: Supervised learning, LSTMS

### Storage Systems

* **Learning Relaxed Belady for Content Distribution Network Caching**, Zhenyu Song and Daniel S. Berger and Kai Li and Wyatt Lloyd, *17th {USENIX} Symposium on Networked Systems Design and Implementation ({NSDI} 20)*

  * Taxonomy Category: Discovery

  * ML Strategies: Imitation Learning

* **Multi-Task Learning for Storage Systems**, Giulio Zhou and Martin Maas, *Workshop on ML for Systems at NeurIPS 2019*

  * Taxonomy Category: Extrapolation

  * ML Strategies: Supervised learning, Transformers, Multi-Task Learning

## Computer Architecture

### Speculation

* **Learning Memory Access Patterns**, Hashemi, Milad and Swersky, Kevin and Smith, Jamie and Ayers, Grant and Litz, Heiner and Chang, Jichuan and Kozyrakis, Christos and Ranganathan, Parthasarathy, *Proceedings of the 35th International Conference on Machine Learning*

  * Taxonomy Category: Forecasting

  * ML Strategies: Supervised Learning, LSTMs, Clustering

* **Dynamic branch prediction with perceptrons**, Jimenez, Daniel A. and Lin, Calvin, *Proceedings HPCA Seventh International Symposium on High-Performance Computer Architecture*

  * Taxonomy Category: Forecasting

  * ML Strategies: Supervised Learning, Perceptrons

### Performance Counters

* **A Zero-Positive Learning Approach for Diagnosing Software Performance Regressions**, Alam, Mejbah and Gottschlich, Justin and Tatbul, Nesime and Turek, Javier S and Mattson, Tim and Muzahid, Abdullah, *Advances in Neural Information Processing Systems 32*

  * Taxonomy Category: Anomaly Detection

  * ML Strategies: Autoencoders

### Hardware Design

* **Chip Placement with Deep Reinforcement Learning**, Azalia Mirhoseini and Anna Goldie and Mustafa Yazgan and Joe Jiang and Ebrahim Songhori and Shen Wang and Young-Joon Lee and Eric Johnson and Omkar Pathak and Sungmin Bae and Azade Nazi and Jiwoo Pak and Andy Tong and Kavya Srinivasa and William Hang and Emre Tuncer and Anand Babu and Quoc V. Le and James Laudon and Richard Ho and Roger Carpenter and Jeff Dean, *arXiv:2004.10746*

  * Taxonomy Category: Optimization

  * ML Strategies: Reinforcement Learning

## Compilers

### Optimizations

* **Learning to Optimize Tensor Programs**, Chen, Tianqi and Zheng, Lianmin and Yan, Eddie and Jiang, Ziheng and Moreau, Thierry and Ceze, Luis and Guestrin, Carlos and Krishnamurthy, Arvind, *Advances in Neural Information Processing Systems 31*

  * Taxonomy Category: Optimization

  * ML Strategies: Supervised Learning, Transfer Learning, Gradient Boosted Trees, TreeGRU

* **Compiler Auto-Vectorization with Imitation Learning**, Mendis, Charith and Yang, Cambridge and Pu, Yewen and Amarasinghe, Dr.Saman and Carbin, Michael, *Advances in Neural Information Processing Systems 32*

  * Taxonomy Category: Discovery, Optimization

  * ML Strategies: Imitation Learning, Graph Neural Networks

### Performance Models

* **A Learned Performance Model for the Tensor Processing Unit**, Samuel J. Kaufman and Phitchaya Mangpo Phothilimthana and Yanqi Zhou and Mike Burrows, *arXiv:2008.01040*

  * Taxonomy Category: Extrapolation, Forecasting

  * ML Strategies: Supervised Learning, Graph Neural Networks

* **Ithemal: Accurate, Portable and Fast Basic Block Throughput Estimation using Deep Neural Networks**, Mendis, Charith and Renda, Alex and Amarasinghe, Saman and Carbin, Michael, *ICML*

  * Taxonomy Category: Extrapolation, Forecasting

  * ML Strategies: Supervised Learning, LSTMs

