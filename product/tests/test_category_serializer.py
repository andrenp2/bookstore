import pytest

from product.factories import CategoryFactory, ProductFactory
from product.serializers import CategorySerializer

@pytest.mark.django_db
def test_category_serializer():
    #setup
    category = CategoryFactory(title='food')
    category_serializer = CategorySerializer(category)

    #Serialize data
    serializer_data = category_serializer.data

    #Asserts
    assert serializer_data['title'] == 'food'