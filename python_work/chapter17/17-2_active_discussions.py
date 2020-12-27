# Using the data from hn_submissions.py, make a bar chart showing the most active discussions currently happening on Hacker News. The height of each bar should correspond to the number of comments each submission has. The label for each bar should include the submission’s title and should act as a link to the discussion page for that submission.

# changing discussions to watchers... after looking at json, did not see an entry for how many discussions are active

import requests
import json

from plotly.graph_objs import Bar
from plotly import offline

# make an API call and store the response
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f'Status code: {r.status_code}')

# process results
response_dict = r.json()
repo_dicts = response_dict['items']
repo_links, watchers, labels = [], [], []
count = 0
grr = json.dumps(repo_dicts[12], indent=4)
print(grr)



for repo_dict in repo_dicts:
    if count > 20:
        break
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)

    watchers.append(repo_dict['watchers'])

    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    label = f"{owner}<br>{description}"
    labels.append(label)
    count += 1

# make visualization
data = [{
    'type': 'bar',
    'x': repo_links,
    'y': watchers,
    'hovertext': labels,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.6
}]

my_layout = {
    'title': 'Most-Watched Python Projects on Github',
    'titlefont': {'size': 28},
    'xaxis': {
        'title': 'Repository',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14}
        },
    'yaxis': {
        'title': 'Watchers',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14}
    }
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_watchers.html')




