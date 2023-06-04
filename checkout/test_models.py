from django.test import TestCase
from django.shortcuts import HttpResponse,  get_object_or_404
from .models import Order, OrderLineItem, Product


class TestModels(TestCase):
    """
    Test for models
    """

    def test_if_it_returns_an_order(self):
        """
        Test to see if it returns order strings
        """
        order = Order.objects.create(
                                        order_number=000,
                                        full_name='Joe Jones',
                                        email='test@foo.com',
                                        phone_number='+353123234432',
                                        street_address1='Main Street',
                                        street_address2='flat2',
                                        town_or_city='Killarney',
                                        postcode='v93',
                                        country='Ireland',
                                        county='Kerry',
        )
        print("order is:", order)
        print("order id is ", order.id)
        self.assertEqual(str(order.county), 'Kerry')
        self.assertEqual(str(order.full_name), 'Joe Jones')

    def test_Checkout_details(self):
        order = Order.objects.create(
                                        order_number=000,
                                        full_name='Joe Jones',
                                        email='test@foo.com',
                                        phone_number='+353123234432',
                                        street_address1='Main Street',
                                        street_address2='flat2',
                                        town_or_city='Killarney',
                                        postcode='v93',
                                        country='Ireland',
                                        county='Kerry',
        )
        print("order is:", order)
        print("order id is ", order.id)
        order = Order.objects.get(id=1)
        self.assertEqual(str(order.county), 'Kerry')
        self.assertEqual(str(order.full_name), 'Joe Jones')
        self.assertEqual(order.email, 'test@foo.com')
        self.assertEqual(order.town_or_city, 'Killarney')

    def test_Checkout_generate_order_number(self):
        
        order = Order.objects.create(
                                        order_number=000,
                                        full_name='Joe Jones',
                                        email='test@foo.com',
                                        phone_number='+353123234432',
                                        street_address1='Main Street',
                                        street_address2='flat2',
                                        town_or_city='Killarney',
                                        postcode='v93',
                                        country='Ireland',
                                        county='Kerry',
        )
        order = Order.objects.get(id=1)
        self.assertFalse(order.order_number == 000)


    """
    def test_if_it_returns_an_orderlineitem(self):
        
        # Test to see if it returns order line items
        
        testorder = Order.objects.create(
                                full_name='Joe Jones',
                                email='test@foo.com',
                                phone_number='+353123234432',
                                street_address1='Main Street',
                                street_address2='flat2',
                                town_or_city='Killarney',
                                postcode='v93',
                                country='Ireland',
                                county='Kerry',
        )
#        testproduct = get_object_or_404(Product, pk=1)


        testproduct = Product.objects.create(
                        pk=102,
                        fields={ name:"Data Protection Policy",
                            category=2,
                            sku="pp5001600425a",
                            slug="pp5001600425a",
                            description="Data Protection Policy2",
                            price=58.99,
                            rating=4.6,
                            image="policy-shop-hero.webp"
                        }
        )


        orderli = OrderLineItem.objects.create(
                order=testorder,
                product=testproduct,
                product_size='XL',
                quantity='10',
                lineitem_total=3
        )
        self.assertEqual(str(orderli.product_size), 'XL')
        self.assertEqual(str(orderli.quantity), 10)
        """
