from bot.serializers import ImageSerializer
from bot.models import Image, Order, Product
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
import datetime
import random
import json
import emoji
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
import requests
from requests.auth import HTTPBasicAuth
import spacy

def multiply(num1, num2):
	answer=num1 * num2
	return answer


message= emoji.emojize("""
*Some commands you can give me:* :sunglasses:

:heavy_check_mark: *[sasa][hey][hi][hello][vipi]*: Greet me and place your order:wave:

:heavy_check_mark: *'merchants':* Get a list of all merchants available on Kwyk :hotel:

:heavy_check_mark: *[quantity][product][merchant][location][phone]*: Start ordering process:tada:

:heavy_check_mark: *Example 1*: 3 mangoes Kakila Nairobi 254712754946 :tada:

:heavy_check_mark: *[shop name]*: Get posters of products sold by that shop :convenience_store:
""", use_aliases=True)

@csrf_exempt
def start(request):
    if request.method == 'POST':
	    phone= request.POST['From']
	    speech=request.POST['Body'].lower()
	    response={
       "actions": [
		{
			"say": {
				"speech": f"Hello there {phone}, you said {speech}"
			}
		},
	]
    }
    return JsonResponse(response)

@csrf_exempt
def start_up(request):
    if request.method == 'POST':
		   response={
       "actions": [
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
						"question": f"What's your name?",
						"name": "first_name",
						"type": "Twilio.FIRST_NAME"
					},
                    {
						"question": f"Great, what's your phone number?",
						"name": "phone_number",
						"type": "Twilio.NUMBER"
					}
				],
				"on_complete": {
					"redirect": "https://techwithnick.com/bot/collect_order"
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
						"url": 'https://techwithnick.com/media/images/Whats_app_order_1_2.jpg'#make it dynamic
					}
				],
				"body": f"Here are our Merchants",
			}
		}
	]
    }
    return JsonResponse(response)

@csrf_exempt
def place_order(request):
    if request.method == 'POST':
	    shop= request.POST.get('Field_shop_name_Value')
	    loc= request.POST.get('Field_location_Value')
	    item = request.POST.get('Field_prod_Value')
	    qty=request.POST.get('Field_qty_Value')
	    mobile=request.POST.get('Field_mobil_Value')
	    memory=json.loads(request.POST.get('Memory'))
       
    response= {
       "actions": [
		{
			"say": "Cool 👍🏾👍🏾 I'll help with that. "
		},
		{
			"say": "Hold on as I process your requirements  🙇🏾‍♂️🙇🏾‍♂️. "
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
					"redirect": "https://techwithnick.com/bot/completed_order"
				}
			}
		},
		{"remember":{'item':item, "quantity":qty, "mobile":mobile}}
	]
    }
    return JsonResponse(response)


