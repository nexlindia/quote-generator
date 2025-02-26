# Quote Generator

This project is a simple web application for generating quotes from an Excel file and allowing customers to download the quotes as PDFs.

## Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/nexlindia/quote-generator.git
    cd quote-generator
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the application:
    ```bash
    python src/app.py
    ```

5. Open your web browser and go to `http://127.0.0.1:5000`.

## Usage

- Fill in the customer information on the web page and click "Generate Quote".
- The generated quote will be downloaded as a PDF file.

## Project Structure

- `src/generate_quote.py`: Functions to read data from the Excel file and generate quotes.
- `src/create_pdf.py`: Function to create a PDF from the generated quote.
- `src/app.py`: Flask web application to handle requests and generate quotes.
- `templates/quote_template.html`: HTML template for the web form.
- `list.xlsx`: Excel file containing the rates.
- `requirements.txt`: List of dependencies.
- `README.md`: Project documentation.