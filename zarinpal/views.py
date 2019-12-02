from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404
from zeep import Client
from orders.models import Order


MERCHANT = '0e25eef0-f310-11e7-814b-000c295eb8fc'
client = Client('https://www.zarinpal.com/pg/services/WebGate/wsdl')
# amount = 20000
description = "ازخریدشما متشکریم"  # Required
CallbackURL = 'http://localhost:8000/zarinpal/verify' # Important: need to edit for realy server.


def send_request(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)
    global amount
    amount = order.get_total_cost()
    result = client.service.PaymentRequest(MERCHANT, amount, description, CallbackURL=CallbackURL)
    if result.Status == 100:
        return redirect('https://www.zarinpal.com/pg/StartPay/' + str(result.Authority))
    else:
        return HttpResponse('Error code: ' + str(result.Status))


def verify(request):
    if request.GET.get('Status') == 'OK':
        result = client.service.PaymentVerification(MERCHANT, request.GET['Authority'], amount)
        if result.Status == 100:
            return HttpResponse('Transaction success.\nRefID: ' + str(result.RefID))
        elif result.Status == 101:
            return HttpResponse('Transaction submitted : ' + str(result.Status))
        else:
            return HttpResponse('Transaction failed.\nStatus: ' + str(result.Status))
    else:
        return HttpResponse('Transaction failed or canceled by user')
