# Propublica Nonprofit Explorer Client
Python client for the ProPublica [NonProfit Explorer API](https://www.propublica.org/datastore/api/nonprofit-explorer-api "ProPublica Nonprofit Explorer API docs").

## Usage
```
>>> from nonprofit import Nonprofit
>>> np = Nonprofit()

# get organization by EIN
>>> org = np.orgs.get('521275227')
>>> org['name']
>>> 'CENTER FOR RESPONSIVE POLITICS'

# get organizations by state
>>> orgs = np.search.get(state='WA')
>>> orgs[0]['name']
>>> '101 CLUB'

# query by multiple parameters (state, c_code, ntee)
>>> orgs = np.search.get(c_code=2, ntee=7)
>>> orgs[0]['name']
>>> '1800 MASSACHUSETTS AVENUE CORP'
```