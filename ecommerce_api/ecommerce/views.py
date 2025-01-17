from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import ValidationError
from .serializers import ProductSerializer, CategorySerializer
from .models import Product, Category
from rest_framework.views import APIView
from django.contrib.auth import get_user_model, authenticate
from rest_framework.permissions import AllowAny , IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication


User = get_user_model()

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        try:
            categories = Category.objects.all()
            data = [{"id": c.id, "name": c.name} for c in categories]
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def create(self, request):
        try:
            name = request.data.get('name')
            if not name:
                raise ValidationError("Name is required")
            category = Category.objects.create(name=name)
            return Response({"id": category.id, "name": category.name}, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def list(self, request):
        try:
            products = Product.objects.all()
            data = [
                {
                    "id": p.id,
                    "name": p.name,
                    "description": p.description,
                    "price": p.price,
                    "category": p.category.name,
                    "stock_quantity": p.stock_quantity,
                    "image_url": p.image_url,
                    "created_date": p.created_date,
                }
                for p in products
            ]
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def create(self, request):
        try:
            data = request.data
            name = data.get('name')
            price = data.get('price')
            stock_quantity = data.get('stock_quantity')
            category_id = data.get('category_id')

            # Validation
            if not name:
                raise ValidationError("Product name is required")
            if price is None or float(price) <= 0:
                raise ValidationError("Price must be a positive value")
            if stock_quantity is None or int(stock_quantity) < 0:
                raise ValidationError("Stock quantity cannot be negative")

            # Fetch category
            try:
                category = Category.objects.get(id=category_id)
            except Category.DoesNotExist:
                raise ValidationError("Category not found")

            # Create product
            product = Product.objects.create(
                name=name,
                description=data.get('description'),
                price=price,
                category=category,
                stock_quantity=stock_quantity,
                image_url=data.get('image_url'),
            )

            return Response({
                "id": product.id,
                "name": product.name,
                "description": product.description,
                "price": product.price,
                "category": product.category.name,
                "stock_quantity": product.stock_quantity,
                "image_url": product.image_url,
            }, status=status.HTTP_201_CREATED)

        except ValidationError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        # Get username and password from the request body
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({'error': 'Username and password are required'}, status=status.HTTP_400_BAD_REQUEST)

        # Authenticate user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Generate JWT tokens
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'message': 'Login successful'
            }, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)

class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "This is a protected endpoint!"})