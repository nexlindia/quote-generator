from flask import Flask, request, send_file, render_template
import os
from generate_quote import get_rates_from_excel, generate_quote
from create_pdf import create_quote_pdf

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('quote_template.html')

@app.route('/generate-quote', methods=['POST'])
def generate_quote_route():
    customer_info = {
        "name": request.form['name'],
        "email": request.form['email']
    }
    rates_df = get_rates_from_excel('../list.xlsx')
    quote = generate_quote(rates_df, customer_info)
    pdf_path = 'quote.pdf'
    create_quote_pdf(quote, pdf_path)
    return send_file(pdf_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)