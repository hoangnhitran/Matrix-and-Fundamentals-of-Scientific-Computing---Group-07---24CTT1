def rank_and_basis(A):
    """
    Tính hạng (rank) và cơ sở của ba không gian cơ bản của A:
      • Không gian cột   Col(A)  — span các cột độc lập tuyến tính
      • Không gian dòng  Row(A)  — span các hàng pivot của dạng bậc thang
      • Không gian nghiệm Null(A) — tập nghiệm của A·x = 0
 
    Thuật toán: khử Gauss–Jordan để đưa A về dạng bậc thang rút gọn (RREF).
 
    Tham số
    A : list[list[float]] — ma trận m×n (không nhất thiết vuông)
 
    Trả về (dict)
    {
      "rank"         : int,
      "col_basis"    : list[list[float]],  # các cột gốc tương ứng pivot
      "row_basis"    : list[list[float]],  # các hàng pivot trong RREF
      "null_basis"   : list[list[float]],  # cơ sở không gian nghiệm
      "pivot_cols"   : list[int],
      "free_cols"    : list[int],
    }
    """
    PIVOT_EPS = 1e-12
    m = len(A)
    n = len(A[0])
 
    # Làm việc trên bản sao float
    M = [[float(A[i][j]) for j in range(n)] for i in range(m)]
    pivot_cols = []
    row = 0
 
    for col in range(n):
        if row >= m:
            break
 
        # Tìm pivot trong cột col từ hàng `row` trở xuống
        pivot = -1
        max_val = PIVOT_EPS
        for i in range(row, m):
            if abs(M[i][col]) > max_val:
                max_val = abs(M[i][col])
                pivot = i
 
        if pivot == -1:
            continue   # cột tự do
 
        # Hoán đổi hàng
        if pivot != row:
            M[row], M[pivot] = M[pivot], M[row]
 
        pivot_cols.append(col)
 
        # Chuẩn hóa hàng pivot
        piv_val = M[row][col]
        for j in range(n):
            M[row][j] /= piv_val
 
        # Khử cả trên lẫn dưới → RREF
        for i in range(m):
            if i == row:
                continue
            factor = M[i][col]
            for j in range(n):
                M[i][j] -= factor * M[row][j]
 
        row += 1
 
    rank = len(pivot_cols)
    free_cols = [c for c in range(n) if c not in pivot_cols]
 
    # Cơ sở không gian cột: các cột gốc của A tại vị trí pivot
    col_basis = [[A[i][c] for i in range(m)] for c in pivot_cols]
 
    # Cơ sở không gian dòng: các hàng pivot trong RREF 
    row_basis = [M[k][:] for k in range(rank)]
 
    # Cơ sở không gian nghiệm 
    # Với mỗi biến tự do f, đặt x_f = 1, các biến tự do khác = 0,
    # rồi đọc các biến pivot từ RREF.
    null_basis = []
    for idx, f in enumerate(free_cols):
        vec = [0.0] * n
        vec[f] = 1.0
        for k, pc in enumerate(pivot_cols):
            # RREF row k: x[pc] + Σ_{free} M[k][free] · x[free] = 0
            vec[pc] = -M[k][f]
        null_basis.append(vec)
 
    return {
        "rank"       : rank,
        "col_basis"  : col_basis,
        "row_basis"  : row_basis,
        "null_basis" : null_basis,
        "pivot_cols" : pivot_cols,
        "free_cols"  : free_cols,
    }
 