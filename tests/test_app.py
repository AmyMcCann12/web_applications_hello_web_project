# Tests for your routes go here

"""
When: I make a POST request to /count_vowels
And: I send "eee" as the body parameter text
Then: I should get a 200 response with 3 in the message
"""
def test_post_count_vowels_eee(web_client):
    response = web_client.post('/count_vowels', data={'text': 'eee'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 3 vowels in "eee"'

"""
When: I make a POST request to /count_vowels
And: I send "eunoia" as the body parameter text
Then: I should get a 200 response with 5 in the message
"""
def test_post_count_vowels_eunoia(web_client):
    response = web_client.post('/count_vowels', data={'text': 'eunoia'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 5 vowels in "eunoia"'

"""
When: I make a POST request to /count_vowels
And: I send "mercurial" as the body parameter text
Then: I should get a 200 response with 4 in the message
"""
def test_post_count_vowels_mercurial(web_client):
    response = web_client.post('/count_vowels', data={'text': 'mercurial'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 4 vowels in "mercurial"'

"""
When: I make a POST request to /sort-names
And: I send names=Joe,Alice,Zoe,Julia,Kieran as the list of names
Then: I should get a 200 response with the names sorted in alphabetical order
"""

def test_sort_names(web_client):
    response = web_client.post('/sort-names', data={'names': 'Joe,Alice,Zoe,Julia,Kieran'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Alice,Joe,Julia,Kieran,Zoe'

"""
When: I make a GET request to /add
And: I add 'Eddie'
Then: I should get a 200 reponse with a list including the additional name added 
"""

def test_add_name(web_client):
    response = web_client.get('/add?name=Eddie')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Alice, Eddie, Julia, Karim'

"""
When: I make a GET request to /add
And: I add 'Eddie, John'
Then: I should get a 200 reponse with a list including the additional names added 
"""

def test_add_multiple_names(web_client):
    response = web_client.get('/add?name=Eddie,John')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Alice, Eddie, John, Julia, Karim'