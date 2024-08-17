from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("add_listing", views.add_listing, name="add_listing"),
    path("active_listings", views.active_listings, name="active_listings"),
    path("page_listing/<int:listing_id>", views.page_listing, name="page_listing"),
    path("comment/<int:listing_id>", views.comment, name="comment"),
    path("bid/<int:listing_id>", views.bid, name="bid"),
    path("categories", views.categories, name="categories"),
    path("category/<str:category_chosen>", views.category, name="category"),
    path("add_to_watchlist/<int:listing_id>", views.add_to_watchlist, name="add_to_watchlist"),
    path("remove/<int:listing_id>", views.remove, name="remove"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("close/<int:listing_id>", views.close, name="close"),
    path("closed_listings", views.closed_listings, name="closed_listings")
]
