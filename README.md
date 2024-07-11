# Stochastic Submodular Data Forgetting
This repository contains the code and data of the paper Stochastic Submodular Data Forgetting.

## Requirements
```
pip install scikit-learn
pip install pandas
pip install statistics
pip install numpy
```
## Data Download
The data is hosted on Google Drive. You can download it using the following link: 
- [Download Data](https://drive.google.com/file/d/1YjCt-RZUyEHslqmA3yJHJi-Tk6SNFlbP/view?usp=sharing)

Once you download it please un-zip it and place it in the same directory as the source files.

## Usage
In order to run `LAZY-GREEDY`, `IndepDF`, and `DepDF` execute
```
python main.py [dataset_choice] [percentage_of_db] [percentage_of_ql] [budget] [n_iterations] [av_stdevs_calculation]
```
The command line arguments correspond to:
- `[dataset_choice]`: The desired dataset $D$ inside the `sample_data` folder. Select one from the list [flight, photo, wiki].
- `[percentage_of_db]`: The percentage of $D$ to use as input data. Select a number inside the continuous interval [0, 1].
- `[percentage_of_ql]`: The percentage of queries from the corresponding query-log $Q$ to use as input log. Select a number inside the continuous interval [0, 1].
- `[budget]`: The budget $B$ is the percentage of $D$ to be kept. Select a number inside the continuous interval [0,1].
- `[n_iterations]`: The number of `SCG` iterations $T$ the `DepDF` routine will perform. Select a number from the list [2000, 10000, 50000, 100000].
- `[av_stdevs_calculation]`: Whether the answer set diversity $ad(Q,D)$ is computed or not. Select `0` (False) not to perform the calculation, and `1` (True) to perform it.

An example is given in the code snippet below,
```
python main.py flight 1 0.25 0.01 2000 0
```
In this example $D$ equals the full flights dataset, $Q$ is the $25$% of the query-log, $B$ is $1$% of $|D|$, $T= 2000$, and $ad(Q,D)$ is not computed.
