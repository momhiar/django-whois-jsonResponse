# django-whois-jsonRespons
a simple, lightweight view written in python django to check whois



really simple and useful when you wanna create a Domain availability check with json
it uses POST method and simply redirects GET requests to a address you want, check views.py

request method: POST method no csrf needed with a json body with blow syntax:


    {
      "domain_name": "YOUR_DESIRED_DOMAIN_NAME",
      "tld": ".com"
    }
