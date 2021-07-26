scores = ["Chris" ,83, "David" , 96 , "Bill" , 92]
highest_score = 0
poster = 0
i = 1
while i < 6:
    print(scores[i])
    
    if scores[i] > poster:
        poster = scores[i]
        print(poster, i )
        highest_score =i
    i = i +2
    
    
print("highest score:" ,scores[highest_score] , "/" , "highest score person:" ,scores[highest_score -1])