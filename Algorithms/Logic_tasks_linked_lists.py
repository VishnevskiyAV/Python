# Linled lists

## Creating of Linked Lists and what is it
class Node:
    # Метод будет принимать значение, которое мы хотим поместить в новый узел
    def __init__(self, data):
        self.data = data
        self.next = None
    # Первое, что мы делаем, это создаем новый узел с заданным значением. 
    def append(self, val):
        end = Node(val)
        n = self          # Затем мы создаем указатель (поинтер) (по сути мы создаем ссылку на головной элемент)
        while (n.next):   # Наконец, мы проходим список
            n = n.next
        n.next = end      # указываем на последний узел, за которым нет следующего узла.    
    
    #Начнем с создания нового объекта Node.
ll = Node(1)
    # С помощью метода append добавим элементы в наш список
ll.append(2)
ll.append(3)
    # Выведем наш связный список
node = ll
print(node.data)
while node.next:
    node = node.next
    print(node.data)