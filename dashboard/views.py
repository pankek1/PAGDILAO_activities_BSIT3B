from django.shortcuts import render

def dashboard_view(request):
    data = [
        {"title": "Users", "count": 150},
        {"title": "Orders", "count": 320},
        {"title": "Revenue", "count": 12450},
    ]
    return render(request, "dashboard.html", {"data": data})

def reports_view(request):
    return render(request, "reports.html")

def settings_view(request):
    return render(request, "settings.html")
