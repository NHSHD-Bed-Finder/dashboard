import requests
import dateutil.parser


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

    filtered_request_list = {}

    for request in request_list:

        if request['status'] == 'Active':

            yourdate = dateutil.parser.parse(request['created'])

            request['created'] = yourdate.strftime("%d-%b-%Y %H:%M:%S")
            request['status'] = 'Waiting'
            request['nhsNumber'] = format_nhs_number(request['nhsNumber'])

            try:
                filtered_request_list[request['nhsNumber']].append(request)

            except KeyError as e:
                filtered_request_list[request['nhsNumber']] = []
                filtered_request_list[request['nhsNumber']].append(request)

    return filtered_request_list


# Gets a list of all accepted requests
def get_accepted_requests():
    response = requests.get('https://camhs-api.herokuapp.com/requests')
    request_list = response.json()
    print(request_list)
    print(len(request_list))

    filtered_request_list = {}

    for request in request_list:

        if request['status'] == 'Accepted':

            yourdate = dateutil.parser.parse(request['created'])

            request['created'] = yourdate.strftime("%d-%b-%Y %H:%M:%S")
            request['status'] = 'Accepted'
            request['nhsNumber'] = format_nhs_number(request['nhsNumber'])

            try:
                filtered_request_list[request['nhsNumber']].append(request)

            except KeyError as e:
                filtered_request_list[request['nhsNumber']] = []
                filtered_request_list[request['nhsNumber']].append(request)

    return filtered_request_list


# Gets a list of all cancelled requests
def get_cancelled_requests():
    response = requests.get('https://camhs-api.herokuapp.com/requests')
    request_list = response.json()
    print(request_list)
    print(len(request_list))

    filtered_request_list = {}

    for request in request_list:
        if request['status'] == 'Cancelled':

            yourdate = dateutil.parser.parse(request['created'])
            request['created'] = yourdate.strftime("%d-%b-%Y %H:%M:%S")
            request['status'] = 'Not Responded'
            request['nhsNumber'] = format_nhs_number(request['nhsNumber'])


            try:
                filtered_request_list[request['nhsNumber']].append(request)

            except KeyError as e:
                filtered_request_list[request['nhsNumber']] = []
                filtered_request_list[request['nhsNumber']].append(request)

    return filtered_request_list


# Gets a list of all cancelled requests
def get_rejected_requests():
    response = requests.get('https://camhs-api.herokuapp.com/requests')
    request_list = response.json()
    print(request_list)
    print(len(request_list))

    filtered_request_list = {}

    for request in request_list:
        if request['status'] == 'Rejected':

            yourdate = dateutil.parser.parse(request['created'])
            request['created'] = yourdate.strftime("%d-%b-%Y %H:%M:%S")
            request['status'] = 'Rejected'
            request['nhsNumber'] = format_nhs_number(request['nhsNumber'])

            try:
                filtered_request_list[request['nhsNumber']].append(request)

            except KeyError as e:
                filtered_request_list[request['nhsNumber']] = []
                filtered_request_list[request['nhsNumber']].append(request)

    return filtered_request_list

trusts = get_all_trust_statuses()

print(trusts)

for i in trusts:
    print(trusts[i])


def format_nhs_number(nhs_number):
    formatted_number = "{0} {1} {2}".format(nhs_number[0:3],
                                            nhs_number[3:6],
                                            nhs_number[6:10])
    print(nhs_number)
    print(formatted_number)
    return formatted_number