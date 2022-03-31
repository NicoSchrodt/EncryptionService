from Service.Text.Text import Text


class CaesarText(Text):
    def __init__(self):
        super().__init__()
        self.set_eligible_characters("std")
