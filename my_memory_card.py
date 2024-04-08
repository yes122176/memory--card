from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout,
                             QVBoxLayout, QGroupBox, QRadioButton,
                             QPushButton, QLabel, QButtonGroup)
from random import shuffle

class Question():
    def __init__(self, text_question, right_answer, wrong1, wrong2, wrong3):
        self.text_question = text_question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

list_question = []
q1 = Question('Когда отменили крепостное право?', '1861', '1896', '1854', '1862')
q2 = Question('Когда гагарин полетел в космос?', '1961', '1965', '1963', '1954')
q3 = Question('Сколько будет 1900 + 2?', '1902', '5', '30', '1')
q4 = Question('Сколько длилась столетняя война?', '116', '1822', '18008', '100')
list_question.append(q1)
list_question.append(q2)
list_question.append(q3)
list_question.append(q4)

max_question = len(list_question)



app = QApplication([])

window = QWidget()
window.setWindowTitle('Memo Card')
window.resize(700, 570)
window.right_count = 0
window.wrong_count = 0


'''Интерфейс приложения Memory Card'''
btn_OK = QPushButton('Ответить')
lb_Question = QLabel('Средняя продолжительность жизни?')
label_stats = QLabel('Статистика')
label_stats.hide()
label_stats2 = QLabel('Количество верных ответов: ')
label_stats3 = QLabel('Рейтинг:')
label_stats2.hide()
label_stats3.hide()

RadioGroupBox = QGroupBox("Варианты ответов")
rbtn_1 = QRadioButton('80')
rbtn_2 = QRadioButton('90')
rbtn_3 = QRadioButton('100')
rbtn_4 = QRadioButton('200')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)


layout_ans1 = QVBoxLayout()
layout_ans2 = QHBoxLayout()
layout_ans3 = QHBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
layout_ans1.addWidget(label_stats)
layout_ans1.addWidget(label_stats2)
layout_ans1.addWidget(label_stats3)

RadioGroupBox.setLayout(layout_ans1)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)

layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2)
layout_line3.addStretch(1)


layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1,stretch=2)
layout_card.addLayout(layout_line2,stretch=8)
layout_card.addLayout(layout_line3,stretch=1)
layout_card.addWidget(label_stats)
layout_card.addWidget(label_stats2)
layout_card.addWidget(label_stats3)


AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('Правильно/Неправильно')
lb_Correct = QLabel('80')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Result, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
layout_line2.addWidget(AnsGroupBox)


def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')
def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

answers = [rbtn_1,rbtn_2,rbtn_3,rbtn_4]
def ask(quest):
    shuffle(answers)
    answers[0].setText(quest.right_answer)
    answers[1].setText(quest.wrong1)
    answers[2].setText(quest.wrong2)
    answers[3].setText(quest.wrong3)
    lb_Question.setText(quest.text_question)
    lb_Correct.setText(quest.right_answer)
    show_question()
def show_correct(res):
        lb_Result.setText(res)
        if RadioGroupBox.isVisible():
            print_stats()
            if res == 'Правильно!':
                window.right_count += 1
            else:
                window.wrong_count += 1
            show_result()
        elif len(list_question) == 0:
            end_test
        else:
            shuffle(list_question)
            quest = list_question[0]
            ask(quest)
            list_question.remove(quest)


def chec_answer():
        if answers[0].isChecked():
            show_correct('Правильно!')
        else:
            show_correct('Неверно!')

        
def print_stats():
    if window.right_count != 0 or window.wrong_count != 0:
        print('Стастистика')
        print('Кол-во верных ответов:', window.right_count)
        print('Кол-во неверных ответов:', window.wrong_count)
        print('Рейтинг:', round(window.right_count * 100 / (window.right_count + window.wrong_count), 2))
    else:
         print('Стастистика')
         print('Кол-во верных ответов:', window.right_count)
         print('Кол-во неверных ответов:', window.wrong_count)   

def end_test():
    AnsGroupBox.hide()
    btn_OK.hide()
    lb_Question.setText('РЕЗУЛЬТАТ ТЕСТА') 
    label_stats.setText('Статистика')
    label_stats2.setText('Количество верных ответов: ' + str(window.right_count))
    label_stats3.setText('Рейтинг: ' + str(round(window.right_count * 100 / (window.right_count + window.wrong_count), 2)))
    label_stats.show()
    label_stats2.show()
    label_stats3.show()


window.setLayout(layout_card)
window.setWindowTitle('Memory  card')
first_quest = list_question[0]
ask(first_quest)
list_question.remove(first_quest)
ask(list_question[0])
btn_OK.clicked.connect(chec_answer)
window.show()
app.exec()
