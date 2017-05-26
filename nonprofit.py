"""
A Python client for the ProPublica Nonprofit Explorer API.

API docs: https://www.propublica.org/datastore/api/nonprofit-explorer-api
"""

import json
import httplib2
import urllib


def check_ntee(ntee):
    """
        Returns true if ntee is a valid NTEE code; false otherwise.
    """
    ntees = range(1,11)

    if ntee not in ntees:
        raise TypeError('Invalid ntee code')


def check_c_code(c_code):
    """
        Returns true if c_code is a valid tax code id; false otherwise.
    """
    c_codes = range(2,29)
    c_codes.append(92)

    if c_code not in c_codes:
        raise TypeError('Invalid c_code')


def check_state(state):
    """
        Returns true if state is a valid US state code; false otherwise.
    """
    states = [
            "AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
            "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
            "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
            "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
            "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY", "ZZ"
            ]

    if state not in states:
        raise TypeError('Invalid state code')


class NonprofitError(Exception):
    """ Exception for general Nonprofit client errors """

    def __init__(self, message, resp=None, url=None):
        super(NonprofitError, self).__init__(message)
        self.message = message
        self.resp = resp
        self.url = url


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
        if not resp.get('status') == '200':
            raise NonprofitError(content, resp, url)

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
                check_state(value)
                key = 'state[id]'

            if key == 'ntee':
                check_ntee(value)
                key = 'ntee[id]'

            if key == 'c_code':
                check_c_code(value)
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