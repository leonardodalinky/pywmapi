# pywmapi

[![github action packaging test badge](https://img.shields.io/github/workflow/status/leonardodalinky/pywmapi/Python%20package%20test/main?label=main)](https://github.com/leonardodalinky/pywmapi/tree/main)
[![pypi package version badge](https://img.shields.io/pypi/v/pywmapi)](https://pypi.org/project/pywmapi/)
![python version badge](https://img.shields.io/badge/python-%3E%3D3.7-blue)
[![license badge](https://img.shields.io/github/license/leonardodalinky/pywmapi)](https://github.com/leonardodalinky/pywmapi/blob/main/LICENSE)
[![star badge](https://img.shields.io/github/stars/leonardodalinky/pywmapi?style=social)](https://github.com/leonardodalinky/pywmapi)


**PY**thon **W**arframe **M**arket **API**(pywmapi)

🔥 API for warframe market, written in Python.

> *"Thank you tinsuit, a fine trade. Transaction complete, haha!" -- Maroo*

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

Feel free to make any issue or PR! 😊

## Installation

```
pip install pywmapi
```

The version of Python **MUST >= 3.7** since `dataclasses` is used.

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

💪 *More functionalities is coming!*

🏗️ *Better documentation is under construction!*

The param `url_name` of some functions is regarded as the unique name for each item. For instance, if I search for the item *Chroma Prime Systems* on warframe market, the url for this page become *https://warframe.market/items/chroma_prime_systems*. And the last part of this url string is exactly the `url_name` for this item, i.e. `chroma_prime_systems`!

Another way to get `url_name` for an item is through the `items.list_items()` function.

### Examples

To list all of the tradable items:
```python
import pywmapi as wm

wm.items.list_items()
```

To get the info for any item with its `url_name`:
```python
import pywmapi as wm

wm.items.get_item("chroma_prime_systems")
```

To get the orders of a specific item:
```python
import pywmapi as wm

wm.items.get_orders("chroma_prime_systems")
```

To get the statistics of historical prices of any item:
```python
wm.statistics.get_statistic("chroma_prime_systems")
```
