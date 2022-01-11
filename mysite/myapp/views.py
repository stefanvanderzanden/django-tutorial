from django.shortcuts import render
from django.views.generic import TemplateView


class MyClassBasedView(TemplateView):
    template_name = "myapp/class-template.html"

    def get_context_data(self, **kwargs):
        context = super(MyClassBasedView, self).get_context_data(**kwargs)
        context.update(
            name="Johan"
        )
        return context


def my_function_view(request):
    return render(request, "myapp/function-template.html", {"name": "Johan"})