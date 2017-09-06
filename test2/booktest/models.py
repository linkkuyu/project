from django.db import models


# Create your models here.
class BookInfoManager(models.Manager):
    def get_queryset(self):
        return super(BookInfoManager, self).get_queryset().filter(isDelet=False)

    def create(cls, btitle, bput_date):
        b = BookInfo()
        b.btitle = btitle
        b.bput_date = bput_date
        b.bread = 0
        b.bcommet = 0
        b.isdelet = False
        return b

class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bput_date = models.DateTimeField(db_column='pub_date')
    bread = models.IntegerField(default=0)
    bcommet = models.IntegerField(null=False)
    isDelet = models.BooleanField(default=False)
    class Meta:
        db_table = 'bookinfo'
    books1 = models.Manager()
    books2 = BookInfoManager()

    @classmethod
    def create(cls, btitle, bput_date):
        b = BookInfo()
        b.btitle = btitle
        b.bput_date = bput_date
        b.bread = 0
        b.bcommet = 0
        b.isdelet = False
        return b

class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField(default=True)
    hcontent = models.CharField(max_length=1000)
    isDelet = models.BooleanField(False)
    book = models.ForeignKey(BookInfo)
