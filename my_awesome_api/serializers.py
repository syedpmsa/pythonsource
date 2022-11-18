from rest_framework import serializers

from my_awesome_api.models import Account,Destination

class AccountSerializer(serializers.ModelSerializer):
   class Meta:
       model = Account
       #fields = ('email_id',  'account_name', 'App_secret_token')
       fields = '__all__'

class DestinationSerializer(serializers.ModelSerializer):
   class Meta:
       model = Destination
       #fields = (' account_id','url', 'http_method', 'headers')  
       fields = '__all__'     