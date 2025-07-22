from flask import Flask, render_template, flash, redirect, url_for
from forms import LeaveApplicationForm
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'supersecretkey'

@app.route('/', methods=['GET', 'POST'])
def leave():
    form = LeaveApplicationForm()
    if form.validate_on_submit():
        start = form.start_date.data
        end = form.end_date.data

        if end < start:
            form.end_date.errors.append("End Date cannot be earlier than Start Date.")
        else:
            duration = (end - start).days + 1
            flash(f'Leave applied successfully for {duration} day(s).', 'success')
            return redirect(url_for('leave'))

    return render_template('leave_form.html', form=form)
