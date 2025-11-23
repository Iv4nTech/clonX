from django.db import models

class User(models.Model):
    name = models.CharField(max_length=30)
    username = models.CharField(max_length=20)
    email = models.EmailField()
    date_born = models.DateField(null=True, blank=True)
    image_profile = models.ImageField(upload_to='profiles/', null=True, blank=True)
    followers = models.IntegerField(default=0)
    following = models.IntegerField(default=0)

    def __str__(self):
        return self.username

class Post(models.Model):
    content = models.TextField(max_length=300)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    past_tense = models.TimeField()
    coments = models.TextField(null=True, blank=True)
    shares = models.IntegerField()
    likes = models.IntegerField()
    views = models.IntegerField()

    def __str__(self):
        return self.content
        


