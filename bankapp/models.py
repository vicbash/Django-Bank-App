from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser
# Create your models here.

ACCOUNT_STATUS = (
("active", "Active"),
("pending", "Pending"),
("in-active", "In-active")
)

MARITAL_STATUS = (
    ("married", "Married"),
    ("single", "Single"),
    ("other", "Other")
)

GENDER = (
    ("male", "Male"),
    ("female", "Female"),
    ("other", "Other")
)

IDENTITY_TYPE = (
("national_id_card", "National ID Card"),
("drivers_license", "Drivers License"),
("international_passport", "International Passport")
)

class User(AbstractUser):
    email = models.EmailField(unique=True)
    username=models.CharField(unique=False, null=True, max_length=50)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
    
    class Meta:
        db_table = 'User_Register'

import random
class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_balance = models.DecimalField(max_digits=12, decimal_places=2, default=1000.00)
    account_number = models.IntegerField(unique=True, null=True)
    #account_id = models.CharField(length=7, unique=True,max_length= 25, prefix="DEX", alphabet="1234567890" )
    pin_number = models.IntegerField(default=0000)
    account_status = models.CharField(max_length=100, choices= ACCOUNT_STATUS, default="active")
    date = models.DateTimeField(auto_now_add=True)
    def save(self, *args, **kwargs):
        if self.account_number == None:
            self.account_number= random.randint(1000000000,9999999999)
        super().save( *args, **kwargs)


    class Meta:
        ordering = ['-date']
        db_table = 'Account'


    def __str__(self):
        return f"{self.user}"
    
    
class UserInfo(models.Model):
    full_name = models.CharField(max_length=1000, null=True, blank=True)
    gender = models.CharField(max_length=45, choices=GENDER, null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account = models.OneToOneField(Account, on_delete=models.CASCADE, null=True, blank=True)
    marital = models.CharField(max_length=45, choices=MARITAL_STATUS, null=True, blank=True)
    phone_number = models.CharField(max_length=11, null=True, blank=True)
    state = models.CharField(max_length=300, null=True, blank=True)
    lga = models.CharField(max_length=300, null=True, blank=True)
    residential_address = models.CharField(max_length=200, null=True, blank=True)
    identity_type = models.CharField(choices=IDENTITY_TYPE, max_length=140, null=True, blank=True)
    identity_image = models.ImageField(upload_to="photo/", null=True, blank=True)
    passport = models.ImageField(upload_to='media/', null=True, blank=True) 
    date_of_birth = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    signature = models.ImageField(upload_to="sign/", null=True, blank=True)
    next_of_kin = models.CharField(max_length=100, null=True, blank=True)
    kin_number = models.CharField(max_length=11,null=True, blank=True)
    is_kyc_complete = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user}"
    
    class Meta:
        db_table = 'userinfo'


class Transaction(models.Model):
    sender = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="sent_transactions")
    receiver = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="received_transactions")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=60, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)


    class Meta:
        db_table = 'Transaction'