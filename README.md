<div align="center">

# 📊 DATA SCIENCE & NUMERICAL COMPUTING LAB 🐍

***A Comprehensive Hands-on Exploration of Python Fundamentals, Vectorized Computing with NumPy, and Data Analysis with Pandas***

[![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org/)
[![NumPy](https://img.shields.io/badge/NumPy-Vectorized_Computing-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data_Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

[💻 **GitHub Profile**](https://github.com/rohanmendon26-byte) • [💼 **LinkedIn**](https://www.linkedin.com/in/rohanmendon/) • [📧 **Contact**](mailto:rohanmendon26@gmail.com)

---

</div>

## 📑 Table of Contents

- [🌌 Overview](#-overview)
- [🧠 Curriculum Structure](#-curriculum-structure)
  - [🐍 Python Fundamentals](#-1-pythonintro--core-python-fundamentals)
  - [🔢 NumPy Numerical Computing](#-2-numpy--high-performance-vectorized-computing)
  - [🐼 Pandas Data Analysis](#-3-pandas--data-structures--ingestion)
- [⚡ Performance Benchmarks](#-performance-benchmarks)
- [💻 Getting Started](#-getting-started)
- [🛣️ Roadmap & Future Modules](#️-roadmap--future-modules)
- [📜 License](#-license)

---

## 🌌 Overview

Welcome to the **Data Science & Numerical Computing Lab** repository created by **Rohan Mendon**. This repository serves as a structured, code-first learning environment for mastering fundamental Python programming, high-performance vectorized computations using NumPy, and data manipulation workflows with Pandas.

Each module contains self-contained interactive Jupyter Notebooks (`.ipynb`) with real code executions, output analyses, memory profiling, and performance benchmarks.

---

## 🧠 Curriculum Structure

```plaintext
Data Science/
├── 📁 Python(Intro)/           # Core Python Language Fundamentals (12 Notebooks)
├── 📁 numpy/                   # High-Performance Vectorized Array Computing (4 Notebooks)
├── 📁 Pandas/                  # Tabular Data Ingestion & DataFrames (1 Notebook + Datasets)
├── 📄 data.json                # Sample JSON datasets
└── 📄 README.md                # Repository documentation
```

---

### 🐍 1. `Python(Intro)` — Core Python Fundamentals

<details>
<summary><b>View Python Notebooks (12 Files)</b></summary>

| Notebook | Focus Area / Key Concepts |
| :--- | :--- |
| `01_python_basics.ipynb` | Syntax fundamentals, dynamic variables, and `print()` operations |
| `02_strings.ipynb` | String immutability, formatting methods, and slicing |
| `03_operator.ipynb` | Arithmetic, logical, bitwise, assignment, and comparison operators |
| `04_input.ipynb` | Handling dynamic user inputs and explicit type casting |
| `05_Operatorprecedence.ipynb` | Operator evaluation order and complex expressions |
| `06_if_else.ipynb` | Decision-making structures, logical branching, and nested conditions |
| `12_sets.ipynb` | Set operations, uniqueness guarantees, unions, and intersections |
| `13_dictionary.ipynb` | Hash maps, key-value manipulations, and nested data access |
| `14_file.ipynb` | File stream I/O (`open()`, `read()`, `write()`, `close()`) |
| `15_json.ipynb` | Parsing and serializing JSON (`json.loads()`, `json.dumps()`) |
| `16_oops.ipynb` | Object-Oriented Programming (Classes, instances, methods) |
| `17_listcomprehension.ipynb` | Pythonic list comprehensions, conditional filtering, and mapping |

</details>

---

### 🔢 2. `numpy` — High-Performance Vectorized Computing

<details>
<summary><b>View NumPy Notebooks (4 Files)</b></summary>

| Notebook | Focus Area / Key Concepts |
| :--- | :--- |
| `whyusenumpy.ipynb` | **Benchmarking Python Lists vs NumPy Arrays**: Memory consumption & execution speed |
| `creatingnumpyarray.ipynb` | Array initialization (`np.array`, `np.zeros`, `np.ones`, `np.arange`) |
| `indexingandslicing.ipynb` | Sub-array extraction, 1D/2D slicing, and strided views |
| `Multidimensional Indexing and Axis.ipynb` | Multi-axis matrix operations (`axis=0`, `axis=1`) and multi-D array manipulation |

</details>

---

### 🐼 3. `Pandas` — Data Structures & Ingestion

<details>
<summary><b>View Pandas Module Details</b></summary>

* 📖 **`Core Data Structures in Pandas.ipynb`**:
  * **Core Data Structures**: `pd.Series` (1D labeled arrays) & `pd.DataFrame` (2D labeled data structures).
  * **Multi-Source Data Ingestion**:
    * CSV Ingestion (`pd.read_csv("data.csv")`)
    * Excel Processing (`pd.read_excel("data.xlsx")`)
    * JSON Data Import (`pd.read_json("data.json")`)
    * Remote HTTP Stream Ingestion (`pd.read_csv("https://raw.githubusercontent.com/.../tips.csv")`)
  * **Data Inspection**: `.head()`, `.tail()`, `.info()`, index customization, and column renaming.

</details>

---

## ⚡ Performance Benchmarks

In `numpy/whyusenumpy.ipynb`, empirical tests highlight the computational efficiency of NumPy over standard Python structures:

| Metric (1,000,000 Elements) | Standard Python List | NumPy `ndarray` | Performance Gain |
| :--- | :--- | :--- | :--- |
| ⏱️ **Vector Addition Execution** | `~0.144 seconds` | `~0.00016 seconds` | ⚡ **~850x Faster** |
| 🧠 **Memory Allocation** | `~8,056,000 bytes` | `~8,000 bytes` | 📦 **~1000x More Compact** |

---

## 💻 Getting Started

### Prerequisites

* **Python 3.10+** installed
* **Jupyter Notebook / JupyterLab** or **VS Code Jupyter Extension**

### Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/rohanmendon26-byte/Data-Science.git
   cd Data-Science
   ```

2. **Create a virtual environment (optional but recommended)**:
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install required dependencies**:
   ```bash
   pip install numpy pandas jupyter openpyxl
   ```

4. **Launch Jupyter Notebook**:
   ```bash
   jupyter notebook
   ```

---

## 🛣️ Roadmap & Future Modules

- [x] **Python Core Basics**: Fundamentals, Control Flow, Collections, and File I/O
- [x] **Vectorized Computing**: Multi-axis NumPy arrays and benchmark analysis
- [x] **Data Ingestion**: Multi-format Pandas DataFrames and remote HTTP streams
- [ ] **Data Cleaning & Wrangling**: Handling missing values, duplicates, and `groupby` aggregations
- [ ] **Data Visualization**: Matplotlib and Seaborn interactive plots
- [ ] **Machine Learning Basics**: Scikit-Learn pipelines, regression, and classification models

---

## 📜 License

This repository is licensed under the [MIT License](LICENSE).

<div align="center">

*Maintained with ❤️ by **Rohan Mendon***

</div>
