from django.core.mail import EmailMessage

from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader, Context
from django.shortcuts import render

import xhtml2pdf.pisa as pisa
import cStringIO as StringIO


def saveHtmlToPdf(sourceHtml, outputFilename):
        # open output file for writing (truncated binary)
    resultFile = open(outputFilename, "w+b")
        # convert HTML to PDF
    pisaStatus = pisa.CreatePDF(
            sourceHtml,                # the HTML to convert
            dest=resultFile)           # file handle to recieve result
        # close output file
    resultFile.close()                 # close output file
        # return True on success and False on errors
    return pisaStatus.err


def send_mail_to_client(title, content, client_email, attachment=None):
    # Create message from arguments
    message = EmailMessage(title, content, to=[client_email])
    # Create attachment if requested
    if not attachment is None:
        message.attach_file(attachment)

    return message.send()


def PDF_HTTP_Response(sourceHtml, filename):
    result = StringIO.StringIO()
    pdf = pisa.pisaDocument(StringIO.StringIO(sourceHtml.encode("UTF-8")), result)
    response = HttpResponse(result.getvalue(), mimetype='application/pdf')
    response['Content-Disposition'] = 'filename=' + filename

    if not pdf.err:
        return response
    return HttpResponse('We had some errors<pre>%s</pre>' % cgi.escape(html))
    



