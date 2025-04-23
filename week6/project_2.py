Admitted = [] #empty list

jamb = int(input("What's your JAMB score? : "))

credits= int(input("How many credits did have for all five key subjects? :"))

interview = input("Did you pass your interview for this course? (yes/no):").lower()

if jamb>=250:
    if credits>=5:
        if interview == 'yes':
            print("Congratulations!!! You have been admitted into the Computer Science Department!")
elif jamb<=250:
    print("I'm sorry, you havent you arent admitted into the Computer Science")
elif credits<5:
 print("I'm sorry, you havent you arent admitted into the Computer Science")
elif interview == 'no':
 print("I'm sorry, you havent you arent admitted into the Computer Science")

 

    
           
           
