import time

class Node: 
    def __init__(self,id):
        self.id=id
        self.data=[]
        self.is_leader=False
        
    def receive_transaction(self, transacao):
        time.sleep(0.3)
        self.data.append(transacao)
        print(f"Node {self.id} recebeu: {transacao}")