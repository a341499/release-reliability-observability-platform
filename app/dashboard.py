# Import Streamlit for building the dashboard UI.
import streamlit as st

# Import telemetry loader to read release telemetry data.
from telemetry_loader import load_telemetry_data

# Import risk calculation logic from the risk assessment module.
from risk_assessment import calculate_risk

# Import recommendation logic from the recommendation engine module.
from recommendation_engine import generate_recommendation


# Configure the Streamlit dashboard page title and layout.
st.set_page_config(
    page_title="Release Reliability Dashboard",
    layout="wide"
)

# Display the main dashboard title.
st.title("🚀 Release Reliability Dashboard")

# Load telemetry data from the CSV file.
df = load_telemetry_data()

# Calculate total number of releases.
total_releases = len(df)

# Count successful releases.
successful_releases = len(
    df[df["status"] == "Successful"]
)

# Count failed releases.
failed_releases = len(
    df[df["status"] == "Failed"]
)

# Count incident releases.
incident_releases = len(
    df[df["status"] == "Incident"]
)

# Create four metric columns for release status.
col1, col2, col3, col4 = st.columns(4)

# Display total release count.
col1.metric(
    "Total Releases",
    total_releases
)

# Display successful release count.
col2.metric(
    "Successful Releases",
    successful_releases
)

# Display failed release count.
col3.metric(
    "Failed Releases",
    failed_releases
)

# Display incident release count.
col4.metric(
    "Incident Releases",
    incident_releases
)

# Add a separator between release KPIs and risk KPIs.
st.divider()

# Display risk distribution section title.
st.subheader("Risk Distribution")

# Create a new column named risk_level by applying risk calculation row by row.
df["risk_level"] = df.apply(
    calculate_risk,
    axis=1
)

# Create a new column named recommendation using the calculated risk level.
df["recommendation"] = df["risk_level"].apply(
    generate_recommendation
)

# Count low-risk releases.
low_risk = len(
    df[df["risk_level"] == "LOW"]
)

# Count medium-risk releases.
medium_risk = len(
    df[df["risk_level"] == "MEDIUM"]
)

# Count high-risk releases.
high_risk = len(
    df[df["risk_level"] == "HIGH"]
)

# Count critical-risk releases.
critical_risk = len(
    df[df["risk_level"] == "CRITICAL"]
)

# Create four metric columns for risk distribution.
risk_col1, risk_col2, risk_col3, risk_col4 = st.columns(4)

# Display low-risk release count.
risk_col1.metric(
    "LOW Risk",
    low_risk
)

# Display medium-risk release count.
risk_col2.metric(
    "MEDIUM Risk",
    medium_risk
)

# Display high-risk release count.
risk_col3.metric(
    "HIGH Risk",
    high_risk
)

# Display critical-risk release count.
risk_col4.metric(
    "CRITICAL Risk",
    critical_risk
)

# Add separator before executive summary.
st.divider()

# Display executive summary section title.
st.subheader("Executive Release Summary")

# Determine overall release health.
if critical_risk > 0:

    # Critical releases require immediate attention.
    overall_health = "ATTENTION REQUIRED"

elif high_risk > 0:

    # High-risk releases require caution.
    overall_health = "CAUTION"

else:

    # No major risks detected.
    overall_health = "HEALTHY"

# Create executive summary columns.
exec_col1, exec_col2 = st.columns(2)

# Display overall release health.
exec_col1.metric(
    "Overall Release Health",
    overall_health
)

# Display total releases.
exec_col2.metric(
    "Total Releases",
    total_releases
)

# Add a separator before the reports download section.
st.divider()

# Add a separator before telemetry details.
st.divider()

# Display telemetry section heading.
st.subheader("Release Telemetry Data with Recommendations")

# Display release telemetry including risk and recommendation columns.
st.dataframe(df, use_container_width=True)

# Display reports section heading.
st.subheader("Download Generated Reports")

# Define the path to the release readiness report file.
readiness_report_path = "reports/release_readiness_report.txt"

# Define the path to the executive summary report file.
executive_summary_path = "reports/executive_release_summary.txt"

# Open the release readiness report file for reading.
with open(readiness_report_path, "r", encoding="utf-8") as readiness_file:

    # Read the full release readiness report content.
    readiness_report_content = readiness_file.read()

# Open the executive summary report file for reading.
with open(executive_summary_path, "r", encoding="utf-8") as executive_file:

    # Read the full executive summary content.
    executive_summary_content = executive_file.read()

# Create two columns for report download buttons.
download_col1, download_col2 = st.columns(2)

# Add download button for the release readiness report.
download_col1.download_button(
    label="Download Release Readiness Report",
    data=readiness_report_content,
    file_name="release_readiness_report.txt",
    mime="text/plain"
)

# Add download button for the executive release summary.
download_col2.download_button(
    label="Download Executive Release Summary",
    data=executive_summary_content,
    file_name="executive_release_summary.txt",
    mime="text/plain"
)