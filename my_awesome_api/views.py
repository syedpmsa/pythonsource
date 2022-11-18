from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
#from rest_framework import ValidationError
from my_awesome_api.serializers import AccountSerializer, DestinationSerializer
#from rest_framework import serializers
from my_awesome_api.models import Account, Destination
from django.shortcuts import get_object_or_404


class AccountViewSet(viewsets.ModelViewSet):
   queryset = Account.objects.all()
   serializer_class = AccountSerializer


class DestinationViewSet(viewsets.ModelViewSet):
   queryset = Destination.objects.all()
   serializer_class = DestinationSerializer

@api_view(['POST'])
def add_Account(request):
    account = AccountSerializer(data=request.data)
  
    # validating for already existing data
    if Account.objects.filter(**request.data).exists():
        #raise account.ValidationError('This data already exists')
        return Response('This data already exists',404)
    if account.is_valid():
        account.save()
        return Response(account.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def add_Destination(request):
    destination = DestinationSerializer(data=request.data)
  
    # validating for already existing data
    account_id = request.data.get('account_id')
    if Destination.objects.filter(**request.data).exists():
        account = get_object_or_404 (Account, id=account_id)
        #raise destination.ValidationError('This data already exists')
        return Response('This data already exists',404)
    if destination.is_valid():
        destination.save()
    if destination.is_valid(raise_exception=True):
        serializers = Destionation.objects.get_or_create(account_id=request.account_id,Account=account)    
        return Response(destination.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND) 

@api_view(['GET'])
def view_Account(request):
    
    # checking for the parameters from the URL
    if request.query_params:
        account = Account.objects.filter(**request.query_param.dict())
    else:
        account = Account.objects.all()
  
    # if there is something in items else raise error
    if account :
        data1 = AccountSerializer(account)
        print(data1.data)
        return Response(data1.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def view_Destination(request):
    
    # checking for the parameters from the URL
    if request.query_params:
        destination = Destination.objects.filter(**request.query_param.dict())
    else:
        destination = Destination.objects.all()
  
    # if there is sview_Destinationomething in items else raise error
    if destination:
        data = DestinationSerializer(destination)
        return Response(data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)  

@api_view(['POST'])
def update_Account(request, pk):
    account = Account.objects.get(pk=pk)
    data = AccountSerializer(instance=account, data=request.data)
  
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def update_Destination(request, pk):
    destination = Destination.objects.get(pk=pk)
    data = DestinationSerializer(instance=account, data=request.data)
  
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_Account(request, pk):
    destination = Destination.objects.get(account_id=pk).delete()
    account = get_object_or_404(Account, pk=pk)
    account.delete()
    return Response(status=status.HTTP_202_ACCEPTED)

#@api_view(['DELETE'])
#def delete_Destination(request, pk):
    #destination = get_object_or_404(Destination, pk=pk)
    #destination.delete()
    #return Response(status=status.HTTP_202_ACCEPTED) 
#@api_view(['DELETE'])
#def delete_Destination(request, pk, format=None):
    #destination = Destination.objects.get(pk)
    #destination.delete()
    #return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(["DELETE"])
def delete_Destination(request, pk):
    destination = Destination.objects.get(account_id=pk).delete()
    return Response(status=status.HTTP_204_NO_CONTENT) 

@api_view(['GET'])
def url_destionation(request, pk):
    try:
        destionation = Destionation.objects.get(account_id=pk)
    except account.DoesNotExist:
        raise Http404("account does not exist")



# Create your views here.
