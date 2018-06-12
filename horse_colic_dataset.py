

class HorseColicRow:
    def __init__(self, row: list):
        self.row = row

    def expected_result(self):
        """
        Returns what eventually happened to the horse:
            0 - lived
            1 - died
            2 - was euthanized
        """
        return self.row[22] - 1

    @staticmethod
    def num_output_categories():
        return 3

    def input(self):
        """
        Returns the data from the row except:
            - hospital number
            - outcome
            - whether the lesion was surgical
            - type of lesion (x3)
            - whether pathology data is present for this case
        """
        return self.row[:2] + self.row[3:22]
