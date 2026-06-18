# Import ChromaDB for vector database storage.
import chromadb

# Import the embedding generation function from Step 5.
from embedding_generator import generate_release_embeddings


# Define the ChromaDB storage folder.
CHROMA_DB_PATH = "data/chroma_release_db"


# Define the ChromaDB collection name.
COLLECTION_NAME = "release_events"


# Create a function to store release embeddings in ChromaDB.
def build_vector_store():

    # Create a persistent ChromaDB client.
    client = chromadb.PersistentClient(path=CHROMA_DB_PATH)

    # Create or reuse a collection for release events.
    collection = client.get_or_create_collection(name=COLLECTION_NAME)

    # Generate release embedding records.
    records = generate_release_embeddings()

    # Loop through each release embedding record.
    for record in records:

        # Add release text, embedding, metadata, and ID into ChromaDB.
        collection.add(
            ids=[record["release_id"]],
            documents=[record["release_text"]],
            embeddings=[record["embedding"].tolist()],
            metadatas=[{"release_id": record["release_id"]}],
        )

    # Return the ChromaDB collection.
    return collection


# Create a function to test semantic search.
def test_vector_search():

    # Build or load the vector store.
    collection = build_vector_store()

    # Pick REL-005 as a sample query release.
    query_release_id = "REL-005"

    # Retrieve the stored document for REL-005.
    query_record = collection.get(ids=[query_release_id], include=["documents", "embeddings"])

    # Extract the embedding for REL-005.
    query_embedding = query_record["embeddings"][0]

    # Search for similar release events.
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3,
    )

    # Print report heading.
    print("\n===== CHROMADB VECTOR SEARCH REPORT =====\n")

    # Print the query release ID.
    print(f"Query Release ID : {query_release_id}")

    # Print similar release IDs.
    print(f"Similar Releases : {results['ids'][0]}")

    # Print matching documents.
    print("\nMatching Release Descriptions:")

    # Loop through returned documents.
    for document in results["documents"][0]:

        # Print each matching release description.
        print(f"- {document}")


# Execute only when run directly.
if __name__ == "__main__":

    # Run the vector search test.
    test_vector_search()