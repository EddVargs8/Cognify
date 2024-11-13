from django.db import models

class Criminal(models.Model):
    SENTENCE_CHOICES = [
        ('traditional', 'Sentencia Tradicional'),
        ('cognify', 'Rehabilitacion Cognify')
    ]
    
    CRIME_TYPE_CHOICES = [
        ('violent', 'Ofensores Violentos'),
        ('financial', 'Crímenes Financieros'),
        ('hate', 'Crímenes de Odio')
    ]

    name = models.CharField(max_length=100)
    crime_type = models.CharField(max_length=20, choices=CRIME_TYPE_CHOICES)
    sentence_type = models.CharField(max_length=20, choices=SENTENCE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Memory(models.Model):
    criminal = models.ForeignKey(Criminal, on_delete=models.CASCADE)
    empathy_level = models.IntegerField(default=1)
    regret_level = models.IntegerField(default=1)
    memory_description = models.TextField()



