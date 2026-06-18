# Import Path to create and manage report file paths.
from pathlib import Path

# Import telemetry loader to read release telemetry data.
from telemetry_loader import load_telemetry_data

# Import risk calculation logic from Step 8.
from risk_assessment import calculate_risk


# Define the reports directory path.
REPORTS_DIR = Path("reports")

# Define the output file for the executive summary.
EXECUTIVE_SUMMARY_FILE = REPORTS_DIR / "executive_release_summary.txt"


# Define a function to export the executive release summary.
def export_executive_summary():

    # Create the reports directory if it does not already exist.
    REPORTS_DIR.mkdir(exist_ok=True)

    # Load telemetry data from the CSV file.
    df = load_telemetry_data()

    # Calculate the total number of releases.
    total_releases = len(df)

    # Count successful releases.
    successful_releases = len(df[df["status"] == "Successful"])

    # Count failed releases.
    failed_releases = len(df[df["status"] == "Failed"])

    # Count incident releases.
    incident_releases = len(df[df["status"] == "Incident"])

    # Initialize low-risk release counter.
    low_risk = 0

    # Initialize medium-risk release counter.
    medium_risk = 0

    # Initialize high-risk release counter.
    high_risk = 0

    # Initialize critical-risk release counter.
    critical_risk = 0

    # Loop through every release row.
    for _, row in df.iterrows():

        # Calculate risk level for the current release.
        risk = calculate_risk(row)

        # Increment low-risk counter.
        if risk == "LOW":
            low_risk += 1

        # Increment medium-risk counter.
        elif risk == "MEDIUM":
            medium_risk += 1

        # Increment high-risk counter.
        elif risk == "HIGH":
            high_risk += 1

        # Increment critical-risk counter.
        elif risk == "CRITICAL":
            critical_risk += 1

    # Set overall health based on critical/high risk presence.
    if critical_risk > 0:

        # Critical releases mean leadership attention is required.
        overall_health = "ATTENTION REQUIRED"

    elif high_risk > 0:

        # High-risk releases mean caution is required.
        overall_health = "CAUTION"

    else:

        # No high or critical risk means the release landscape is healthy.
        overall_health = "HEALTHY"

    # Create a list to store summary lines.
    summary_lines = []

    # Add report title.
    summary_lines.append("===== EXECUTIVE RELEASE SUMMARY =====")

    # Add blank line.
    summary_lines.append("")

    # Add release count metrics.
    summary_lines.append(f"Total Releases      : {total_releases}")
    summary_lines.append(f"Successful Releases : {successful_releases}")
    summary_lines.append(f"Failed Releases     : {failed_releases}")
    summary_lines.append(f"Incident Releases   : {incident_releases}")

    # Add blank line.
    summary_lines.append("")

    # Add risk distribution metrics.
    summary_lines.append(f"Low Risk Releases      : {low_risk}")
    summary_lines.append(f"Medium Risk Releases   : {medium_risk}")
    summary_lines.append(f"High Risk Releases     : {high_risk}")
    summary_lines.append(f"Critical Risk Releases : {critical_risk}")

    # Add blank line.
    summary_lines.append("")

    # Add overall release health.
    summary_lines.append(f"Overall Release Health : {overall_health}")

    # Join all summary lines into one text block.
    summary_text = "\n".join(summary_lines)

    # Write executive summary text to output file.
    EXECUTIVE_SUMMARY_FILE.write_text(summary_text, encoding="utf-8")

    # Print success message.
    print("\nExecutive release summary exported successfully.")

    # Print output file path.
    print(f"Output File: {EXECUTIVE_SUMMARY_FILE}")


# Execute only when this file is run directly.
if __name__ == "__main__":

    # Export executive release summary.
    export_executive_summary()