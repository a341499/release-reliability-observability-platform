# Import telemetry loader to read release data from CSV.
from telemetry_loader import load_telemetry_data

# Import risk calculation logic from the risk assessment module.
from risk_assessment import calculate_risk

# Import recommendation logic from the recommendation engine module.
from recommendation_engine import generate_recommendation


# Define a function to generate the release readiness report.
def generate_readiness_report():

    # Load release telemetry data into a DataFrame.
    df = load_telemetry_data()

    # Print the report heading.
    print("\n===== RELEASE READINESS REPORT =====\n")

    # Loop through each release record in the dataset.
    for _, row in df.iterrows():

        # Calculate the risk level for the current release.
        risk = calculate_risk(row)

        # Generate the recommendation for the calculated risk.
        recommendation = generate_recommendation(risk)

        # Print a separator for readability.
        print("-" * 70)

        # Print release identifier.
        print(f"Release ID        : {row['release_id']}")

        # Print service name.
        print(f"Service           : {row['service']}")

        # Print release date.
        print(f"Release Date      : {row['release_date']}")

        # Print CPU utilization.
        print(f"CPU Utilization   : {row['cpu_pct']}%")

        # Print memory utilization.
        print(f"Memory Utilization: {row['memory_pct']}%")

        # Print error count.
        print(f"Error Count       : {row['error_count']}")

        # Print availability percentage.
        print(f"Availability      : {row['availability_pct']}%")

        # Print severity.
        print(f"Severity          : {row['severity']}")

        # Print final release status.
        print(f"Status            : {row['status']}")

        # Print calculated risk level.
        print(f"Risk Level        : {risk}")

        # Print generated recommendation.
        print(f"Recommendation    : {recommendation}")


# Execute this block only when the file is run directly.
if __name__ == "__main__":

    # Generate and display the readiness report.
    generate_readiness_report()