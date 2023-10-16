import pytest

from pywmapi.auth.api import signin
from pywmapi.common import *
from pywmapi.orders import *
from tests.test_auth_api import get_test_signin_dict


def test_get_orders():
    get_orders("mirage_prime_systems", include=IncludeOption.item)
    get_orders("heavy_trauma", include=IncludeOption.item)


@pytest.mark.skipif(get_test_signin_dict() is None, reason="No test account.")
def test_get_current_orders():
    d = get_test_signin_dict()
    sess = signin(**d)
    get_current_orders(sess)


@pytest.mark.skipif(get_test_signin_dict() is None, reason="No test account.")
def test_add_delete_order():
    d = get_test_signin_dict()
    sess = signin(**d)
    # "Flame Gland" item id
    new_item = OrderNewItem(
        item_id="5be5f5a23ffcc7038857f119",
        order_type=OrderType.sell,
        platinum=1000,
        quantity=1,
        rank=0,
        visible=False,
        subtype=None,
    )
    new_order = add_order(sess, new_item)
    delete_order(sess, new_order.id)
