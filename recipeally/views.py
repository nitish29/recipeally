import urllib.request
import urllib.parse
import json
from django.shortcuts import render
import pdb
# Create your views here.
from .forms import SignUpForm
from .forms import ProfileForm
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.db.models.signals import post_save
from .forms import PostForm
from recipesearch.models import User,UserProfile
from django.contrib.auth.decorators import login_required

from django.contrib.auth import logout
def registration(request):
	title = 'Welcome'
	# if request.user.is_authenticated():
	# 	title="My Title %s" %(request.user)
	# print request
	# if request.method=="POST":
	# 	print(request.POST)
	form=SignUpForm(request.POST or None)
	form2=ProfileForm(request.POST or None)
	context={
		"title": title,
		"form": form,
		"form2":form2
	}

	if form.is_valid():
		if form2.is_valid():
			instance=form.save(commit=False)
			instance.save()
			instance2=form2.save(commit=False)
			instance2.user=instance
			instance2.save()
	
			context={
				"title": "Thank You"
			}
	return render(request, "registration.html",context)


def recipe_adhip(request):
    form=PostForm(request.POST or None)
    context={
        "form": form
    }

    if form.is_valid():
        instance=form.save(commit=False)
        instance.user_id=1
        instance.recipe_str="3847"
        instance.save()
    
        context={
                        "title": "Thank you for your comment"
            }
    return render(request, "recipe.html",context)

# def comment(request):
#     form=PostForm(request.POST or None)
#     context={
#     "form": form
#     }
#     if form.is_valid():
#         instance=form.save(commit=False)
#         instance.recipe_id=1
#         instance.user_id=1
#         instance.save()
#     return render(request,"comments.html",context)

def user_login(request):
    # Like before, obtain the context for the user's request.
    context = RequestContext(request,{'errormessage':''})
    
    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            #print "Invalid login details: {0}, {1}".format(username, password)
            #return HttpResponse("Invalid login details supplied.")
            context = RequestContext(request,{'errormessage':'Invalid login details supplied.'})
            return render_to_response('login.html', {}, context)

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render_to_response('login.html', {}, context)

@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/')


    # Display a particular recipe.
def recipe(request):
    #f = open(D:/dummy_tweets_future_use/Tweets_iphone6s_reviews_40_english_16092015.json)
    #str = []
    #str = '[{"created_at": "2015-09-16T22:18:25Z", "id": "644274166506479616", "lang_en": "en", "text_en": "Apple iPhone 6s Plus vs. Samsung Galaxy Note 5 Specs, Review: 2 of the Latest ... - Latin Post http://t.co/4iamYbC0P6 #GalaxyNote4", "twitter_hashtags": ["GalaxyNote4"], "twitter_urls": ["note5cases.com", "http://www.note5cases.com", "http://t.co/XoAY430Gux"]},{"created_at": "2015-09-16T22:18:25Z", "id": "644274163398500352", "lang_en": "en", "text_en": "Apple iPhone 6s Plus vs. Samsung Galaxy Note 5 Specs, Review: 2 of the Latest ... - Latin Post http://t.co/VQ0TyZfcF9 #GalaxyNote4", "twitter_hashtags": ["GalaxyNote4"], "twitter_urls": ["note4cases.com", "http://www.note4cases.com", "http://t.co/5QYCbO1e8Q"]}]'
    form3=PostForm(request.POST or None)
    if request.method == "POST":
        

        if form3.is_valid():
            print("*********")
            instance=form3.save(commit=False)
            instance.user_id=1
            instance.recipe_str="3847"
            instance.save()
            context={   
                "form3": form3
                }
    
    # if request.method == 'GET':

    search_context = request.GET['q']

    search_context = search_context.strip()
    formatted_string = search_context.replace(",", " ")
    formatted_string = ' '.join(formatted_string.split())

    data = urllib.parse.urlencode({'q': formatted_string, 'wt': 'json', 'indent': 'true'})

    data = data.encode('utf-8')

    req = urllib.request.urlopen('http://52.34.128.215:8983/solr/recipeally/select', data)
    
    content = req.read()

    reply = json.loads(content.decode())
    
    reply_response = reply["response"]
    list_recipe = reply_response["docs"]
    context={
            "recipe_list": list_recipe,
            "form3": form3
            }
    return render(request, "recipe.html",context)



