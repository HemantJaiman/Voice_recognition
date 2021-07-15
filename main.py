import csv
import math
from scipy.stats import multivariate_normal
import numpy as np
import matplotlib.pyplot

male_c = 0
female_c = 0

with open('voice.csv', 'r') as person:
    data_table = list(csv.DictReader(person))

with open('voice.csv','r') as person1:
    only_data=list(csv.reader(person1))

#print(only_data[0])
male_mean = []
female_mean = []

pure_data_male = []
pure_data_female = []

for i in range(0,1500):
    pure_data_male.append(list(map(lambda arg: float(arg), only_data[85:1585][i][0:20])))
    pure_data_female.append(list(map(lambda arg: float(arg), only_data[1585:3085][i][0:20])))

male_data = np.array(pure_data_male)
female_data = np.array(pure_data_female)

male_data = male_data.T
female_data = female_data.T

male_data = list(male_data)
female_data = list(female_data)

for i in range(1,19):
    matplotlib.pyplot.scatter(male_data[0], male_data[i+1])

for i in range(0,19):
    male_mean.append(np.mean(male_data[0:1500][i]))
    female_mean.append(np.mean(female_data[0:1500][i]))

male_mean = np.array(male_mean)
female_mean = np.array(female_mean)

male_cov = np.array(np.cov(male_data[0:19]))
female_cov = np.array(np.cov(female_data[0:19]))

testing_data=[]

for i in range(1,85):
    testing_data.append(only_data[i])
for i in range(3085,3169):
    testing_data.append(only_data[i])

acc=0

pure_testing_data = []
for person in testing_data:
    pure_testing_data.append(list(map(lambda arg: float(arg), person[0:20])))

for person in pure_testing_data:

    prob_male = multivariate_normal.pdf(np.array(person).T, male_mean, male_cov)
    prob_female = multivariate_normal.pdf(np.array(person).T, female_mean, female_cov)

    if prob_male>prob_female and person[20] == 'male':
        acc=acc+1

    elif prob_female>prob_male and person[20] == 'female':
        acc=acc+1

print("program accuracy is " +str((acc/168)*100) + " percent")
