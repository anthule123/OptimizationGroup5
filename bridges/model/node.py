class Node:
    def __init__(self, id, goal_order, potenial_neighbor_ids, x,y, ):
        self.id = id
        self.goal_order = goal_order
        self.potenial_neighbor_ids = potenial_neighbor_ids
        self.x = x
        self.y = y
    def __repr__(self):
        return f'Node(id: {self.id}, goal_order: {self.goal_order}, {self.potenial_neighbor_ids},x= {self.x},y= {self.y})'