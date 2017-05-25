import unittest
import json
import httplib2
import urllib
from nonprofit import Nonprofit, NonprofitError

# Test case
EIN = '142007220'
ORG = 'Delta'
US_STATE = 'CA'
NTEE = 7     # Public, Societal Benefit
C_CODE = 3   # 501(c)(3)


class NonprofitTest(unittest.TestCase):

    def setUp(self):
        self.nonprofit = Nonprofit()
        self.http = httplib2.Http()


    def check_response(self, result, url):
        resp = json.loads(self.http.request(url)[1])
        self.assertEqual(result, resp)


class OrgsTest(NonprofitTest):

    def test_get_search_term(self):
        result = self.nonprofit.search.get(q=ORG)
        url = "https://projects.propublica.org/nonprofits/api/v2/search.json?q={0}".format(ORG)
        self.check_response(result, url)


    def test_get_search_state(self):
        result = self.nonprofit.search.get(state=US_STATE)
        url = "https://projects.propublica.org/nonprofits/api/v2/search.json?state%5Bid%5D={0}".format(US_STATE)
        self.check_response(result, url)


    def test_get_search_ntee(self):
        result = self.nonprofit.search.get(ntee=NTEE)
        url = "https://projects.propublica.org/nonprofits/api/v2/search.json?ntee%5Bid%5D={0}".format(NTEE)
        self.check_response(result, url)


    def test_get_search_c_code(self):
        result = self.nonprofit.search.get(c_code=C_CODE)
        url = "https://projects.propublica.org/nonprofits/api/v2/search.json?c_code%5Bid%5D={0}".format(C_CODE)
        self.check_response(result, url)


    def test_get_search_all(self):
        result = self.nonprofit.search.get(q=ORG, state=US_STATE, ntee=NTEE, c_code=C_CODE)
        url = "https://projects.propublica.org/nonprofits/api/v2/search.json?q={0}&state%5Bid%5D={1}&ntee%5Bid%5D={2}&c_code%5Bid%5D={3}"
        url = url.format(ORG, US_STATE, NTEE, C_CODE)
        self.check_response(result, url)


    def test_get_org(self):
        org = self.nonprofit.orgs.get(EIN)
        url = "https://projects.propublica.org/nonprofits/api/v2/organizations/{0}.json".format(EIN)
        self.check_response(org, url)


if __name__ == "__main__":
    unittest.main()
    