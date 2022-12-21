
# import python module
from xhtml2pdf import pisa
from jinja2 import Environment, BaseLoader
import random
# open text file in read mode
text_file = open("./index.html", "r")
# read whole file to a string
source_html = text_file.read()
# close file
text_file.close()


# Define your data
output_filename = "test.pdf"

# Utility function


def addValuesToTemplateHTML(source_html, data):
    rtemplate = Environment(loader=BaseLoader).from_string(source_html)
    html = rtemplate.render(data)

    return html


def convert_html_to_pdf(source_html, output_filename):
    # open output file for writing (truncated binary)
    result_file = open(output_filename, "w+b")

    # convert HTML to PDF
    pisa_status = pisa.CreatePDF(
        source_html,                # the HTML to convert
        dest=result_file)           # file handle to recieve result

    # close output file
    result_file.close()                 # close output file

    # return False on success and True on errors
    return pisa_status.err


def generate_transactions():
    transactions = []
    for n in range(300):
        transactions.append({"consumer": "07-Nov", "process": "07-Nov",
                            "commerce": "Rappi", "amount": "-S/"+str(random.randint(10, 50))+".00",
                             "tea": "21.70%", })
    return transactions


# Main program
if __name__ == "__main__":
    # pisa.showLogging()
    convert_html_to_pdf(addValuesToTemplateHTML(
        source_html, {"name": "Raico", "billingStartDate": "20/11/2022",
                      "billingEndDate": "20/12/2022",
                      "transactions": generate_transactions()}), output_filename)
