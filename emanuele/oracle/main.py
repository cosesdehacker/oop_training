#!/usr/bin/python3
from random import choice


# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

def reply_question(name, previous_answer=None):
    question = input(f"Què necessites saber, {name}?\n")
    while '?' not in question:
        question = input(f"Això no és una pregunta. Esforça't més, caguntot, {name}.\n")
    answer = get_answer(previous_answer)
    print(answer)
    return answer


def get_answer(previous_answer=None):
    possible_answers = ["Sí", "No", "Gestiona tu", "Què va!", "Tu m'has vist a mi cara d'oracle?"]
    if previous_answer is not None:
        possible_answers.remove(previous_answer)
    answer = choice(possible_answers)
    return answer


def ask_more():
    ask_more_reply = input("Tens alguna altra pregunta per l'oracle? S/N\n")
    while ask_more_reply.upper() not in ['S', 'N', 'SI', 'NO']:
        ask_more_reply = input("Has de respondre només 'S' o 'N', ensumallufes!\n")
    if ask_more_reply.upper() == 'S':
        return True
    else:
        return False


def oracle():
    name = input("Ciao! Com et dius?\n")
    print("Benvinguda al servei interactiu d'Oracles SL. \n")
    answer = reply_question(name)
    while ask_more():
        answer = reply_question(name, answer)
    print("Doncs au, bon vent i barca nova!")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    oracle()
