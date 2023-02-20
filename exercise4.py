class que():
    def __init__(self):
        self.queue=[]
        
    def show_que(self):
        print(self.queue)
        
    def push(self,x):
        self.queue.append(x)
        
    def pop(self):
        if len(self.queue)==0:
            return None
        else:
            return self.queue.pop()
    
    
first_que=que()
first_que.push(1)
first_que.push(2)
first_que.push(3)
first_que.push(4)
first_que.show_que()
first_que.pop()
first_que.show_que()
first_que.pop()
first_que.show_que()