'''9. Γράψτε μια συνάρτηση η οποία να ονομάζεται maxSequence η οποία να παίρνει σαν είσοδο μία λίστα και να επιστρέφει την υπολίστα (συνεχόμενα στοιχεία μέσα στη λίστα) που έχει το μέγιστο άθροισμα.
Παράδειγμα: maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]) επιστρέφει 6: [4, -1, 2, 1] '''


def maxSequence(ls):
    if len(ls) == 0:
       raise Exception("Array empty") # should be non-empty
      
    runSum = maxSum = ls[0]
    i = 0
    start = finish = 0

    for j in range(1, len(ls)):
        if ls[j] > (runSum + ls[j]):
            runSum = ls[j]
            i = j
        else:
            runSum += ls[j]

        if runSum > maxSum:
            maxSum = runSum
            start = i
            finish = j
            global start1
            global finish1
            start1=start
            finish1=finish


    maxsequencenumbs=[]
    for p in range(start, finish+1):
       maxsequencenumbs.append(ls[p])
    print ("Τhe maxSequence total is", maxSum)
    print ("the maxSequence numbers",maxsequencenumbs)
    
        
   


maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])







