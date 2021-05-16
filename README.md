# ft_linear_regression
21 School project about linear regression
# About the project
The goal of the project is to introduce students to linear regression. In this project we have to files: `train.py` and `predict.py`.
The task is to get coefficients of linear function by training on `data.csv`. In `data.csv` we have car's prices and mileage. When the model is trained, we should to test it, and make a prediction by runnint `predict.py`.
## Installing dependecies and running virtual envirnment
To install all dependecies
```
>./start.sh
```
To activate virtual envirnment
```
>source .venv/bin/activate
```
## Set configurations
To set train configurations configure `configurations/train_configurations.json`
To set pridict configurations configure `configurations/predict_configurations.json`
## Train model
To start train use
```
>./train.py
```
* Results

![results](https://github.com/Bazarovinc/ft_linear_regression/blob/master/imagies/lr_train.png)

* Error dependens

![error](https://github.com/Bazarovinc/ft_linear_regression/blob/master/imagies/errors.png)

* Determination dependens

![determination](https://github.com/Bazarovinc/ft_linear_regression/blob/master/imagies/determination.png)

## Predict
To predict price run
```
>./predict.py <km>
```
where km is an integer
* Results

![results_predict](https://github.com/Bazarovinc/ft_linear_regression/blob/master/imagies/lr_predict.png)

## Statistics
The reason why I set learning rate 0.9 you cat see on the next imagies
```
>./statistics.py
```
![zeros](https://github.com/Bazarovinc/ft_linear_regression/blob/master/imagies/stat_zeros.png)
![random](https://github.com/Bazarovinc/ft_linear_regression/blob/master/imagies/stat_random.png)
