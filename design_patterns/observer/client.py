from flipkart import Flipkart


from invoice_generator import InvoiceGenerator
from email_sender import EmailSender

InvoiceGenerator()
EmailSender()

order_info = {
    "Title": "GOF",
    "Price": 12321
}

Flipkart.get_instance().order_placed(order_info)