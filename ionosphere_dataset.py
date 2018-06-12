

class IonosphereRow:
    def __init__(self, row: list):
        self.row = row

    def expected_result(self):
        """
        Returns:
            1 if the row is "good",
            0 if the row is "bad".
        """
        return self.row[34]

    @staticmethod
    def num_output_categories():
        return 2

    def input(self):
        """Returns the data related to the flag itself."""
        return self.row[:34]
