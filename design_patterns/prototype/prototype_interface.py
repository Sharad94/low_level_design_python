import zope.interface

class ProtoTypeInterface(zope.interface.Interface):
    def copy(self):
        pass
