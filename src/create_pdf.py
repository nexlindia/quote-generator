from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Quote', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

def create_quote_pdf(quote: dict, output_path: str):
    pdf = PDF()
    pdf.add_page()
    
    pdf.set_font('Arial', '', 12)
    pdf.cell(0, 10, f'Customer: {quote["customer"]["name"]}', 0, 1)
    pdf.cell(0, 10, f'Email: {quote["customer"]["email"]}', 0, 1)
    pdf.cell(0, 10, '', 0, 1)  # Empty line

    for item in quote["quote_items"]:
        pdf.cell(0, 10, f'{item["description"]}: {item["quantity"]} x ${item["rate"]} = ${item["total"]}', 0, 1)

    pdf.output(output_path)