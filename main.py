from currency_converter import CurrencyConverter

# c = CurrencyConverter()
# print(c.currencies)

import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('design.ui', self)

        self.converter = CurrencyConverter()

        self.current_cur1 = 'RUB'
        self.current_cur2 = 'USD'

        self.update()

        self.calendarWidget.setVisible(False)
        self.hidden_description.setVisible(False)

        self.full_des_btn.clicked.connect(self.show_description)
        self.input.textChanged.connect(self.update)

    def update(self):
        cur1 = self.input.text()

        if cur1.isdigit():
            updated_cur2 = round(self.converter.convert(
                cur1,
                self.current_cur1,
                self.current_cur2
            ), 4)

            self.output.setText(str(updated_cur2))

            cur_for_1_input = round(self.converter.convert(
                1,
                self.current_cur1,
                self.current_cur2
            ), 5)

            self.cur_des.setText('1 {} = {} {}'.format(
                self.current_cur1,
                cur_for_1_input,
                self.current_cur2
            ))

            cur_for_1_output = round(self.converter.convert(
                1,
                self.current_cur2,
                self.current_cur1
            ), 5)

            self.cur_des2.setText('1 {} = {} {}'.format(
                self.current_cur2,
                cur_for_1_output,
                self.current_cur1
            ))

        else:
            self.output.setText('')
            self.cur_des.setText('Можно вводить только числа.')
            self.cur_des2.setText('')

    def show_description(self):
        if not self.hidden_description.isVisible():
            self.hidden_description.setVisible(True)
            self.full_des_btn.move(0, 433)
            self.full_des_btn.setText("Скрыть")
        else:
            self.hidden_description.setVisible(False)
            self.full_des_btn.move(6, 290)
            self.full_des_btn.setText("Развернуть")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
