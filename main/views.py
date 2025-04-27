from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.models import User
from .models import Product, Order, ProductOrder

def user_detail(request, username):
    user = get_object_or_404(User, username=username)

    user_data = {
        "email": user.email,
        "signup_date": user.date_joined.strftime("%Y-%d-%m"),
        "username": user.username
    }
    return JsonResponse(user_data)

def product_all(request):
    products = Product.objects.all()
    product_list = []
    for product in products:
        product_list.append({
            "id": product.id,
            "name": product.name,
            "price": product.price,
            "stock": product.stock,
            "category": product.category
        })
    return JsonResponse(product_list, safe=False)

def productById(request, id):
    try:
        product = Product.objects.get(id=id)
        product_data = {
            "id": product.id,
            "name": product.name,
            "price": product.price,
            "stock": product.stock,
            "category": product.category
        }
        return JsonResponse(product_data)
    except Product.DoesNotExist:
        return JsonResponse({"error": "Product ID not Found!"}, status=404)

def order_by_product_id(request, id):
    product_orders = ProductOrder.objects.filter(product_id=id)

    if not product_orders.exists():
        return JsonResponse({"error": "No orders found for this product ID!"}, status=404)

    order_list = []
    for po in product_orders:
        order_list.append({
            "order_id": po.order.id,
            "customer": po.order.customer.username,
            "product": po.product.name,
            "quantity": po.quantity,
            "total_price": po.total_price,
            "order_status": po.order.status
        })
    return JsonResponse(order_list, safe=False)

def summarize(request):
    summary_data = {
        "total_products": Product.objects.count(),
        "total_orders": Order.objects.count(),
        "total_users": User.objects.count()
    }
    return JsonResponse(summary_data)
