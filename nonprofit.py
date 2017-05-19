"""
A Python client for the ProPublica Nonprofit Explorer API.

API docs: https://www.propublica.org/datastore/api/nonprofit-explorer-api
"""

import os
import json
import httplib2
import urllib


class NonprofitError(Exception):
    """ Exception for general Nonprofit client errors """


class Client(object):

    BASE_URI = "https://projects.propublica.org/nonprofits/api/v2/"

    def __init__(self, cache='.cache'):
        self.http = httplib2.Http(cache)


    def fetch(self, path):
        """ Make the API request. """
        url = self.BASE_URI + path

        resp, content = self.http.request(url)
        content = json.loads(content)

        # TODO: check for content not found
        # TODO: customized error response
        if not resp.get('status') == '200':
            raise NonprofitError()

        return content


class SearchClient(Client):

    def get(self):
        """
            Returns a list of organizations matching the given search terms.
        """
        path = "search.json"


class OrgsClient(Client):

    def get(self, ein):
        """ Returns an organization object for the given employer
            identification number (EIN).
        """
        path = "organizations/{0}.json".format(ein)
        return self.fetch(path)


class Nonprofit(Client):
    """
        The public interface for the Nonprofit API client.
    """

    def __init__(self, cache='.cache'):
        super(Nonprofit, self).__init__(cache)
        self.search = SearchClient(cache)
        self.orgs = OrgsClient(cache)