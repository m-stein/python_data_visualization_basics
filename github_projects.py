import requests
import json
import io
import plotly.express as px

export_response = False


def request(url, headers):
    with requests.get(url=url, headers=headers) as response:
        result = response.json()

    if response.status_code != 200:
        print('Error: API request failed')
        exit(-1)

    return result


rate_limit_response = request('https://api.github.com/rate_limit', {})
print(f'Rate limit: {rate_limit_response['resources']['core']['remaining']}/'
      f'{rate_limit_response['resources']['core']['limit']}')

repos_response = request(
    'https://api.github.com/search/repositories?q=language:python+sort:stars+stars:>10000',
    {'Accept': 'application/vnd.github.v3+json'})

if export_response:
    with io.open('github_projects_response.json', mode='w+') as file:
        file.write(json.dumps(repos_response, indent=3))

repos = repos_response['items']
print(f'Results complete: {not repos_response['incomplete_results']}')
print(f'Total count: {repos_response['total_count']}')
print(f'Number of repos returned: {len(repos)}')

for repo in repos[:3]:
    print(f'\nName: {repo['name']}')
    print(f'Owner: {repo['owner']['login']}')
    print(f'Stars: {repo['stargazers_count']}')
    print(f'Description: {repo['description']}')

repo_links, stars, hover_names = [], [], []
for repo in repos:
    repo_links.append(f'<a href="{repo['html_url']}">{repo['full_name']}</a>')
    stars.append(repo['stargazers_count'])
    hover_names.append(f'{repo['description']}')

fig = px.bar(x=repo_links, y=stars, title='Most-Starred Python Projects on GitHub',
             labels={'x': 'Repository', 'y': 'Stars'}, hover_name=hover_names)

# You can use any CSS color name in marker_color.
# See https://plotly.com/python/plotly-express and https://plotly.com/python/styling-plotly-express for more info
# on Plotly Express!
fig.update_traces(marker_color='SteelBlue', marker_opacity=0.6)
fig.show()
