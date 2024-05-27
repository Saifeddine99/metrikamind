def extract_before_total_score(s):
    phrase = " total score"
    if phrase in s:
        return s.split(phrase)[0].strip()
    else:
        return s
    
def query_patients():
    from google.auth import default
    from googleapiclient.discovery import build

    # Set up authentication
    credentials, project_id = default()

    # Set up the Healthcare API service
    healthcare_service = build('healthcare', 'v1', credentials=credentials)

    # Set up the request parameters
    parent = f'projects/{project_id}/locations/europe-west2/datasets/metricamind/fhirStores/data'
    resource_type = 'Patient'

    # Make the request to list patients
    response = healthcare_service.projects().locations().datasets().fhirStores().fhir().search(
        parent=parent,
        body={"resourceType": resource_type}
    ).execute()

    patient_ids = {}
    full_names = []
    telecoms = []

    counter = 1
    # Print patient data
    for patient in response.get('entry', []):
        patient_data = patient.get('resource')


        patient_ids[counter] = patient_data['id']
        counter += 1


        if 'family' in list(patient_data["name"][0].keys()):
            family_name = patient_data["name"][0]["family"]
            first_name = patient_data["name"][0]["given"][0]

            patient_name = first_name + " " + family_name

        elif 'text' in list(patient_data["name"][0].keys()):

            patient_name = patient_data["name"][0]["text"]
            if "@" in patient_name:
                username, domain = patient_name.split("@")
                
                if "." in username:
                    name, surname = username.split(".")
                    patient_name = name + " " + surname
                else:
                    patient_name = username

        full_names.append(patient_name)    


        telecom = patient_data["telecom"][0]["value"]

        telecoms.append(telecom)

    return(full_names, telecoms, patient_ids)

def query_scores(patient_id):
    title_scores_dict = {}
    from google.auth import default
    from googleapiclient.discovery import build

    # Set up authentication
    credentials, project_id = default()

    # Set up the Healthcare API service
    healthcare_service = build('healthcare', 'v1', credentials=credentials)

    # Set up the request parameters
    parent = f'projects/{project_id}/locations/europe-west2/datasets/metricamind/fhirStores/data'
    resource_type = 'Observation'

    # Make the request to list patients
    response = healthcare_service.projects().locations().datasets().fhirStores().fhir().search(
        parent=parent,
        body={"resourceType": resource_type}
    ).execute()

    # Print patient data
    for observation in response.get('entry', []):
        observation_data = observation.get('resource')
        if observation_data["subject"]["reference"] == ("Patient/" + patient_id):

            questionnaire_title = extract_before_total_score(observation_data["code"]["coding"][0]["display"])
            date = observation_data["meta"]["lastUpdated"]
            score = observation_data["valueInteger"]

            if questionnaire_title in list(title_scores_dict.keys()):

                title_scores_dict[questionnaire_title]["dates"].append(date)
                title_scores_dict[questionnaire_title]["scores"].append(score)

            else:
                title_scores_dict[questionnaire_title] = {"dates": [date], "scores": [score]}

    return title_scores_dict