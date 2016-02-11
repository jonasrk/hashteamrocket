class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    """
    :returns neighbour_indices
    """
    def k_nearest(self, kd_tree, num_neighbours):
        return [kd_tree.data[x] for x in kd_tree.query()[1]