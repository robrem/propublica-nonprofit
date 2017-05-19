import unittest
import os
import json
import httplib2
import urllib
from nonprofit import Nonprofit, NonprofitError

# Propublica employer identification number
EIN = '142007220'

class NonprofitTest(unittest.TestCase):

    def setUp(self):
        self.nonprofit = Nonprofit()
        self.http = httplib2.Http()


    def check_response(self, result, url):
        resp = json.loads(self.http.request(url)[1])
        self.assertEqual(result, resp)


class OrgsTest(NonprofitTest):

    def test_get_org(self):
        org = self.nonprofit.orgs.get(EIN)
        url = "https://projects.propublica.org/nonprofits/api/v2/organizations/{0}.json".format(EIN)
        self.check_response(org, url)


if __name__ == "__main__":
    unittest.main()