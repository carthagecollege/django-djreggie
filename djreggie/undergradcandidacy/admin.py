#admin.py is where we create 'actions' that users can do to entries
#within this app, undergradcandidacy, as well as settings to change how
#we view entries within 'undergradcandidacy'

#'admin' - necessary to change view settings when viewing an 'undergradcandidacy' object
#'messages' - necessary to change success/fail messages when performing an action to an 'undergradcandidacy' object
from django.contrib import admin, messages
from djreggie.undergradcandidacy.models import UndergradModel
#from undergradCandForm.production_models import AaRec, AcadRec, IdRec, ProgramEnrollRec, GradwalkRec


#This is an 'action' a user can perform to a 'excavatebore' object
def push_to_production(modeladmin, request, queryset):
    push_to_production.short_description = 'Push to production server' #What the user sees
    
    
    # This is the bulk of moving data from the development to production databases
    #
    # *Understand this first - The data that exists in the form will be moved to separate
    # tables in the production server. Some fields might be moved to table 'A', others to table
    # 'B', and the rest might go to table 'C'. 
    # 
    # Steps to accomplish this:
    # 1) Find all of the tables where your data will be moving when it goes to the production
    # server. 
    #
    # 2) Download MySQLWorkbench and make copies of the tables on your local machine you found in step 1.
    # Be sure to copy the structure of the table exactly as found on the production server (including the name of the table)
    #
    # 3) Run this command and be sure 'newmodels.py' has been created in your project
    # (Run the command while within the 'root' project folder on your local machine. This
    # assumes you have been developing the form on your local machine)
    #       python manage.py inspectdb --database=default2 > newmodels.py
    #
    #   *Note: 'default2' is the name of your database where you have created the tables in
    #   step 2. This database should be a copy of the production database on the server (at the very least a copy of the tables you will need from step 1)
    #   This is found in the project's 'settings.py' file
    #
    # 4) On the top of this page, import the 'newmodels.py' file
    #
    # 5) Look in 'newmodels.py', you will see a bunch of classes. Each class represents a 
    # table. Now look at the fields in each class. For the below sample code, assume you had two classes
    # in 'newmodels.py' named 'table_one' and 'table_two'
    #
    #   'table_one' has these fields:
    #       id, name, tel
    #
    #   'table_two' has these fields:
    #       id, address
    #
    #   Also assume that your form has these fields:
    #       my_id, form, phone_number
    #
    # 6) For each class, use some code like below to save the data to your production database (keep this code in the function this comment is in)
    # *Note: replace 'default2' with the name YOU used for your production database (in 'settings.py')
    # *Note: feel free to un-comment the code below and make changes you need, you can keep these comments for reference
    # *Note: .get_or_create() makes an object if one is not found or updates an existing one if found
    # *Note: 'created' is a boolean that is true if an object was created from .get_or_create()
    # *Note: .save() saves the data to the production server
    # *Note: parameters within .get_or_create() are ... .get_or_create(field_from_newmodels.py=each.field_in_my_form)
    #
    #   for each in queryset: #Loops through all instances of the form object
    #       (obj, created) = table_one.objects.using('default2').get_or_create(id=each.my_id,name=each.name,tel=each.phone_number)
    #       obj.save()
    #       (obj, created) = table_two.objects.using('default2').get_or_create(id=each.my_id,address=each.address)
    #       if not obj.address:
    #           #You can also use 'warning', 'debug', 'info' and 'success' in place of 'error'
    #           messages.error(request, 'Object did not have an address')
    #       obj.save()
    #       messages.success(request, 'Object was moved to production!')
    
    #for item in queryset:
    #    (student, created) = IdRec.objects.using('default2').get_or_create(id=item.student_id)
    #    student.firstname = item.fname
    #    student.middlename = item.mname
    #    student.lastname = item.lname
    #    student.save()
    #    if item.carthage_email:
    #        aa_code = 'EML1'
    #    else:
    #        aa_code = 'EML2'
    #    (obj, created) = AaRec.objects.using('default2').get_or_create(id=student, aa=aa_code)    
    #    obj.line1 = item.email
    #    obj.save()
    #    (obj, created) = AaRec.objects.using('default2').get_or_create(id=student, aa='MAIL')    
    #    obj.line1 = item.address
    #    obj.city = item.city
    #    obj.st = item.state
    #    obj.zip = item.zipcode
    #    obj.save()
    #    (obj, created) = AaRec.objects.using('default2').get_or_create(id=student, aa='CELL')    
    #    obj.phone = item.best_phone
    #    obj.save()
    #    (obj, created) = AcadRec.objects.using('default2').get_or_create(id=item.student_id)
    #    item_majors = list(item.majors.all())
    #    item_minors = list(item.minors.all())
    #    if len(item_majors) >= 1:
    #        obj.major1=item_majors[0]
    #    if len(item_majors) >= 2:
    #        obj.major2=item_majors[1]
    #    if len(item_majors) >= 3:
    #        obj.major3=item_majors[2]
    #    if len(item_minors) >= 1:
    #        obj.minor1=item_minors[0]
    #    if len(item_minors) >= 2:
    #        obj.minor2=item_minors[1]
    #    if len(item_minors) >= 3:
    #        obj.minor3=item_minors[2]
    #    obj.save()
        
    #    (obj, created) = GradwalkRec.objects.using('default2').get_or_create(id=student)
    #    obj.name_on_diploma = "%s %s %s" % (item.fname, item.mname, item.lname)
    #    if item.participate_in_graduation:
    #        obj.plan2walk = 'Y'
    #    else:
    #        obj.plan2walk = 'N'
    #    obj.grad_sess = item.finish_requirements_by
    #    obj.save()


class FormAdmin(admin.ModelAdmin):
    readonly_fields = ('date',) #You will not be able to change these fields when editing an 'undergradcandidacy' object
    actions = [push_to_production] #Includes the action we defined earlier in this page


admin.site.register(UndergradModel, FormAdmin) #Always be sure to add the model before adding the admin class                                 
