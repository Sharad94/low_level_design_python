import zope.interface


class SubscriberInterface(zope.interface.Interface):
    def notify(self, order_info):
        pass