@csrf_exempt
def complete_order(request):
    if request.method == 'POST':
	    memory=json.loads(request.POST.get('Memory'))
	    answers=memory['twilio']['collected_data']['order_product']['answers']
	    location=answers['location']['answer']
	    c_phone=memory['phone']
	    c_name=memory['name']
	    sentence=memory['sentence']
	    nlp = spacy.load('en_core_web_sm')
	    about_text = sentence
	    about_doc = nlp(about_text)
	    nouns = []
	    for token in about_doc:
		    if token.pos_ == 'NOUN':
			    nouns.append(token)
	    nums=[int(s) for s in about_text.split() if s.isdigit()]
	    try:
		    prod_0=Product.objects.get(name=nouns[0])
	    except IndexError:
		    prod_0=Product.objects.get(name='default')
	    try:
	        prod_1=Product.objects.get(name=nouns[1])
	    except IndexError:
		    prod_1=Product.objects.get(name='default')
	    try:
	        prod_2=Product.objects.get(name=nouns[2])
	    except IndexError:
		    prod_2=Product.objects.get(name='default')
	    try:
	        prod_3=Product.objects.get(name=nouns[2])
	    except IndexError:
		    prod_3=Product.objects.get(name='default')
	    try:
		    qt_0=nums[0]
	    except IndexError:
		    qt_0=0
	    try:
		    qt_1=nums[1]
	    except IndexError:
		    qt_1=0
	    try:
		    qt_2=nums[2]
	    except IndexError:
		    qt_2=0
	    try:
		    qt_3=nums[3]
	    except IndexError:
		    qt_3=0

	    # print(c_phone, item,quantity,location, c_name)
	    # x=Product.objects.get(name=item.lower())
	    if prod_0:
		    total_0=multiply(int(prod_0.price), int(qt_0))
	    if prod_1:
		    total_1=multiply(int(prod_1.price), int(qt_1))
	    if prod_2:
		    total_2=multiply(int(prod_2.price), int(qt_2))
	    total=total_0 + total_1 + total_2
		
	    Order.objects.create(
			product=prod_0,
			quantity=qt_0,
			location=location,
			customer=c_name
		)
	    Order.objects.create(
			product=prod_1,
			quantity=qt_1,
			location=location,
			customer=c_name
		)
	    Order.objects.create(
			product=prod_2,
			quantity=qt_2,
			location=location,
			customer=c_name
		)
	    Order.objects.create(
			product=prod_3,
			quantity=qt_3,
			location=location,
			customer=c_name
		)
	    endpoint='https://api.sms.to/sms/send'
	    auth_token='30KY3acPpY8q7i8diA4MKCgOFUsZnhYE'
	    headers = {'Authorization': 'Bearer ' + auth_token}
	    payload = {
			"message" : f"Dear merchant, {c_name} just placed an order of KSHS {total}. Here is their mobile number {c_phone}.", 
			"to" : "+254713754946", 
			"sender_id" : "SMSto"
               }
	    payload2 = {
			"message" : f"Dear rider head over to Kakila organic ,there is a delivery job for you.", 
			"to" : "+25492793366", 
			"sender_id" : "SMSto"
               }
	    payload3 = {
			"message" : f"An order was placed by {c_name} number {c_phone}.", 
			"to" : "+25492793366", 
			"sender_id" : "SMSto"
               }
	    res=requests.post(endpoint,headers=headers,data=payload)
	
    response= {
       "actions": [
		     
		{
			"say": f"{location}, Cool 👍🏾👍🏾 I'll help with that. "
		},
		{
			"say": "Hold on as I process your requirements  🙇🏾‍♂️🙇🏾‍♂️. "
		},
		# {
		# 	"say": f"Gotcha! So you want to order {quantity} {item} to be delivered in {location}"
			
		# },
		{
			"say": f"Calculating totals...⌛💰⏳"
			
		},
		{
			"say": f"""Alright {c_name} your cart 🛒 will cost KSHS 💵💵{total:.2f} """
			
		},
		{
			"say": f"Mpesa request will be sent to {c_phone}, please pay KSHS {total:.2f}."
		},
		{
					"redirect": f"https://techwithnick.com/bot/pay"
		},
		{"remember":{'phone':c_phone, "total":total}}
		
		
	]
    }
    return JsonResponse(response)


@csrf_exempt
def completed_order(request):
    if request.method == 'POST':
	    shop= request.POST.get('Field_shop_name_Value')
	    loc= request.POST.get('Field_location_Value')
	    item = request.POST.get('Field_prod_Value')
	    qty=request.POST.get('Field_qty_Value')
	    mobile=request.POST.get('Field_mobil_Value')
	    memory=json.loads(request.POST.get('Memory'))

	    x=Product.objects.get(name=item.lower())
	    if x:
		    total=multiply(int(x.price), int(qty))
		    print(total)
	    Order.objects.create(
			product=x,
			quantity=qty,
			location=loc,
			customer=mobile
		)


	
    response= {
       "actions": [
		
		{
			"say": f"Calculating totals...⌛💰⏳"
			
		},
		{
			"say": f"""Alright your cart 🛒 will cost KSHS 💵💵{total:.2f} """
			
		},
		{
			"say": f"Mpesa request sent to {mobile}, please pay KSHS {total:.2f}."
		},
		{
					"redirect": f"https://techwithnick.com/bot/pay"
		},
		{"remember":{'phone':mobile, "total":total}}
	]
    }
    return JsonResponse(response)



@csrf_exempt
def make_payment(request):
    if request.method == 'POST':
	    memory=json.loads(request.POST.get('Memory'))
	    c_phone=memory['phone']
	    total=memory['total']
	    print(total,c_phone)
	    answers=memory['twilio']['collected_data']['pay_now']['answers']
	    jibu=answers['affirm']['answer']
	    if jibu=='YES':
		    pass #push stk to user
	    else:
		    pass #bot says you chose to pay on delivery order sent
	    # phone_number=str(c_phone)
	    code=254
	    minus= c_phone.lstrip(c_phone[0])
	    final_num=f'{code}{minus}'
		
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
                 "PhoneNumber": final_num,
                 "CallBackURL":base_url,
                 "AccountReference": "account",
                 "TransactionDesc": "test" ,
                }
	    response_data=requests.post(
                  mpesa_endpoint,
                  json=req_body,
                  headers=headers,
                  )
	    print(response_data.status_code)
	    return HttpResponse('Issued Mpesa')

	   

