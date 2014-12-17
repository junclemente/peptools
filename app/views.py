from flask import render_template
from app import app
from forms import ConvertOneForm
from config import aa_dict
from my_functions import PeptideChain


@app.route('/', methods=['GET', 'POST'])
def index():
    result = {'chain': '',
              'length': '',
              'conversion': '',
              'aa_stats': '',
              'mo_weight': ''}

    form = ConvertOneForm()

    if form.validate_on_submit():
        # result = convert_1_to_3(form.aa_string.data, form.d_forms.data)
        peptide1 = PeptideChain(form.aa_string.data, form.d_forms.data,
                                form.convert3.data)
        print form.d_forms.data
        print form.convert3.data
        result['chain'] = peptide1.peptide_chain()
        result['length'] = peptide1.peptide_length()
        result['conversion'] = peptide1.convert1_to_3()
        result['aa_stats'] = peptide1.peptide_stats()
        result['mo_weight'] = peptide1.mo_weight()

    return render_template('index.html', aa_dict=aa_dict,
                           result=result, form=form)
