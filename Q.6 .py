string_list = ["Empathy", "Empathy", "Kindness", "Kindness", "Compassion", "Humble", "Humble"]
b=[]
i=0
while i<len(string_list):
    if string_list[i] not in b:
        b.append(string_list[i])
    i=i+1
print(b)    

