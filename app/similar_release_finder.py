# Import the vector store builder from Step 6.
# This gives us access to the ChromaDB collection.
from vector_store import build_vector_store


# Define a function to find releases similar to a given release ID.
def find_similar_releases(release_id, top_k=3):

    # Build or load the ChromaDB vector store.
    collection = build_vector_store()

    # Retrieve the selected release from ChromaDB.
    query_record = collection.get(
        ids=[release_id],
        include=["documents", "embeddings"]
    )

    # Check whether the release ID exists in ChromaDB.
    if not query_record["ids"]:

        # Print a clear message if the release ID was not found.
        print(f"Release ID not found: {release_id}")

        # Stop execution because there is nothing to search.
        return

    # Extract the embedding vector for the selected release.
    query_embedding = query_record["embeddings"][0]

    # Search ChromaDB for similar releases.
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k,
    )

    # Print report heading.
    print("\n===== SIMILAR RELEASE FINDER REPORT =====\n")

    # Print the release ID used as the search input.
    print(f"Query Release ID : {release_id}")

    # Print the number of requested results.
    print(f"Top Matches      : {top_k}")

    # Print the matched release IDs.
    print(f"Similar Releases : {results['ids'][0]}")

    # Print a section heading for readable descriptions.
    print("\nMatching Release Descriptions:")

    # Loop through matched release descriptions.
    for document in results["documents"][0]:

        # Print each matching release description.
        print(f"- {document}")


# Execute this block only when run directly.
if __name__ == "__main__":

    # Choose the release ID to search against.
    # Change this value later to test other releases.
    search_release_id = "REL-010"

    # Run similar release search.
    find_similar_releases(search_release_id, top_k=3)