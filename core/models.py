from django.db import models



class Contact(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length= 30)
    email = models.EmailField(max_length=30)
    phone_number = models.CharField(max_length= 13)
    message = models.TextField()

    def __str__(self):
        return f"{self.first_name}'s comment"

    class Meta:
        verbose_name = "Contact Us Comment"
        verbose_name_plural = "Contact Us Comments"


class Faq(models.Model):
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return f'FAQ {self.id}'

    class Meta:
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"


class Employees(models.Model):
    name = models.CharField(max_length=50)
    profession = models.CharField(max_length=50)
    image = models.ImageField(upload_to="employee_images")
    about = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees"


class OurTeam(models.Model):
    name = models.CharField(max_length= 50)
    image = models.ImageField(upload_to="team_images")
    position = models.CharField(max_length= 30)

    def __str__(self):
        return self.name


class Blog(models.Model):
    image = models.ImageField(upload_to='blog_images')
    blog_date = models.DateField()
    description = models.TextField()
    author = models.CharField(max_length= 50)

    def __str__(self):
        return self.author


class Instagram(models.Model):
    image = models.ImageField(upload_to='instagram_images')

    def __str__(self):
        return f'Instagram {self.id}'


class Logo(models.Model):
    image = models.ImageField(upload_to='logo_images')

    def __str__(self):
        return f'Logo {self.id}'


class Subscribe(models.Model):
    email = models.EmailField(max_length=30, unique=True)

    def __str__(self):
        return self.email
