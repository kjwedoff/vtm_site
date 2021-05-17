from flask import Flask
from flask import render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mike')
def mike():
    return render_template('mike.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/estimate', methods=['GET'])
def estimate():
    return render_template('estimate.html')

@app.route('/calculate', methods=['POST'])
def add():
    if request.method == 'POST':
        radius = int(request.form['radius'])
        height = int(request.form['height'])
        area_top = 3.14 * (radius * radius)
        area_side = 2 * (3.14 * (radius * height))
        total_area = area_top + area_side
        total_area_sq = total_area/144
        material_cost = total_area_sq * 25 
        labor_cost = total_area_sq * 15 
        total_price = material_cost + labor_cost
        print(total_price)
    return render_template('estimate.html', myValue = total_price)

if __name__ == '__main__':
    app.run(debug=True)