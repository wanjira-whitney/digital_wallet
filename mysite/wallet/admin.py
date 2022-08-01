from django.contrib import admin

# Register your models here.
from .models import Customer,Currency,Wallet,Account,Transaction,Card,Thirdparty,Notification,Loan,Reward
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name','last_name',)

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Currency)
admin.site.register(Wallet)
admin.site.register(Account)
admin.site.register(Transaction)
admin.site.register(Card)
admin.site.register(Thirdparty)
admin.site.register(Notification)
admin.site.register(Loan)
admin.site.register(Reward)