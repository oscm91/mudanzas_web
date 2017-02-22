from django.http import JsonResponse
from django.views.generic import View
import os
from ecommerce.settings import MEDIA_ROOT, MEDIA_URL

from .forms import CargoForm
from .models import TxtFile

import requests as requests_api


class CargoUploadView(View):
    def post(self, request):
        form = CargoForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            txt_file = form.save()

            data = {
                'days': None,
                'items': [],
            }

            with open(os.path.join(MEDIA_ROOT, txt_file.qqfile.name)) as txt_file_source:
                content_file = [x.strip() for x in txt_file_source]

            data['days'] = int(content_file[0])
            del content_file[0]
            i = 0

            while i < len(content_file):
                data['items'].append({'values': content_file[int(i + 1): i + int(content_file[i]) + 1]})
                i = i + int(content_file[i]) + 1

            resp = requests_api.post('http://138.68.48.167:3000/api/trackings', json=data)

            if resp.status_code != 200:
                resultJSON = {'success': False, 'error': '%s' % repr(resp.status_code)}
            else:
                jsonFileResult = resp.json()
                jsonFileResultUrl = os.path.join(MEDIA_ROOT, txt_file.qqfile.name.replace('.txt', 'result.txt'))

                try:
                    with open(jsonFileResultUrl, 'w') as txt_file_source_resolved:
                        for item in jsonFileResult:
                            txt_file_source_resolved.write("Case #{0}: {1}\n".format(item['id'], item['maxTravels']))
                except Exception as e:
                    raise e

                txt_file.qqfilesolved = jsonFileResultUrl.replace(MEDIA_ROOT + '/', MEDIA_URL)
                txt_file.qqworkdays = data['days']
                txt_file.save()

                resultJSON = {'success': True, 'name': txt_file.qqfile.name,
                              'url': jsonFileResultUrl.replace(MEDIA_ROOT + '/', MEDIA_URL),
                              'data': resp.json()}
        else:
            resultJSON = {'success': False, 'error': '%s' % repr(form.errors)}
        return JsonResponse(resultJSON)