@csrf_exempt
def pay(request):
    if request.method == 'POST':
	    memory=json.loads(request.POST.get('Memory'))
	    c_phone=memory['phone']
	    total=memory['total']
	    response= {
       "actions": [
		
		{
			"collect": {
				"name": "pay_now",
				"questions": [
					{
						"question": f"Proceed to pay?",
						"name": "affirm",
						"type": "Twilio.YES_NO"
					}
				],
				"on_complete": {
					"redirect": "https://techwithnick.com/bot/make_payment"
				}
			}
		},
		{"remember":{'phone':c_phone, "total":total}}
	]
    }
    return JsonResponse(response)

products=[
        "mangoes",
        "tomatoes",
        "onions",
        "cabbages",
        "carrots"]

@csrf_exempt
def collect_order(request):
    if request.method == 'POST':
	    memory=json.loads(request.POST.get('Memory'))
	    # print(memory)
	    answers=memory['twilio']['collected_data']['customer']['answers']
	    c_name=answers['first_name']['answer']
	    c_phone=answers['phone_number']['answer']
	    # print(c_name,c_phone)
	    response= {
       "actions": [
		   {
			"say": {
				"speech": f"Am delighted to connect with you, {c_name} 😊"
			}
		},
		{
			"show": {
				"images": [
					{
						"label": f"Here are our shops",
						"url": 'https://techwithnick.com/media/images/Whats_app_order_1_2.jpg'#make it dynamic
					}
				],
				"body": f"Here are our shops",
			}
		},
		{
			"collect": {
				"name": "orders_product",
				"questions": [
					 {
						"question": f"Which shop would you like to order from?",
						"name": "shop",
						"type": "Twilio.FIRST_NAME"
					},
				],
				"on_complete": {
					"redirect": "https://techwithnick.com/bot/continue_collect_order"
				}
			}
		},
		
		{
			"remember": {
				"phone": c_phone,
				"name": c_name
			}
		}		
		
	]
    }
    return JsonResponse(response)



@csrf_exempt
def continue_collect_order(request):
    if request.method == 'POST':
	    memory=json.loads(request.POST.get('Memory'))
	    answers=memory['twilio']['collected_data']['orders_product']['answers']
	    selected_shop=answers['shop']['answer']
	    c_phone=memory['phone']
	    c_name=memory['name']

	    response= {
       "actions": [
		{
			"show": {
				"images": [
					{
						"label": f"Here are {selected_shop}'s products ",
						"url": 'https://techwithnick.com/media/images/Kakila.jpg'#make it dynamic
					}
				],
				"body": f"Here are {selected_shop}'s products ",
			}
		},
		{
			"collect": {
				"name": "ordered_product",
				"questions": [
					{
						"question": f"What products would you like to order?",
						"name": "products",
					}
				],
				"on_complete": {
					"redirect": "https://techwithnick.com/bot/almost_complete_order"
				}
			}
		},
		
		{
			"remember": {
				"phone": c_phone,
				"name": c_name,
				'shop':selected_shop
			}
		}		
		
	]
    }
    return JsonResponse(response)


@csrf_exempt
def almost_complete_order(request):
    if request.method == 'POST':
	    memory=json.loads(request.POST.get('Memory'))
	    answers=memory['twilio']['collected_data']['ordered_product']['answers']
	    utterance=answers['products']['answer']
	    c_phone=memory['phone']
	    c_name=memory['name']

	    response= {
       "actions": [
		{
			"collect": {
				"name": "order_product",
				"questions": [
					 {
						"question": f"Where should your order be delivered?",
						"name": "location",
						"type": "Twilio.CITY"
					}
				],
				"on_complete": {
					"redirect": "https://techwithnick.com/bot/complete_order"
				}
			}
		},
		
		{
			"remember": {
				"phone": c_phone,
				"name": c_name,
				'sentence':utterance
			}
		}		
		
	]
    }
    return JsonResponse(response)

@csrf_exempt
def commands(request):
    if request.method == 'POST':
	    response= {
       "actions": [
		{
			"say": {
				"speech": f"{message}"
			}
		},	
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
						"url": 'https://techwithnick.com/media/images/Kakila.jpg'#make it dynamic
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
    "Amount": 1,
    "PartyA": "254713754946",
    "PartyB": "174379",
    "PhoneNumber": 254713754946,
    "CallBackURL":base_url + "/c2b/confirm",
    "AccountReference": "account",
    "TransactionDesc": "test" ,
    }
    response_data=requests.post(
        mpesa_endpoint,
        json=req_body,
        headers=headers,
    )
    print(response_data.status_code)
    return HttpResponse('Issued Mpesa')


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
