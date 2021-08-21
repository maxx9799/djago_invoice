
from myapi.models import Invoice
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .forms import ProductForm
from .models import *


from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.views.generic import ListView



# Create your views here.
def home(request):
    f = ProductForm()
    return render(request, 'invoice.html', {'form' : f})



# def detail(request, pk):
# 	task = Invoice.objects.get(id=pk)

# 	form = ProductForm(instance=task)

# 	if request.method == 'POST':
# 		form = ProductForm(request.POST, instance=task)
# 		if form.is_valid():
# 			form.save()

# 	context = {'form':form}

# 	return render(request, 'detail.html', context)


def detail(request):
    form = ProductForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect(render_pdf_view)

    data = Invoice.objects.all()
    return render(request, "new.html", {'data':data})

def render_pdf_view(request, *args, **kwargs):
    pk = kwargs.get('pk')
    customer = get_object_or_404(Invoice, pk=pk)
    template_path = 'detail.html'
    context = {'customer': customer}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response



