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
from recipesearch.models import User, UserProfile, Comments
from django.contrib.auth.decorators import login_required

from django.contrib.auth import logout

from django.dispatch import Signal
def registration(request):
    #pdb.set_trace()
    title = 'Welcome'
    # if request.user.is_authenticated():
    #   title="My Title %s" %(request.user)
    # print request
    # if request.method=="POST":
    #   print(request.POST)
    form = SignUpForm(request.POST or None)
    form2 = ProfileForm(request.POST or None)
    context = {
        "title": title,
        "form": form,
        "form2": form2
    }

    if form.is_valid():
        if form2.is_valid():
            instance = form.save(commit=False)
            instance.save()
            instance2 = form2.save(commit=False)
            instance2.user = instance
            instance2.save()

            context = {
                "title": "Thank You"
            }
    if request.user.is_authenticated():
        context={"title":"You are already logged in"}
        return render(request, "home.html", context)
    return render(request, "registration.html", context)


def user_login(request):
    # Like before, obtain the context for the user's request.
    context = RequestContext(request, {'errormessage': ''})
    
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
            # print "Invalid login details: {0}, {1}".format(username, password)
            # return HttpResponse("Invalid login details supplied.")
            context = RequestContext(
                request, {
                    'errormessage': 'Invalid login details supplied.'})
            return render_to_response('login.html', {}, context)

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        if request.user.is_authenticated():
            context={"title":"You are already logged in"}
            return render(request, "home.html", context)
        return render(request, "login.html", context)


@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/')


# Display a particular recipe.
def recipe(request):

    form3 = PostForm(request.POST or None)

    if request.method == "POST":

        recipe_id = request.POST["id"]
        current_user=request.user.id
        if(current_user != None):
            if form3.is_valid():
                instance = form3.save(commit=False)
                instance.user_id = request.user.id
                instance.recipe_str = recipe_id
                instance.save()

                form3 = PostForm()

                context = {
                    "form3": form3
                }
        else:
            context={
            "form3": '<a href="/login">Log in </a> to comment'
            }

    search_context = request.GET['q']

    search_context = search_context.strip()
    formatted_string = search_context.replace(",", " ")
    formatted_string = ' '.join(formatted_string.split())

    data = urllib.parse.urlencode(
        {'q': formatted_string, 'wt': 'json', 'indent': 'true'})

    data = data.encode('utf-8')

    req = urllib.request.urlopen(
        'http://52.34.128.215:8983/solr/recipeally/select', data)

    content = req.read()

    reply = json.loads(content.decode())

    reply_response = reply["response"]
    list_recipe = reply_response["docs"]
    current_user=request.user.id
    if(current_user == None):
        form3=''
    logged_in=current_user != None
    context = {
        "recipe_list": list_recipe,
        "form3": form3,
        "logged_in": logged_in
    }
    return render(request, "recipe.html", context)

def returnCommentsData(list_recipe):
    pdb.set_trace()
    for recipe in list_recipe:
        comment_id = recipe['id']
        comments = Comments.objects.all().filter(recipe_str = comment_id)
        if comments is not None:
            print(comments)