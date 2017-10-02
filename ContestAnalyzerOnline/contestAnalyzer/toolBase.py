import os

class toolBase(object):
    def __init__(self, name):
        m_name = name

    def __str__(self):
        return m_name

    def applyToAll(self, contest):
        pass

    def applyToRow(self, row):
        return row
