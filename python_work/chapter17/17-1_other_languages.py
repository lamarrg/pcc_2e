# Modify the API call in python_repos.py so it generates a chart showing the most popular projects in other languages. Try languages such as JavaScript, Ruby, C, Java, Perl, Haskell, and Go.

import requests

from plotly.graph_objs import Bar
from plotly import offline

# make an API call and store the response
url = 'https://api.github.com/search/repositories?q=language:go&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f'Status code: {r.status_code}')

# process results
response_dict = r.json()
repo_dicts = response_dict['items']
repo_names, stars = [], []
for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

# make visualization
data = [{
    'type': 'bar',
    'x': repo_names,
    'y': stars
}]

my_layout = {
    'title': 'Most-Starred Go Projects on Github',
    'xaxis': {'title': 'Repository'},
    'yaxis': {'title': 'Stars'}
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='go_repos.html')






