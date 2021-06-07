from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
import datetime
import random
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def start_up(request):
    if request.method == 'POST':
        message = request.POST.get("Body")
        print(message)
        data= {
        'actions': [
                     {'say': f"Hello my name is Kwyk AI, what can I help you with today?"},
                     {'listen': True},
                    ]
                }
    return JsonResponse(data)

@csrf_exempt
def order(request):
    if request.method == 'POST':
        shop= request.POST.get('Field_shop_name_Value')
        item = request.POST.get('Field_prod_Value')
        qty=request.POST.get('Field_qty_Value')
        #send to firebase
	    #generate user location number
        response= {
       "actions": [
		{
			"say": "I'll help with that. "
		},
		{
			"say": "Hold on as I analyse your requirements. "
		},
		{
			"collect": {
				"name": "order_product",
				"questions": [
					{
						"question": f"Gotcha! So you want to order {qty} {item} from {shop} . Is this correct?",
						"name": "true_false",
						"type": "Twilio.YES_NO"
					},
                    {
						"question": "Where are you located?",
						"name": "location",
						"type": "Twilio.CITY"
					},
					{
						"question": "Awesome, I will update the cart with your location as the point of delivery, is it okay?",
						"name": "affirm",
						"type": "Twilio.YES_NO"
					}
				],
				"on_complete": {
					"redirect": "task://complete_order"
				}
			}
		}
	]
    }
    return JsonResponse(response)