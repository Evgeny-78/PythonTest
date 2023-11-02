from bibl_class_test import *

cat1 = Cat('Пушок', 'Мейн Кун', 2, 3.0, 15, 'мужской', ['Машка','Матроскин'])
cat2 = Cat('Матроскин', 'Дворняга', 4, 7.0, 33, 'мужской', [])
cat3 = Cat('Катя', 'Бенгальская', 8, 4.0, 27,'женский', ['Пушок', 'Моська'])
cat4 = Cat('Бос', 'Манчкин', 3, 5.0, 29,'мужской', [])
corm1 = Corm('кошачий', 'сухой', 0.3)
print(cat1.get_num())
print(cat1.get_listObj())
print(cat1 == cat4)
cat4.action_mymy()
print('end programm')