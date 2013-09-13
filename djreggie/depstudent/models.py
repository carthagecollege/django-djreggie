from django.db import models
from django import forms
from django.forms.models import modelformset_factory
from django.utils.safestring import mark_safe
from djzbar.settings import INFORMIX_EARL_TEST
from sqlalchemy import create_engine
# Create your models here.
# Each class will exist in a separate table in the database
#SQL Alchemy
'''engine = create_engine(INFORMIX_EARL_TEST)
connection = engine.connect()


sql1 = "select * from st_table"
state = connection.execute(sql1)
array1 = []
for row in state:
    array1.append((row['st'],row['txt']))   
CHOICES1 = tuple(array1)'''
class Depend(models.Model):

    PHONES= (
            ("CELL", "Cell Phone"),
            ("HOME", "Home Phone"),
            ("WORK", "Work Phone"),
    )

    fname = models.CharField(max_length=100)
    mname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    ssn = models.CharField(max_length=11)
    address = models.CharField(max_length=500)
    dob = models.DateField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    zip = models.CharField(max_length=5)
    email = models.EmailField()
    hphone = models.CharField(max_length=16)
    phonetype = models.CharField(max_length= 100, choices=PHONES)
    cphone = models.CharField(max_length=16, blank=True)
    phonetype2 = models.CharField(max_length= 100, choices=PHONES, blank=True)
    file = models.FileField(upload_to='files', blank=True)
    file2 = models.FileField(upload_to='files', blank=True)
    IRSDRT= (
        ("HAS", mark_safe("The student has used the IRS Data Retrieval Tool in FAFSA on the Web to retrieve and transfer 2012 IRS income information into the student's FAFSA, either on the initial FAFSA or when making a correction to the FAFSA. (The student's school will use the IRS information that was transferred in the verification process.)<br><br>")),
        ("HASN", mark_safe("The student has not yet used the IRS Data Retrieval Tool in FAFSA on the Web, but will use the tool to retrieve and transfer 2012 IRS income information into the student's FAFSA once the student has filed a 2012 IRS tax return. See instructions above for information on how to use the IRS Data Retrieval Tool. (The student's school cannot complete the verification process until the IRS information has been transferred into the FAFSA.)<br><br>")),
        ("WONT", mark_safe("The student is unable or chooses not to use the IRS Data Retrieval Tool in FAFSA on the Web, and the student will submit to the school a 2012 IRS tax return transcript-not a photocopy of the income tax return. To obtain an IRS tax return transcript, go to www.IRS.gov and click on the \"Order a Return or Account Transcript\" link, or call 1-800-908-9946. Make sure to request the \"IRS tax return transcript\" and not the \"IRS tax account transcript.\" You will need your Social Security Number, date of birth, and the address on file with the IRS (normally this will be the address used when the 2012 IRS tax return was filed). It takes up to two weeks for IRS income information to be available for electronic IRS tax return filers, and up to eight weeks for paper IRS tax return filers.")),        
    )
    
    TACHED= (
        ("IS", mark_safe('Check here if the student\'s IRS tax return transcript is attached to this worksheet.<br><br>')),
        ("ISNT", mark_safe('Check here if the student\'s IRS tax return transcript will be submitted to the student\'s school later. Verification cannot be completed until the IRS tax return transcript has been submitted to the student\'s school')),    
    )
    
    PLOY= (
        ("WAS", mark_safe('The student was not employed and had no income earned from work in 2012.<br><br>')),
        ("WSNT", 'The student was employed in 2012 and has listed below the names of all the student\'s employers, the amount earned from each employer in 2012, and whether an IRS W-2 form is attached. Attach copies of all 2012 IRS W-2 forms issued to the student by employers. List every employer even if they did not issue an IRS W-2 form.'),    
    )
    
    useddata = models.CharField(choices=IRSDRT, max_length=500, default="HAS")
    attached = models.CharField(choices=TACHED, max_length=500, default="IS")
    employed = models.CharField(choices=PLOY, max_length=500, default="WAS")
    IRSDRT2= (
        ("HAS", mark_safe("The student's parent has used the IRS Data Retrieval Tool in FAFSA on the Web to retrieve and transfer 2012 IRS income information into the student's FAFSA, either on the initial FAFSA or when making a correction to the FAFSA. (The student's school will use the IRS information that was transferred in the verification process.)<br><br>")),
        ("HASN", mark_safe("The student's parent has not yet used the IRS Data Retrieval Tool in FAFSA on the Web, but will use the tool to retrieve and transfer 2012 IRS income information into the student's FAFSA once the student has filed a 2012 IRS tax return. See instructions above for information on how to use the IRS Data Retrieval Tool. (The student's school cannot complete the verification process until the IRS information has been transferred into the FAFSA.)<br><br>")),
        ("WONT", mark_safe("The parent is unable or chooses not to use the IRS Data Retrieval Tool in FAFSA on the Web, and the parent will submit to the student's school a 2012 IRS tax return transcript-not a photocopy of the income tax return. To obtain an IRS tax return transcript, go to www.IRS.gov and click on the \"Order a Return or Account Transcript\" link, or call 1-800-908-9946. Make sure to request the \"IRS tax return transcript\" and not the \"IRS tax account transcript.\" You will need your Social Security Number, date of birth, and the address on file with the IRS (normally this will be the address used when the 2012 IRS tax return was filed). It takes up to two weeks for IRS income information to be available for electronic IRS tax return filers, and up to eight weeks for paper IRS tax return filers.")),        
        )
    
    TACHED2= (
        ("IS", 'Check here if an IRS tax return transcript(s) is attached to this worksheet.'),
        ("ISNT", 'Check here if IRS tax return transcript(s) will be submitted to the student\'s school later. Verification cannot be completed until the IRS tax return transcript(s) has been submitted to the school.'),    
        )
    
    PLOY2= (
        ("WAS", 'Was employed in 2012'),
        ("WSNT", 'Was not employed in 2012'),             
    )
    useddata2 = models.CharField(choices=IRSDRT2, max_length=500, default="HAS")
    attached2 = models.CharField(choices=TACHED2, max_length=500, default="IS")
    employed2 = models.CharField(choices=PLOY2, max_length=500, default="WAS")
    snapbenefits = models.BooleanField()
    childsupport = models.BooleanField()
    confirm = models.BooleanField()
    date = models.DateField(auto_now_add=True)
    
class FamInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(max_length=3)
    relationship = models.CharField(max_length=100)
    college = models.CharField(max_length=200)
    halftimeenroll = models.BooleanField()
    student = models.ForeignKey(Depend)
    
class Studwork(models.Model):
    empname = models.CharField(max_length=250)
    money = models.IntegerField(max_length=10)
    w2attach = models.BooleanField()
    student = models.ForeignKey(Depend)


class Parwork(models.Model):
    empname = models.CharField(max_length=250)
    money = models.IntegerField(max_length=10)
    w2attach = models.BooleanField()
    student = models.ForeignKey(Depend)
    
class CS(models.Model):
    namepaid = models.CharField(max_length=200, blank=True)
    namepaidto = models.CharField(max_length=200, blank=True)
    namechild = models.CharField(max_length=200, blank=True)
    amntpaid = models.IntegerField(max_length=10, blank=True)
    student = models.ForeignKey(Depend)
