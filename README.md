# Propublica Nonprofit Explorer Client
Python client for the ProPublica [NonProfit Explorer API](https://www.propublica.org/datastore/api/nonprofit-explorer-api "ProPublica Nonprofit Explorer API docs").

Query data on over 1.6 million nonprofit organizations. No API key is required, but please refer to ProPublica's terms of use.

## Usage
```
>>> from nonprofit import Nonprofit
>>> np = Nonprofit()

# get organization by employer identification number (EIN)
>>> org = np.orgs.get('521275227')
>>> org['name']
>>> 'CENTER FOR RESPONSIVE POLITICS'

# get organizations by keyword
>>> orgs = np.search.get(q='responsive')
>>> orgs[0]['name']
>>> 'RESPONSIVE EDUCATION SOLUTIONS'

# get organizations by state
>>> orgs = np.search.get(state='WA')
>>> orgs[0]['name']
>>> '101 CLUB'

# query by multiple parameters (state, c_code, ntee)
>>> orgs = np.search.get(c_code=2, ntee=7)
>>> orgs[0]['name']
>>> '1800 MASSACHUSETTS AVENUE CORP'
```