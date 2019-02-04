'''1.Γράψτε τον κώδικα μιας συνάρτησης που θα ονομάζεται sumIntervals η οποία παίρνει σαν είσοδο μια λίστα από διαστήματα και επιστρέφει το άθροισμα του μήκους των διαστημάτων. Προσοχή: Διαστήματα που επικαλύπτονται θα πρέπει να μετρώνται μόνο μια φορά.
Παραδείγματα:
sumIntervals( [[1,2], [6, 10], [11, 15] ] ) Επιστρέφει 9
sumIntervals( [[1,4], [7, 10], [3, 5] ] ) Επιστρέφει 7
sumIntervals( [[1,5], [10, 20], [1, 6], [16, 19], [5, 11]] ) Επιστρέφει 19 '''
def sumIntervals(L):                                                                                                                                                                                                
    global sum
    sum=0
    dontforgetlist=[]
    listlengh=len(L)
    for i in range(0,listlengh,1):
        a=L[i][0]
        b=L[i][1]
        for j in range(a,b,1):
           sum=sum+1
           for k in range(0,len(dontforgetlist)):
           	  if j==dontforgetlist[k]:
           	  	sum= sum-1
           dontforgetlist.append(j)
           
           
           	  	

    print ("the result is ",+ sum)

 
sumIntervals( [[1,2], [6, 10], [11, 15] ])
sumIntervals( [[1,4], [7, 10], [3, 5] ] )
sumIntervals( [[1,5], [10, 20],[1,6], [16,19],[5,11]])
