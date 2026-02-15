#Calculator With History

#User input whole equation-- 5+5 , then data is stored in .txt file

History_file= "history.txt"

def show_history():
    file= open(History_file ,'r')
    lines= file.readlines()
    if (len(lines)==0):
        print("No History Found!")
    else:
        for line in reversed(lines):
            print(line.strip())
    file.close()
         
       
def clear_history():
    file= open(History_file, 'w')
    file.close()
    print("History Cleared")
    
def save_to_history(equation, result):
    file= open(History_file, 'a')
    file.write(equation+"="+str(result)+"\n")
    file.close()
    
def calculate(user_input):
    parts= user_input.split()
    if len(parts)!=3:
        print("Invalid input , use formal no operator , ex- 2+2, 4*5")
        
    num1= float(parts)[0]
    opr= parts[1]
    num2= float(parts)[2]
    
    if opr=='+':
        result= num1+num2
    elif opr=="-":
        result= num1-num2
    elif opr=="*":
        result= num1*num2
    elif opr=="/":
        if num2==0:
            print("Cannot divide by 0")
            return
        result= num1/num2
    else:
        print("Invalid Selection")
        
    if int(result)==result:
        result= int(result)
        
    print("Result",result)
    
    save_to_history(user_input, result)
    
    
    
def main():
    print("---SAMPLE CALCULATOR---")
    while True:
            
        user_input= input("Enter Calculation")
        
        if user_input=='exit':
                print("Good Bye")
                break
        elif user_input=='history':
                show_history()
                
        elif user_input=='clear':
                clear_history()
        else:
            calculate(user_input)
                
        
        
main()