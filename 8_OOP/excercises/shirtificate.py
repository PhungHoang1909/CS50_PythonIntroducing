from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'CS50 Shirtificate', 0, 1, 'C')

def main():
    name = input("Enter your name: ")

    pdf = PDF()
    pdf.add_page()

    pdf.set_font('Arial', '', 12)
    pdf.cell(0, 10, name, 0, 1, 'C')

    pdf.image('shirtificate.png', x = 105, y = None, w = 0, h = 0, type = '', link = '')

    pdf.output('shirtificate.pdf', 'F')

if __name__ == "__main__":
    main()
