from bot.serializers import ImageSerializer
from bot.models import Image, Order, Product
from django.http.response import JsonResponse
from django.shortcuts import render
import datetime
import random
import json
import emoji
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
import requests
from requests.auth import HTTPBasicAuth


def multiply(num1, num2):
	answer=num1 * num2
	return answer


message= emoji.emojize("""
*Some commands you can give me:* :sunglasses:

:heavy_check_mark: *'shops':* Get a list of all merchants available on Kwyk :hotel:

:heavy_check_mark: *'merchants':* Get a list of all merchants available on Kwyk :hotel:

:heavy_check_mark: *'patners':* Get a list of all merchants available on Kwyk :hotel:

:heavy_check_mark: i want *[quantity] [product]* from *[merchant]* am in *[location]*: Start ordering process:tada:

:heavy_check_mark: send *[quantity] [product]* from *[merchant]* to *[location]*: Start ordering process:tada:

:heavy_check_mark: deliver *[quantity] [product]* from *[merchant]* to *[location]*: Start ordering process:tada:

:heavy_check_mark: *[shop name]*: Get all products sold by that shop :convenience_store:

:heavy_check_mark: show me *[shop name]*: Get all products sold by that shop :convenience_store:
""", use_aliases=True)

@csrf_exempt
def start_up(request):
    if request.method == 'POST':
		#    num= request.POST.get('From')
		#    print(num)
		   response={
       "actions": [
		{
			"show": {
				"images": [
					{
						"label": f"Here are our Merchants",
						"url": 'https://53fe58a0bbc0.ngrok.io/media/images/Whats_app_order_1.jpg'#make it dynamic
					}
				],
				"body": f"Here are our Merchants",
			}
		},
		{
			"say": {
				"speech": f"Hello there 👋🏾! Poa sana , my name is Kwyk AI" + f" and I help wonderful users like you place and pay for orders right here on WhatsApp 😊"
			}
		},
		{
			"collect": {
				"name": "customer",
				"questions": [
					{
						"question": f"What is your name?",
						"name": "first_name",
						"type": "Twilio.FIRST_NAME"
					},
                    {
						"question": f"Great, your phone number is?",
						"name": "phone_number",
						"type": "Twilio.NUMBER"
					}
				],
				"on_complete": {
					"redirect": "https://53fe58a0bbc0.ngrok.io/bot/done_deal"
				}
			}
		}
	]
    }
    return JsonResponse(response)


@csrf_exempt
def shops(request):
    if request.method == 'POST':
		   response={
       "actions": [
		{
			"show": {
				"images": [
					{
						"label": f"Here are our Merchants",
						"url": 'https://53fe58a0bbc0.ngrok.io/media/images/Whats_app_order_1.jpg'#make it dynamic
					}
				],
				"body": f"Here are our Merchants",
			}
		}
	]
    }
    return JsonResponse(response)

@csrf_exempt
def order(request):
    if request.method == 'POST':
	    shop= request.POST.get('Field_shop_name_Value')
	    loc= request.POST.get('Field_location_Value')
	    item = request.POST.get('Field_prod_Value')
	    qty=request.POST.get('Field_qty_Value')
	    memory=json.loads(request.POST.get('Memory'))
	    answers=memory['twilio']['collected_data']['customer']['answers']
	    c_name=answers['first_name']['answer']
	    c_phone=answers['phone_number']['answer']
       
    response= {
       "actions": [
		{
			"say": "Cool I'll help with that. "
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
						"question": f"Great! You want the order delivered in {loc} right?",
						"name": "location",
						"type": "Twilio.YES_NO"
					}
				],
				"on_complete": {
					"redirect": "https://53fe58a0bbc0.ngrok.io/bot/complete_order"
				}
			}
		}
	]
    }
    return JsonResponse(response)


@csrf_exempt
def complete_order(request):
    if request.method == 'POST':
	    shop= request.POST.get('Field_shop_name_Value')
	    loc= request.POST.get('Field_location_Value')
	    item = request.POST.get('Field_prod_Value')
	    qty=request.POST.get('Field_qty_Value')
	    memory=json.loads(request.POST.get('Memory'))
	    answers=memory['twilio']['collected_data']['customer']['answers']
	    c_name=answers['first_name']['answer']
	    c_phone=answers['phone_number']['answer']
	    print(c_name,c_phone)
	    x=Product.objects.get(name=item.lower())
	    if x:
		    total=multiply(int(x.price), int(qty))
		    print(total)
	    Order.objects.create(
			product=x,
			# shop=shop,
			quantity=qty,
			location=loc,
			customer=c_name
		)
	
    response= {
       "actions": [
		     
		{
			"say": f"Hold on a second...calculating the totals..."
		},
		{
			"say": f"""Alright {c_name} here is your cart 🛒 and will cost KSHS {total:.2f}"""
		},
		{
			"collect": {
				"name": "post_process",
				"questions": [
					{
						"question": f"I am going to ask you to make a payment now :)",
						"name": "true_false",
						"type": "Twilio.YES_NO"
					},
                   
				],
				"on_complete": {
					"redirect": "https://53fe58a0bbc0.ngrok.io/bot/make_payment"
				}
			}
		}
	]
    }
    return JsonResponse(response)



