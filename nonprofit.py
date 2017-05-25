"""
A Python client for the ProPublica Nonprofit Explorer API.

API docs: https://www.propublica.org/datastore/api/nonprofit-explorer-api
"""

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

    def get(self, **kwargs):
        """
            Returns a list of organizations matching the given search terms.
        """

        """
            TODO:
            - regular search: q='terms'
            - "exact" search appears to make no difference
            - exact order: exact='terms'
            - and: require=['term1', 'term2', 'etc']
            - exclude: exclude='terms'
            - state id: state='state_id'
        """
        params = {}
        for key, value in kwargs.iteritems():

            if key == 'state':
                key = 'state[id]'

            if key == 'ntee':
                key = 'ntee[id]'

            if key == 'c_code':
                key = 'c_code[id]'

            params[key] = value

        params = urllib.urlencode(params)
        path = 'search.json?%s' % (params)
        return self.fetch(path)


class OrgsClient(Client):

    def get(self, ein):
        """ Returns an organization object for the given employer
            identification number (ein).
        """
        path = 'organizations/{0}.json'.format(ein)
        return self.fetch(path)


class Nonprofit(Client):
    """
        The public interface for the Nonprofit API client.
    """

    def __init__(self, cache='.cache'):
        super(Nonprofit, self).__init__(cache)
        self.search = SearchClient(cache)
        self.orgs = OrgsClient(cache)