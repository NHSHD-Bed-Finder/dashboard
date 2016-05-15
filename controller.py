import requests

# requests_url = 'https://camhs-api.herokuapp.com/requests'
# trusts_url = 'https://camhs-api.herokuapp.com/trusts'

# response = requests.get(requests_url)
# request_list = response.json()

# for request in request_list:
#     print(request['status'])


def get_trust_statuses(list_of_trust_ids):
    print(list_of_trust_ids)
    trust_statuses = []

    for trust_id in list_of_trust_ids:
        response = requests.get('https://camhs-api.herokuapp.com/trust/{0}'.format(trust_id))
        trust_status = response.json()
        print(trust_status)
        trust_statuses.append(trust_status)

    print(trust_statuses)

    return trust_statuses


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

get_active_requests()