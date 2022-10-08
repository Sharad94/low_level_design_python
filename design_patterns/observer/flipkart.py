import threading

class Flipkart:
    __instance = None
    __instance_lock = threading.Lock()

    def __init__(self):
        self.subscribers_list = []

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            with cls.__instance_lock:
                if cls.__instance is None:
                    cls.__instance = Flipkart()

        return cls.__instance

    def add_to_subscribers(self, subscriber):
        self.subscribers_list.append(subscriber)

    def remove_from_subscribers(self, subscriber):
        self.subscribers_list.remove(subscriber)

    def order_placed(self, order_info):
        for subscriber in self.subscribers_list:
            subscriber.notify(order_info)