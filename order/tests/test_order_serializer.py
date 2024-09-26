import pytest
from order.factories import OrderFactory, ProductFactory
from order.serializers import OrderSerializer

@pytest.mark.django_db
def test_order_serializer():
    #Setup
    product_1 = ProductFactory()
    product_2 = ProductFactory()

    order = OrderFactory(prodcut=(product_1, product_2))
    order_serializer = OrderSerializer(order)

    #Serialize data
    serializer_data = order_serializer.data

    #Assertions
    assert serializer_data['product'][0]['title'] == product_1.title
    assert serializer_data['product'][1]['title'] == product_2.title

