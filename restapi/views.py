from rest_framework.generics import RetrieveDestroyAPIView, ListCreateAPIView

from restapi import models, serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework_api_key.permissions import HasAPIKey


# Create your views here.
class ExpenseListCreate(ListCreateAPIView):
    serializer_class = serializers.Expense
    queryset = models.Expense.objects.all()
    filterset_fields = ['category', 'merchant']
    permission_classes = [HasAPIKey]


class ExpenseRetrieveDelete(RetrieveDestroyAPIView):
    serializer_class = serializers.Expense
    queryset = models.Expense.objects.all()
    permission_classes = [HasAPIKey]

