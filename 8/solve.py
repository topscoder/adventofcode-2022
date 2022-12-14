

def tree_is_visible(grid, row, col, tree):
    print(f"checking tree {tree} from grid pos [{row},{col}]")
    if grid[row][col] != tree:
        raise ValueError("Wrong value passed to scan_row")

    # Scan to left
    scanpos_col = col - 1
    view_blocked = False
    while scanpos_col >= 0:
        # print(f"scanning to left: pos [{row, scanpos_col}]")

        # If scanned tree is taller or equal than the tree we're looking for
        # this scanned tree is in the way
        if grid[row][scanpos_col] >= tree:
            view_blocked = True
            break

        if grid[row][scanpos_col] > grid[row][scanpos_col + 1]:
            view_blocked = True
            break

        scanpos_col = scanpos_col - 1

    if view_blocked is False:
        return True

    # Scan to right
    scanpos_col = col + 1
    view_blocked = False
    while scanpos_col < len(grid[row]):
        # print(f"scanning to right: pos[{row, scanpos_col}]")

        # If scanned tree is taller or equal than the tree we're looking for
        # this scanned tree is in the way
        if grid[row][scanpos_col] >= tree:
            view_blocked = True
            break

        if grid[row][scanpos_col] > grid[row][scanpos_col - 1]:
            view_blocked = True
            break

        scanpos_col = scanpos_col + 1

    if view_blocked is False:
        return True

    # Scan to top
    scanpos_row = row - 1
    view_blocked = False
    while scanpos_row >= 0:
        # print(f"scanning to top: pos [{scanpos_row}, {col}]")

        # If scanned tree is taller or equal than the tree we're looking for
        # this scanned tree is in the way
        if grid[scanpos_row][col] >= tree:
            view_blocked = True
            break

        if grid[scanpos_row][col] > grid[scanpos_row][col + 1]:
            view_blocked = True
            break

        scanpos_row = scanpos_row - 1

    if view_blocked is False:
        return True

    # Scan to bottom
    scanpos_row = row
    invisible = False
    while scanpos_row < len(grid):
        scanpos_row = scanpos_row + 1

        if scanpos_row == len(grid):
            break

        print(f"scanning to bottom: pos [{scanpos_row}, {col}, {len(grid)}]")

        # If scanned tree is taller or equal than the tree we're looking for
        # this scanned tree is in the way
        if not grid[scanpos_row]:
            print(f"scanning to bottom halted because row {scanpos_row} is not available in the grid.")
            break

        if not grid[scanpos_row][col]:
            print(
                f"scanning to bottom halted because col {col} is not available in grid row {scanpos_row}.")
            break

        if grid[scanpos_row][col] >= tree:
            invisible = True
            break

        if grid[scanpos_row][col] > grid[scanpos_row][col - 1]:
            invisible = True
            break

    if invisible is False:
        return True

    return False


with open('input.txt') as f:
    grid = f.read()
    gridlines = grid.split("\n")
    row = -1
    col = -1
    visibles = 0

    # print(f"")
    # print(f"{grid}")
    # print(f"")

    for line in gridlines:
        # process each tree.
        # is it visible from all sides?
        if len(line.strip()) == 0:
            continue

        row = row + 1
        col = -1

        # All trees in FIRST row are always visible from outside.
        if row == 0:
            visibles = visibles + len(line)
            continue

        # All trees in LAST row are always visible from outside.
        if row == (len(gridlines) - 1):
            visibles = visibles + len(line)
            continue

        print(f"{line}")

        for tree in line:
            col = col + 1

            # First tree in a row is always visible from outside
            if col == 0:
                visibles = visibles + 1
                continue

            # Last tree in a row is always visible from outside
            if col == (len(line) - 1):
                visibles = visibles + 1
                continue

            if tree_is_visible(gridlines, row, col, tree) is True:
                visibles = visibles + 1

        print(f"")


print(f"")
print(f"The amount of trees that are visible from outside the grid: {visibles}")
print(f"")