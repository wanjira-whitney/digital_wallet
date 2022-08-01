from django.db import models

# Create your models here.
from inspect import signature
from django.db import models
from locale import currency
import mailcap
from operator import countOf
from symtable import Symbol
from django.db import models
from django.utils import timezone
# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    GENDER_CHOICE=(("M","Male"),("F","Female"))
    gender = models.CharField(max_length=1,choices=GENDER_CHOICE,null=True)
    address = models.TextField(max_length=15,null=True)
    age = models.PositiveIntegerField()
    nationality = models.CharField(max_length=15,null=True)
    id_number = models.CharField(max_length=10,null=True)
    phone_number = models.CharField(max_length=15,null=True)
    email=models.EmailField(max_length=30,null=True)
    pin=models.TextField(max_length=8,null=True)
    occupation=models.CharField(max_length=20,null=True)
class Currency (models.Model):
    amount=models.PositiveIntegerField()
    Symbol=models.CharField(max_length=15,null=True)
    country_of_origin=models.CharField(max_length=24,null=True)
class Wallet (models.Model):
    currency=models.ForeignKey('Currency',on_delete=models.CASCADE,related_name='Wallet_currency')
    customer=models.ForeignKey('Customer',on_delete=models.CASCADE,related_name='Wallet_customer')
    balance=models.PositiveIntegerField()
    amount=models.PositiveIntegerField()
    date=models.DateTimeField(default=timezone.now)
    status=models.CharField(max_length=15,null=True)
    pin=models.TextField(max_length=8,null=True)
class Account (models.Model):
    account_type=models.CharField(max_length=15,null=True)
    balance=models.PositiveIntegerField()
    account_name=models.CharField(max_length=20,null=True)
    wallet=models.ForeignKey('Wallet',on_delete=models.CASCADE,related_name='Account_wallet')
class Transaction(models.Model):
    wallet=models.ForeignKey('Wallet',on_delete=models.CASCADE,related_name='Transaction_wallet')
    transaction_amount=models.IntegerField()
    transaction_type=models.CharField(max_length=15,null=True)
    transaction_charge=models.IntegerField()
    transaction_date=models.DateTimeField(default=timezone.now)
    receipt=models.ForeignKey('Customer',on_delete=models.CASCADE,related_name='Transaction_receipt')
    origin_account=models.ForeignKey('Account',on_delete=models.CASCADE,related_name='Transaction_receipt')
    destination_account=models.ForeignKey('Account',on_delete=models.CASCADE,related_name='Transaction_destination_account')
class Card(models.Model):
    date_issued=models.DateTimeField(default=timezone.now)
    card_name=models.CharField(max_length=15,null=True)
    card_number=models.IntegerField()
    card_type=models.CharField(max_length=15,null=True)
    exipry_date=models.DateTimeField(default=timezone.now)
    card_status=models.CharField(max_length=15,null=True)
    security_code=models.IntegerField()
    signature=models.ImageField()
    Wallet=models.ForeignKey('Account',on_delete=models.CASCADE,related_name='Card_wallet')
    account=models.ForeignKey('Account',on_delete=models.CASCADE,related_name='Card_account')
    issuer=models.CharField(max_length=15,null=True)
class Thirdparty (models.Model):
    account=models.ForeignKey('Account',on_delete=models.CASCADE,related_name='Thirdparty_account')
    name=models.CharField(max_length=15,null=True)
    thirdparty_id=models.IntegerField()
    phone_number=models.IntegerField()
class Notification (models.Model):
    notifications_id=models.IntegerField()
    name=models.CharField(max_length=15,null=True)
    status=models.CharField(max_length=15,null=True)
    date_and_time=models.DateTimeField(default=timezone.now)
    receipt=models.ForeignKey('Thirdparty',on_delete=models.CASCADE,related_name='Notifications_receipt')
class Receipt (models.Model):
    receipt_type=models.CharField(max_length=15,null=True)
    receipt_date=models.DateField(default=timezone.now)
    receipt_file=models.FileField()
    total_amount=models.IntegerField()
    transaction=models.ForeignKey('Account',on_delete=models.CASCADE,related_name='Receipt_transaction')
class Loan (models.Model):
    loan_number=models.IntegerField()
    loan_type=models.CharField(max_length=15,null=True)
    amount=models.IntegerField()
    date_and_time=models.DateTimeField(default=timezone.now)
    wallet=models.ForeignKey('Account',on_delete=models.CASCADE,related_name='Loan_wallet')
    interest_rate=models.IntegerField()
    guarantor=models.ForeignKey('Customer',on_delete=models.CASCADE,related_name='Loan_guarantor')
    pay_due_date=models.DateTimeField(default=timezone.now)
    loan_balance=models.IntegerField()
class Reward (models.Model):
    transaction=models.ForeignKey('Account',on_delete=models.CASCADE,related_name='Reward_transaction')
    date_and_time=models.DateTimeField(default=timezone.now)
    customer_id=models.IntegerField()
    GENDER_CHOICES=(("M","Male"),("F","Female"))
    gender=models.CharField(max_length=1,choices=GENDER_CHOICES,null=True)
    bonus=models.IntegerField()