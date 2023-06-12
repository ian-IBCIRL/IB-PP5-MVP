from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404  # noqa
from django.contrib import messages

from products.models import Product


def ordersheet(request):
    """ A view that renders the ordersheet contents page """

    return render(request, 'ordersheet/ordersheet.html')


def add_to_ordersheet(request, item_id):
    """ Add a quantity of the specified product to the shopping ordersheet """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    ordersheet = request.session.get('ordersheet', {})

    if size:
        if item_id in list(ordersheet.keys()):
            if size in ordersheet[item_id]['items_by_size'].keys():
                ordersheet[item_id]['items_by_size'][size] += quantity
                messages.success(request, f'Updated size {size.upper()} {product.name} quantity to {ordersheet[item_id]["items_by_size"][size]}')   # noqa
            else:
                ordersheet[item_id]['items_by_size'][size] = quantity
                messages.success(request, f'Added size {size.upper()} {product.name} to your ordersheet')   # noqa
        else:
            ordersheet[item_id] = {'items_by_size': {size: quantity}}
            messages.success(request, f'Added size {size.upper()} {product.name} to your ordersheet')   # noqa
    else:
        if item_id in list(ordersheet.keys()):
            ordersheet[item_id] += quantity
            messages.success(request, f'Updated {product.name} quantity to {ordersheet[item_id]}')   # noqa
        else:
            ordersheet[item_id] = quantity
            messages.success(request, f'Added {product.name} to your ordersheet')   # noqa

    request.session['ordersheet'] = ordersheet
    return redirect(redirect_url)


def adjust_ordersheet(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    ordersheet = request.session.get('ordersheet', {})

    if size:
        if quantity > 0:
            ordersheet[item_id]['items_by_size'][size] = quantity
            messages.success(request, f'Updated size {size.upper()} {product.name} quantity to {ordersheet[item_id]["items_by_size"][size]}')   # noqa
        else:
            del ordersheet[item_id]['items_by_size'][size]
            if not ordersheet[item_id]['items_by_size']:
                ordersheet.pop(item_id)
            messages.success(request, f'Removed size {size.upper()} {product.name} from your ordersheet')   # noqa
    else:
        if quantity > 0:
            ordersheet[item_id] = quantity
            messages.success(request, f'Updated {product.name} quantity to {ordersheet[item_id]}')   # noqa
        else:
            ordersheet.pop(item_id)
            messages.success(request, f'Removed {product.name} from your ordersheet')   # noqa

    request.session['ordersheet'] = ordersheet
    return redirect(reverse('ordersheet'))


def remove_from_ordersheet(request, item_id):
    """Remove the item from the shopping ordersheet"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        ordersheet = request.session.get('ordersheet', {})

        if size:
            del ordersheet[item_id]['items_by_size'][size]
            if not ordersheet[item_id]['items_by_size']:
                ordersheet.pop(item_id)
            messages.success(request, f'Removed size {size.upper()} {product.name} from your ordersheet')   # noqa
        else:
            ordersheet.pop(item_id)
            messages.success(request, f'Removed {product.name} from your ordersheet')  # noqa

        request.session['ordersheet'] = ordersheet
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
