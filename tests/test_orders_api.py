from pywmapi.common import *
from pywmapi.orders import *


def test_get_orders():
    get_orders("mirage_prime_systems", include=IncludeOption.item)
    get_orders("heavy_trauma", include=IncludeOption.item)
