import requests
# note we could do 60 but for testing and throtting reasons we will do just 3
def get_github_loads(minpage=1,maxpage=3):
    parsed_data = []
    for i in range(minpage,maxpage,1):
        data = get_github_load(i)
        parsed_data.append(parse(data))
    return parsed_data

        
    
def get_github_load(page=1):
    url = 'https://api.github.com/search/repositories?q=language:python&sort=stars&order=desc&page='+str(page)+'&per_page=100'
    return requests.get(url).json()
def get_server_data():
    url = 'http://127.0.0.1:8000/django_api/record/'
    return requests.get(url).json()
def parse(data):
    data_values = {}
    values = []
        #Store the list of repositories in a database table. 
    #The table must contain the 
    #repository ID
    #, name
    #, URL
    #, created date
    #, last push date
    #, description
    #, and number of stars.
    for bit in data['items']:
        data_values['repository_ID'] = bit['id']
        data_values['name'] = bit['name']
        data_values['description'] = bit['description']
        data_values['created_date'] = bit['created_at']
        data_values['last_push_date'] = bit['pushed_at']
        data_values['url'] = bit['url']
        data_values['stars'] = bit['stargazers_count']
        values.append(data_values)
        data_values = {}
    return values
        
def main():
    while True:
        parsed_data = get_github_loads()
        server_data = get_server_data()
        patched_data,new_data = compare(server_data,parsed_data)
        upload(patched_data)
        # seconds , mins, one hour
        time.sleep(60 * 60 * 1)
def test_parse():
    get_github_loads()
test_parse()
    
    
