from column import Column


class Grid:
    def __init__(self, n, m):
        self.cols = []
        for _ in range(m):
            self.cols.append(Column(n))

    def drop(self, col_idx, p):
        target_col = self.cols[col_idx]
        phases = target_col.drop(p, verbose=False)

        for phase in phases:
            all_col_strs = [col.str_helper() for col in self.cols]
            all_col_strs[col_idx] = phase
            rows = []
            for row_items in zip(*all_col_strs):
                rows.append("".join(row_items))
            print("\n".join(rows))
        print("\n")
