from django.test import TestCase
from restapi import models
from django.urls import reverse


class TestModels(TestCase):
    def test_expense(self):
        # expense = pk
        expense = models.Expense.objects.create(amount=249.99, merchant='amazon',
                                                description='anc headphones',
                                                category='music')
        inserted_expense = models.Expense.objects.get(pk=expense.id)

        self.assertEqual(249.99, inserted_expense.amount)
        self.assertEqual('amazon', inserted_expense.merchant)
        self.assertEqual('anc headphones', inserted_expense.description)
        self.assertEqual('music', inserted_expense.category)


class TestViews(TestCase):
    def test_expense_create(self):
        payload = {
            'amount': 50,
            'merchant': 'AT&T',
            'description': 'cell phone subscription',
            'category': 'utilities',
        }

        res = self.client.post(reverse('restapi:expense-list-create'), payload, format='json')
        #reverse function constructs the path from the rest api namespace 'expense-list-create'

        self.assertEqual(201, res.status_code)

        json_res = res.json()

        self.assertEqual(str(payload['amount']), json_res['amount'])
        self.assertEqual(payload['merchant'], json_res['merchant'])
        self.assertEqual(payload['description'], json_res['description'])
        self.assertEqual(payload['category'], json_res['category'])
        self.assertIsInstance(json_res['id'], int)

    def test_expense_list(self):
        res = self.client.get(reverse('restapi:expense-list-create'), format='json')

        self.assertEqual(200, res.status_code)

        json_res = res.json()

        self.assertIsInstance(json_res, list) # checks if json_rest is of type list

        expenses = models.Expense.objects.all()
        self.assertEqual(len(expenses), len(json_res))