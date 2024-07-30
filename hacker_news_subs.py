from operator import itemgetter
from util import request_json


class SubmissionDownloader:
    def __init__(self, max_num_subs):
        self.max_num_subs = max_num_subs

    def fetch(self):
        sub_ids = request_json('https://hacker-news.firebaseio.com/v0/topstories.json', {})
        subs = []
        while sub_ids and len(subs) < self.max_num_subs:
            sub = request_json(f'https://hacker-news.firebaseio.com/v0/item/{sub_ids.pop(0)}.json', {})
            # Skip promotional subs that don't allow for comments
            if 'descendants' in sub.keys():
                subs.append({'title': sub['title'],
                             'num_comments': sub['descendants'],
                             'url': f'https://news.ycombinator.com/item?id={sub['id']}'})
        return subs


# List subs sorted by number of comments
sub_downloader = SubmissionDownloader(3)
subs = sub_downloader.fetch()
for s in sorted(subs, key=itemgetter('num_comments'), reverse=True):
    print(f'\nTitle: {s['title']}')
    print(f'Comments: {s['num_comments']}')
    print(f'Link: {s['url']}')