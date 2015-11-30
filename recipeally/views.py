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


def comment(request):
    form=PostForm(request.POST or None)
    context={
    "form": form
    }
    if form.is_valid():
        instance=form.save(commit=False)
        instance.recipe_id=1
        instance.user_id=1
        instance.save()
    return render(request,"comments.html",context)

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
def recipe2(request):
    #f = open(D:/dummy_tweets_future_use/Tweets_iphone6s_reviews_40_english_16092015.json)
    #str = []
    #str = '[{"created_at": "2015-09-16T22:18:25Z", "id": "644274166506479616", "lang_en": "en", "text_en": "Apple iPhone 6s Plus vs. Samsung Galaxy Note 5 Specs, Review: 2 of the Latest ... - Latin Post http://t.co/4iamYbC0P6 #GalaxyNote4", "twitter_hashtags": ["GalaxyNote4"], "twitter_urls": ["note5cases.com", "http://www.note5cases.com", "http://t.co/XoAY430Gux"]},{"created_at": "2015-09-16T22:18:25Z", "id": "644274163398500352", "lang_en": "en", "text_en": "Apple iPhone 6s Plus vs. Samsung Galaxy Note 5 Specs, Review: 2 of the Latest ... - Latin Post http://t.co/VQ0TyZfcF9 #GalaxyNote4", "twitter_hashtags": ["GalaxyNote4"], "twitter_urls": ["note4cases.com", "http://www.note4cases.com", "http://t.co/5QYCbO1e8Q"]}]'
    str =  [{"image": "http://images.media-allrecipes.com/userphotos/250x250/00/96/08/960892.jpg","source": "allrecipes","url": "http://allrecipes.com/Recipe/Garlic-Butter/Detail.aspx","description": "\"Sometimes the basics are the best!  I've used this simple recipe for years to make garlic bread, and any leftovers go great on barbequed steaks, pasta, rice or potatoes. You can use any butter or margarine you like. Also, fresh or minced garlic in a jar works well. Adjust the amount of garlic to your taste.\"","id": "516c3d7996cc62548fd2b14a","name": "Garlic Butter","_version_": 1519165045568700416,"prepTime": "PT10M","ingredients": "1 cup butter, softened 1 tablespoon minced garlic 1/4 cup grated Parmesan cheese 1 tablespoon garlic salt 1 teaspoon Italian seasoning 1/2 teaspoon ground black pepper 1/4 teaspoon ground paprika","recipeYield": "1 cup"}, {"image": "http://ichef.bbci.co.uk/food/ic/food_16x9_448/recipes/prawnswithgarlicbutt_86031_16x9.jpg","source": "bbcfood","url": "http://www.bbc.co.uk/food/recipes/prawnswithgarlicbutt_86031","description": "This simple recipe for prawns in a garlicky sauce makes a delicious addition to a tapas spread - just add lots of crusty bread.","id": "51607c0c96cc6208c179367c","name": "Prawns with garlic butter","recipeYield": "Serves 2-3","_version_": 1519165023563284480,"prepTime": "PT30M","ingredients": "1 tbsp olive oil 50g/2oz butter 12 large raw prawns 2 garlic salt and freshly ground black pepper small handful parsley","cookTime": "PT10M"}]
    
    #a = []
    #a = json.loads(str)
    #for x in a:
        #str1 = x["id"]
    context={
                "recipe_list": str
            }
    return render(request, "recipe.html",context)

def recipe(request):

    #context = RequestContext(request)

    pdb.set_trace()

    if request.method == 'GET':

        search_context = request.GET['q']

        search_context = search_context.strip()
        formatted_string = search_context.replace(",", " ")
        formatted_string = ' '.join(formatted_string.split())

        data = urllib.parse.urlencode({'q': formatted_string, 'wt': 'json', 'indent': 'true'})

        data = data.encode('utf-8')

        req = urllib.request.urlopen('http://52.34.128.215:8983/solr/recipeally/select', data)
        
        content = req.read()

        # reply = json.loads(content)

        reply = json.loads(content.decode())
        #print(reply)

        #final_reply = json.dumps(reply)

        for data in reply:
        # now song is a dictionary
            for attribute, value in data.iteritems():
                print(attribute)
                print (value) # example usage

        #print(final_reply)




