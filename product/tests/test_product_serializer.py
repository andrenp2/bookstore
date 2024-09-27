import pytest

from product.factories import CategoryFactory, ProductFactory
from product.serializers import ProductSerializer

@pytest.mark.django_db
def test_product_serializer():
    #setup
    category = CategoryFactory(title='food')
    product = ProductFactory(title='chicken', price=30, category=[category])

    #serializing:
    product_serializer = ProductSerializer(product)
    serializer_data = product_serializer.data

    #Asserts
    assert serializer_data['price'] == 30
    assert serializer_data['title'] == 'chicken'
    assert serializer_data['category'][0]['title'] == 'food'