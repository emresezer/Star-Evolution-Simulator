import matplotlib.pyplot as plt
print("🌟 Star Evolution Simulator")
print("---------------------------")
while True:
    try:
        mass = float(input("Enter the star's mass (in Solar masses, M☉): "))
        if mass <= 0:
            print("Mass cannot be zero or negative! Please enter again.")
            continue
        break
    except ValueError:
        print("Invalid input! Please enter a number.")
main_sequence_years = 1e10 * (mass ** -2.5)
red_giant_years = main_sequence_years * 0.1
if mass < 8:
    final_stage = "White Dwarf"
elif mass < 20:
    final_stage = "Neutron Star"
else:
    final_stage = "Black Hole"
stages = ["Main Sequence", "Red Giant", "Final Stage"]
durations = [main_sequence_years, red_giant_years, 1]
cumulative = [0, main_sequence_years, main_sequence_years + red_giant_years]
print("\n🔭 Estimated Life Cycle:")
print(f"Main Sequence Phase: {main_sequence_years:.2e} years")
print(f"Red Giant Phase: {red_giant_years:.2e} years")
print(f"Final Stage: {final_stage}")
plt.figure(figsize=(8,5))
plt.barh(stages, durations, left=cumulative, color=['yellow', 'red', 'grey'])
plt.xlabel("Years (approx.)")
plt.title(f"Life Cycle of a {mass} M☉ Star")
plt.grid(axis='x', linestyle='--', alpha=0.5)
plt.show()
