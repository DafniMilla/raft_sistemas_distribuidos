from node import Node
import time

class RaftCluster:
    def __init__(self):
        self.nodes =[Node(1), Node(2), Node(3)]
        self.leader = self.nodes[0]
        self.leader.is_leader=True
        
    def send_transaction(self, transaction):
        print(f"\nLíder {self.leader.id} processando transação")
        time.sleep(1)
        
        for node in self.nodes:
            time.sleep(0.5) 
            node.receive_transaction(transaction)
            
    def simulate_failure(self):
        print("\n Líder falhou!")
        time.sleep(2)
        
        self.leader.is_leader=False
        
        #escolhe novo lider
        for node in self.nodes:
            if not node.is_leader:
                self.leader=node
                break
            
        time.sleep(1)
            
        self.leader.is_leader=True
        print(f"Novo Líder: Node {self.leader.id}")