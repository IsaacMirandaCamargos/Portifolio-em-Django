from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.messages import constants
from .models import Quote
from django.views.decorators.http import require_http_methods


# Create your views here.

@require_http_methods(['GET'])
def quotes_crud_list(request):
    quotes = Quote.objects.all()
    context = {'quotes': quotes}
    return render(request, 'quotes/index.html', context)




@require_http_methods(['POST'])
def quotes_crud_delete(request):
    quote_id = request.POST.get('quote_id')
    try:
        quote = Quote.objects.get(id=quote_id)
        quote.delete()
        messages.add_message(request, constants.SUCCESS, "Citação deletada com sucesso.")
        return redirect('/quotes/')
    except:
        messages.add_message(request, constants.ERROR, "Erro ao deletar a citação.")
        return redirect('/quotes/')

@require_http_methods(['POST'])
def quotes_crud_edit(request):
    try:
        quote_id = request.POST.get('quote_id')
        quote_thinker = request.POST.get('quote_thinker')
        quote_text = request.POST.get('quote_text')
        quote = Quote.objects.get(id=quote_id)

        quote.text = quote_text
        quote.thinker = quote_thinker

        quote.save()
        messages.add_message(request, constants.SUCCESS, "Citação editada com sucesso.")
        return redirect('/quotes/')
    except:
        messages.add_message(request, constants.ERROR, "Erro ao editar citação.")
        
        return redirect('/quotes/')


@require_http_methods(['POST'])
def quotes_crud_create(request):
    try:
        quote_thinker = request.POST.get('quote_thinker')
        quote_text = request.POST.get('quote_text')

        quote = Quote.objects.create(thinker=quote_thinker, text=quote_text)
        quote.save()

        messages.add_message(request, constants.SUCCESS, 'Sucesso ao criar a citação.')
        return redirect('/quotes/')
    except:
        messages.add_message(request, constants.ERROR, "Erro ao criar citação.")
        
        return redirect('/quotes/')
