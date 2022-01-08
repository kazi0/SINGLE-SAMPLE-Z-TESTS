import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv

df = pd.read_csv('medium_data.csv')
data = df['reading_time'].tolist()

def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index= random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

mean_list = []

for i in range(0,1000):
  set_of_means = random_set_of_mean(100)
  mean_list.append(set_of_means)

std_deviation = statistics.stdev(mean_list)
mean = statistics.mean(mean_list)

print("Mean of sampling distribution = ", mean)
print("Standard Deviation of sampling distribution = ", std_deviation)

fig = ff.create_distplot([data],['reading_time'],show_hist=False)
fig.show()

mean = statistics.mean(data)
stddeviation = statistics.stdev(data)

print("mean of population - ", mean)
print("standard deviation of population - ", stddeviation)

first_std_deviation_start , first_std_deviation_end = mean-stddeviation,mean+stddeviation
second_std_deviation_start,second_std_deviation_end = mean-(2*stddeviation),mean+(2*stddeviation)
third_std_deviation_start,third_std_deviation_end = mean-(3*stddeviation),mean+(3*stddeviation)

mean_of_sample1 = statistics.mean(data)
print("Mean of sample 1 = ", mean_of_sample1)

z_score = (mean_of_sample1 - mean)/std_deviation
print("The Z score is = ", z_score)

fig = ff.create_distplot([mean_list],['studentMarks'], show_hist = False)
fig.add_trace(go.Scatter(x=[mean,mean], y=[0,0.17], mode = 'lines', name = 'mean'))
fig.add_trace(go.Scatter(x=[mean_of_sample1,mean_of_sample1], y=[0,0.17], mode = 'lines', name = 'mean_of_students_who_had_extra_class'))
fig.add_trace(go.Scatter(x = [first_std_deviation_end,first_std_deviation_end], y = [0,0.17], mode = 'lines', name = 'std_deviation_1_end'))
fig.add_trace(go.Scatter(x = [second_std_deviation_end,second_std_deviation_end], y = [0,0.17], mode = 'lines', name = 'std_deviation_2_end'))
fig.add_trace(go.Scatter(x = [third_std_deviation_end,third_std_deviation_end], y = [0,0.17], mode = 'lines', name = 'std_deviation_3_end'))
fig.show()
