import jinja2
import pdfkit


def create_pdf(url_template, parameters, url_css=''):
    template_name = url_template.split('/')[-1]
    template_folder = url_template.replace(template_name, '')

    jinja = jinja2.Environment(
        loader=jinja2.FileSystemLoader(template_folder))

    template = jinja.get_template(template_name)
    html = template.render(parameters)

    options = {'page-size': 'A4',
               'margin-top': '0',
               'margin-right': '0',
               'margin-left': '0',
               'margin-bottom': '0',
               'zoom': '1.2',
               'encoding': "UTF-8", }
    config = pdfkit.configuration(wkhtmltopdf="/usr/bin/wkhtmltopdf")
    output = "/home/anthbravo/bcp/git/python/html-pdf/pdfkit-wkhtmltopdf-jinja/output.pdf"

    pdfkit.from_string(html, output,
                       configuration=config, options=options)

    print(html)


parameters = {"name": "Anthony", "account": "123456789"}

create_pdf(
    '/home/anthbravo/bcp/git/python/html-pdf/pdfkit-wkhtmltopdf-jinja/template.html', parameters)
