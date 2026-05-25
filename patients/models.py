from django.db import models

# Create your models here.
class Patient(models.Model):
    firstName = models.CharField(max_length=100,null=False,blank=False)
    lastName = models.CharField(max_length=100,null=False,blank=False)
    sex = models.CharField(max_length=6,null=False,blank=False,choices={"male":"Male","femal":"Female"})
    dob = models.DateField(null=False,blank=False)
    pob = models.CharField(max_length=200,null=True,blank=True)
    address = models.CharField(max_length=200,null=True,blank=True)
    profileImage = models.ImageField(upload_to='profile/',default='',null=True,blank=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        db_table= "Patient"
        ordering = ["-created"]

    def __str__(self):
        return f"{self.firstName} {self.lastName}"
    
class doctor(models.Model):
    firstName = models.CharField(max_length=100,null=False,blank=False)
    lastName = models.CharField(max_length=100,null=False,blank=False)
    sex = models.CharField(max_length=6,null=False,blank=False,choices={"male":"Male","femal":"Female"})
    dob = models.DateField(null=False,blank=False)
    phone = models.CharField(max_length=200,null=True,blank=True)
    address = models.CharField(max_length=200,null=True,blank=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table= "Doctor"
        ordering = ["-created"]

    def __str__(self):
        return f"{self.firstName} {self.lastName}"
    
class appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(doctor,on_delete=models.PROTECT)
    date_appointment = models.DateTimeField(null=False,blank=False)
    reason = models.CharField(max_length=200,null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        db_table= "appoinment"
        ordering = ["-created"]

    def __str__(self):
        return f"{self.patient} -> {self.doctor}"
