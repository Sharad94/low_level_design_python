class StudentRegistry:
    def __init__(self):
        self._register_map = {}

    def add_to_registry(self, name, proto):
        self._register_map[name] = proto

    def get_from_registry(self, name):
        return self._register_map[name]