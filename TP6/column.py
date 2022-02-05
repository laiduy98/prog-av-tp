class Column:
    def __init__(self, num_rows) -> None:
        self.items = [None] * num_rows

    def drop(self, p, verbose=True):
        phases = []
        i = 0
        for i, item in enumerate(self.items):
            if item is not None:
                break
            if i - 1 >= 0:
                self.items[i - 1] = None
            self.items[i] = p
            if verbose:
                print(self)
            phases.append(self.str_helper())
        # Convenient for ex 3
        return phases

    def str_helper(self):
        s = []
        for item in self.items:
            s.append("+---+")
            center = item.symbol if item is not None else " "
            s.append(f"| {center} |")
        s.append("+---+")
        return s

    def __str__(self) -> str:
        return "\n".join(self.str_helper())
