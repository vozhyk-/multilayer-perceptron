

class FlagsRow:
    def __init__(self, row: list):
        self.row = row

    def expected_result(self):
        """Returns the religion of the flag's country."""
        return self.row[6]

    @staticmethod
    def num_output_categories():
        return 8

    def input(self):
        """Returns the data related to the flag itself."""
        return self.row[7:]
