def intersect(a, b):
     return list(set(a) & set(b))

ours = open("ours_at_least_all_of_them","r") 
ours_holder=[]

for line in ours: 
    # print (line)
    line_new=line.strip("\n")
    line_new_new=line_new.lower()
    ine_new_new_new=line_new_new.strip()
    ours_holder.append(ine_new_new_new)


ours = open("ritter_at_least_all_of_them","r") 
ritter_holder=[]
for line in ours: 
    # print (line)
    line_new=line.strip("\n")
    line_new_new=line_new.lower()
    ine_new_new_new=line_new_new.strip()
    ritter_holder.append(ine_new_new_new)

intersection=intersect(ours_holder,ritter_holder)
t_minus_c=list(set(ours_holder) - set(ritter_holder))
c_minus_t=list(set(ritter_holder) - set(ours_holder))
# two_2_c=len(list(set(flatten_annotations) - set(unioned)))


file = open("intersection", "w")

for i in intersection:
    file.write(i+"\n")

file.close() 

file = open("t_minus_c", "w")

for i in t_minus_c:
    file.write(i+"\n")

file.close() 
file = open("c_minus_t", "w")

for i in c_minus_t:
    file.write(i+"\n")

file.close() 



print(len(intersection),len(t_minus_c),len(c_minus_t))