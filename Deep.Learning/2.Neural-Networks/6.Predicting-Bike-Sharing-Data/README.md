# Predicting Bike Sharing Data

 * [Your First Neural Network](Your_first_neural_network.ipynb)

## Training the Network - Wrong Formula

| Iterations | Learning Rate | Hidden Nodes | Loss Graph | Predictions |
| ---------- | ------------- | ------------ | ---------- | ----------- |
| 100 | 0.1 | 2 | ![LG1](images/LG1.png) | ![P1](images/P1.png) |
| 500 | 0.1 | 2 | ![LG2](images/LG2.png) | ![P2](images/P2.png) |
| 100 | 0.5 | 2 | ![LG3](images/LG3.png) | ![P3](images/P3.png) |
| 100 | 0.1 | 5 | ![LG4](images/LG4.png) | ![P4](images/P4.png) |
| 500 | 0.01 | 4 | ![LG5](images/LG5.png) | ![P5](images/P5.png) |
| 400 | 0.2 | 8 | ![LG6](images/LG6.png) | ![P6](images/P6.png) |
| 400 | 0.3 | 6 | ![LG7](images/LG7.png) | ![P7](images/P7.png) |
| 500 | 0.2 | 12 | ![LG8](images/LG8.png) | ![P8](images/P8.png) |

## Training the Network - Correct Formula

| Iterations | Learning Rate | Hidden Nodes | Loss Graph | Predictions |
| ---------- | ------------- | ------------ | ---------- | ----------- |
| 100 | 0.1 | 2 | ![LG01](images/LG01.png) | ![P01](images/P01.png) |
| 500 | 0.2 | 24 | ![LG01](images/LG01.png) | ![P01](images/P01.png) |
 
 ## With Loss output.
 
 Goal is Training Loss on *0.09* and Validation Loss on *0.18*
 
| Iterations | Learning Rate | Hidden Nodes | Training Loss | Validation Loss |
| ---------- | ------------- | ------------ | ---------- | ----------- |
| 500 | 0.1 | 40 | 0.417 | 0.685 |
| 750 | 0.1 | 40 | 0.336 | 0.554 |
| 750 | 0.15 | 45 | 0.324 | 0.489 |
| 1000 | 0.15 | 45 | 0.297 | 0.464 |
| 1000 | 0.25 | 45 | 0.262 | 0.441 |
| 2000 | 0.08 | 20 | 0.324 | 0.527 |
| 20000 | 0.01 | 25 | 0.286 | 0.452 |
| 20000 | 0.1 | 25 | 0.077 | 0.171 |
| 20000 | 0.1 | 30 | 0.073 | 0.169 |
| 20000 | 0.15 | 25 | 0.066 | 0.159 |
| 15000 | 0.15 | 25 | 0.068 | 0.155 |
| 12500 | 0.15 | 25 | 0.074 | 0.173 |
| 10000 | 0.16 | 25 | 0.081 | 0.219 |
| 10000 | 0.18 | 25 | 0.085 | 0.223 |
| 10000 | 0.2 | 25 | 0.077 | 0.175 |
| 10000 | 0.23 | 25 | 0.083 | 0.232 |
| 10000 | 0.2 | 27 | 0.090 | 0.187 |
| 12000 | 0.2 | 25 | 0.058 | 0.158 |
| 11000 | 0.2 | 25 | 0.071 | 0.210 |
| 10000 | 0.21 | 25 | 0.072 | 0.152 |
| 10000 | 0.22 | 25 | 0.073 | 0.170 |
| 10000 | 0.215 | 25 | 0.073 | 0.165 |
| 10000 | 0.205 | 25 | 0.088 | 0.169 |
| 10000 | 0.212 | 25 | 0.080 | 0.190 |
| 15000 | 0.18 | 15 | 0.069 | 0.187 |
| 15000 | 0.2 | 15 | 0.057 | 0.138 |
| 13000 | 0.2 | 15 | 0.062 | 0.144 |
| 10000 | 0.2 | 15 | 0.070 | 0.169 |
| 10000 | 0.22 | 15 | 0.070 | 0.152 |
| 11000 | 0.23 | 15 | 0.067 | 0.140 |
