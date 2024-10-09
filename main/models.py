from django.db import models

# Create your models here.

class WhyUs(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class OurSertificate(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

class OurClients(models.Model):
    company_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.company_name

class OurServices(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

class PriceList(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

class Tariflar(models.Model):
    plan = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    get = models.BooleanField(default=False)

    def __str__(self):
        return self.plan

class FAQ(models.Model):
    savol = models.CharField(max_length=212)
    javob = models.CharField(max_length=212)

    def __str__(self):
        return self.savol

class About(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

class Feedback(models.Model):
    fullname = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    description = models.TextField()

    def __str__(self):
        return self.fullname




class Portfolio(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    cat = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Xodim(models.Model):
    fullname = models.CharField(max_length=100)
    job = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.fullname


class NimaUchunBiz(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    xodim = models.ForeignKey(Xodim, on_delete=models.CASCADE)
    kimlar_uchun = models.ForeignKey(NimaUchunBiz, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.title)



class Services(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title



class Contact(models.Model):
    fullname = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    service = models.ForeignKey(Services, on_delete=models.CASCADE)
    message = models.TextField()
    is_checked = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fullname