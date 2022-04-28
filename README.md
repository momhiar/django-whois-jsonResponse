# django-whois-jsonRespons
a simple, lightweight view written in python django to check whois



really simple and useful when you wanna create a Domain availability check with json
it uses POST method and simply redirects GET requests to a address you want, check views.py
NOTE: .ir domains have an issue : if you encounter an error it results True anyway.

request method: POST method no csrf needed with a json body with blow syntax:


    {
      "domain_name": "YOUR_DESIRED_DOMAIN_NAME",
      "tld": ".com"
    }


there is responses based on blow syntax:

    {
     "result": "{result}",
     "domain": "YOUR_DESIRED_DOMAIN_NAME.tld"
    }
   
   results:
   "True" if domain is available
   "False" if domain is not available
   "socket" if backend encounters an socket error
