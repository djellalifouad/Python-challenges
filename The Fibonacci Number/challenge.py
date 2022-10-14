def fibonacci(num):
 if(num in [0,1]):
   return 1
 else:
   return fibonacci(num-1) + fibonacci(num-2)
