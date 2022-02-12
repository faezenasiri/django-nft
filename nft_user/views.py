from .models import nft , userp 
from .serializers import nftserializer , userpserializer 
from django.db.models import Q
from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets



class nftViewSet(APIView):

    def get(self, request, format=None):
        nfts = nft.objects.all()
        serializer = nftserializer(nfts, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = nftserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)     




class nftdetail(APIView):

    def get_object(self, pk):
        try:
            return nft.objects.get(pk=pk)
        except nft.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = nftserializer(snippet)
        return Response(serializer.data)        



class userpview(APIView):

    def get(self, request, format=None):
        userps = userp.objects.all()
        serializer = userpserializer(userps, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = userpserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    

class userpviewdetail(APIView):

    def get_object(self, pk):
        try:
            return userp.objects.get(pk=pk)
        except nft.DoesNotExist:
            raise Http404

    def get(self, request, pk,format=None):
        snippet = self.get_object(pk)
        serializer = userpserializer(snippet)
        return Response(serializer.data) 
   
class userpviewdetailpk(APIView):

    def get_object(self, public_key):
        try:
            return userp.objects.get(public_key=public_key)
        except nft.DoesNotExist:
            raise Http404

    def get(self, request, public_key,format=None):
        snippet = self.get_object(public_key)
        serializer = userpserializer(snippet)
        return Response(serializer.data) 

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)        



