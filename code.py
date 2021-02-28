#merge sort algorithm to sort the given items
#START OF MERGE SORT ALGORITHM
def merge(arr, l, m, r): 
    n1 = m - l + 1
    n2 = r- m 
    L = [0] * (n1) 
    R = [0] * (n2) 
    for i in range(0 , n1): 
        L[i] = arr[l + i] 
  
    for j in range(0 , n2): 
        R[j] = arr[m + 1 + j] 
  
    
    i = 0     
    j = 0     
    k = l
  
    while i < n1 and j < n2 : 
        if L[i][0] <= R[j][0]: 
            arr[k] = L[i] 
            i += 1
        else: 
            arr[k] = R[j] 
            j += 1
        k += 1
  
    while i < n1: 
        arr[k] = L[i] 
        i += 1
        k += 1
  
    while j < n2: 
        arr[k] = R[j] 
        j += 1
        k += 1
def mergeSort(arr,l,r): 
    if l < r: 
        m = (l+(r-1))//2
        mergeSort(arr, l, m) 
        mergeSort(arr, m+1, r) 
        merge(arr, l, m, r) 
#END OF MERGE SORT ALGORITHM

#GETTING DATA FROM THE FILE
with open('input.txt') as f:           #open the input file and read each line and lines will the array data.
    lines = f.readlines()
arr=[]

#CLEANING THE DATA(PREPROCESSING)
for i in range(len(lines)):			   #Traverse each line and clean the data
	if(i!=len(lines)-1):
		arr.append(lines[i][:-1])
ans=[]
for i in arr:						  #Traverse each time and store the data as a tuple(itemvalue,itemname) and add to the ans array
	if("Number of employees" in i):
		l=i.split(":")
		Number_of_employees=int(l[1])
	else:
		if("Goodies and Prices" in i):
			continue
		else:
			if(i):
				l=i.split(":")
				ans.append((int(l[1]),l[0]))

#ACTUAL LOGIC
mergeSort(ans,0,len(ans)-1)                     #sort the answer array
min1=99999999999999
p=-1
for i in range(0,len(ans)-Number_of_employees+1):        #traverse through the array and find the index that has minimum difference
	if(ans[i+Number_of_employees-1][0]-ans[i][0] < min1):
		min1=ans[i+Number_of_employees-1][0]-ans[i][0]
		p=i

#WRITE THE OUTPUT TO THE OUTPUT.TXT FILE
file1=open("output.txt","w")                              #open output.txt file in the write mode.
l=[]
string1="The goodies selected for the distribution are:\n"
string2="\n"
file1.write(string1)									#start writing into the file as mentioned in output.
file1.write(string2)
for i in range(p,p+Number_of_employees):				#since we got the index with minimum difference,traverse through the number of emplooyess and fetch the required data
	temp=ans[i][1]+": "+str(ans[i][0])+"\n"
	l.append(temp)
file1.writelines(l)										#write the fetched data to the file.
file1.write(string2)
difference=ans[p+Number_of_employees-1][0]-ans[p][0]
string3="And the difference between the chosen goodie with highest price and the lowest price is "+str(difference)
file1.write(string3)

#output will be present in the given format in output.txt file.
