import pandas as pd
import random 
import plotly.figure_factory as ff 
import plotly.graph_objects as go 
import statistics as stats

lists =pd.read_csv('medium_data.csv')

population = lists['reading_time'].to_list()
population_mean = stats.mean(population)

def random_set_of_mean(UL) : 
    dataset = []
    for i in range(0,UL) : 
        random_index = random.randint(0,len(population)-1)
        value = population[random_index]
        dataset.append(value)

    mean = stats.mean(dataset)
    return mean

mean_list = []
for i in range(0,100) : 
    set_of_means = random_set_of_mean(30)
    mean_list.append(set_of_means)

sample_mean_value = stats.mean(mean_list)
std = stats.stdev(mean_list)

st_dev_first_start , st_dev_first_end = sample_mean_value - std , sample_mean_value + std
st_dev_second_start , st_dev_second_end = sample_mean_value - (std * 2) , sample_mean_value + (std * 2)
st_dev_third_start , st_dev_third_end = sample_mean_value - (std * 3) , sample_mean_value + (std * 3)

fig = ff.create_distplot([mean_list] , ["Population"] , show_hist = False)

fig.add_trace(go.Scatter(x = [population_mean , population_mean] , y = [0,0.85] , mode = 'lines' , name = 'Real Mean of the data'))
fig.add_trace(go.Scatter( x = [sample_mean_value , sample_mean_value] , y = [0,0.85] , mode = 'lines' , name = 'Sample Mean of the data'))
fig.add_trace(go.Scatter( x = [st_dev_first_start , st_dev_first_start] , y = [0,0.85] , mode = 'lines' , name = 'Std 1 start'))
fig.add_trace(go.Scatter( x = [st_dev_first_end , st_dev_first_end] , y = [0,0.85] , mode = 'lines' , name = 'Std 1 end'))
fig.add_trace(go.Scatter( x = [st_dev_second_start , st_dev_second_start] , y = [0,0.85] , mode = 'lines' , name = 'Std 2 start'))
fig.add_trace(go.Scatter( x = [st_dev_second_end , st_dev_second_end] , y = [0,0.85] , mode = 'lines' , name = 'Std 2 end'))
fig.add_trace(go.Scatter( x = [st_dev_third_start , st_dev_third_start] , y = [0,0.85] , mode = 'lines' , name = 'Std 3 start'))
fig.add_trace(go.Scatter( x = [st_dev_third_end , st_dev_third_end] , y = [0,0.85] , mode = 'lines' , name = 'Std 3 end '))

fig.show()

print('')
print('The actual mean of the population is :- {}'.format(population_mean))
print('The sampling mean of the population is :- {}'.format(sample_mean_value))
print('')
print('STD 1 :- Start : {} , End :- {}'.format(st_dev_first_start , st_dev_first_end))
print('STD 2 :- Start : {} , End :- {}'.format(st_dev_second_start , st_dev_second_end))
print('STD 3 :- Start : {} , End :- {}'.format(st_dev_third_start , st_dev_third_end))
print('')

if (population_mean > sample_mean_value) : 
    print('Intervention of the project is successful')
else : 
    print('Intervention of the project is not successful')
    
z_score = (sample_mean_value-population_mean)/std
print('')
print('Z-Score :- {}'.format(z_score))
print('')
