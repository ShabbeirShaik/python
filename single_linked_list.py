class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
class linkedList:
    def __init__(self):
        self.head=None
    def insert_at_begining(self,data):
        node=Node(data,self.head)
        self.head=  node
    def insert_at_end(self,data):
        if self.head is None:
            self.head=Node(data,None)
            return
        else:
            itr=self.head
            while(itr.next):
                itr=itr.next
            itr.next=Node(data,None)      
    def print(self):
        if self.head is None:
            print("It is blank")
            return
        else:
            itr=self.head
            llstr=''
            while itr:
                llstr+=str(itr.data) + '-->'
                itr=itr.next   
            print(llstr)    
    def insert_values(self,data_list):
        self.head=None
        for data in data_list:
            self.insert_at_end(data)
    def get_length(self):
        itr=self.head
        counter=0
        while itr:
            counter += 1
            itr=itr.next
        return counter    
    def remove_at(self,index):
        if index<0 or index>self.get_length():
            raise Exception("Invalid")
        if index==0:
            self.head=self.head.next        
        else:
            itr=self.head
            count=0
            while(itr):
                if count==index-1:
                    itr.next=itr.next.next
                    break
                itr=itr.next
                count +=1    
    def insert_at_particular_index(self,index,data):
        if index<0 or index>self.get_length():
            raise Exception("invalid index is given")
        if index==0:
            self.insert_at_begining(data)     
            return
        else:
            itr=self.head
            count=0
            while(itr):
                if count==index-1:
                    node=Node(data,itr.next)
                    itr.next=node
                    break
                itr=itr.next 
                count += 1   
    def insert_after(self,index,data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid index") 
        else:
            itr=self.head
            count=0
            while(itr):
                if count==index:
                    node=Node(data,itr.next) 
                    itr.next=node
                itr=itr.next
                count+=1
if __name__ == '__main__':
     l1=linkedList()
     #l1.insert_at_begining(7)
     #l1.insert_at_begining(8)
     #l1.insert_at_begining(9)  
     #l1.insert_at_end(16) 
     l1.insert_values(["sai","kumar","shabbeir","ahammad","patel"])
     #l1.remove_at(3)
     #l1.remove_at(30)
     #l1.remove_at(-3)
     #l1.insert_at_particular_index(0,"madhavi")
     #l1.insert_at_particular_index(2,"chinni pandu")
     l1.insert_after(2,["hai","hello"])
     l1.print()
     print("length is",l1.get_length())
