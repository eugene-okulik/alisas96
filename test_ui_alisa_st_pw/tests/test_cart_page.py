def test_item_displayed_in_cart(add_item_to_cart, opened_cart, cart_page):
    cart_page.check_cart_is_not_empty()


def test_checkout(add_item_to_cart, opened_cart, cart_page):
    cart_page.go_to_checkout()
    cart_page.check_there_is_a_shipping_form()


def test_remove_item_from_cart(add_item_to_cart, opened_cart, cart_page):
    cart_page.remove_item_from_cart()
    cart_page.check_cart_is_empty()
