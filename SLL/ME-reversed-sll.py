from MeSLL import SLL 

def reverseSLL(sll: 'SLL'):
    prev = sll.getSentinel()
    curr = sll.getFirst() 
    next = curr.getPointer() 

    while next is not None:
        curr.setPointer(prev.getItem())
        prev = prev.getPointer()
        curr = curr.getPointer() 
        next = next.getPointer() 

    return sll 

sll = SLL()
sll.insert(10)
sll.insert(20)
sll.insert(30)
sll.insert(17)
print(sll)

print(reverseSLL(sll))



def reverseSLL(sll: 'SLL'):
    prev = None
    curr = sll.getFirst() 

    while curr is not None:
        next = curr.getPointer()
        curr.setPointer(prev) 
        prev = curr 
        curr = next 

    sll.getSentinel().setPointer(prev) 
 

    return sll 
