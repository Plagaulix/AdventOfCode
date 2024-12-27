import pandas as pd
import numpy as np
import time

start = time.time()

input = pd.read_csv('input.txt', sep='   ', header=None, names=["List 1","List 2"], engine='python', dtype=int)

#~~~~~~~~~~ Solution 1 ~~~~~~~~~~#

input_1 = input.sort_values(by=["List 1"])["List 1"]
input_2 = input.sort_values(by=["List 2"])["List 2"]

#sorted_input = pd.DataFrame(np.array([input_1, input_2])).T
#print(sorted_input.head(10))

distances = np.abs(np.array(input_1) - np.array(input_2))
#print(distances[:10])

result = np.sum(distances)
print(result)


#~~~~~~~~~~ Solution 2 ~~~~~~~~~~#

#print(np.sum(np.abs(np.sort(np.array(input['List 1'])) - np.sort(np.array(input['List 2'])))))

print("(Done in {:.2f}ms)".format(float(time.time() - start)*100))