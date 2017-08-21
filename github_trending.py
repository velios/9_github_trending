import requests
from datetime import date
from datetime import timedelta


def get_offset_date(modifed_date, offset_in_days):
    return date.isoformat(modifed_date + timedelta(days=int(offset_in_days)))


def get_trending_repositories(start_search_date, number_of_results=20):
    github_api_uri = 'https://api.github.com'
    query_search_url = '{}/search/repositories'.format(github_api_uri)
    query_parameters = {'q': 'created:>{}'.format(start_search_date),
                        'sort': 'stars',
                        'order': 'desc',
                        'per_page': number_of_results}
    trending_repositories_json_list = requests.get(query_search_url,
                                                   query_parameters).json()['items']
    result_trending_list = []
    for repository in trending_repositories_json_list:
        repository_name = repository['name']
        repoditory_owner = repository['owner']['login']
        result_trending_list.append({'repo_name': str(repository_name),
                                     'repo_owner': str(repoditory_owner),
                                     'stars': repository['stargazers_count'],
                                     'issues': repository['open_issues'],
                                     'url': repository['html_url']
                                     })
    return result_trending_list


def get_open_issues_amount(repo_owner, repo_name):
    github_api_uri = 'https://api.github.com'
    query_search_url = '{0}/repos/{1}/{2}/issues'.format(github_api_uri,
                                                         repo_owner,
                                                         repo_name)
    issues_json_data = requests.get(query_search_url).json()
    number_of_open_issues = len([ x for x in issues_json_data if x['state'] == 'open' ])
    return number_of_open_issues


def print_result_to_console():
    print('Program prints {} most popular repositories since {}\n'.format(number_of_results, week_earlier_date))
    for index, repo in enumerate(top_repositories_list):
        good_choice_label = ''
        if not repo['issues']:
            good_choice_label = 'Try it!'
        print('{0:2} {4:7} {1:70} {2:5} stars {3:2} issues'.format(index + 1,
                                                                   repo['url'],
                                                                   repo['stars'],
                                                                   repo['issues'],
                                                                   good_choice_label))


if __name__ == '__main__':
    date_offset_in_days = -7
    week_earlier_date = get_offset_date(date.today(), date_offset_in_days)
    number_of_results = 20
    top_repositories_list = get_trending_repositories(week_earlier_date,
                                                      number_of_results)
    print_result_to_console()
