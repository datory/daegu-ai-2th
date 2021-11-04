# pow() 는 내장함수이고 = built-in functions
# math, random 같은 것들은 내장 모듈이다 = library
# 둘다 파이썬이 설치될때 포함되서 설치되는 것이다.

# pypi.org 에 가면 The Python Package Index (PyPI) is a repository of software for the Python programming language. 가 있고 판다스 또한 존재한다.

# Top 10 Python Libraries:
# TensorFlow.
# Scikit-Learn.
# Numpy.
# Keras.
# PyTorch.
# LightGBM.
# Eli5.
# SciPy.


import pandas
house = pandas.read_csv('https://gist.githubusercontent.com/egoing/65a3ab6f5decef22d3ef49dcdcc9b33e/raw/eca4ed834144351aa238f00efc07a50e69171d93/boston_house_prices_dataset.csv')

print(house)
print(house.head(2))
print(house.describe())