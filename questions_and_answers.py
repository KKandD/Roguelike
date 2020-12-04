import random

question1 = 'Hobbiton to: '
question2 = '\'ghash\' co to znaczy w języku orków??? '
question3 = 'Glamdring to: '
question4 = 'Księga odnaleziona w Morii przez Gandlafa to: '
question5 = 'Dlaczego było Dziewięciu Piechurów w Drużynie??? '
question6 = 'Ile oskarów za adaptacje powieści Tolkiena otrzymał Peter Jackson: '
answers = [['A - wioska w Shire ', 'B - Dom Froda i Bilba Bagginsów', 'C - Dom Bagginsów z Sackville', 'D - Kraj Toma Bombadila'],
['A - imprezka', 'B - ogień', 'C - akohol', 'D - mama wołająca na obiad'],
['A - Elficki smatfon', 'B - Miecz Gandalfa', 'C - Nóż do smarowania elfickiego chleba', 'D - Miecz Sarumana Białego'],
['A - Kronika dziejów Balina', 'B - Przepis na bimber dziadka', 'C - Hinduski tutorial z Pythona', 'D - Testament Balina'],
['A - Bo nie mieli kanapek dla dziesiątego', 'B - Bo nie było więcej chętnych', 'C - Bo Frodo nie chcia', 'D - Bo było Dziewięciu Jeźdźców - Nazguli'],
['A - 17', 'B - 13', 'C - 7', 'D - 21']]

questions_list = [question1, question2, question3, question4, question5, question6]
# random_index = random.randint(0, len(questions_list) - 1)
# random_question = questions_list[random_index]

questions_dictionary = {
question1 : 'a',
question2 : 'b',
question3 : 'b',
question4 : 'a',
question5 : 'd',
question6 : 'a'
}