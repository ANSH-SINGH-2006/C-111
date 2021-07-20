import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd

student_marks=pd.read_csv("data.csv")
data=student_marks["Math_score"].to_list()

fig=ff.create_distplot([data], ["Math Scores"], show_hist=False)
fig.show()

mean=statistics.mean(data)
std_dev=statistics.stdev(data)

def random_set_of_mean(counter):
    dataset=[]
    for i in range(0, counter):
        random_index=random.randint(0, len(data)-1)
        value= data[random_index]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean

mean_list=[]
for i in range(0, 1000):
    set_of_means=random_set_of_mean(100)
    mean_list.append(set_of_means)

std_dev=statistics.stdev(mean_list)
first_std_dev_start, first_std_dev_end= mean-std_dev, mean+std_dev
two_std_dev_start, two_std_dev_end= mean-(2*std_dev), mean+(2*std_dev)
third_std_dev_start, third_std_dev_end= mean-(3*std_dev), mean+(3*std_dev)

#finding the mean of the first data()students who got tabs and plotting the graph

df=pd.read_csv("data1.csv")
data=df["Math_score"].tolist()
mean_of_sample1= statistics.mean(data)
print("Mean of sample1: ", mean_of_sample1)

fig=ff.create_distplot([mean_list], ["Student Marks"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="Mean"))
fig.add_trace(go.Scatter(x=[mean_of_sample1, mean_of_sample1], y=[0, 0.17], mode="lines", name="Mean of sample"))
fig.add_trace(go.Scatter(x=[first_std_dev_end, first_std_dev_end], y=[0, 0.17], mode="lines", name="first_std_dev_end"))
fig.add_trace(go.Scatter(x=[two_std_dev_end, two_std_dev_end], y=[0, 0.17], mode="lines", name="two_std_dev_end"))
fig.add_trace(go.Scatter(x=[third_std_dev_end, third_std_dev_end], y=[0, 0.17], mode="lines", name="third_std_dev_end"))

fig.show()

#finding the mean of the first data()students who got extra classes and plotting the graph

df=pd.read_csv("data2.csv")
data=df["Math_score"].tolist()
mean_of_sample2= statistics.mean(data)
print("Mean of sample2: ", mean_of_sample2)

fig=ff.create_distplot([mean_list], ["Student Marks"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="Mean"))
fig.add_trace(go.Scatter(x=[mean_of_sample2, mean_of_sample2], y=[0, 0.17], mode="lines", name="Mean of sample2"))
fig.add_trace(go.Scatter(x=[first_std_dev_end, first_std_dev_end], y=[0, 0.17], mode="lines", name="first_std_dev_end"))
fig.add_trace(go.Scatter(x=[two_std_dev_end, two_std_dev_end], y=[0, 0.17], mode="lines", name="two_std_dev_end"))
fig.add_trace(go.Scatter(x=[third_std_dev_end, third_std_dev_end], y=[0, 0.17], mode="lines", name="third_std_dev_end"))

fig.show()

#finding the mean of the first data()students who got tabs and plotting the graph

df=pd.read_csv("data3.csv")
data=df["Math_score"].tolist()
mean_of_sample3= statistics.mean(data)
print("Mean of sample3: ", mean_of_sample3)

fig=ff.create_distplot([mean_list], ["Student Marks"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="Mean"))
fig.add_trace(go.Scatter(x=[mean_of_sample3, mean_of_sample3], y=[0, 0.17], mode="lines", name="Mean of sample3"))
fig.add_trace(go.Scatter(x=[first_std_dev_end, first_std_dev_end], y=[0, 0.17], mode="lines", name="first_std_dev_end"))
fig.add_trace(go.Scatter(x=[two_std_dev_end, two_std_dev_end], y=[0, 0.17], mode="lines", name="two_std_dev_end"))
fig.add_trace(go.Scatter(x=[third_std_dev_end, third_std_dev_end], y=[0, 0.17], mode="lines", name="third_std_dev_end"))

fig.show()

z_score1= (mean-mean_of_sample1)/std_dev
print(z_score1)

z_score2= (mean-mean_of_sample2)/std_dev
print(z_score2)

z_score3= (mean-mean_of_sample3)/std_dev
print(z_score3)