import requests
from plotly.graph_objs import Bar
from plotly import offline

#Создаем вызова API и сохранение ответа 
ur1 = 'https://api.github.com/search/repositories?q=language:kotlin&sort=stars'
headers = {'Accept': 'application/vnd.github.v5+json'}
r = requests.get(ur1, headers = headers)
print(f"Status code: {r.status_code}")

#Обработка результатов
response_dict = r.json()
repo_dicts = response_dict['items']
print(f"Total repositories: {response_dict['total_count']}")
repo_names, stars = [], []
for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

#Построение визуализации
data = [{
    'type': 'bar',
    'x': repo_names,
    'y': stars,
}]

my_layout = {
    'title': 'Most-Starred Kotlin Project on GitHub',
    'xaxis': {'title': 'Repository'},
    'yaxis': {'title': 'Stars'},
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename = 'kotlin_repos.html')