from django.shortcuts import render
from django.views.generic import TemplateView


class MyClassBasedView(TemplateView):
    template_name = "my"


def my_function_view(request):
    return render(request, "myapp/function-template.html", {"name": "Johan"})