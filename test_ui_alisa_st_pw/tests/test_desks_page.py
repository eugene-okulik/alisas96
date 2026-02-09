def test_items_displayed_with_price_and_img(opened_desks, desks_page):
    desks_page.check_items_displayed()
    desks_page.check_all_items_have_price()
    desks_page.check_all_items_have_img()


def test_sort_by_price_low_to_high(opened_desks, desks_page):
    desks_page.sort_by_price_low_to_high()
    desks_page.check_sorted_by_price_low_to_high()


def test_add_to_cart_from_desks_page(opened_desks, desks_page):
    desks_page.add_desk_to_cart()
    desks_page.check_cart_counter_equals_qty_of_items("1")
