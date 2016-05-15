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
    list_of_trusts = ['R1A', 'R1A02','RA708']
    trust_data = controller.get_trust_statuses(list_of_trusts)

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
    trust_data = controller.get_all_trust_statuses()
    return render_template('units.html',
                           trusts=trust_data)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(
        host="0.0.0.0",
        port = port,
        debug=True
    )