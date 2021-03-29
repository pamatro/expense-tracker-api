from rest_framework.generics import RetrieveDestroyAPIView, ListCreateAPIView

from restapi import models, serializers
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class ExpenseListCreate(ListCreateAPIView):
    serializer_class = serializers.Expense
    queryset = models.Expense.objects.all()
    filterset_fields = ['category', 'merchant']
    permission_classes = [IsAuthenticated]


class ExpenseRetrieveDelete(RetrieveDestroyAPIView):
    serializer_class = serializers.Expense
    queryset = models.Expense.objects.all()

