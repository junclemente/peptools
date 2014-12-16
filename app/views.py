from flask import render_template
from app import app
from forms import ConvertOneForm
from config import aa_dict
from my_functions import convert_1_to_3, PeptideChain


@app.route('/', methods=['GET', 'POST'])
def index():
    result = {}
    form = ConvertOneForm()

    if form.validate_on_submit():
        result = convert_1_to_3(form.aa_string.data, form.d_forms.data)

    return render_template('index.html', aa_dict=aa_dict,
                           result=result, form=form)
