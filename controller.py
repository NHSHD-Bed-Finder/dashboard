import requests


# Get the statuses of a list of specific trusts
def get_trust_statuses(list_of_trust_ids):
    print(list_of_trust_ids)
    trust_statuses = []

    for trust_id in list_of_trust_ids:
        response = requests.get('https://camhs-api.herokuapp.com/trust/{0}'.format(trust_id))
        trust = response.json()

        if trust['beds_available_type1'] < 1:
            trust['type1_class'] = 'danger'
        elif trust['beds_available_type1'] < 2:
            trust['type1_class'] = 'warning'
        else:
            trust['type1_class'] = 'success'

        if trust['beds_available_type2'] < 1:
            trust['type2_class'] = 'danger'
        elif trust['beds_available_type2'] < 2:
            trust['type2_class'] = 'warning'
        else:
            trust['type2_class'] = 'success'

        if trust['beds_available_type3'] < 1:
            trust['type3_class'] = 'danger'
        elif trust['beds_available_type3'] < 2:
            trust['type3_class'] = 'warning'
        else:
            trust['type3_class'] = 'success'

        print(trust)
        trust_statuses.append(trust)

    print(trust_statuses)

    return trust_statuses


# Gets the statuses of all trusts in the system
def get_all_trust_statuses():
    trust_statuses = {}

    response = requests.get('https://camhs-api.herokuapp.com/trusts')
    all_trusts = response.json()

    for trust in all_trusts:

        trust_status = {
            'name': trust['name'],
            'id': trust['id'],
            'beds_type1': trust['beds_type1'],
            'beds_type2': trust['beds_type2'],
            'beds_type3': trust['beds_type3'],
            'beds_available_type1': trust['beds_available_type1'],
            'beds_available_type2': trust['beds_available_type2'],
            'beds_available_type3': trust['beds_available_type3']
        }

        if trust['beds_available_type1'] < 1:
            trust_status['type1_class'] = 'danger'
        elif trust['beds_available_type1'] < 2:
            trust_status['type1_class'] = 'warning'
        else:
            trust_status['type1_class'] = 'success'

        if trust['beds_available_type2'] < 1:
            trust_status['type2_class'] = 'danger'
        elif trust['beds_available_type2'] < 2:
            trust_status['type2_class'] = 'warning'
        else:
            trust['type2_class'] = 'success'

        if trust['beds_available_type3'] < 1:
            trust_status['type3_class'] = 'danger'
        elif trust['beds_available_type3'] < 2:
            trust_status['type3_class'] = 'warning'
        else:
            trust_status['type3_class'] = 'success'

        try:
            trust_statuses[trust['region']].append(trust_status)
        except KeyError as e:
            trust_statuses[trust['region']] = []
            trust_statuses[trust['region']].append(trust_status)

    print(trust_statuses)

    return trust_statuses


# Gets a list of all open requests
def get_active_requests():
    response = requests.get('https://camhs-api.herokuapp.com/requests')
    request_list = response.json()
    print(request_list)
    print(len(request_list))

    filtered_request_list = []

    for request in request_list:
        if request['status'] == 'Active':
            filtered_request_list.append(request)

    return filtered_request_list


# Gets a list of all rejected requests
def get_rejected_requests():
    response = requests.get('https://camhs-api.herokuapp.com/requests')
    request_list = response.json()
    print(request_list)
    print(len(request_list))

    filtered_request_list = []

    for request in request_list:
        if request['status'] == 'Rejected':
            filtered_request_list.append(request)

    return filtered_request_list

trusts = get_all_trust_statuses()

print(trusts)

for i in trusts:
    print(trusts[i])

