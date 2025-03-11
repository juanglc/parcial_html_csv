from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
from flask_session import Session
from arrays.create_arrays import create_arrays
from arrays.add_array import add_array
from arrays.delete_array import delete_array
from arrays.order_array import order_asc, order_desc
from arrays.search_array import search_array

app = Flask(__name__)
app.secret_key = 'uwu'
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

data = create_arrays.create_array()
print(len(data))

@app.route('/')
def home():
    filtered_data = session.get('filtered_data', data)
    data_length = len(data)
    return render_template('index.html', data=filtered_data, data_length=data_length)

@app.route('/data')
def get_data():
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))
    start = (page - 1) * per_page
    end = start + per_page
    filtered_data = session.get('filtered_data', data)
    paginated_data = filtered_data[start:end]
    return jsonify(paginated_data)

@app.route('/add', methods=['POST'])
def add():
    try:
        fecha = str(request.form['fecha'])
        cod_depto = int(request.form['cod_depto'])
        depto = request.form['depto']
        cod_muni = int(request.form['cod_muni'])
        muni = request.form['muni']
        cant = float(request.form['cant'])

        if cod_depto <= 0 or cod_muni <= 0 or cant <= 0:
            flash("⚠️ Los valores numéricos deben ser mayores que 0", "error")
            return redirect(url_for('home'))

        add_array.add_to_array(data, fecha, cod_depto, depto.upper(), cod_muni, muni.upper(), cant)
        session['filtered_data'] = order_asc.order_asc_date(data[:])
        flash("✅ Registro añadido exitosamente", "success")
    except ValueError:
        flash("❌ Error en el formato de los datos", "error")
    print(len(data))
    return redirect(url_for('home') + '#data-table')

@app.route('/delete', methods=['POST'])
def delete():
    ID = int(request.form['id'])
    delete_array.remove_from_array(data, ID)
    session['filtered_data'] = data[:]
    print(len(data))
    return redirect(url_for('home') + '#data-table')

@app.route('/sort')
def sort():
    column = request.args.get('column')
    order = request.args.get('order')

    if column and order:
        filtered_data = session.get('filtered_data', data[:])[:]

        if order == 'asc':
            if column == 'fecha':
                filtered_data = order_asc.order_asc_date(filtered_data)
            elif column == 'depto':
                filtered_data = order_asc.order_asc_dept(filtered_data)
            elif column == 'muni':
                filtered_data = order_asc.order_asc_muni(filtered_data)
            elif column == 'cant':
                filtered_data = order_asc.order_asc_cant(filtered_data)
        elif order == 'desc':
            if column == 'fecha':
                filtered_data = order_desc.order_desc_date(filtered_data)
            elif column == 'depto':
                filtered_data = order_desc.order_desc_dept(filtered_data)
            elif column == 'muni':
                filtered_data = order_desc.order_desc_muni(filtered_data)
            elif column == 'cant':
                filtered_data = order_desc.order_desc_cant(filtered_data)

        session['filtered_data'] = filtered_data[:]
    return redirect(url_for('home') + '#data-table')

@app.route('/search', methods=['POST'])
def search():
    criterion = request.form['criterion']
    value = request.form['value']
    result = []

    if value.strip():
        if criterion == 'date':
            result = search_array.filter_by_date(data, value)
        elif criterion == 'dept':
            result = search_array.filter_by_dept(data, value)
        elif criterion == 'muni':
            result = search_array.filter_by_muni(data, value)
        elif criterion == 'cant':
            result = search_array.filter_by_cant(data, float(value))

    if not result:
        result = data[:]

    session['filtered_data'] = result[:]
    return redirect(url_for('home') + '#data-table')

@app.route('/show_all', methods=['POST'])
def show_all():
    session.pop('filtered_data', None)
    return redirect(url_for('home') + '#data-table')

if __name__ == '__main__':
    app.run(debug=True)