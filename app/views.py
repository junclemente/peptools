from flask import render_template
from app import app
from forms import ConvertOneForm
from config import aa_dict
from my_functions import convert_1_to_3


@app.route('/', methods=['GET', 'POST'])
def index():
    # global amino_acid_dict
    result = {}

    form = ConvertOneForm()

    # print len(aa_dict)

    if form.validate_on_submit():
        # print form.aa_string.data
        # print form.d_forms.data
        result = convert_1_to_3(form.aa_string.data, form.d_forms.data)
        # print result
        # return render_template('index.html', aa_dict=aa_dict, title='Peptide \
        #                        Sequence Conversion Tool', form=form)

    return render_template('index.html', aa_dict=aa_dict,
                           result=result, form=form)
