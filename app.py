import os

import bed_data
import controller

from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/')
@app.route('/dashboard')
def dashboard():

    # Get trust statuses
    list_of_trusts = ['R1A', 'R1A02','R1A03']
    trust_data = controller.get_trust_statuses(list_of_trusts)

    for trust in trust_data:
        if trust['beds_available_type1'] < 1:
            trust['type1_class'] = 'danger'
        elif trust['beds_available_type1'] < 5:
            trust['type1_class'] = 'warning'
        else:
            trust['type1_class'] = 'active'

    for trust in trust_data:
        if trust['beds_available_type2'] < 1:
            trust['type2_class'] = 'danger'
        elif trust['beds_available_type2'] < 5:
            trust['type2_class'] = 'warning'
        else:
            trust['type2_class'] = 'active'

    for trust in trust_data:
        if trust['beds_available_type3'] < 1:
            trust['type3_class'] = 'danger'
        elif trust['beds_available_type3'] < 5:
            trust['type3_class'] = 'warning'
        else:
            trust['type3_class'] = 'active'

    # Get active requests
    active_request_list = controller.get_active_requests()
    no_of_requests = len(active_request_list)
    active_request_data = {
        'count': no_of_requests,
        'requests': active_request_list
    }

    # Get rejected requests
    rejected_request_list = controller.get_rejected_requests()
    no_of_requests = len(rejected_request_list)
    rejected_request_data = {
        'count': no_of_requests,
        'requests': rejected_request_list
    }

    # Get cancelled requests
    cancelled_request_list = controller.get_rejected_requests()
    no_of_requests = len(cancelled_request_list)
    cancelled_request_data = {
        'count': no_of_requests,
        'requests': cancelled_request_list
    }

    return render_template('dashboard.html',
                           trusts=trust_data,
                           active_request_list=active_request_data,
                           rejected_request_list=rejected_request_data,
                           cancelled_request_list=cancelled_request_data
                           )


@app.route('/units')
def units():
    return render_template('units.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(
        host="0.0.0.0",
        port = port,
        debug=True
    )