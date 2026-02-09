def test_add_item_to_cart(opened_product, product_page, cart_page):
    chosen_item_text = product_page.get_item_name_text()
    product_page.add_to_cart()
    product_page.check_cart_counter_equals_qty_of_items('1')
    product_page.open_cart()
    cart_page.check_chosen_item_in_cart(chosen_item_text)


def test_add_qty_to_cart(opened_product, product_page):
    qty_of_items = "3"
    product_page.insert_qty_of_items(qty_of_items)
    product_page.add_to_cart()
    product_page.check_cart_counter_equals_qty_of_items(qty_of_items)


def test_search_string_is_working(opened_product, product_page, search_page):
    requested_text = "Software"
    product_page.enter_item_name_in_search_string(requested_text)
    search_page.check_requested_item_found(requested_text)
