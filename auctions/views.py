from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.db.models import Max

from .models import *

def close(request, listing_id):
    listing = Listing.objects.get(pk=listing_id)
    listing.active = False
    listing.save()

    return render(request, "auctions/page_listings.html", {
        "listing": listing,
        "close": "You have closed your listing",
        "win": "Congrats" 
    })
 
def closed_listings(request):
    not_active = Listing.objects.filter(active=False) 
    return render(request, "auctions/not_active.html", {
         "notactive": not_active
      }) 

def index(request):
    is_active = Listing.objects.filter(active=True) 
    return render(request, "auctions/index.html", {
        "is_active": is_active,
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

@login_required(login_url='/login')
def add_listing(request):
    if request.method == "POST":
        thing = Listing()

        thing.seller = request.user.username
        thing.title = request.POST["title"]
        thing.description = request.POST["description"]
        thing.image_link = request.POST["image_link"]
        thing.category = request.POST["category"]
        thing.starting_bid = request.POST["starting_bid"]
        
        thing.save()

        return HttpResponseRedirect(reverse("index"))
    return render(request, "auctions/add_listing.html")

def active_listings(request):
    active_listings = Listing.objects.filter(active=False)
    return render(request, "auctions/active_listings.html", {
        "active_listings": active_listings,
    })


def page_listing(request, listing_id):
    thing = Listing.objects.get(pk=listing_id)
    comments = Comment.objects.filter(listingid=listing_id)
    is_listing_in_watchlist = ActiveWatchlist.objects.filter(listingid=listing_id, user=request.user.username)
    obj = Bid.objects.filter(listing=listing_id)
    notactive = Listing.objects.filter(pk=listing_id, active=False)
    closedwinner = notactive 
    is_active = Listing.objects.filter(pk=listing_id, active=True)

    nobids = Listing.objects.filter(pk=listing_id, newbid__iexact='')

    return render(request, "auctions/page_listings.html", {
        "nobids": nobids,
        "closedwinner": closedwinner,
        "in_watchlist": is_listing_in_watchlist,
        "is_active": is_active,
        "comments": comments,
        "listing": thing,
    })

@login_required(login_url='/login')
def comment(request, listing_id):
    comment = Comment()
    comment.comment = request.POST["comment"]
    comment.user = request.user.username
    comment.listingid = listing_id
    comment.save()
    return HttpResponseRedirect(reverse("page_listing", args=(listing_id, )))



@login_required(login_url='/login')
def bid(request, listing_id):
    if request.method == "POST":
        bid = Listing.objects.get(pk=listing_id)

        newbidold = bid.starting_bid
        newbidoldd = bid.newbid
        new_bid = int(request.POST["newbid"])

        if bid.newbid == 0:
            if new_bid > newbidold:
                obj = Bid()
                obj.bid = new_bid
                obj.userr = request.user.username
                obj.title = bid.title
                obj.listing = listing_id
                bid.newbiduser = obj.userr
                bid.newbid = obj.bid
                obj.save()
                bid.save()
                bid = Listing.objects.get(pk=listing_id)
                is_active = Listing.objects.filter(pk=listing_id, active=True)
                return render(request, "auctions/page_listings.html", {
                "is_active": is_active,
                "listing": bid,
                "woo": "Bid was updated successfully",
                "updated": True
                })
            else:
                is_active = Listing.objects.filter(pk=listing_id, active=True)
                return render(request, "auctions/page_listings.html", {
                    "is_active": is_active,
                    "listing": bid,
                "error": "Bid must be higher than current bid",
                "updated": True
            })  
        else:
            if new_bid > newbidoldd:
                obj = Bid()
                obj.bid = new_bid
                obj.userr = request.user.username
                obj.title = bid.title
                obj.listing = listing_id
                bid.newbiduser = obj.userr
                bid.newbid = obj.bid
                obj.save()
                bid.save()
                bid = Listing.objects.get(pk=listing_id)
                is_active = Listing.objects.filter(pk=listing_id, active=True)
                return render(request, "auctions/page_listings.html", {
                    "is_active": is_active,
                    "listing": bid,
                    "woo": "Bid was updated successfully",
                    "updated": True
                })

            else:
                is_active = Listing.objects.filter(pk=listing_id, active=True)
                return render(request, "auctions/page_listings.html", {
                    "is_active": is_active,
                    "listing": bid,
                    "error": "Bid must be higher than current bid",
                    "updated": True
                })  



def categories(request):
    return render(request, "auctions/categories.html", {
    })

def category(request, category_chosen):
    listings = Listing.objects.filter(category=category_chosen)
    no_listing = False
    if len(listings) == 0:
        no_listing = True
    return render(request, "auctions/category.html", {
        "category_chosen": category_chosen,
        "no_listing": no_listing,
        "listings": listings
    })

@login_required(login_url='/login')
def add_to_watchlist(request, listing_id):
    add_watchlist_listing = ActiveWatchlist.objects.filter(listingid=listing_id, user=request.user.username)
    add = ActiveWatchlist()
    add.user = request.user.username
    add.listingid = listing_id
    add.save() 
    return HttpResponseRedirect(reverse("page_listing", args=(listing_id, )))

@login_required(login_url='/login')
def remove(request, listing_id):
    listing = ActiveWatchlist.objects.filter(listingid=listing_id, user=request.user.username)
    if listing:
        listing.delete()
    return HttpResponseRedirect(reverse("page_listing", args=(listing_id, )))

@login_required(login_url='/login')
def watchlist(request):
    lst = ActiveWatchlist.objects.filter(user=request.user.username)
    prodlst = []
    try:
        for item in lst:
            product = Listing.objects.get(id=item.listingid)
            prodlst.append(product)
    except:
        product = None
    return render(request, "auctions/watchlist.html",{
        "listings": prodlst,
    })  