# Create a simulation showing what happens when you roll two eight-sided dice 1000 times. Try to picture what you think the visualization will look like before you run the simulation; then see if your intuition was correct. Gradually increase the number of rolls until you start to see the limits of your system’s capabilities.

from plotly.graph_objs import Bar, Layout
from plotly import offline
from die import Die


# Create a D6 and D10
die_1 = Die(8)
die_2 = Die(8)

# make some rolls, and store results in a list
results = []
for roll_num in range(500_000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# analyze the results
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)

# visialize the results
x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling two D8', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d8_d8.html')



