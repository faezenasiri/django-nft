from django.contrib import admin
from .models import nft , userp 

class nftAdmin(admin.ModelAdmin):
    nft = ('nft_id', 'category','nft_id_str')
# Register your models here.

admin.site.register(nft, nftAdmin)


class userpAdmin(admin.ModelAdmin):

   userp = ('public_key','nftlike')


admin.site.register(userp, userpAdmin)


