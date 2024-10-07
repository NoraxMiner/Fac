input_data = open('input.txt', 'r') 
n= input_data.read() 
#-------------------------------------------------------------------------
fact_n = 1
for i in range(1,int(n) + 1):
    fact_n *= i

#-------------------------------------------------------------------------
output_data = open('output.txt', 'w') 
output_data.write(str(fact_n)) 

input_data.close() 
output_data.close()