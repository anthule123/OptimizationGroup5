class Arc:
    def __init__(self, source_node_id, end_node_id, weight=1):
        self.weight = weight
        self.source_node_id = source_node_id
        self.end_node_id = end_node_id
        