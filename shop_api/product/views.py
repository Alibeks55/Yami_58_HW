from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Category, Product, Review
from .serializers import CategorySerializer,CategoryDetailSerializer,ProductSerializer,ProductDetailSerializer,ReviewSerializer,ReviewDetailSerializer


@api_view(http_method_names=['GET'])
def category_list_api_view(request):
    categories = Category.objects.all()
    data = CategorySerializer(categories, many=True).data
    return Response(
        data=data,
        status=status.HTTP_200_OK,
    )

@api_view(http_method_names=['GET'])
def category_detail_api_view(request, id):
    try:
        categories = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return Response(
            status=status.HTTP_404_NOT_FOUND,
            data={'text': 'Category does not exist'},
        )
    data=CategoryDetailSerializer(categories).data
    return Response(
        data=data,
        status=status.HTTP_200_OK
    )


@api_view(http_method_names=['GET'])
def product_list_api_view(request):
    products = Product.objects.all()
    data = ProductSerializer(products, many=True).data
    return Response(
        data=data,
        status=status.HTTP_200_OK
    )

@api_view(http_method_names=['GET'])
def product_detail_api_view(request,id):
    try:
        products = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(
            status=status.HTTP_404_NOT_FOUND,
            data={'text': 'Product does not exist'},
        )
    data = ProductDetailSerializer(products).data
    return Response(
        data=data,
        status=status.HTTP_200_OK
    )


@api_view(http_method_names=['GET'])
def review_list_api_view(request):
    reviews = Review.objects.all()
    data = ReviewSerializer(reviews, many=True).data
    return Response(
        data=data,
        status=status.HTTP_200_OK
    )

@api_view(http_method_names=['GET'])
def review_detail_api_view(request,id):
    try:
        reviews = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(
            status=status.HTTP_404_NOT_FOUND,
            data={'text': 'Review does not exist'},
        )
    data = ReviewDetailSerializer(reviews).data
    return Response(
        data=data,
        status=status.HTTP_200_OK
    )