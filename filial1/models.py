from django.db import models

class User(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.email
    class Meta:
        abstract = True
    

class Client(User):
    name = models.CharField(max_length=20)
    card_number = models.IntegerField()

    class Meta(User.Meta):
        pass

class Worker(User):
    name = models.CharField(max_length=20)
    position = models.CharField(max_length=20)

    class Meta(User.Meta):
        pass

class Ingridient(models.Model):
    name = models.CharField(max_length=20)
    extra_price = models.IntegerField()

    def __str__(self):
        return self.name
    

class Food(models.Model):
    name = models.CharField(max_length=20)
    start_price = models.IntegerField()
    orders = models.ManyToManyField(Ingridient, related_name='food', through='Order')

    

class Order(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    ingridient = models.ForeignKey(Ingridient,on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    worker = models.ForeignKey(Worker,on_delete=models.CASCADE)
    order_date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.food.name} - {self.ingridient.name} - {self.client.name} - {self.worker.name}'

