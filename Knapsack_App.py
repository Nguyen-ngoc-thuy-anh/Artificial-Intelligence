from Knapsack_Solving import Knapsack
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit, QTextEdit, QInputDialog, QMessageBox

class KnapsackApp(QWidget):
   def __init__(self):
       super().__init__()
       self.show_error = False #Biến kiểm tra xem có cần hiển thị thông báo lỗi hay không?
       self.initUI()

   def initUI(self):
       self.setWindowTitle('Knapsack Problem Solver')
     
       # Widgets for max capacity
       self.capacity_label = QLabel('Maximum Capacity:')
       self.capacity_input = QLineEdit()
       self.capacity_input.setPlaceholderText('Enter maximum capacity')

       #Enter button for max capacity
       self.max_capacity_button = QPushButton("Enter")
       self.max_capacity_button.clicked.connect(self.enable_add_item_button)
       self.max_capacity_button.setEnabled(False)
     
       # Button to add items
       self.add_item_button = QPushButton('Add Item')
       self.add_item_button.clicked.connect(self.add_item)
       self.add_item_button.setEnabled(False)  # Initially disabled

       #Button to delete items
       self.delete_item_button = QPushButton('Delete Item')
       self.delete_item_button.clicked.connect(self.delete_item)
       self.delete_item_button.setEnabled(False) # Initially disabled

       # Display for input items
       self.input_items_display = QTextEdit()
       self.input_items_display.setReadOnly(True)

       # Display for out items
       self.output_items_display = QTextEdit()
       self.output_items_display.setReadOnly(True)

       # Button to solve knapsack
       self.solve_button = QPushButton('Solve Knapsack')
       self.solve_button.clicked.connect(self.solve_knapsack)
       self.solve_button.setEnabled(False)  # Initially disabled

       # Button to refresh screen
       self.refresh_button = QPushButton('Refresh')
       self.refresh_button.clicked.connect(self.refresh_screen)

       # Error label
       self.error_label = QLabel()

       # Layout setup
       vbox = QVBoxLayout()
       hbox1 = QHBoxLayout()
       hbox2 = QHBoxLayout()
       hbox3 = QHBoxLayout()

       hbox1.addWidget(self.capacity_label)
       hbox1.addWidget(self.capacity_input)
       hbox1.addWidget(self.max_capacity_button)

       hbox2.addWidget(self.add_item_button)
       hbox2.addWidget(self.delete_item_button)
       hbox2.addWidget(self.solve_button)

       hbox3.addWidget(self.refresh_button)

       vbox.addLayout(hbox1)
       vbox.addLayout(hbox2)
       vbox.addWidget(self.input_items_display)
       vbox.addWidget(self.output_items_display)
       vbox.addLayout(hbox3)

       self.setLayout(vbox)

       self.error_label = QLabel()
       vbox.addWidget(self.error_label)

       self.knapsack = Knapsack(max_capacity=0)

       # Connect signals to update button states
       self.capacity_input.textChanged.connect(self.update_max_capacity_button)
       self.capacity_input.textChanged.connect(self.show_capacity_error)

   def add_item(self):
        weight = self.get_positive_float('Enter Weight', 'Weight:')
        if weight is None:
                return
            
        value = self.get_positive_float('Enter Value', 'Value:')
        if value is None:
                return

        self.knapsack.items.append((weight, value))
        self.input_items_display.append(f'Added item - Weight: {weight:.2f}, Value: {value:.2f}')
        self.solve_button.setEnabled(True)  # Enable Solve Knapsack button after adding an item
        self.delete_item_button.setEnabled(True)

   def get_positive_float(self, title, label):
        while True:
            text, ok = QInputDialog.getText(self, title, label)
            if not ok:
                return None
            try:
                value = float(text)
                if value >= 0:
                    return value
                else:
                    self.show_error_message("Error", f"{label} must be greater than 0.")
            except ValueError:
                self.show_error_message("Error", f"{label} must be a valid number.")
   
   def delete_item(self):
        item_text, ok = QInputDialog.getItem(self, 'Delete Item', 'Select item to delete:', self.get_input_items())
        if ok:
            item_index = self.get_input_items().index(item_text)
            del self.knapsack.items[item_index]
            self.input_items_display.clear()
            for weight, value in self.knapsack.items:
                self.input_items_display.append(f'Weight: {weight:.2f}, Value: {value:.2f}')
 	    
        self.output_items_display.clear()
        self.knapsack.output_items = []
   
   def get_input_items(self):
        return [f'Weight: {weight:.2f}, Value: {value:.2f}' for weight, value in self.knapsack.items]                    

   def solve_knapsack(self):
       max_capacity = float(self.capacity_input.text())
       if max_capacity <= 0:
           self.show_error = True #Cần hiển thị thông báo lỗi
           return
     
       self.show_error = False
       self.error_label.clear() #Clear any previous error message

       self.knapsack.max_capacity = max_capacity
       total_value, total_weight = self.knapsack.knapsack_greedy()
       
       self.output_items_display.append('Selected items:')
       for weight, value in self.knapsack.output_items:
           if weight != 0.0 and value != 0.0:
               self.output_items_display.append(f'Weight: {weight:.2f}, Value: {value:.2f}')

       self.output_items_display.append('*********************************') 
       self.output_items_display.append(f'Maximum value: {total_value:.2f}')
       self.output_items_display.append(f'Total weight: {total_weight:.2f}')

   def refresh_screen(self):
       self.input_items_display.clear()
       self.output_items_display.clear()
       self.capacity_input.clear()
     
       if self.show_error:
           self.error_label.setText("Error: Maximum capacity must be greater than 0")
       else:
           self.error_label.clear()
     
       self.knapsack = Knapsack(max_capacity=0)
       self.add_item_button.setEnabled(False)  # Disable Add Item button after refresh
       self.solve_button.setEnabled(False)  # Disable Solve Knapsack button after refresh

   def update_button_states(self):
       # Enable Add Item button if text is not empty
       self.add_item_button.setEnabled(bool(self.capacity_input.text()))

   #Take input from the max capacity
   def update_max_capacity_button(self):
       max_capacity_text = self.capacity_input.text()
       max_capacity = max_capacity_text
       if max_capacity_text:
           max_capacity = float(max_capacity_text)
           if max_capacity > 0:
               self.max_capacity_button.setEnabled(True)
           else:
               self.max_capacity_button.setEnabled(False)
               # self.show_error_message("Error", "Maximum capacity must be greater than 0.")
 
   #Enter for maximum capacity will appear first then add item
   def enable_add_item_button(self):
       max_capacity_text = self.capacity_input.text()
       if max_capacity_text:
           max_capacity = float(max_capacity_text)
           if max_capacity > 0:
               self.knapsack.max_capacity = max_capacity #update maximum capacity
               self.error_label.clear()
               self.show_error = False
               self.add_item_button.setEnabled(True) # add_item button appears
               self.solve_button.setEnabled(True)
               self.max_capacity_button.setEnabled(False)
               self.capacity_input.setFocus()
           else:
               self.error_label.setText("Error: Maximum capacity must be greater than 0")
               self.show_error = True
       else:
           self.show_error_message("Error", "Maximum capacity is required.")

   def show_capacity_error(self):
       max_capacity_text = self.capacity_input.text()
       if max_capacity_text == '0':
           error_dialog = QMessageBox()
           error_dialog.setWindowTitle("Error")
           error_dialog.setText("Maximum capacity must be greater than 0.")
           error_dialog.setStandardButtons(QMessageBox.StandardButton.Ok)
           error_dialog.exec()
           self.show_error = True
       else:
           self.error_label.clear()
           self.show_error = False