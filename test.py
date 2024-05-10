from google.cloud import bigquery

# Initialize the BigQuery client
client = bigquery.Client()

# Define your project ID and dataset ID
project_id = 'globalehr-dev'
dataset_id = 'Metricamind'

# Define the table ID
table_id = 'Patient'

# Define the specific patient_id you want to delete
specific_patient_id = '0348e285-e30b-4eae-b0e7-2ceec93dc75e'

# Define the SQL query to delete rows with the specific patient_id
sql = f"""
    DELETE FROM `{project_id}.{dataset_id}.{table_id}`
    WHERE id = '{specific_patient_id}'
"""

# Run the query
query_job = client.query(sql)

# Wait for the query to complete
query_job.result()

print(f"Rows with patient_id '{specific_patient_id}' deleted successfully.")
