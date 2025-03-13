import pandas as pd
print('The pandas version is:', pd.__version__)

mydataset = {
    'cars': ["BMW", "Volvo", "Ford"],
    'passing': [2, 4, 5]
}

varOne = (pd.DataFrame(mydataset))

#pandas series
a = [1, 2, 4]

varTwo = pd.Series(a)

print(varTwo)
print(varOne)