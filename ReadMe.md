# FX Solver PySide2

A simple FX solver application built with PySide2. This application allows users to input two mathematical expressions
that are functions of x then solves for x where the two expressions are equal.

It also includes a feature to plot the two functions on a graph for visual comparison.

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [How to Install and Use](#how-to-install-and-use)
  - [Download](#download)
  - [Install Dependencies](#install-dependencies)
  - [Run the Application](#run-the-application)
- [Snapshots](#snapshots)
- [Demo Video](#demo-video)

## Features

- Input two mathematical expressions as functions of x.
- Solve for x where the two expressions are equal.
- Plot the two functions on a graph for visual comparison.
- User-friendly interface with error handling for invalid inputs.
- Reset functionality to clear inputs and outputs.


## Requirements

<img src="https://img.shields.io/badge/Python-3.6%20--%203.10-3776AB?style=for-the-badge&logo=python&logoColor=white" />
<br>
<img src="https://img.shields.io/badge/PySide2-Qt%20for%20Python-41CD52?style=for-the-badge&logo=qt&logoColor=white" />
<br>
<img src="https://img.shields.io/badge/Matplotlib-Visualization-11557c?style=for-the-badge&logo=plotly&logoColor=white" />
<br>
<img src="https://img.shields.io/badge/NumPy-Array%20Computing-013243?style=for-the-badge&logo=numpy&logoColor=white" />


## How to Install and Use
### Directory Structure
```
fx-solver-pyside2/
│├── assets/
│   ├── snapshots/
│   └── videos/
│├── src/
│   ├── fxsolver/
│   │ ├── parser.py
│   │ └── solver.py
│   │ 
│   ├── widgets/
│   │ ├── app.py
│   │ ├── solver_ui.py
│   │ ├── plotter_widget.py
│   │ └── input_widget.py
│   └── main.py
│├── test/
│   ├── fxsolver/
│   │ ├── parser_tests.py
│   │ └── solver_tests.py
│   └── UI/
│     └── app_test.py
│├── requirements.txt
│├── .gitignore
│├── pytest.ini
│└── ReadMe.md
└── ReadMe.md
```
### Download
Clone the repository:

```sh
git clone https://github.com/AhmedBakrXI/fx-solver-pyside2.git
cd fx-solver-pyside2
```
### Install Dependencies
Install the required dependencies using pip:

```sh
pip install -r requirements.txt
```

### Run the Application
Run the application using Python:
```sh
cd src
python main.py
```

## Snapshots

![Welcome Screen](assets/snapshots/start.png)
<div style="text-align: center; font-style: italic">
    Welcome screen showing the main interface
</div>
<br>

![Test 1 Valid](assets/snapshots/test1_valid.png)
<div style="text-align: center; font-style: italic">
    Valid input screen with two intersecting points
</div>
<br>

![Test 2 Valid](assets/snapshots/test2_valid.png)
<div style="text-align: center; font-style: italic">
    Valid input screen with one intersecting point
</div>
<br>

![Test 3 Valid](assets/snapshots/test3_valid.png)
<div style="text-align: center; font-style: italic">
    Valid input with undefined interval for solutions
</div>
<br>

![No Solution](assets/snapshots/no_solution.png)
<div style="text-align: center; font-style: italic">
    Welcome screen showing the main interface
</div>
<br>

![Test 1 Invalid](assets/snapshots/test1_invalid.png)
<div style="text-align: center; font-style: italic">
    Test invalid characters in input
</div>
<br>

![Test 2 Invalid](assets/snapshots/test2_invalid.png)
<div style="text-align: center; font-style: italic">
    Test empty input
</div>

## Demo Video
[![Demo Video](assets/snapshots/start.png)](assets/videos/Demo.mp4)

