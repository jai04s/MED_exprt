from django.db import models

# Create your models here.
class dummy(models.Model):
    usr_id = models.CharField(max_length=30, primary_key= True)
    name = models.CharField(max_length=30)
    age = models.PositiveIntegerField()


class FAQ(models.Model):
    Q = models.TextField()
    ANS = models.TextField()

    def __str__(self):
        return f"{self.Q}{self.ANS}"
    
class contactus(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    sub = models.CharField(max_length=120)
    msg = models.TextField()

class usrdata(models.Model):
    email = models.EmailField(primary_key= True)
    Pw = models.CharField(max_length=50,blank=True,null=True)
    # img = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, null=True)
    name = models.CharField(max_length=30)
    dob = models.DateField(blank=True,null=True)
    edulvl = models.TextField(blank=True,null=True)
    edufld = models.TextField(blank=True,null=True)

class BodyPart(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Symptom(models.Model):
    name=models.CharField(max_length=100)
    body_part=models.ForeignKey(BodyPart,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Disease(models.Model):
    name=models.CharField(max_length=100)
    description = models.TextField(blank=True)
    img = models.ImageField(blank=True)

    symptoms=models.ManyToManyField(Symptom)
    def __str__(self):
        return self.name

class Hospital(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    address = models.TextField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    Country = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    website = models.URLField(blank=True)
    img = models.ImageField()
    def __str__(self):
        return self.name

class diets(models.Model):
    disease = models.CharField(max_length=50)
    diet = models.TextField()
    def __str__(self):
        return self.disease

class med(models.Model):
    disease = models.CharField(max_length=25)
    medi = models.TextField()
    def __str__(self):
        return self.disease
    
class feedback(models.Model):
    u_id = models.EmailField()
    name = models.CharField(max_length=30)
    msg = models.TextField(blank=False)





# class Video(models.Model):
#     title = models.CharField(max_length=100)
#     description = models.TextField()
#     Video_url = models.URLField()

