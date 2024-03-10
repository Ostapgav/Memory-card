from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit,
    QHBoxLayout, QVBoxLayout, QPushButton, QLabel

menu_win = QWidget()

Ib_quest = QLabel("Введіть запитання:")
Ib_right_ans = QLabel("Введіть вірну відповідь:")
Ib_wrong_ans1 = QLabel("Введіть першу хибну відповідь")
Ib_wrong_ans2 = QLabel("Введіть другу хибну відповідь")
Ib_wrong_ans3 = QLabel("Введіть третю хибну відповідь")

le_question = QLineEdit()
le_right_ans = QLineEdit()
le_wrong_ans1 = QLineEdit()
le_wrong_ans2 = QLineEdit()
le_wrong_ans3 = QLineEdit()

vl_labels = QVBoxLayout()
vl_labels.addWidget(Ib_quest)
vl_labels.addWidget(Ib_right_ans)
vl_labels.addWidget(Ib_right_ans1)
vl_labels.addWidget(Ib_right_ans2)
vl_labels.addWidget(Ib_right_ans3)

vl_lineEdits = QVBoxLayout()
vl_lineEdits.addWidget(le_question)
vl_lineEdits.addWidget(le_right_ans)
vl_lineEdits.addWidget(le_wrong_ans1)
vl_lineEdits.addWidget(le_wrong_ans2)
vl_lineEdits.addWidget(le_wrong_ans3)

hl_question = QHBoxLayout()
hl_question.addLayout(vl_labels)
hl_question.addLayout(vl_lineEdits)


