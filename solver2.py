f = open("sgb-words.txt", "r")
data = f.read().splitlines() 
f.close()

f = open("sgb-words.txt", "r")
data2 = f.read().replace('\n', '')
f.close()

letter_freq = {}
for i in data2:
    if i in letter_freq:
        letter_freq[i] = letter_freq[i]+1
    else:
        letter_freq[i] = 1

for i in letter_freq:
    letter_freq[i]=letter_freq[i]/28785

score_list = []
for j in range(len(data)):
    score = 0
    for i in letter_freq:
        if i in set(data[j]):
            score = score+letter_freq[i]
    score_list.append(score)

word_scores = dict(zip(data,score_list))

sorted_word_scores=dict(sorted(word_scores.items(),key=lambda item: item[1],reverse=True ))

sorted_word_list=list(sorted_word_scores.keys())
print("Here are first guess suggestions:")
for i in range(10):
    print(sorted_word_list[i])

help0="y"
greys_letters=[]
#yellows_letters=[]
#greens_letters=[]
greens_dict={}
yellows_dict={}

while help0=="y":
    print("Enter your guess:")
    guess=input()
    print("Enter result (g for greens, y for yellows, x for greys):")
    result=input()
    
    
    greens=[i for i, x in enumerate(result) if x == "g"]
    yellows=[i for i, x in enumerate(result) if x == "y"]
    greys=[i for i, x in enumerate(result) if x == "x"]
    
    #greys_letters=[]
    for i in greys:
        greys_letters.append(guess[i])
    
    greens_letters=[]
    for i in greens:
        greens_letters.append(guess[i])

    #greens_dict = dict(zip(greens,greens_letters))
    for o in greens:
        greens_dict.update({o: guess[o]})
    
    yellows_letters=[]
    for i in yellows:
        yellows_letters.append(guess[i])
    
    for o in yellows:
        yellows_dict.update({o: guess[o]})

    new_word_list=[]
    for i in sorted_word_list:
        a = 0
        for j in greys_letters:
            if j in i:
                a = a + 1
            else:
                a = a
        for k in yellows_letters:
            if k not in i:
                a = a + 1
            else:
                a = a
        for l in greens_dict:
            if i[l] != greens_dict[l]:
                a = a + 1        
            elif greens_dict[l] not in i:
                a = a + 1
            else:
                a = a
        for l in yellows_dict:
            if i[l] == yellows_dict[l]:
                a = a + 1        
            elif yellows_dict[l] not in i:
                a = a + 1
            else:
                a = a
        if a == 0:
            new_word_list.append(i)
            
    print(len(new_word_list),"remaining solutions from",len(data), "total possibilities. Here are next guess suggestions:")
    for i in range(min(len(new_word_list),10)):
        print(new_word_list[i])
    
    
    print("Still need help? y or n")
    help0=input()
    if help0 == "n":
        break
