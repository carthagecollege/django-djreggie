from django.db import models
from datetime import date
from djzbar.settings import INFORMIX_EARL_TEST
from sqlalchemy import create_engine
# Create your models here.
# Each class will exist in a separate table in the database
#SQL Alchemy
engine = create_engine(INFORMIX_EARL_TEST)
connection = engine.connect()


sql1 = "select * from st_table"
state = connection.execute(sql1)  
CHOICES1 = tuple((row['st'], row['txt']) for row in state)

class Major(models.Model):

    txt = models.CharField(db_column='txt', max_length=128)

    #How the class is displayed in the admin page
    def __unicode__(self):
        return self.txt

class Minor(models.Model):
    txt = models.CharField(db_column='txt', max_length=128)

    #How the class is displayed in the admin page
    def __unicode__(self):
        return self.txt

#The main fields in the form are in this class listed below
class UndergradForm(models.Model):
    year = date.today().year
    if date.today().month <= 5:
            year = year - 1
    #All the fields in the form are below
    fname = models.CharField(max_length=200, verbose_name='First Name') #'max_length' is required in (most) all fields
    mname = models.CharField(max_length=200,
                             null=True,
                             blank=True,
                             verbose_name='Middle Name') #'null=True' means this data member can be represented as null in the database
    lname = models.CharField(max_length=200, verbose_name='Last Name')
    student_id = models.PositiveIntegerField() #Only positive numbers are valid
    majors = models.ManyToManyField(Major)
    minors = models.ManyToManyField(Minor, null=True, blank=True) #'blank=True' means the field is not required
    participate_in_graduation = models.BooleanField() #Renders as a checkbox

    FINISH_REQUIREMENTS_LIST = (
        ('RA', 'I will be finished with all required courses & degree requirements by the end of the %d/%d Fall Term (December)' % (year, year+1)),
        ('RB', 'I will be finished with all required courses & degree requirements by the end of the %d/%d J-Term (January)' % (year, year+1)),
        ('RC', 'I will be finished with all required courses & degree requirements by the end of the %d/%d Spring Term (May)' % (year, year+1)),
        ('RE', 'I will be finished with all required courses & degree requirements by the end of the %d/%d Summer Term (August)' % (year, year+1)),
    )
    finish_requirements_by = models.CharField(max_length=200, choices=FINISH_REQUIREMENTS_LIST) #Renders as a select box

    WHEN_TEACH_LIST = (
        ('fall1', 'Fall Term %d' % (year)),
        ('spring', 'Spring Term %d' % (year+1)),
        ('fall2', 'Fall Term %d' % (year+1)),
    )
    when_teach = models.CharField(max_length=200,
                                  null=True,
                                  blank=True,
                                  choices=WHEN_TEACH_LIST)

    best_phone = models.CharField(max_length=16, verbose_name='Best phone')
    cell = models.CharField(max_length=16,
                            null=True,
                            blank=True,
                            verbose_name='Cell')
    carthage_email = models.BooleanField(verbose_name='Check if carthage email')
    email = models.EmailField(verbose_name='Email')
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=2, choices=CHOICES1)
    zipcode = models.PositiveIntegerField(max_length=5, verbose_name='Zip')
    date = models.DateField(auto_now_add=True) #'auto_now_add' sets the date to the current date and makes this field invisible in the form

    #How the class is displayed in the admin page
    def __unicode__(self):
        return '%s, %s %d' % (self.lname, self.fname, self.student_id)
