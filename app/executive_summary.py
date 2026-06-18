# Import telemetry loader.
from telemetry_loader import load_telemetry_data

# Import risk calculation logic.
from risk_assessment import calculate_risk


# Generate executive summary report.
def generate_executive_summary():

    # Load telemetry dataset.
    df = load_telemetry_data()

    # Calculate release counts.
    total_releases = len(df)

    successful_releases = len(
        df[df["status"] == "Successful"]
    )

    failed_releases = len(
        df[df["status"] == "Failed"]
    )

    incident_releases = len(
        df[df["status"] == "Incident"]
    )

    # Initialize risk counters.
    low_risk = 0
    medium_risk = 0
    high_risk = 0
    critical_risk = 0

    # Evaluate risk for each release.
    for _, row in df.iterrows():

        # Calculate risk level.
        risk = calculate_risk(row)

        # Increment corresponding risk bucket.
        if risk == "LOW":
            low_risk += 1

        elif risk == "MEDIUM":
            medium_risk += 1

        elif risk == "HIGH":
            high_risk += 1

        elif risk == "CRITICAL":
            critical_risk += 1

    # Determine overall health.
    if critical_risk > 0:
        overall_health = "ATTENTION REQUIRED"

    elif high_risk > 0:
        overall_health = "CAUTION"

    else:
        overall_health = "HEALTHY"

    # Print report.
    print("\n===== EXECUTIVE RELEASE SUMMARY =====\n")

    print(f"Total Releases      : {total_releases}")
    print(f"Successful Releases : {successful_releases}")
    print(f"Failed Releases     : {failed_releases}")
    print(f"Incident Releases   : {incident_releases}")

    print()

    print(f"Low Risk Releases      : {low_risk}")
    print(f"Medium Risk Releases   : {medium_risk}")
    print(f"High Risk Releases     : {high_risk}")
    print(f"Critical Risk Releases : {critical_risk}")

    print()

    print(f"Overall Release Health : {overall_health}")


# Execute only when run directly.
if __name__ == "__main__":

    # Generate executive summary.
    generate_executive_summary()