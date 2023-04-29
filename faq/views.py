from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Faqs
from .forms import FaqsForm


def faq(request):
    """
    Display faqs on the faq page
    """
    faq = Faqs.objects.all()

    template = 'faq/faq.html'

    context = {
        'faqs': faq,
    }

    return render(request, template, context)


@login_required
def add_faq(request):
    """
    Add a new faq to the store
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry - You are not authorised')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = FaqsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'FAQ added successfully!')
            return redirect('faq')
        else:
            messages.info(
                request, 'Failed to update.\
                     Please ensure the form is valid.'
            )
    else:
        form = FaqsForm()

    template = 'faq/add_faq.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_faq(request, item_id):
    """
    Edit a faq and update
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry - You are not authorised')
        return redirect(reverse('home'))

    item = get_object_or_404(Faqs, pk=item_id)

    if request.method == 'POST':
        form = FaqsForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, 'FAQ updated successfully!')
            return redirect('faq')
        else:
            messages.info(request, 'Failed to update.\
                Please ensure the form is valid.')
    else:
        form = FaqsForm(instance=item)

    template = 'faq/edit_faq.html'
    context = {
        'form': form,
        'item': item,
    }

    return render(request, template, context)


@login_required
def delete_faq(request, item_id):
    """
    Delete a faq from the store
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry - You are not authorised')
        return redirect(reverse('home'))
    item = get_object_or_404(Faqs, pk=item_id)
    item.delete()
    messages.success(request, f'{item} is deleted successfully !')
    return redirect('faq')
