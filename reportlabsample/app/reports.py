from django.http import HttpResponse
from reportlab.lib.pagesizes import LETTER
from reportlab.pdfgen.canvas import Canvas
from rest_framework.views import APIView

WIDTH = LETTER[0]
HEIGHT = LETTER[1]


class CustomerReport(APIView):
    """This class container customer report."""

    def get(self, request, *args, **kwargs):
        """Generate pdf customer report."""
        response = HttpResponse(content_type='application/pdf')

        pdf = Canvas(response)
        pdf.setPageSize(LETTER)

        pdf.drawString(100, HEIGHT - 100, 'Hello world!')

        pdf.showPage()
        pdf.save()

        return response


customer_report = CustomerReport.as_view()
