#!/usr/bin/python3
from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/items')
def items():
    # JSON fayldan məlumat oxuma
    try:
        with open('items.json', 'r') as f:
            data = json.load(f)
            items_list = data.get('items', [])
    except Exception as e:
        print(f"Error reading JSON file: {e}")
        items_list = []

    # Template-ə göndər
    return render_template('items.html', items=items_list)


# Əvvəlki route-ları da saxlaya bilərsiniz
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
