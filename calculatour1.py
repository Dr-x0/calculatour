while True :

  while True :
    try :
       first_number = float(input("enter first number : "))
       break
    except ValueError :
       print("invaled input . please entre a numirc value : ")        
  while True :
    try :
      operation = input("enter operation : ")
      if operation in ("+","-","/","*","**","!","%"):
        break
      else :
        raise ValueError 
    except ValueError :
        print("invaled oprator . please entere + , - , / , * ,**,!,%")

  
  while True :
    try :
      second_number = float(input("enter second number : ")) 
      if operation == "!":
         break
      if second_number == 0 and operation == "/":
       raise ZeroDivisionError
      break 
    except ValueError :
       print("invaled input , please entre a numirc value : ")
    except ZeroDivisionError: 
       print("cannot divide by zero . please enter another numirc value") 
  
     
  if operation == "+" :
       result = first_number + second_number
  elif operation == "*" :
      result = first_number * second_number
  elif operation == "-" :
      result = first_number - second_number
  elif operation == "%" :
      result = first_number % second_number
  elif operation == "/" :
      result = first_number / second_number
  elif operation =="**": 
      result = first_number ** second_number
  elif operation =="!": 
      del second_number
      result = first_number*(first_number+1)/2
        
  else :
      result = None
     

  if result != None : 
    print(result)


    repeat = input ("do you want to preform another operation (yes/no) : ")
  if repeat == "no" or "No" or "nO" or "NO":  
    break
 
print ("program exicted ")



















