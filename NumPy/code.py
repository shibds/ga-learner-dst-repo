# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)

#Code starts here

# print(data.shape)
record = np.asarray(new_record)
census = np.concatenate((data, record), axis = 0)
# print(census.shape)

# age = census[:,0]
# print(age)

# max_age = np.max(age)
# min_age = np.min(age)
# age_mean = np.mean(age)
# age_std = np.std(age)
# print(max_age, min_age, age_mean, age_std)

race_0 = census[census[:,2] == 0][:,2]
race_1 = census[census[:,2] == 1][:,2]
race_2 = census[census[:,2] == 2][:,2]
race_3 = census[census[:,2] == 3][:,2]
race_4 = census[census[:,2] == 4][:,2]

len_0 = np.size(race_0)
len_1 = np.size(race_1)
len_2 = np.size(race_2)
len_3 = np.size(race_3)
len_4 = np.size(race_4)

print(len_0, len_1, len_2, len_3, len_4)
minority_race = len_3

senior_citizens = census[census[:,0] > 60][:,6]
working_hours_sum = np.sum(senior_citizens)

senior_citizens_len = np.size(senior_citizens)


avg_working_hours = round(working_hours_sum/senior_citizens_len,2)
print(working_hours_sum)
print(avg_working_hours)


high = census[census[:,1]>10][:,7]
low = census[census[:,1]<=10][:,7]

avg_pay_high = round(np.mean(high),2)
avg_pay_low = round(np.mean(low),2)

print(avg_pay_high, avg_pay_low)



