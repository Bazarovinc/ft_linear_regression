# ft_linear_regression
21 School project about linear regression
## start
To install all dependecies
```
>./start.sh
>.venv/bin/activate
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
