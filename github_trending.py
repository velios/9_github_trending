import requests
import logging
from datetime import date
from datetime import timedelta

GITHUB_API_URI='https://api.github.com'
DEFAULT_AUTH_FILE_PATH = 'auth.txt'
VERBOSITY_TO_LOGGING_LEVELS = {
    0: logging.WARNING,
    1: logging.INFO,
    2: logging.DEBUG
}


def get_offset_date(modifed_date, offset_in_days):
    return date.isoformat(modifed_date + timedelta(days=int(offset_in_days)))


def get_trending_repositories(start_search_date, number_of_results=20):
    query_search_url = '{}/search/repositories'.format(GITHUB_API_URI)
    query_parameters = {'q':'created:>{}'.format(start_search_date),
                        'sort': 'stars',
                        'order': 'desc',
                        'per_page': number_of_results}
    trending_repositories_json = requests.get(query_search_url,
                                              query_parameters).json()['items']
    short_list = []
    for repository in trending_repositories_json:
        repo_name = repository['name']
        repo_owner = repository['owner']['login']
        #number_of_open_issues = get_open_issues_amount(repo_owner, repo_name)
        short_list.append({'repo_name': str(repo_name),
                           'repo_owner': str(repo_owner),
                           'stars': repository['stargazers_count'],
                           'issues': repository['open_issues'],
                           'url': repository['html_url']
                           })
    return short_list


def get_open_issues_amount(repo_owner, repo_name):
    query_search_url = '{0}/repos/{1}/{2}/issues'.format(GITHUB_API_URI,
                                                         repo_owner, repo_name)
    issues_json_data = requests.get(query_search_url).json()
    open_issues = 0
    for issue in issues_json_data:
        if issue['state'] == 'open':
            open_issues += 1
    return open_issues


def print_result_to_console():
    print('Программа печатает 20 самых популярных репозитариев начиная с {}'.format(week_earlier_date))
    for index, repo in enumerate(top_repositories_list):
        good_choice_label = ''
        if not repo['issues']:
            good_choice_label = ' Try it!'
        print('{0:2} {1:70} {2:3} stars {3:2} issues'.format(index, repo['url'] + good_choice_label, repo['stars'],
                                                                 repo['issues']))


if __name__ == '__main__':
    week_earlier_date = get_offset_date(date.today(), '-7')
    top_repositories_list = get_trending_repositories(week_earlier_date)
    #print(top_repositories_list)
    print_result_to_console()
