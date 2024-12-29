import pandas as pd
import numpy as np
import time

#~~~~~~~~~~ Solution 1 ~~~~~~~~~~#

def d1_s1(input):
    input_1 = input.sort_values(by=["List 1"])["List 1"]
    input_2 = input.sort_values(by=["List 2"])["List 2"]

    #sorted_input = pd.DataFrame(np.array([input_1, input_2])).T
    #print(sorted_input.head(10))

    distances = np.abs(np.array(input_1) - np.array(input_2))
    #print(distances[:10])

    result = np.sum(distances)
    print(result)

#d1_s1(input)

#~~~~~~~~~~ Solution 2 ~~~~~~~~~~#

def d1_s2(input):
    print(np.sum(np.abs(np.sort(np.array(input['List 1'])) - np.sort(np.array(input['List 2'])))))

#d1_s2(input)


#-------------------Part 2-------------------#

def repetition_calcul(list_i):
    '''
    Count the number of time the first number in the list is repeated
    
    repetition_calcul(list)
    '''
    i = list_i[0]
    count = 0
    while list_i[0] == i :
        count += 1
        i = list_i[count] # nbr at the next index
    return count


def d1_p2(input):
    input_1 = list(input.sort_values(by=["List 1"])["List 1"])
    input_2 = list(input.sort_values(by=["List 2"])["List 2"])
    #print(input_1[:10])
    #print(input_2[:10])

    similarity_score = 0
    for i in range(len(np.unique(input_1))) :
        if input_2 and input_1:
            while input_2[0] < input_1[0]:  # Test if <
                del input_2[0]
                if not input_2:
                    #print("List 2 is empty")
                    break
                #print("Nbr skipped in list 2")
            if  input_2 and input_1 and input_2[0] == input_1[0] :   # Test if =
                rep_list_1 = repetition_calcul(input_1)
                rep_list_2 = repetition_calcul(input_2)
                #print(f"{input_1[0]} repeated {rep_list_1} time in list 1 and {rep_list_2} time in list 2")
                similarity_score = similarity_score + input_1[0]*rep_list_1*rep_list_2 # nbr_value * nbr_of_repetition_in_list_1 * nbr_of_repetition_in_list_2
                
                # Enlever des listes les répétitions du nbr déjà compter
                del input_1[0:rep_list_1]
                del input_2[0:rep_list_2]
            elif input_1:          # Skip this nbr in list 1
                del input_1[0]
                #print("Nbr skipped in list 1")
            #print(input_1[:10])
            #print(input_2[:10])
        
    
    print(similarity_score)



######################## Robin ########################

def separer_listes():
    liste_1 = []
    liste_2 = []
    fichier_path = 'input.txt' 

    with open(fichier_path, 'r') as fichier:
        for ligne in fichier:
            nombres = ligne.split()
            if len(nombres) == 2: 
                liste_1.append(nombres[0])
                liste_2.append(nombres[1])

    return liste_1, liste_2

def j1_2():
    liste_1, liste_2 = separer_listes()
    similarity = 0
    for i in liste_1 :
        occurs = 0
        for j in liste_2 :
            if i == j :
                occurs += 1
        similarity += int(i)*occurs
    print(similarity)



#++++++++++++++++ Main ++++++++++++++++# 
if __name__ == '__main__':
    start = time.time()

    input = pd.read_csv('input.txt', sep='   ', header=None, names=["List 1","List 2"], engine='python', dtype=int)
    
    #d1_s1(input)   # Best time 0.602ms

    #d1_s2(input)   # Best time 0.5ms

    #d1_p2(input)   # Best time 0.7ms

    j1_2()         # Best time 3.19ms
    
    print("(Done in {:.3f}ms)".format(float(time.time() - start)*100))