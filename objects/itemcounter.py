# ===========================================
# = Module for items counter and management =
# ===========================================

class ItemsCounter:

    def __init__(self):
        self.counter_value = 3

    # -------------------------------------------------------------------------
    def decrease(self):
        self.counter_value -= 1
