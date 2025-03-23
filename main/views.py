from django.shortcuts import render
from django.http import JsonResponse

USERS = [
    {"username": "katherine", "email": "cat@example.com", "signup_date": "2024-15-03"},
    {"username": "octopus", "email": "octopus@example.com", "signup_date": "2024-16-03"},
    {"username": "pudding", "email": "pudding@example.com", "signup_date": "2024-17-03"},
]

PRODUCTS = [
    {"id": 1, "name": "mouse", "price": 100},
    {"id": 2, "name": "keyboard", "price": 200},
    {"id": 3, "name": "headphone", "price": 300},
]

COMMENTS = [
    {"id": 1, "product_id": 1, "user": "user1", "comment": "very good"},
    {"id": 2, "product_id": 1, "user": "user2", "comment": "เอาไปเลย 5 ดาว"},
    {"id": 3, "product_id": 1, "user": "user3", "comment": "ชอบมากค่ะ"},
    {"id": 4, "product_id": 2, "user": "user1", "comment": "แย่มาก"},
    {"id": 5, "product_id": 2, "user": "user2", "comment": "เอาไปเลยหนึ่งนิ้วโป้ง"},
]

def user_detail(request, username):
    user_data = None
    for user in USERS:
        if user["username"] == username:
            user_data = user
            break
    
    if not user_data:
        return JsonResponse({"error": "User not found"}, status=404)

    if request.GET.get("format") == "json":
        return JsonResponse(user_data)
    
    return render(request, "user.html", user_data)

def product_all(request):
    if request.GET.get("format") == "json":
        return JsonResponse(PRODUCTS, safe=False)
    return render(request, "product_all.html", {"products": PRODUCTS})

def productById(request, id):
    product = None
    for p in PRODUCTS:
        if p["id"] == id:
            product = p
            break

    if not product:
        return JsonResponse({"error": "Product not found"}, status=404)
    
    if request.GET.get("format") == "json":
        return JsonResponse(product)
    
    return render(request, "productById.html", product)

def comment(request, id):
    filtered_comments = []
    for c in COMMENTS:
        if c["product_id"] == id:
            filtered_comments.append(c)

    if request.GET.get("format") == "json":
        return JsonResponse(filtered_comments, safe=False)

    return render(request, "comment.html", {"comments": filtered_comments, "id": id})

def summarize(request):
    mock_data = {
        "total_products": len(PRODUCTS),
        "total_orders": 10,
        "total_comments": len(COMMENTS)
    }

    if request.GET.get("format") == "json":
        return JsonResponse(mock_data)

    return render(request, "summarize.html", mock_data)
