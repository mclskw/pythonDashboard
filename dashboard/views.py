from django.shortcuts import render, redirect

def dashboard_view(request):
    # Logic for your dashboard goes here
    return render(request, 'index.html')

#def dashboard_view(request):
        # Logic for your dashboard goes here
 #       return redirect('dashboard/django_plotly_dashapp/DiabetesDashboard/')