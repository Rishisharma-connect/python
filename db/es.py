from elasticsearch import Elasticsearch


# Create the client instance
client = Elasticsearch(
    "http://localhost:9200"
)

# Successful response!
print(client.info())
# {'name': 'instance-0000000000', 'cluster_name': ...}