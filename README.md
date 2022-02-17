# pywmapi

[![github action packaging test badge](https://img.shields.io/github/workflow/status/leonardodalinky/pywmapi/Python%20package%20test/main?label=main)](https://github.com/leonardodalinky/pywmapi/tree/main)
[![pypi package version badge](https://img.shields.io/pypi/v/pywmapi)](https://pypi.org/project/pywmapi/)
![python version badge](https://img.shields.io/badge/python-%3E%3D3.7-blue)
[![license badge](https://img.shields.io/github/license/leonardodalinky/pywmapi)](https://github.com/leonardodalinky/pywmapi/blob/main/LICENSE)
[![star badge](https://img.shields.io/github/stars/leonardodalinky/pywmapi?style=social)](https://github.com/leonardodalinky/pywmapi)


**PY**thon **W**arframe **M**arket **API**(pywmapi)

🔥 API for warframe market, implemented in Python.

> *"Thank you tinsuit, a fine trade. Transaction complete, haha!" -- Maroo*

For now, the implemented function is listed below:

* auth
  * ✅ sign in
  * 🆖 register
  * 🆖 restore password
* profile
  * ✅ get current user's profile
  * 🔲 manage current user profile
  * ✅ get a user's profile
  * 🔲 get all of a user's achievements
  * 🔲 get all of a user's reviews
  * ✅ set current user's online/offline status
* items
  * ✅ list all tradable items
  * ✅ get info about an item
* statistics
  * ✅ get statistics of an item
  * 🔲 get global market statistics
* orders
  * ✅ get orders of a single item
  * 🔲 get orders for the last 4 hours
  * 🔲 get individual order from current profile
  * 🔲 update a single order on the current profile
  * 🔲 delete a single order on the current profile
  * 🔲 add a new order for the current profile
  * 🔲 get all of the current profile's orders
  * 🔲 get user's sale statistics(closed orders)
  * 🔲 get all of a user's orders
* liches
  * ✅ list all lich weapons
  * ✅ list all lich ephemeras
  * ✅ list all lich quirks
* rivens
  * ✅ list all riven items
  * ✅ get a list of riven attributes
* auctions
  * 🔲 create auction
  * 🔲 get a list of riven auctions by given search params
  * 🔲 get a list of lich auctions by given search params
* auction entry
  * 🔲 get info about auction by auction id
  * 🔲 get auction bids by auction id

"✅" means implemented. "🆖" means unreachable due to some intractable problem. "🔲" means not being implemented yet.

There're more APIs that are not recorded in the official documentation. Once all the above APIs are done, we would get on these undocumented APIs ASAP.

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
├── exceptions
├── items
├── lang
├── liches
├── orders
├── profile
├── rivens
└── statistics
```

* `auth`: authentication such as signin
* `items`: item related
* `liches` lich related
* `orders`: orders maniplation
* `profile`: user profile maniplation
* `rivens`: riven related
* `statistics`: statistics of items

💪 *More functionalities is coming!*

🏗️ *Better documentation is under construction!*

The param `url_name` of some functions is regarded as the unique name for each item. For instance, if I search for the item *Chroma Prime Systems* on warframe market, the url for this page become *https://warframe.market/items/chroma_prime_systems*. And the last part of this url string is exactly the `url_name` for this item, i.e. `chroma_prime_systems`!

Another way to get `url_name` for an item is through the `items.list_items()` function.

### Examples

First, we import the package as:
```python
import pywmapi as wm
```

To list all of the tradable items:
```python
wm.items.list_items()
```

To get the info for any item with its `url_name`:
```python
wm.items.get_item("chroma_prime_systems")
```

To get the orders of a specific item:
```python
wm.items.get_orders("chroma_prime_systems")
```

To get the statistics of historical prices of any item:
```python
wm.statistics.get_statistic("chroma_prime_systems")
```

Some of these function may have various optional params, such as `platform`, `lang`, `include`, etc.

## Reference

[Warframe market official API documentation](https://warframe.market/api_docs)

[WFCD/market-api-spec](https://github.com/WFCD/market-api-spec)

[Public WM API](https://docs.google.com/document/d/1121cjBNN4BeZdMBGil6Qbuqse-sWpEXPpitQH5fb_Fo)

## Changelog

See [CHANGELOG.md](CHANGELOG.md).

## Contributing
Feel free to make any issue or PR! 😊

*Or contact me in game!*

## Donating

Any sort of donation in game would be appretiated.

Contact me in game:
```
/w AyajiLin Hi! ${Your words here}.
```

🤣 *Relics or 5 platinums would be enough.*