@csrf_exempt
def make_payment(request):
    if request.method == 'POST':
	    item = request.POST.get('Field_prod_Value')
	    qty=request.POST.get('Field_qty_Value')
	    memory=json.loads(request.POST.get('Memory'))
	    answers=memory['twilio']['collected_data']['customer']['answers']
	    c_name=answers['first_name']['answer']
	    c_phone=answers['phone_number']['answer']
	    x=Product.objects.get(name=item.lower())
	    if x:
		    total=multiply(int(x.price), int(qty))
		    print(total)
	    
	    mpesa_endpoint='https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest'
	    headers={"Authorization": "Bearer %s" % get_token()}
	    req_body={
                 "BusinessShortCode": "174379",
                 "Password": "MTc0Mzc5YmZiMjc5ZjlhYTliZGJjZjE1OGU5N2RkNzFhNDY3Y2QyZTBjODkzMDU5YjEwZjc4ZTZiNzJhZGExZWQyYzkxOTIwMTgwNDA5MDkzMDAy",
                 "Timestamp": "20180409093002",
                 "TransactionType": "CustomerPayBillOnline",
                 "Amount": total,
                 "PartyA": "254743236834",
                 "PartyB": "174379",
                 "PhoneNumber": c_phone,
                 "CallBackURL":base_url,
                 "AccountReference": "account",
                 "TransactionDesc": "test" ,
                }
	    response_data=requests.post(
                  mpesa_endpoint,
                  json=req_body,
                  headers=headers,
                  )
	    return response_data.json()
	
    response= {
       "actions": [
		{
			"say": f"An Mpesa pop up will display , please enter your PIN to authorise payment."
		},{
			"collect": {
				"name": "post_process",
				"questions": [
					{
						"question": f"Have you made payment ?",
						"name": "true_false",
						"type": "Twilio.YES_NO"
					},
                   
				],
				"on_complete": {
					"redirect": "https://53fe58a0bbc0.ngrok.io/bot/done_deal"
				}
			}
		}
	]
    }
	#send notification to merchant.id, customer care
    return JsonResponse(response)



@csrf_exempt
def done_deal(request):
    if request.method == 'POST':
	    memory=json.loads(request.POST.get('Memory'))
	    print(memory)
	    answers=memory['twilio']['collected_data']['customer']['answers']
	    c_name=answers['first_name']['answer']
	    c_phone=answers['phone_number']['answer']
	    print(c_name,c_phone)
	    response= {
       "actions": [
		   {
			"say": {
				"speech": f"Am delighted to connect with you, {c_name} 😊"
			}
		},
		{
			"say": {
				"speech": f"{message}"
			}
		}	
		
	]
    }
    return JsonResponse(response)



@csrf_exempt
def get_shop_poster(request):
    if request.method == 'POST':
	    shop= request.POST.get('Field_shop_Value')
	    x=Image.objects.get(name=shop)
	    print(x)
	    image=x.image.url
	    print(image)
	
    response={
       "actions": [
		{
			"show": {
				"images": [
					{
						"label": f"{shop}'s products",
						"url": 'https://53fe58a0bbc0.ngrok.io/media/images/Kakila.jpg'#make it dynamic
					}
				],
				"body": f"{shop}'s products",
			}
		},
		{
			"say": {
				"speech": f"Getting {shop}'s products..."
			}
		}
	]
    }
    return JsonResponse(response)


consumer_key='GG8EvAN7sbUMtanArLSSfUsE0rjL55m7'

consumer_secret='3JmnEJq8qgYCBN0A'
base_url='https://53fe58a0bbc0.ngrok.io'

@csrf_exempt
def push(request):
    mpesa_endpoint='https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest'
    headers={"Authorization": "Bearer %s" % get_token()}
    req_body={
    "BusinessShortCode": "174379",
    "Password": "MTc0Mzc5YmZiMjc5ZjlhYTliZGJjZjE1OGU5N2RkNzFhNDY3Y2QyZTBjODkzMDU5YjEwZjc4ZTZiNzJhZGExZWQyYzkxOTIwMTgwNDA5MDkzMDAy",
    "Timestamp": "20180409093002",
    "TransactionType": "CustomerPayBillOnline",
    "Amount": "1",
    "PartyA": "254713754946",
    "PartyB": "174379",
    "PhoneNumber": "254743236834",
    "CallBackURL":base_url + "/c2b/confirm",
    "AccountReference": "account",
    "TransactionDesc": "test" ,
    }
    response_data=requests.post(
        mpesa_endpoint,
        json=req_body,
        headers=headers,
    )
    return response_data.json()


def token():
    data=get_token()
    return data
   

def get_token():
    mpesa_auth_url='https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
    data= (requests.get(mpesa_auth_url, auth=HTTPBasicAuth(consumer_key, consumer_secret))).json()
    return data['access_token']



class ImageViewset(viewsets.ModelViewSet):
	queryset=Image.objects.all()
	serializer_class=ImageSerializer
