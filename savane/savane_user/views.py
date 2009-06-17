from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django import forms

def index( request ):
    return render_to_response( 'savane_user/index.html',
                               RequestContext( request,
                                               ) )
def sv_login( request ):
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate( username=username, password=password )

    if user is not None:
        login( request, user )
    else:
        login_error = u"User or password didn't match"
        return render_to_response( 'error.html',
                                   {'error' : login_error
                                    } )

    return HttpResponseRedirect ( '/' )

def sv_logout( request ):
    logout( request )

    return HttpResponseRedirect( '/' )


def sv_conf( request ):

    form_pass = PasswordForm ()
    form_mail = MailForm ()
    form_identity = IdentityForm ()

    return render_to_response( 'savane_user/conf.html',
                               RequestContext( request,
                                               { 'form_pass' : form_pass,
                                                 'form_mail' : form_mail,
                                                 'form_identity' : form_identity,
                                                 }
                                               ) )
def sv_identity( request ):

    if 'action' in request.POST and request.user.is_authenticated():
        request.user.first_name = request.POST['new_name']
        request.user.last_name = request.POST['new_last_name']
        request.user.save()

    return render_to_response( 'savane_user/identity.html',
                               RequestContext( request,
                                               ) )
def sv_authentication( request ):
    if request.user.is_authenticated() is False:
        return HttpResponseRedirect( '/' )

    error = ''
    if request.method == 'POST':
        form = PasswordForm( request.POST )

        if form.is_valid():
            if request.user.check_password( request.POST['old_password'] ):
                form = PasswordForm( )
                return render_to_response( 'savane_user/authentication.html',
                                           RequestContext( request,
                                                           { 'form' : form,
                                                             'success_message' : success,}
                                                           ) )
            else:
                return render_to_response( 'savane_user/authentication.html',
                                           RequestContext( request,
                                                           { 'form' : form,
                                                             'error_message' : "Current password doesn't match",}
                                                           ))
        else:
            error = u"Isn't valid"
    else:
        form = PasswordForm()

    return render_to_response( 'savane_user/authentication.html',
                               RequestContext( request,
                                               {'form' : form,
                                                'error_message' : error,}
                                               ) )


def sv_mail( request ):

    if request.method == 'POST':
        form = MailForm( request.POST )

        if form.is_valid():
            request.user.email = request.POST['email']
            request.user.save()
            return render_to_response( 'savane_user/mail.html',
                                       RequestContext( request,
                                                       { 'form' : form,
                                                         'success_message' : 'The E-mail address was succesfully changed'
                                                         }
                                                       ) )
        else:
            return render_to_response( 'savane_user/mail.html',
                                       RequestContext( request,
                                                       { 'form' : form,
                                                         'error_message' : 'Could not change the e-mail address'
                                                         }
                                                       ) )
    else:
        form = MailForm()

    return render_to_response( 'savane_user/mail.html',
                               RequestContext( request,
                                               { 'form' : form }
                                               ) )

class MailForm( forms.Form ):
    email = forms.CharField(required=True)

class PasswordForm( forms.Form ):
    old_password = forms.CharField(widget=forms.PasswordInput,required=True)
    new_password = forms.CharField(widget=forms.PasswordInput,required=True)
    repated_password = forms.CharField(widget=forms.PasswordInput,required=True)
    accion = forms.CharField( widget=forms.HiddenInput, required=True, initial='update_password' )

    def clean( self ):
        cleaned_data = self.cleaned_data
        new_password = cleaned_data.get('new_password')
        old_password = cleaned_data.get('old_password')

class IdentityForm( forms.Form ):
    name = forms.CharField( required = True )
    last_name = forms.CharField( required = False )
