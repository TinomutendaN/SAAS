from django.shortcuts import render
from django.http import HttpResponse
import pathlib
from visits.models import PageVisit

this_dir = pathlib.Path(__file__).resolve().parent

def home_page_view(request, *args, **kwargs):
    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path = request.path) 
    my_title = "My page"
    my_context = {
        "page_title": my_title,
        "page_vist_count": page_qs.count(),
        "percent": (page_qs.count()* 100.0)/qs.count(),
        "total_visit_count": qs.count
    }
    html_template = "home.html"
    PageVisit.objects.create(path = request.path)
    return render(request, html_template, my_context)


def my_old_home_page_view(request, *args, **kwargs):
    my_title = "My page"
    my_context = {
        "page_title": my_title
    }
    html_ = """
    <!DOCTYPE html>
<html>
<body>
    <h1>{page_title} anything ?</h1>
</body>
</html>

    """.format(**my_context)
    return HttpResponse(html_)