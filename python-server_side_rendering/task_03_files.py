#!/usr/bin/python3
from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)


# --- JSON oxuma funksiyası ---
def read_json_file(filename):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error reading JSON file: {e}")
        return []


# --- CSV oxuma funksiyası ---
def read_csv_file(filename):
    data = []
    try:
        with open(filename, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # CSV-dakı id və price convert etmək
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                data.append(row)
    except Exception as e:
        print(f"Error reading CSV file: {e}")
    return data


# --- Products Route ---
@app.route('/products')
def products():
    source = request.args.get('source', '').lower()
    product_id = request.args.get('id', type=int)

    # Data oxumaq
    if source == 'json':
        products_data = read_json_file('products.json')
    elif source == 'csv':
        products_data = read_csv_file('products.csv')
    else:
        return render_template('product_display.html', error='Wrong source', products=[])

    # Filter id ilə
    if product_id is not None:
        filtered = [p for p in products_data if p.get('id') == product_id]
        if not filtered:
            return render_template('product_display.html', error='Product not found', products=[])
        products_data = filtered

    return render_template('product_display.html', products=products_data, error=None)


# --- Əvvəlki route-lar ---
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)
