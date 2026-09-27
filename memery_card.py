from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QMessageBox, QRadioButton, QGroupBox, QPushButton, QButtonGroup)
from random import shuffle, randint

class Question:
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question1 = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

New_question = []
New_question.append(Question('На каком языке программирования написанно это прложение?', "Питон", "С++", "Паскаль", "0101"))
New_question.append(Question('Что делать если загорелся комп?', "вытащить шнур из разетки и попробывать потушить пожар", "Попить чая", "выпрегнуть с окна", "Вызвать помощь"))
New_question.append(Question('В каком году началась война?', "в 1939", "в 1940", "в 1942", "в 1938"))
New_question.append(Question('Кто поет лунная саната?', "Битховен", "Леонардо Эль-капри (я не знаю ктоэто)", "Давинчи", "Моцард"))
New_question.append(Question('Кто написалкартину <Мона Лиза>?', "Давинчи", "Метафосфор", "Леонель пепси", "Рональда" ))
New_question.append(Question('Сколько месяцев в году имеют 31 день?', "7 месяцев", "5 месяцев", "8 месяцев", "6 месяцев"))
New_question.append(Question(' Сколько планет в Солнечной системе (по современной классификации)?', " всего 8", "наверно 7", 'всего 9', "возможно10"))
New_question.append(Question('Сколько длиться здоровый сон у нормального чвеловека', "12 часов", "8 часов", "5 часов(столькоя исплю)", "Вообще не спать"))
New_question.append(Question('Сколько длиться тренирока погресивного спортсмена? ', "3 часа минимум", "1 час", "2 часа", "полтора часа"))
New_question.append(Question('Сколько раз надокушатьв днеь что бы набпрать мышечную массу ? и что надо есть ?', "3 раза, белок, углеводы, кальций", "3 раза, мясо", "2 раза в день, просто углеводы", "4 раза, без разницы"))
New_question.append(Question('Сколько мтнут надо бегать что бы кровь разогреласб?', "пол часа", "2 часа(это больше для весогонки чем для разагревасуставов)", 'кровь и так разогрета зачем это?', '1 час'))
New_question.append(Question("Сколько учеников поместиться в класс если га весь класс только 11 парт?", "22 человека", '21 человека', '20 человека', '19 человека'))


def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    button.setText('Следующий вопросс')

def show_qestion():
    AnsGroupBox.hide()
    RadioGroupBox.show()
    button.setText('Ответить')
    GroupBox.setExclusive(False)
    rbtn1.setChecked(False)
    rbtn2.setChecked(False)
    rbtn3.setChecked(False)
    rbtn4.setChecked(False)
    GroupBox.setExclusive(True)

def ask(q):
    shuffle(answers)
    qeustion.setText(q.question1)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_correct.setText(q.right_answer)
    show_qestion()

def show_correct(res):
    lb_result.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правда')
        window.score += 1
        print('Статистика\n- Всего вопросов:', window.total, '\n-Правильных ответов:', window.score)
        print('Рейтинг:',(window.score/window.total*100), '%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('неверно')
            print('рейтинг:', (window.score/window.total*100), '%')
    

def next_question():
    window.total += 1 
    print('Статистика\n- Всего вопросов:', window.total, '\n-Правильных ответов:', window.score)
    cur_question =  randint(0, len(New_question) - 1)
    q = New_question[cur_question]
    ask(q)

def click_ok(): 
    if button.text() == 'Ответить':
        check_answer()
    else:
        next_question() 

app = QApplication([])
window = QWidget()
button = QPushButton("Ответить")
window.resize(600, 400)
window.setWindowTitle('Карточки для запоминания')

qeustion = QLabel('Выбери правильные ответы:')

rbtn1 = QRadioButton('1')
rbtn2 = QRadioButton('2')
rbtn3 = QRadioButton('3')
rbtn4 = QRadioButton('4')


answers = [rbtn1, rbtn2, rbtn3, rbtn4]

GroupBox = QButtonGroup()
GroupBox.addButton(rbtn1)
GroupBox.addButton(rbtn2)
GroupBox.addButton(rbtn3)
GroupBox.addButton(rbtn4)


RadioGroupBox = QGroupBox()

main_group_line = QVBoxLayout()
group_line1 = QHBoxLayout()
group_line2= QHBoxLayout()

group_line1.addWidget(rbtn1)
group_line1.addWidget(rbtn2)
group_line2.addWidget(rbtn3)
group_line2.addWidget(rbtn4)

main_group_line.addLayout(group_line1)
main_group_line.addLayout(group_line2)

RadioGroupBox.setLayout(main_group_line)

AnsGroupBox = QGroupBox('Результат теста')
lb_result = QLabel('Правда\неправда')
lb_correct = QLabel('Верный ответ')

ans_group_line = QVBoxLayout()
ans_group_line.addWidget(lb_result, alignment=(Qt.AlignTop | Qt.AlignLeft))
ans_group_line.addWidget(lb_correct, alignment=Qt.AlignCenter)

AnsGroupBox.setLayout(ans_group_line)
main_line = QVBoxLayout()
line1=QHBoxLayout()
line2=QHBoxLayout()
line3=QHBoxLayout()

line1.addWidget(qeustion, alignment=Qt.AlignCenter)
line2.addWidget(RadioGroupBox)
line2.addWidget(AnsGroupBox)
line3.addStretch(2)
line3.addWidget(button, stretch=2)
line3.addStretch(2)
AnsGroupBox.hide()

main_line.addLayout(line1, stretch=2)
main_line.addLayout(line2,stretch=8)
main_line.addStretch(1)
main_line.addLayout(line3, stretch=2)
main_line.addStretch(1)
main_line.addSpacing(5)

window.setLayout(main_line)

window.setStyleSheet("""
    QWidget {
        background-color: #f0f0f0;
        font-family: 'Segoe UI', sans-serif;
        font-size: 14px;
    }
    QGroupBox {
        background-color: white;
        border: 1px solid #ccc;
        border-radius: 8px;
        margin-top: 10px;
        padding-top: 10px;
    }
    QGroupBox::title {
        subcontrol-origin: margin;
        left: 10px;
        padding: 0 5px;
        color: #2c3e50;
        font-weight: bold;
    }
    QRadioButton {
        spacing: 10px;
        padding: 5px;
    }
    QRadioButton::indicator {
        width: 18px;
        height: 18px;
    }
    QPushButton {
        background-color: #3498db;
        color: white;
        border: none;
        border-radius: 6px;
        padding: 10px 20px;
        font-weight: bold;
    }
    QPushButton:hover {
        background-color: #2980b9;
    }
    QPushButton:pressed {
        background-color: #1f618d;
    }
    QLabel {
        color: #2c3e50;
    }
""")

window.score = 0
window.total = 0
next_question()
button.clicked.connect(click_ok)
window.show()
app.exec()
