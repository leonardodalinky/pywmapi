from pywmapi.common import *
from pywmapi.items import *


def test_list_items():
    list_items()


def test_get_item():
    get_item("mirage_prime_systems")
    get_item("heavy_trauma")


def test_get_orders():
    get_orders("mirage_prime_systems", include=IncludeOption.item)
    get_orders("heavy_trauma", include=IncludeOption.item)
