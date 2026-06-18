# Import telemetry loader from Step 3
from telemetry_loader import load_telemetry_data


# Function to analyze release reliability metrics
def analyze_release_reliability():

    # Load telemetry dataset
    df = load_telemetry_data()

    # Calculate total releases
    total_releases = len(df)

    # Calculate successful releases
    successful_releases = len(
        df[df["status"] == "Successful"]
    )

    # Calculate failed releases
    failed_releases = len(
        df[df["status"] == "Failed"]
    )

    # Calculate incident releases
    incident_releases = len(
        df[df["status"] == "Incident"]
    )

    # Calculate success percentage
    success_rate = (
        successful_releases / total_releases
    ) * 100

    # Calculate failure percentage
    failure_rate = (
        failed_releases / total_releases
    ) * 100

    # Calculate average CPU utilization
    avg_cpu = df["cpu_pct"].mean()

    # Calculate average memory utilization
    avg_memory = df["memory_pct"].mean()

    # Calculate average availability
    avg_availability = df["availability_pct"].mean()

    # Display report heading
    print("\n===== RELEASE RELIABILITY REPORT =====\n")

    # Display release counts
    print(f"Total Releases        : {total_releases}")
    print(f"Successful Releases   : {successful_releases}")
    print(f"Failed Releases       : {failed_releases}")
    print(f"Incident Releases     : {incident_releases}")

    print()

    # Display success and failure percentages
    print(f"Success Rate (%)      : {success_rate:.2f}")
    print(f"Failure Rate (%)      : {failure_rate:.2f}")

    print()

    # Display average utilization metrics
    print(f"Average CPU (%)       : {avg_cpu:.2f}")
    print(f"Average Memory (%)    : {avg_memory:.2f}")
    print(f"Average Availability  : {avg_availability:.2f}")


# Execute only when run directly
if __name__ == "__main__":

    # Run reliability analysis
    analyze_release_reliability()