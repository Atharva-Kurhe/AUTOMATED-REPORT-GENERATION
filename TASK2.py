import pandas as ps
from fpdf import FPDF

def read_and_analyze_infomation(file_path):
    info = ps.read_csv(file_path)
    info['Total'] = info['Quantity'] * info['Price']
    total_sales = info['Total'].sum()
    most_sold_product = info.loc[info['Total'].idxmax()]
    return info, total_sales, most_sold_product

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B''U', 20)
        self.cell(200, 10, 'Electronic Sales Analysis Report', align='C', ln=True)
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 12)
        self.cell(0, 10, f'Page {self.page_no()}', align='C')

def create_pdf(info, total_sales, most_sold_product, saved_file):
    pdf = PDF()
    pdf.add_page()
    pdf.set_font('Arial', '', 14)

    pdf.cell(0, 10, f'Total Electronics Sales: Rs. {total_sales}', ln=True)
    pdf.cell(0, 10, f'Most Sold Electronic Product: {most_sold_product["Product"]} (Rs. {most_sold_product["Total"]})', ln=True)
    pdf.ln(10)

    pdf.set_font('Arial', 'B', 16)
    pdf.cell(40, 10, 'Product', border=1,align='C')
    pdf.cell(40, 10, 'Quantity', border=1,align='C')
    pdf.cell(40, 10, 'Price', border=1,align='C')
    pdf.cell(40, 10, 'Total', border=1,align='C')
    pdf.ln()

    pdf.set_font('Arial', '', 14)
    for _, row in info.iterrows():
        pdf.cell(40, 10, row['Product'], border=1,align='C')
        pdf.cell(40, 10, str(row['Quantity']), border=1,align='C')
        pdf.cell(40, 10, str(row['Price']), border=1,align='C')
        pdf.cell(40, 10, str(row['Total']), border=1,align='C')
        pdf.ln()

    pdf.output(saved_file)
    print(f"Report generated: {saved_file}")
    
if __name__ == "__main__":
    file_path = "electronic_sales.csv"

    info, total_sales, most_sold_product = read_and_analyze_infomation(file_path)

    saved_file = "electronic_sales_report.pdf"
    create_pdf(info, total_sales, most_sold_product, saved_file)
