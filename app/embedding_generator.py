# Import hashlib to create stable numeric values from text tokens.
import hashlib

# Import numpy to store embedding vectors as numeric arrays.
import numpy as np

# Import the telemetry loader function created earlier.
from telemetry_loader import load_telemetry_data


# Define the embedding vector size.
EMBEDDING_DIMENSION = 64


# Convert one release row into descriptive semantic text.
def build_release_text(row):

    # Create a readable text description from release telemetry fields.
    release_text = (
        f"Release {row['release_id']} for {row['service']} "
        f"had CPU utilization {row['cpu_pct']} percent, "
        f"memory utilization {row['memory_pct']} percent, "
        f"error count {row['error_count']}, "
        f"availability {row['availability_pct']} percent, "
        f"severity {row['severity']}, "
        f"and final status {row['status']}."
    )

    # Return the generated release description.
    return release_text


# Generate a simple deterministic embedding from text.
def generate_embedding(text, dimension=EMBEDDING_DIMENSION):

    # Create an empty numeric vector.
    vector = np.zeros(dimension)

    # Split the text into lowercase words.
    tokens = text.lower().split()

    # Process each token in the text.
    for token in tokens:

        # Convert the token into a stable hash value.
        token_hash = int(hashlib.md5(token.encode()).hexdigest(), 16)

        # Map the hash value to a vector position.
        index = token_hash % dimension

        # Increase the value at the selected vector position.
        vector[index] += 1

    # Calculate the vector length for normalization.
    norm = np.linalg.norm(vector)

    # Normalize the vector only if it is not empty.
    if norm > 0:

        # Divide each value by the vector length.
        vector = vector / norm

    # Return the final embedding vector.
    return vector


# Generate release texts and embeddings for all telemetry records.
def generate_release_embeddings():

    # Load telemetry data from the CSV file.
    df = load_telemetry_data()

    # Create an empty list to store embedding records.
    embedding_records = []

    # Loop through each release row in the dataset.
    for _, row in df.iterrows():

        # Convert the row into semantic text.
        release_text = build_release_text(row)

        # Convert the semantic text into an embedding vector.
        embedding = generate_embedding(release_text)

        # Store release id, text, and embedding together.
        embedding_records.append(
            {
                "release_id": row["release_id"],
                "release_text": release_text,
                "embedding": embedding,
            }
        )

    # Return all generated embedding records.
    return embedding_records


# Execute this block only when the file is run directly.
if __name__ == "__main__":

    # Generate embeddings for release events.
    records = generate_release_embeddings()

    # Print report heading.
    print("\n===== RELEASE EMBEDDING GENERATION REPORT =====\n")

    # Print total number of generated embeddings.
    print(f"Total Embeddings Generated : {len(records)}")

    # Print a sample release id.
    print(f"Sample Release ID          : {records[0]['release_id']}")

    # Print the semantic text used for embedding.
    print(f"Sample Release Text        : {records[0]['release_text']}")

    # Print the first 10 numbers from the embedding vector.
    print(f"Sample Embedding Preview   : {records[0]['embedding'][:10]}")