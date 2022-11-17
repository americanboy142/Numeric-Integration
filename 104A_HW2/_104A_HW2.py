import simposons_rule as sr
import Trapezoidal as td
import Gauss3 as g3
import functions as fc
import pandas as pd
from numpy import array as numarr
from numpy import log as numlog
from numpy import zeros as numzero
from numpy import errstate as error

#%{
#       FOR GRADING
#           if all files are put into the same project everything is imported though this main file
#               csv files are not created each run they are just updated
#                   - so for correct output the csv files, or empty ones with the same name need to be in the project
#}






#%{
#   MISC VARIABLE ASSIGNMENTS
#}

main_matrix = numzero([10,9])
index = numarr([1,2,4,2**3,2**4,2**5,2**6,2**7,2**8,2**9])
error_matrix = numzero([10,9])
error_matrix_9x9 = numzero([9,9])
error_matrix_9x9_formated = numzero([9,9])
eindex = numarr(["r0","r1","r2","r3","r4","r5","r6","r7","r8"])


#%{
#   TABLE 1 
#   OUTPUT THE APROXIMATION FOR EACH N
#   The three functions are imported from functions.py
#   main matrix does not inclued index
#       - a 10x9 matrix just values
#}

funcs = [fc.f,fc.g,fc.h]
for fun in range(len(funcs)):
    for i in range(10):
        trap_aprox = td.Trap(-1,1.1,index[i],funcs[fun]).Trap()

        simp_aprox = sr.simpsons_rule(-1,1.1,index[i],funcs[fun]).simpsons()

        gauss_aprox = g3.G3(-1,1.1,index[i],funcs[fun]).G3()
        
        main_matrix[i,fc.trap_index+fun] = trap_aprox
        main_matrix[i,fc.simp_index+fun] = simp_aprox
        main_matrix[i,fc.Gauss_index+fun] = gauss_aprox

        error_matrix[i,fc.trap_index+fun] = abs(trap_aprox - fc.TrueValues[fun])
        error_matrix[i,fc.simp_index+fun] = abs(simp_aprox - fc.TrueValues[fun])
        error_matrix[i,fc.Gauss_index+fun] = abs(gauss_aprox - fc.TrueValues[fun])


#%{
#   ERROR MATRIX   
#       - input will be values from main matrix
#   each line is rate of convergence
#       - or change in error
#
#}

for column in range(3):
    for i in range(9):
        # grabs trap error
        error_matrix_9x9[i,fc.trap_index+column] = (numlog(error_matrix[i,fc.trap_index+column]/error_matrix[i+1,fc.trap_index+column]))/(numlog(index[i+1]/index[i]))
        # grabs simp error
        error_matrix_9x9[i,fc.simp_index+column] = (numlog(error_matrix[i,fc.simp_index+column]/error_matrix[i+1,fc.simp_index+column]))/(numlog(index[i+1]/index[i]))
        # grabs guass error
        error_matrix_9x9[i,fc.Gauss_index+column] = (numlog(error_matrix[i,fc.Gauss_index+column]/error_matrix[i+1,fc.Gauss_index+column]))/(numlog(index[i+1]/index[i]))

#%{
#   FORMATED ERROR MATRIX 
#       formats the original error matrix to fit the look
#}

count = 0
for i in range(3):
    # format trapezoidal
    error_matrix_9x9_formated[:,count] = error_matrix_9x9[:,fc.trap_index+i]
    # format simp
    count += 1
    error_matrix_9x9_formated[:,count] = error_matrix_9x9[:,fc.simp_index+i]
    # format gauss
    count += 1
    error_matrix_9x9_formated[:,count] = error_matrix_9x9[:,fc.Gauss_index+i]
    count += 1



#%{
#   converts main matix/error matrix to a data frame
#       - uses multi index to give desired look
#       - index is then added by setting DataFrame(index=index)
#           - this is the array or 2**n n in [0,9]
#   then sends the created data frame to the csv file
#}


heads = pd.DataFrame(
    [['Trapezoidal', 'cosine'], ["", 'C1 function'], ["", 'normal dist'], ['Simpson', 'cosine'], 
     ['', 'C1 function'], ['', 'normal dist'], ['Gauss3', 'cosine'], ['', 'C1 function'], ['', 'normal dist']],
    columns=["#Subintervals","-"],
)

