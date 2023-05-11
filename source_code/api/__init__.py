from flask import Flask

app = Flask(__name__)
app.config['CACHE_TYPE'] = 'simple'

from source_code.api.E_comm.admin_apis import add_items_to_wishlist, add_new_orders, \
    add_new_vendor_ratings, add_new_vendors, add_new_view_details, clear_all_views, clear_wishlist, \
    delete_items_from_cart,delete_items_from_wishlist, delete_vendor_ratings, deleting_views, update_cart, \
    update_orders, update_vendor_details, update_views_count

from source_code.api.E_comm.functional_apis import get_all_ratings_of_vendor, get_avg_ratings_of_vendor, \
    get_order_details_by_order_id, get_order_details_of_user, get_wishlist_items
