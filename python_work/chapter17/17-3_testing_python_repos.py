# In python_repos.py, we printed the value of status_code to make sure the API call was successful. Write a program called test_python_repos.py that uses unittest to assert that the value of status_code is 200. Figure out some other assertions you can make—for example, that the number of items returned is expected and that the total number of repositories is greater than a certain amount.

# confirming that the test passes response code 200. other items described can change... omitting 

import unittest

import python_repos
import requests

class TestStatusCode(unittest.TestCase):
    def test_status_code_200(self):
        # headers = {'Accept': 'application/vnd.github.v3+json'}
        url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
        r = requests.get(url)
        self.assertEqual(r.status_code, 200)

if __name__ == '__main__':
    unittest.main()


