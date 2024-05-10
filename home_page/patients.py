def patients_list_extraction(results):
    
    all_patients_list = []
    patients_ids_with_response = []

    responses = []

    # Process the results
    for row in results:

        # Extracting patients IDs:
        patient_id = row["id"]


        # Extracting patients names
        if row["name"][0]["family"] is None:
            # Split the email address by the "@" symbol
            email = row["name"][0]["text"]
            username, domain = email.split("@")

            if "." in username:
                name, surname = username.split(".")
                patient_name = name + " " + surname
            else:
                patient_name = username

        else:
            family_name = row["name"][0]["given"][0]
            first_name = row["name"][0]["family"]
            patient_name = first_name + " " + family_name


        # Extracting patients emails
        patient_email = row["telecom"][0]["value"]


        patient_dict = {
            "id": patient_id,
            "name": patient_name,
            "email": patient_email
        }

        if patient_dict not in all_patients_list:
            all_patients_list.append(patient_dict)
        


        if row["Patient_ID_Observation"] is not None:
            patients_ids_with_response.append(row["Patient_ID_Observation"])
            responses.append({row["Patient_ID_Observation"]: [row["date"], row["total_score"]]})

        
    return(all_patients_list, patients_ids_with_response, responses)
