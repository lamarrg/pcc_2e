# When you roll two dice, you usually add the two numbers together to get the result. Create a visualization that shows what happens if you multiply these numbers instead.

from plotly.graph_objs import Bar, Layout
from plotly import offline
from die import Die


# Create a D6 and D10
die_1 = Die()
die_2 = Die()

# make some rolls, and store results in a list
# results = []
# for roll_num in range(50000):
#     result = die_1.roll() * die_2.roll()
#     results.append(result)
results = [die_1.roll() * die_2.roll() for x in range(50000)]

# analyze the results
# frequencies = []
max_result = die_1.num_sides * die_2.num_sides
# for value in range(1, max_result + 1):
#     frequency = results.count(value)
#     frequencies.append(frequency)
frequencies = [results.count(x) for x in range(1, max_result+1)]

print(frequencies)

# visialize the results
x_values = list(range(1, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of multipying two D6', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d8_d8.html')



