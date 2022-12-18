## pdfkit-wkhtmltopdf-jinja

**Dependencias:**

- sudo apt-get install wkhtmltopdf: Este binario permite el procesamiento del html y css para su exportación. Se integra con pdf-kit para la interacción con el mismo
- pip3 install pdfkit (1.0.0): Esta biblioteca nos permitira interactuar con wkhtmltopdf para lograr exportar html a pdf.
- pip3 install jinja2 (2.10.1): Esta biblioteca nos permitira reemplazar los palabras claves introducidas en el html.

**Repositorio:**

- [https://github.com/anthbravo21/python/html-pdf/pdfkit-wkhtmltopdf-jinja](https://github.com/anthbravo21/python/tree/develop/html-pdf/pdfkit-wkhtmltopdf-jinja)

**Referencias:**

- [https://pypi.org/project/pdfkit/](https://pypi.org/project/pdfkit/)
- [https://www.youtube.com/watch?v=9XKlnD11lAA](https://www.youtube.com/watch?v=9XKlnD11lAA)

**Resumen:**

- AWS GLUE no permite agregar binarios al contenedor que realiza el procesamiento, por lo cual vuelve inviable esta solución.

## fpdf2

**Dependencias:**

- pip install fpdf2 (2.6.0): Esta biblioteca nos permitirá la creación de un pdf linea a linea.

**Repositorio:**

**Referencias:**

- [https://pypi.org/project/fpdf2/](https://pypi.org/project/fpdf2/)
- [https://www.youtube.com/watch?v=rtXLsf6Vfss](https://www.youtube.com/watch?v=rtXLsf6Vfss)

Decisión

- Basado en plantilla html (no), la complejidad es alta al momento de diseñar
- Permitir encriptación mediante password (si)
- Soporta Paginación (no se logro validar)

## xhtml2pdf

**Dependencias:**

- pip install xhtml2pdf (0.2.8): Esta biblioteca nos permite generar un pdf a partir de un template en html.

**Repositorio:**

- 

**Referencias:**

- [https://xhtml2pdf.readthedocs.io/](https://xhtml2pdf.readthedocs.io/)
- [https://www.youtube.com/watch?v=zvsCmSTGAYY](https://www.youtube.com/watch?v=zvsCmSTGAYY)

**No soporta:**

- border-radius
- line-gradient
- svg

**Soporte:**

- margin
- padding
- table
- img
- background-image (a nivel de pagina y con opacidad obligado por bug en la biblioteca)
- display: inline-block (limitado)

**Validaciones**

- Basado en plantilla html (si con limitaciones)
- Permitir encriptación mediante password (si)
- Soporta Paginación (si)

**Licencia**

- Apache License 2.0
