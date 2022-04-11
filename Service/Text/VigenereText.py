from Service.Text.Text import Text


class VigenereText(Text):
    def __init__(self):
        super().__init__()
        self.set_eligible_characters_list("std")
