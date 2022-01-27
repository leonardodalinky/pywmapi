# pywmapi

PYthon Warframe Market API(pywmapi)

API for warframe market, written in Python.

For now, the implemented function is listed below:

* auth
  * [x] sign in
  * [ ] register
  * [ ] restore password
* items
  * [x] list all tradable items
  * [x] get info about an item
  * [x] get list of orders of an item
* statistics
  * [x] get statistics of an item
* profile
  * [ ] create an order
* Liches
  * [ ] list all lich weapons
  * [ ] list all lich ephemeras
  * [ ] list all lich quirks
* rivens
  * [ ] list all riven items
  * [ ] get a list of riven attributes
* auctions
  * [ ] create auction
  * [ ] get a list of riven auctions by given search params
  * [ ] get a list of lich auctions by given search params
* auction entry
  * [ ] get info about auction by auction id
  * [ ] get auction bids by auction id

## Installation

*Not uploaded yet*

```
pip install pywmapi
```

The version of Python **MUST** greater than **3.6**.

## Guidance

package of pywmapi is structured as:
```
.
├── auth
├── common
├── items
├── lang
└── statistics
```

For authentication, look up the `auth` package.

For items maniplation, look up the `items` package.

For getting statistics of items, look up the `statistics` package.

*More functionalities is coming!*
