def delete_patient(resource_id):

    # Imports the Google API Discovery Service.
    from googleapiclient import discovery

    api_version = "v1"
    service_name = "healthcare"

    # Returns an authorized API client by discovering the Healthcare API
    # and using GOOGLE_APPLICATION_CREDENTIALS environment variable.
    client = discovery.build(service_name, api_version)

    # TODO(developer): Uncomment these lines and replace with your values.
    project_id = 'globalehr-dev'
    location = 'europe-west2'
    dataset_id = 'metricamind'
    fhir_store_id = 'data'
    resource_type = 'Patient'

    fhir_store_parent = (
        f"projects/{project_id}/locations/{location}/datasets/{dataset_id}"
    )
    fhir_resource_path = f"{fhir_store_parent}/fhirStores/{fhir_store_id}/fhir/{resource_type}/{resource_id}"

    request = (
        client.projects()
        .locations()
        .datasets()
        .fhirStores()
        .fhir()
        .delete(name=fhir_resource_path)
    )
    response = request.execute()
    print(f"Deleted {resource_type} resource with ID {resource_id}.")

    #return response

if __name__ == "__main__":
    patient_id = "32809252-1e9e-4cb8-b549-3df0b6e48a6d"
    delete_patient(patient_id)