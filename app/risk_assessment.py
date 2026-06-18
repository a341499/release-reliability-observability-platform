# Import the telemetry data loader created earlier.
from telemetry_loader import load_telemetry_data


# Define a function to calculate the risk level for one release row.
def calculate_risk(row):

    # Check whether the release meets any critical-risk condition.
    if (
        row["cpu_pct"] >= 90
        or row["memory_pct"] >= 90
        or row["error_count"] >= 50
        or row["availability_pct"] < 95
        or row["severity"] == "Critical"
    ):

        # Return CRITICAL when the release has severe operational signals.
        return "CRITICAL"

    # Check whether the release meets any high-risk condition.
    if (
        row["cpu_pct"] >= 80
        or row["memory_pct"] >= 80
        or row["error_count"] >= 30
        or row["severity"] == "High"
    ):

        # Return HIGH when the release has strong warning signals.
        return "HIGH"

    # Check whether the release meets any medium-risk condition.
    if (
        row["cpu_pct"] >= 60
        or row["memory_pct"] >= 60
        or row["error_count"] >= 10
        or row["severity"] == "Medium"
    ):

        # Return MEDIUM when the release has moderate warning signals.
        return "MEDIUM"

    # Return LOW when no warning thresholds are crossed.
    return "LOW"


# Define a function to generate the full release risk report.
def generate_risk_report():

    # Load telemetry data from the CSV file.
    df = load_telemetry_data()

    # Print the report heading.
    print("\n===== RELEASE RISK ASSESSMENT REPORT =====\n")

    # Loop through each release record in the telemetry dataset.
    for _, row in df.iterrows():

        # Calculate risk level for the current release.
        risk = calculate_risk(row)

        # Print a simple one-line risk summary for the release.
        print(
            f"{row['release_id']} | "
            f"{row['service']} | "
            f"Risk={risk}"
        )


# Execute this block only when the file is run directly.
if __name__ == "__main__":

    # Generate and display the release risk report.
    generate_risk_report()