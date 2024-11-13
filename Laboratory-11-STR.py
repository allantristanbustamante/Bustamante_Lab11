foods = []

print("Enter different kinds of foods")
count = 0
while count < 10:
    food = input(f"Food {count + 1} ")
    foods.append(food) 
    count +=1 
    
num_letters = int(input("Enter the number of letters to filter foods by: "))

result = []
for food in foods: 
    if len(food) == num_letters:
        result.append(food)
        
if result:
    print("Foods with", num_letters, "letters:", ", ".join (result))
else: 
    print("No foods found with", num_letters, "letters.")