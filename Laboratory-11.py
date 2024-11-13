counter = 0
passed = 0
list = []

for x in range(5):
    num = int(input("Enter the grades of 5 students:"))
    if num <= 39 or num >= 101:
        print("Invalid Input. Number must be between 40 and 100")
        break
    else:
        list.append(num)
    if num >=75:
        passed += 1
        counter += 1
    else:
        counter += 1
    if counter == 5:
        print ()
        sumNums = sum(list)
        averageGrade = sumNums / 5
        averageGrade = round(averageGrade, 2)
        
        PassingPercentage = (passed / len(list)) * 100
        PassingPercentage = round(PassingPercentage, 2)
        
        print("Given Grade: " + str(list))
        print("Average Grade: " + str(averageGrade))
        print("Number of students who passed: " + str(passed))
        print("Percentage of the students who passed: " + str(PassingPercentage) + "%") 