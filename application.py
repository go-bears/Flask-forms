from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index_page():
    """Serves an index page."""
    
    return render_template("index.html")

    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    #
    # return render_template("index.html")
    
@app.route("/application-form")
def serve_application_form():
    """Serves template application-form.html at the route /application-form """
    
    return render_template("application-form.html")
    
@app.route("/application", methods="POST")
def confirm_form_submission():
    """Serves the the template application-response.html at the route /application
    
    receives data from application-form.html and posts message to application-response.html
    """
    
    #uses flask request get() to grab form's data
    first_name = request.form.get("firstname")
    last_name = request.form.get("lastname")
    salary = request.form.get("salary")
    job = request.form.get("job")
    print job
    
    submission_msg = """
    Thank you, %s %s , for applying to be a %s. Your
    minimum salary requirement is %s dollars.
    """ % (first_name, last_name, job, salary)
    
    return render_template("application-response.html", msg = submission_msg)

if __name__ == "__main__":
    app.run(debug=True)
    #for settings for deploying flask app on cloud9
