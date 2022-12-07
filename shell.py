from filial1 .models import *

# shaurma = 50
# gamburger = 25
# chees = 10
# chicken = 70
# beef = 80
# salad = 15
# free = 15

client1 = Client(email= 'nikname21@gmail.com', password ='defender42', name = 'Азат Соколов', card_number = '4147565798789009')

worker1 = Worker(email = 'altywa1998@gmail.com', password= 'nono34',name = 'Алтынай Алиева', position = 'Оператор кассы')
client1.save()
worker1.save()

ingridients_chees = Ingridient.objects.create(name='chees',extra_price=10)
ingridients_chicken = Ingridient.objects.create(name='chicken',extra_price=70)
ingridients_beef = Ingridient.objects.create(name='beef',extra_price=80)
ingridients_salad = Ingridient.objects.create(name='salad',extra_price=15)
ingridients_free = Ingridient.objects.create(name='free',extra_price=15)

food_shaurma = Food.objects.create(name='shaurma',start_price=50)
food_gamburger = Food.objects.create(name='gamburger',start_price=25)


food_shaurma.orders.set([ingridients_beef, ingridients_chees, ingridients_salad,ingridients_free], through_defaults={'client':client1, 'worker':worker1})
shaurma_price = food_shaurma.start_price + ingridients_beef.extra_price + ingridients_chees.extra_price + ingridients_salad.extra_price + ingridients_free.extra_price
print(shaurma_price)

food_gamburger.orders.set([ingridients_chicken, ingridients_salad], through_defaults={'client':client1, 'worker':worker1})
gamburger_price = food_gamburger.start_price + ingridients_chicken.extra_price + ingridients_salad.extra_price
print(gamburger_price)

# client = Азат у Алтынай: shaurma + beef + chees + salad + free
#                         gamburger + chicken + salad

#     Выведите по отдельности стоимость:
#     Шаурмы которую заказал Азат

#     Гамбургера которую заказал Азат
#     Общую стоимость заказа
