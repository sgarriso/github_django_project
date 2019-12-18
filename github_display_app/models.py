from django.db import models

# Create your models here.
class GithubRecord(models.Model):
    #Store the list of repositories in a database table. 
    #The table must contain the 
    #repository ID
    #, name
    #, URL
    #, created date
    #, last push date
    #, description
    #, and number of stars. 
    repository_ID = models.CharField(max_length=2000)
    name = models.CharField(max_length=2000,blank=True,null=True)
    url = models.CharField(max_length=2000,blank=True,null=True)
    created_date = models.DateTimeField()
    last_push_date = models.DateTimeField()
    description = models.CharField(max_length=2000,blank=True,null=True)
    stars = models.PositiveIntegerField()
    remove_list = ['id']
    def get_all_fields(self):
        fields = []
        for f in self._meta.fields:

            fname = f.name    
            # resolve picklists/choices, with get_xyz_display() function
            get_choice = 'get_'+fname+'_display'
            if hasattr(self, get_choice):
                value = getattr(self, get_choice)()
            else:
                try:
                    value = getattr(self, fname)
                except AttributeError:
                    value = None
                    # only display fields with values and skip some fields entirely

            fields.append(
                {
                    'label':f.verbose_name, 
                    'name':f.name, 
                    'value':value,
                     }
                )

        return fields
    def get_printable_fields(self):
        
        fields = self.get_all_fields()
        removelist = self.remove_list
        printable_list = []
        
        for field in fields:
            if field['name'] not in removelist :
                printable_list.append(field)
        return printable_list
    