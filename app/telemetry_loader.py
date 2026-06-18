# Import the pandas library.
# Pandas is used to load and work with tabular data such as CSV files.
import pandas as pd

# Import Path from pathlib.
# Path provides a platform-independent way to work with file paths.
from pathlib import Path


# Define the location of the telemetry CSV file.
# This assumes the script is executed from the project root directory.
DATA_FILE = Path("data/release_telemetry.csv")


# Define a reusable function that loads telemetry data.
# The function returns a Pandas DataFrame.
def load_telemetry_data(file_path: Path = DATA_FILE) -> pd.DataFrame:

    """
    Load telemetry dataset from CSV.

    Parameters:
        file_path:
            Location of the telemetry CSV file.

    Returns:
        Pandas DataFrame containing telemetry records.
    """

    # Check whether the telemetry file exists.
    # This prevents confusing errors later when attempting to read the file.
    if not file_path.exists():

        # Raise a clear exception showing which file is missing.
        raise FileNotFoundError(
            f"Telemetry file not found: {file_path}"
        )

    # Read the CSV file into a Pandas DataFrame.
    # Each CSV row becomes a DataFrame row.
    telemetry_df = pd.read_csv(file_path)

    # Return the loaded DataFrame to the caller.
    return telemetry_df


# Execute the following block only when this script
# is run directly from the command line.
# It will not execute when imported into another module.
if __name__ == "__main__":

    # Load the telemetry dataset using the function above.
    df = load_telemetry_data()

    # Print a blank line and success message
    # to make console output easier to read.
    print("\nTelemetry data loaded successfully.\n")

    # Display the first five rows of the dataset.
    # This provides a quick verification that loading worked.
    print(df.head())