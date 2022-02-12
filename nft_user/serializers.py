from rest_framework import serializers
from .models import nft
from .models import userp



class nftserializer(serializers.ModelSerializer):
     class Meta:
        model = nft
        fields = ['id', 'nft_id', 'nft_id_str',  'category']



class userpserializer(serializers.ModelSerializer):   
     class Meta:
        model = userp
        fields = ['id', 'public_key','nftlike']
        depth = 1


