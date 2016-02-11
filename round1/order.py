class Order:
    """
    :param items {prod_id : amount}
    """
    def __init__(self, position, items):
        self.position = position
        self.items = items