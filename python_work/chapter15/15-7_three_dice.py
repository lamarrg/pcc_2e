# When you roll three D6 dice, the smallest number you can roll is 3 and the largest number is 18. Create a visualization that shows what hap- pens when you roll three D6 dice.

from plotly.graph_objs import Bar, Layout
from plotly import offline
from die import Die


# Create a D6 and D10
die_1 = Die()
die_2 = Die()
die_3 = Die()

# make some rolls, and store results in a list
results = []
for roll_num in range(50000):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)

# analyze the results
frequencies = []
max_result = die_1.num_sides + die_2.num_sides +die_3.num_sides
for value in range(3, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)

# visialize the results
x_values = list(range(3, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling three D6', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d8_d8.html')




