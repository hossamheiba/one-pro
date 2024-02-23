from django.db import models



JOB_TYPE=(
    ('full time', 'full time'),
    ('part time', 'part time'),
)
class Job (models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000, default="des")
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    job_type=models.CharField(max_length=100 , choices=JOB_TYPE)
    salary = models.IntegerField(default=0)
    experienc = models.IntegerField(default=1)
    cateogry = models.ForeignKey('Cateogry', on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("job")
        verbose_name_plural = ("job")
        
    def __str__(self):
        return str(self.title)
    
    
class Cateogry (models.Model):
    name = models.CharField(max_length=25)
    
    class Meta:
        verbose_name = ("Cateogry")
        verbose_name_plural = ("Cateogry")

    def __str__(self):
        return self.name.capitalize()
    


    

