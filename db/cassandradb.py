from cassandra.cluster import  Cluster

try:
    from cassandra.cluster import Cluster
    cluster = Cluster(['localhost'])
    session = cluster.connect()
    print(session)
    print(session.execute("SELECT release_version FROM system.local").one())
    # session.set_keyspace('users')
    # print(session.execute("SELECT * FROM users"))


except Exception as ex:
    print ('Error:', ex)
    exit('Failed to connect, terminating.')
