from django.shortcuts import render, redirect
from django.contrib import messages
from .models import connexion
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

def home(request):
    context = {}
    return render(request, "Factures/home.html", context)

def login(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        email = request.POST.get('email')
        mdp = request.POST.get('motdepasse')
        cmdp = request.POST.get('confirmationmdp')
        telephone = request.POST.get('Tel')

        # Validate the nom field
        if not nom.isalpha() or not nom[0].isupper():
            messages.error(request, 'Le nom doit contenir uniquement des lettres et commencer par une majuscule.')

        # Validate the prenom field
        if not prenom.replace(' ', '').isalpha() or not prenom.split()[0][0].isupper():
            messages.error(request, 'Le prénom doit contenir uniquement des lettres et commencer par une majuscule.')

        # Validate the telephone field
        telephone_validator = RegexValidator(r'^(77|78|76|75)\d{7}$')
        try:
            telephone_validator(telephone)
        except ValidationError:
            messages.error(request, 'Le numéro de téléphone doit commencer par 77, 78, 76 ou 75, et doit contenir exactement 9 chiffres.')

        # Validate the motdepasse and confirmationmdp fields
        if mdp != cmdp:
            messages.error(request, 'Les mots de passe ne correspondent pas.')

        # Check if any validation errors occurred
        if messages.get_messages(request):
            return redirect("login")  # Redirect back to the login page if there are validation errors

        try:
            # If all validations pass, create the 'connexion' object and save it to the database
            pers = connexion(nom=nom, prenom=prenom, email=email, Tel=telephone, motdepasse=mdp, confirmationmdp=cmdp)
            pers.save()
            messages.success(request, 'Inscription validée')
            return redirect("home")
        except:
            messages.error(request, 'Inscription non validée')

    context = {}
    return render(request, 'Factures/login.html', context)
