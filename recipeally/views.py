from django.shortcuts import render

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
def recipe(request):
    context={
                "title":"Welcome"
            }
    return render(request, "recipe.html",context)