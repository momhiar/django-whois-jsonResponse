from django.shortcuts import redirect
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
import json
from whois import whois
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def domain_whois(request):
    def is_domain_available(domain, body):
        try:
            get_info = whois(domain)
            if get_info['domain_name'] is None and body['tld'] != '.ir':
                return 'socket'
            elif body['tld'] == '.ir':
                if get_info['emails'] is None:
                    return True
                else:
                    return False
            return False
        except:
            return True

    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        domain_name = body['domain_name'] + body['tld']

        if body['domain_name'] != '' and len(body['domain_name']) <= 20:
            result = str(is_domain_available(domain_name, body))

        elif len(body['domain_name']) > 20:
            result = 'long'
        elif body['domain_name'] == '':
            result = 'empty'
        else:
            result = str(False)

        return JsonResponse({'result': result,
                             'domain': domain_name})
    else:
        return redirect('https://piroozweb.com')  # TODO replace what url you want!
