from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import OrderProduct

def index(request):
    return render(request, 'myapp/index.html')

@csrf_exempt
def checkout(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            cart_items = data.get('cartItems', [])
            total_price = data.get('totalPrice', 0)
            notes = data.get('notes', '')

            # 檢查購物車是否為空
            if not cart_items:
                return JsonResponse({'message': '購物車是空的，請添加商品後再結帳。'}, status=400)

            # 保存訂單到資料庫
            order = OrderProduct.objects.create(
                customer_name="客人姓名",  # 這裡可以根據實際情況獲取客人資訊
                customer_phone="客人電話",  # 這裡可以根據實際情況獲取客人資訊
                cart_item=cart_items,
                total_price=total_price,
                notes=notes
            )

            print(f"收到的購物車項目: {cart_items}")
            print(f"總金額: {total_price}")
            print(f"備註: {notes}")
            return JsonResponse({'message': '結帳成功！', 'redirect': '/confirmation/'})
        except json.JSONDecodeError:
            return JsonResponse({'message': '無效的數據'}, status=400)
    return redirect('index')

def confirmation(request):
    return render(request, 'myapp/confirmation.html')

def total(request):
    return render(request, 'myapp/total.html')

def review_order(request):
    return render(request, 'myapp/review_order.html')