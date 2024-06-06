import sys
from PyQt6.QtWidgets import QApplication
from Knapsack_App import KnapsackApp

if __name__ == '__main__':
   app = QApplication(sys.argv)
   knapsack_app = KnapsackApp()
   knapsack_app.show()
   sys.exit(app.exec())