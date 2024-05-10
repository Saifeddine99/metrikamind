def create_patient(first_name, last_name, gender, birthdate, email):

    # Imports the Google API Discovery Service.
    from googleapiclient import discovery

    api_version = "v1"
    service_name = "healthcare"

    # Returns an authorized API client by discovering the Healthcare API
    # and using GOOGLE_APPLICATION_CREDENTIALS environment variable.
    client = discovery.build(service_name, api_version)
    
    project_id = 'globalehr-dev'
    location = 'europe-west2'
    dataset_id = 'metricamind'
    fhir_store_id = 'data'

    fhir_store_parent = (
        f"projects/{project_id}/locations/{location}/datasets/{dataset_id}"
    )
    fhir_store_name = f"{fhir_store_parent}/fhirStores/{fhir_store_id}"

    patient_body = {
        "name": [{"use": "official", "family": last_name, "given": [first_name]}],
        "gender": gender,
        "birthDate": birthdate,
        "telecom": [{"system": "email", "use": "work", "value": email}],
        "resourceType": "Patient",
    }

    request = (
        client.projects()
        .locations()
        .datasets()
        .fhirStores()
        .fhir()
        .create(parent=fhir_store_name, type="Patient", body=patient_body)
    )

    # Sets required application/fhir+json header on the googleapiclient.http.HttpRequest.
    request.headers["content-type"] = "application/fhir+json;charset=utf-8"
    response = request.execute()

    print(f"Created Patient resource with ID {response['id']}")

    return (response['id'])

if __name__ == "__main__":
    
    first_name = "Saif"
    last_name = "Baccouche"
    gender = "Male"
    birthdate = "1999-07-18"
    email = "saif.baccouche@gmail.com"

    resp_id = create_patient(first_name, last_name, gender, birthdate, email)