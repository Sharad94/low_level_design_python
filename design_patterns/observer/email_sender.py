import zope.interface
from subscriber_interface import SubscriberInterface
from flipkart import Flipkart

@zope.interface.implementer(SubscriberInterface)
class EmailSender:
    def __init__(self):
        Flipkart.get_instance().add_to_subscribers(self)

    def notify(self, order_info):
        print("Email sender, order_info {0}".format(order_info))


