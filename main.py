from cluster import RaftCluster

cluster = RaftCluster()

#transacao 1
cluster.send_transaction({"valor": 100, "tipo": "pagamento"})

#simula falha
cluster.simulate_failure()

#transacao 2
cluster.send_transaction({"valor": 200, "tipo": "transferência"})