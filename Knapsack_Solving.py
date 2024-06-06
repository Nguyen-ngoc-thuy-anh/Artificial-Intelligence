class Knapsack:
   def __init__(self, max_capacity):
       self.max_capacity = max_capacity
       self.items = []  # List of (weight, value) tuples
       self.output_items = []  # List to store selected items

   def knapsack_greedy(self):
       # Filter out items with zero weight or zero value
       valid_items = [(weight, value) for weight, value in self.items if weight > 0 and value > 0]

       # Calculate value-to-weight ratio for each item
       items_with_ratio = [(value / weight, weight, value) for weight, value in valid_items]
       items_with_ratio.sort(reverse=True, key=lambda x: x[0])  # Sort by ratio in descending order

       total_value = 0
       total_weight = 0
       remaining_capacity = self.max_capacity
       for _, weight, value in items_with_ratio:
            if weight <= remaining_capacity:
                total_value += value
                total_weight += weight
                remaining_capacity -= weight
                self.output_items.append((weight, value))  # Add selected item
                if remaining_capacity == 0:
                    break
            else:
                # Fractional part of the last item
                fraction = remaining_capacity / weight
                fractional_value = fraction * value
                if fraction > 0 and fractional_value > 0:
                    total_weight += remaining_capacity
                    total_value += fractional_value
                    self.output_items.append((remaining_capacity, fractional_value))  # Add fractional item
                break

       return total_value, total_weight
   
