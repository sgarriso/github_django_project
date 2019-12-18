import requests
import json
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
def upload_data_records(records):
    def upload_data(record):
        json_string = json.dumps(record) 
        url = 'http://127.0.0.1:8000/django_api/record/'
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        r=requests.post(url,json=record)
        if r.status_code != 201:
            print(json_string)
        print(r)
    for record in records:
        for r in record:
            upload_data(r)
def get_server_data():
    url = 'http://127.0.0.1:8000/django_api/record/'
    return requests.get(url).json()
def parse(data):
    MAX=2000
    def check_len(values):
        lookup = ['name','description','url']
        for key in lookup:
            if values[key] and len(values[key]) > MAX:
                values[key] = values[key][0:2000]
        return values
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
        data_values=check_len(data_values)
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
    parsed_data=get_github_loads()
    server_data = get_server_data()
    #print(server_data)
    upload_data_records(parsed_data)
test_parse()
    
    
    
