scores = [["Chris" ,83], ["David" , 96 ], ["Bill" , 92 ]]
poster = 0
i = 0
highest_score = 0

while i < 3:
    print(scores[i][1])
    
    if scores[i][1]> poster:
        poster = scores[i][1]
        print(poster, i )
        highest_score =i
    i = i+1
    
    
print(scores[highest_score])