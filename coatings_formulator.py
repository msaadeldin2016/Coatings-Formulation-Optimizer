import matplotlib.pyplot as plt

class CoatingFormulator:
    def __init__(self, formulation_name):
        self.name = formulation_name
        self.ingredients = {}
        
    def add_ingredient(self, name, weight_grams, cost_per_kg):
        """Adds a chemical ingredient with its weight and cost."""
        self.ingredients[name] = {
            'weight': weight_grams,
            'cost_per_kg': cost_per_kg
        }
        
    def calculate_formulation(self):
        """Calculates total weight, percentages, and total cost."""
        total_weight = sum(item['weight'] for item in self.ingredients.values())
        
        print(f"\n--- Formulation Report for: {self.name} ---")
        print(f"Total Weight: {total_weight:.2f} grams\n")
        print(f"{'Ingredient':<15} | {'Weight (g)':<10} | {'Percentage (%)':<15} | {'Cost/kg ($)':<12}")
        print("-" * 60)
        
        total_cost = 0
        names = []
        percentages = []
        
        for name, data in self.ingredients.items():
            percentage = (data['weight'] / total_weight) * 100
            cost_contribution = (percentage / 100) * data['cost_per_kg']
            total_cost += cost_contribution
            
            names.append(name)
            percentages.append(percentage)
            
            print(f"{name:<15} | {data['weight']:<10.2f} | {percentage:<14.2f}% | ${data['cost_per_kg']:<11.2f}")
            
        print("-" * 60)
        print(f"Calculated Raw Material Cost: ${total_cost:.2f} per kg")
        
        # Economic Optimization Advice
        if total_cost > 4.5:
            print("⚠️ Optimization Warning: High-cost formulation. Consider increasing Filler percentage.")
        else:
            print("✅ Optimization Status: Cost-effective formulation.")
            
        return names, percentages

    def plot_formulation(self, names, percentages):
        """Generates a pie chart for the chemical composition."""
        plt.figure(figsize=(8, 6))
        colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']
        plt.pie(percentages, labels=names, autopct='%1.1f%%', startangle=140, colors=colors, shadow=True)
        plt.title(f"Chemical Composition Breakdown - {self.name}")
        plt.axis('equal')
        plt.show()

# --- Execution Example (Testing the Powder Coating formulation) ---
if __name__ == "__main__":
    # Create a new Powder Coating Formulation instance
    coatings_app = CoatingFormulator("Eco-Powder Coating V1")
    
    # Adding chemical ingredients (Name, Weight in grams, Cost per kg)
    coatings_app.add_ingredient("Epoxy Resin", 550, 5.20)
    coatings_app.add_ingredient("Hardener", 150, 6.50)
    coatings_app.add_ingredient("TiO2 Pigment", 100, 3.80)
    coatings_app.add_ingredient("Barium Sulfate", 200, 1.10) # Filler
    
    # Run analysis
    names, percentages = coatings_app.calculate_formulation()
    
    # Generate visual data
    coatings_app.plot_formulation(names, percentages)