
class ToolBase(object):
    def __init__(self, name):
        self.m_name = name

    def __str__(self):
        return self.m_name

    def apply_to_all(self, contest):
        pass

    def apply_to_row(self, row):
        return row
