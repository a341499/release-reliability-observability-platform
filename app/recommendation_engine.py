# Import telemetry loader to read release data.
from telemetry_loader import load_telemetry_data

# Import risk calculation logic from Step 8.
from risk_assessment import calculate_risk


# Define a function to map risk level to recommendation.
def generate_recommendation(risk):

    # Critical releases should be blocked until reviewed.
    if risk == "CRITICAL":

        # Return recommendation for critical risk.
        return "Block release and investigate before deployment"

    # High-risk releases need review before proceeding.
    if risk == "HIGH":

        # Return recommendation for high risk.
        return "Review before deployment and require approval"

    # Medium-risk releases may proceed with monitoring.
    if risk == "MEDIUM":

        # Return recommendation for medium risk.
        return "Proceed with enhanced monitoring"

    # Low-risk releases can proceed normally.
    return "Proceed with release"


# Define a function to generate recommendations for all releases.
def generate_release_recommendations():

    # Load release telemetry data.
    df = load_telemetry_data()

    # Print report heading.
    print("\n===== RELEASE RECOMMENDATION REPORT =====\n")

    # Loop through every release row.
    for _, row in df.iterrows():

        # Calculate release risk using Step 8 logic.
        risk = calculate_risk(row)

        # Generate recommendation based on risk.
        recommendation = generate_recommendation(risk)

        # Print release recommendation summary.
        print(
            f"{row['release_id']} | "
            f"{row['service']} | "
            f"Risk={risk} | "
            f"Recommendation={recommendation}"
        )


# Execute this block only when run directly.
if __name__ == "__main__":

    # Generate release recommendations.
    generate_release_recommendations()