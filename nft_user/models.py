from django.db import models

class nft(models.Model):
    nft_id = models.IntegerField(blank=True, null=True)
    nft_id_str = models.TextField(default = '1')
    category = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.nft_id_str


class userp(models.Model):
    public_key = models.TextField()
    nftlike = models.TextField(default = '1')
     
    def __str__(self):
        return self.public_key


     
   
