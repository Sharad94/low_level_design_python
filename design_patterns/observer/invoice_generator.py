import zope.interface
from subscriber_interface import SubscriberInterface
from flipkart import Flipkart


@zope.interface.implementer(SubscriberInterface)
class InvoiceGenerator:

    def __init__(self):
        Flipkart.get_instance().add_to_subscribers(self)

    def notify(self, order_info):
        print("Invoice generator, order_info {0}".format(order_info))


