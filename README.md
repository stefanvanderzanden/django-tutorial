# Django-tutorial
Small Django Tutorial with Docker

## Start server
Vanuit de root van het project, run `docker-compose up --build`. 
Dit zal een server starten die je kunt benaderen vanaf localhost:18000

## Django structuur
### mysite
De root is `mysite` en daaronder heb je de een manage.py. 
Dit command kun je gebruiken voor het uitvoeren van allerlei management functies, zoals bijv. het uitvoeren van migraties 
of het starten van de ontwikkelserver.

#### settings.py
Hier staan de settings gedefinieerd voor het project. Bijv. configuratie van de database (`DATABASES`)

#### urls.py
Dit is de routing van de applicatie en hier kun je zelf ook eigen routes aan toevoegen per app 
(uitleg over app zie hieronder bij `myapp`)

### myapp
Dit is een app waarvan er meerdere binnen een django applicatie kunnen bestaan. 
Deze bestaat uit verschillende bestanden (Open de bestanden voor voorbeelden)

#### migrations
Folder voor alle migratie bestanden

#### templates
Hier worden alle templates van een app onder bewaard.
Deze wordt niet standaard aangemaakt, maar kun je toevoegen bij het aanmaken van een nieuwe app
Best practice is om hierin een folder te maken met de naam van je app zodat je bij het gebruik van de templates weet 
uit welke app een template komt. 

Bijv. als je twee `custom-page.html` pagina's hebt, zie je aan het path `app1/custom-page.html` of `app2/custom-page.html` 
uit welke app de template komt.

#### admin.py
Hier kun je formulieren en overzichten creëren van de modellen

#### models.py
Hier kun je je modellen definiëren die staan voor verschillende tabellen in de database

#### views.py
Hier kun je zogenaamde `views` definiëren die logica van verschillende pagina's bepalen en (meestal) een template renderen

## Django commando
Je kunt inloggen op de container `docker exec -it django-tutorial-container bash` en een van de volgende commando's uitvoeren
1. `python manage.py makemigrations` --> Wanneer je iets aan de modellen verandert, zorgt dit commando voor de migratie bestanden die je met `migrate` kunt uitvoeren
2. `python manage.py migrate` --> pas de migraties toe op je database
3. `python manage.py createsuperuser` --> maak een superuser aan waarmee je kunt inloggen op http://localhost:18000/admin


## Maak een nieuwe app
1. Log in op de container en run `django-admin startapp [APP_NAME]`
2. Voeg de app toe aan de `INSTALLED_APPS` in `_project/settings.py`