head = pd.MultiIndex.from_frame(heads)
df = pd.DataFrame(main_matrix,columns=head,index=index)



df.to_csv("MethodIntegrand.csv")



heads = pd.DataFrame(
    [['cosine','Trapezoidal'], ["", 'Simpson'], ["", 'Gauss3'], ['C1 function', 'Trapezoidal'], 
     ['', 'Simpson'], ['', 'Gauss3'], ['normal dist', 'Trapezoidal'], ['', 'Simpson'], ['', 'Gauss3']],
    columns=["r#","-"],
)

head = pd.MultiIndex.from_frame(heads)
dfe = pd.DataFrame(error_matrix_9x9_formated,columns=head,index=eindex)


dfe.to_csv("IntegrandMethod.csv")



#%{
#   TEST 2
#       same as top for [-1,1]
#       sends to new file to keep original for eval
#}

for fun in range(len(funcs)):
    for i in range(10):
        trap_aprox = td.Trap(-1,1,index[i],funcs[fun]).Trap()

        simp_aprox = sr.simpsons_rule(-1,1,index[i],funcs[fun]).simpsons()

        gauss_aprox = g3.G3(-1,1,index[i],funcs[fun]).G3()
        
        main_matrix[i,fc.trap_index+fun] = trap_aprox
        main_matrix[i,fc.simp_index+fun] = simp_aprox
        main_matrix[i,fc.Gauss_index+fun] = gauss_aprox

        error_matrix[i,fc.trap_index+fun] = abs(trap_aprox - fc.TrueValues_2[fun])
        error_matrix[i,fc.simp_index+fun] = abs(simp_aprox - fc.TrueValues_2[fun])
        error_matrix[i,fc.Gauss_index+fun] = abs(gauss_aprox - fc.TrueValues_2[fun])


#print(error_matrix)

with error(divide='ignore', invalid='ignore'):
    for column in range(3):
        for i in range(9):
            # grabs trap error
                error_matrix_9x9[i,fc.trap_index+column] = (numlog(error_matrix[i,fc.trap_index+column]/error_matrix[i+1,fc.trap_index+column]))/(numlog(index[i+1]/index[i]))

            # grabs simp error
                error_matrix_9x9[i,fc.simp_index+column] = (numlog(error_matrix[i,fc.simp_index+column]/error_matrix[i+1,fc.simp_index+column]))/(numlog(index[i+1]/index[i]))

            # grabs guass error
                error_matrix_9x9[i,fc.Gauss_index+column] = (numlog(error_matrix[i,fc.Gauss_index+column]/error_matrix[i+1,fc.Gauss_index+column]))/(numlog(index[i+1]/index[i]))


#print(main_matrix)
count = 0
for i in range(3):
    # format trapezoidal
    error_matrix_9x9_formated[:,count] = error_matrix_9x9[:,fc.trap_index+i]
    # format simp
    count += 1
    error_matrix_9x9_formated[:,count] = error_matrix_9x9[:,fc.simp_index+i]
    # format gauss
    count += 1
    error_matrix_9x9_formated[:,count] = error_matrix_9x9[:,fc.Gauss_index+i]
    count += 1




heads = pd.DataFrame(
    [['Trapezoidal', 'cosine'], ["", 'C1 function'], ["", 'normal dist'], ['Simpson', 'cosine'], 
     ['', 'C1 function'], ['', 'normal dist'], ['Gauss3', 'cosine'], ['', 'C1 function'], ['', 'normal dist']],
    columns=["#Subintervals","-"],
)

head = pd.MultiIndex.from_frame(heads)
df = pd.DataFrame(main_matrix,columns=head,index=index)



df.to_csv("MethodIntegrand_2.csv")



heads = pd.DataFrame(
    [['cosine','Trapezoidal'], ["", 'Simpson'], ["", 'Gauss3'], ['C1 function', 'Trapezoidal'], 
     ['', 'Simpson'], ['', 'Gauss3'], ['normal dist', 'Trapezoidal'], ['', 'Simpson'], ['', 'Gauss3']],
    columns=["r#","-"],
)

head = pd.MultiIndex.from_frame(heads)
dfe = pd.DataFrame(error_matrix_9x9_formated,columns=head,index=eindex)
print(dfe,df)

dfe.to_csv("IntegrandMethod_2.csv")