immutadle_var=1,2,3,"a","time"
print(immutadle_var)
#immutadle_var[1]=4
#print(b=immutadle_var)- #операция выдает ошибку и помечена коментарием
#Кортежи неизменяемый объект
mutable_list=[1,2,3,'a','time']
mutable_list[1]=4
print(mutable_list)
mutable_list=[1,2,3,'a','time']
mutable_list.append("b")
print(mutable_list)