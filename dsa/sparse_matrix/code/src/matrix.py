def load_sparse_matrix(filename):
    """Reads a sparse matrix from a file."""
    with open(filename, 'r') as file:
        try:
            rows = int(file.readline().strip().split('=')[1])
            cols = int(file.readline().strip().split('=')[1])
        except:
            raise ValueError("Input file format is incorrect.")

        matrix = {}
        for line in file:
            line = line.strip()
            if not line:
                continue
            if not (line.startswith('(') and line.endswith(')')):
                raise ValueError("Incorrect format in input file.")
            try:
                r, c, v = map(int, line[1:-1].split(','))
                if r not in matrix:
                    matrix[r] = {}
                matrix[r][c] = v
            except:
                raise ValueError("Incorrect format in input file.")
    return matrix, rows, cols


def perform_matrix_operation(m1, m2, op, r1, c1, r2, c2):
    """Performs add, subtract, or multiply on sparse matrices."""
    if op in ["add", "subtract"] and (r1 != r2 or c1 != c2):
        raise ValueError("Matrix dimensions must match for addition or subtraction.")
    if op == "multiply" and c1 != r2:
        raise ValueError("Matrix dimensions not compatible for multiplication.")

    result = {}

    if op == "add" or op == "subtract":
        keys = set(m1.keys()).union(m2.keys())
        for i in keys:
            row1 = m1.get(i, {})
            row2 = m2.get(i, {})
            result_row = {}
            all_cols = set(row1.keys()).union(row2.keys())
            for j in all_cols:
                a = row1.get(j, 0)
                b = row2.get(j, 0)
                res = a + b if op == "add" else a - b
                if res != 0:
                    result_row[j] = res
            if result_row:
                result[i] = result_row

    elif op == "multiply":
        for i in m1:
            for k in m1[i]:
                if k in m2:
                    for j in m2[k]:
                        val = m1[i][k] * m2[k][j]
                        if val != 0:
                            if i not in result:
                                result[i] = {}
                            result[i][j] = result[i].get(j, 0) + val

    return result


def save_matrix_to_file(matrix, output_file):
    """Saves matrix to file in sparse format."""
    if not matrix:
        return
    rows = max(matrix.keys()) + 1
    cols = max((max(row.keys()) for row in matrix.values()), default=-1) + 1
    with open(output_file, 'w') as f:
        f.write(f"rows={rows}\n")
        f.write(f"cols={cols}\n")
        for r, row in matrix.items():
            for c, val in row.items():
                f.write(f"({r}, {c}, {val})\n")


def main():
    try:
        file1 = input("Path of first file: ").strip()
        file2 = input("Path of second file: ").strip()
        operation = input("Operation [add, subtract, multiply]: ").strip()
        output_file = input("Output file name: ").strip() or f"result_{operation}.txt"

        m1, r1, c1 = load_sparse_matrix(file1)
        m2, r2, c2 = load_sparse_matrix(file2)

        result = perform_matrix_operation(m1, m2, operation, r1, c1, r2, c2)
        save_matrix_to_file(result, output_file)

        print(f"✅ Result saved to {output_file}")
    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    main()
