# Import Path to create and manage report file paths.
from pathlib import Path

# Import telemetry loader to read release data from CSV.
from telemetry_loader import load_telemetry_data

# Import risk calculation logic from Step 8.
from risk_assessment import calculate_risk

# Import recommendation logic from Step 9.
from recommendation_engine import generate_recommendation


# Define the reports directory path.
REPORTS_DIR = Path("reports")

# Define the output report file path.
REPORT_FILE = REPORTS_DIR / "release_readiness_report.txt"


# Define a function to export the readiness report to a text file.
def export_release_readiness_report():

    # Create the reports directory if it does not already exist.
    REPORTS_DIR.mkdir(exist_ok=True)

    # Load telemetry data from the CSV file.
    df = load_telemetry_data()

    # Create an empty list to hold report lines.
    report_lines = []

    # Add report title.
    report_lines.append("===== RELEASE READINESS REPORT =====")
    report_lines.append("")

    # Loop through each release record.
    for _, row in df.iterrows():

        # Calculate risk level for the release.
        risk = calculate_risk(row)

        # Generate recommendation from risk level.
        recommendation = generate_recommendation(risk)

        # Add separator line.
        report_lines.append("-" * 70)

        # Add release details to the report.
        report_lines.append(f"Release ID        : {row['release_id']}")
        report_lines.append(f"Service           : {row['service']}")
        report_lines.append(f"Release Date      : {row['release_date']}")
        report_lines.append(f"CPU Utilization   : {row['cpu_pct']}%")
        report_lines.append(f"Memory Utilization: {row['memory_pct']}%")
        report_lines.append(f"Error Count       : {row['error_count']}")
        report_lines.append(f"Availability      : {row['availability_pct']}%")
        report_lines.append(f"Severity          : {row['severity']}")
        report_lines.append(f"Status            : {row['status']}")
        report_lines.append(f"Risk Level        : {risk}")
        report_lines.append(f"Recommendation    : {recommendation}")

    # Combine all report lines into one text block.
    report_text = "\n".join(report_lines)

    # Write the report text to the output file.
    REPORT_FILE.write_text(report_text, encoding="utf-8")

    # Print confirmation message.
    print("\nRelease readiness report exported successfully.")

    # Print output file path.
    print(f"Output File: {REPORT_FILE}")


# Execute this block only when run directly.
if __name__ == "__main__":

    # Export release readiness report.
    export_release_readiness_report()