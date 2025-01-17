# A classification of Markoff-Fibonacci m-triples

## Description

This repository contains two files that are used in _A classification of Markoff-Fibonacci m-triples_ (2024) to computationally check some lemmas.

### check_minimal_triples.py

This program is used to check Lemma 4.5, in which we need to proof that m = 21 is the only
m-value with more than one minimal Fibonacci triple. Given the indexes of the Fibonacci
elements (a,b,c), this program checks all triples up to c=500.

To run it:
```sh
python check_minimal_triples.py
```

### markoff_fibonacci.ipynb

This Python notebook was used to provide the tables mentioned in Remark 2.2 and check Lemma 4.13.

The first section contains all functions used to determine the upper and lower bounds explained in Lemma 2.1. The second section contains the calculations used in Lemma 4.13.


## Getting Started

### Prerequisites

- Matplotlib >= 3.8
- Pandas >= 2.2
- Sympy >= 1.12

### Installation

1. Clone the repository
   ```sh
   git clone https://github.com/CIAMOD/markoff_fibonacci_m_triples
   ```
2. Install the required packages
   ```sh
   pip install -r requirements.txt
   ```

## Affiliation

This research was supported by project CIAMOD (Applications of computational methods and artificial intelligence to the study of moduli spaces, project PP2023_9) funded by Convocatoria de Financiación de Proyectos de Investigación Propios 2023, Universidad Pontificia Comillas, and by grants PID2022-142024NB-I00 and PID2019-104735RB-C42 funded by MCIN/AEI/10.13039/501100011033.

