# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 10:30:04 2021

@author: sagar kumar
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next= None
class linkedlist:
    def __init__(self):
        self.head = None
        
    def show(self):
        node = self.head
        if node is None:
            print('empty list')
        else:
            while node is not None:
               print(node.data)
               node = node.next
        
    def add(self,new):
        new_node = Node(new)
        new_node.next = self.head
        self.head = new_node
        
    def append(self,new):
        new_node = Node(new)
        if self.head is None:
            self.head = new_node
            return
        else:
             last = self.head
             while(last.next):
                  last = last.next
             last.next = new_node
             
    def add_after(self,val,new):
       if val is None:
           return
       else:
           new_node = Node(new)
           new_node.next = val.next
           val.next = new_node
     
    def add_pos(self,pos,new):
        new_node = Node(new)
        if (pos<1):
            print('invalid')
        elif( pos == 1):
            new_node.next = self.head
            self.head = new_node
        else:
            temp = self.head
            for i in range(1,pos-1):
                if (temp!=None):
                    temp = temp.next
            if( temp!=None):
                     new_node.next = temp.next
                     temp.next = new_node
            else:
                    print('invalid')
                
    def length(self):
      temp = self.head
      count = 0 
      while(temp is not None):
        temp = temp.next
        count +=1
      return count
  
    def deleteattail(self):
        if self.head == None:
            return None
        if self.head.next == None:
            self.head = None
            return None
        second_last = self.head
        while(second_last.next.next):
            second_last = second_last.next
        second_last.next = None
        return self.head
    
    def deleteatfirst(self):
        if self.head == None:
            return None
        temp = self.head
        self.head = self.head.next
        temp = None
        return self.head

    def deletenode(self, key):
       if self.head is None:
            print("Linked List is empty")
            return

       temp = self.head
       prev = None 
       found = False
       while(temp is not None):
          if temp.data == key:
              found = True
              break
                
          prev = temp
          temp = temp.next

       if found:
        prev.next = temp.next
        temp.data = None
        temp.next = None
        
    def reverse(self):
      prev = None
      current = self.head
      while(current is not None):
         next = current.next
         current.next = prev
         prev = current
         current = next
      self.head = prev




ll = linkedlist()
print('\nadd')
ll.add(4)
ll.show()
print('\nadd')
ll.add(3)
ll.show()
print('\nappend')
ll.append(7)
ll.show()
print('\nadd_after')
ll.add_after(ll.head,8)
ll.show()
print('\nadd_pos')
ll.add_pos(2,9)
ll.show()
print('\ndeleteattail')
ll.deleteattail()
ll.show()
print('\ndeleteatfirst')
ll.deleteatfirst()
ll.show()
print('\ndeletenode')
ll.deletenode(8)
ll.show()
print('\nreverse')
ll.reverse()
ll.show()
print('\n')
len= ll.length()
print('total len ',len)



