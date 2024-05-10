def total_scores(patient_id, responses):
    dates = []
    total_scores = []

    for response in responses:
        response_id = list(response.keys())[0]
        if response_id == patient_id:

            response_value = list(response.values())[0]

            dates.append(response_value[0])
            total_scores.append(response_value[1])
            

    return dates, total_scores