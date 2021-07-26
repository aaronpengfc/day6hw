score = [11 ,45 ,34]
name = ["aaron" , "ian" , "paul"]
highest_score = 0 
poster = 0
i = 0
while i < 3:
    #print(score[i])
    #print(name[i])
    
    if score[i] > poster:
        poster = score[i]
        print(poster, i )
        highest_score =i
    i = i+1
    
    
print(score[highest_score] , name[highest_score])