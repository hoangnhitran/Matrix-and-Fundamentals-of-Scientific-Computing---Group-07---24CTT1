import warnings

PIVOT_EPS = 1e-12
PIVOT_WARN = 1e-8

def inverse(A):
    """
    Tính ma trận nghịch đảo A⁻¹ bằng phương pháp Gauss–Jordan.
 
    Mở rộng [A | I] và thực hiện khử hoàn toàn (cả trên lẫn dưới) để
    thu được [I | A⁻¹].
 
    Tham số
    -------
    A : list[list[float]] — ma trận vuông n×n
 
    Trả về
    ------
    inv : list[list[float]] — ma trận nghịch đảo n×n
 
    Ngoại lệ
    --------
    ValueError nếu A không vuông hoặc A suy biến (det = 0).
    """

    n = len(A)
    if any(len(row) != n for row in A):
        raise ValueError("inverse() chỉ áp dụng cho ma trận vuông.")
 
    # Tạo ma trận tăng cường [A | I_n]
    M = [A[i][:] + [1.0 if i == j else 0.0 for j in range(n)]
         for i in range(n)]
 
    for col in range(n):
        # ── Partial pivoting ────────────────────────────────────────────────
        pivot = col
        max_val = abs(M[col][col])
        for i in range(col + 1, n):
            if abs(M[i][col]) > max_val:
                max_val = abs(M[i][col])
                pivot = i
 
        if max_val < PIVOT_EPS:
            raise ValueError(
                f"Ma trận suy biến tại cột {col} "
                f"(|pivot| = {max_val:.2e}) — không tồn tại nghịch đảo."
            )
        if max_val < PIVOT_WARN:
            warnings.warn(
                f"Pivot tại cột {col} rất nhỏ ({max_val:.2e}). "
                "Ma trận có thể ill-conditioned — nghịch đảo kém chính xác.",
                RuntimeWarning,
                stacklevel=2,
            )
 
        if pivot != col:
            M[col], M[pivot] = M[pivot], M[col]
 
        # ── Chuẩn hóa hàng pivot ────────────────────────────────────────────
        piv_val = M[col][col]
        for j in range(2 * n):
            M[col][j] /= piv_val
 
        # ── Khử cả trên lẫn dưới (Jordan) ──────────────────────────────────
        for i in range(n):
            if i == col:
                continue
            factor = M[i][col]
            for j in range(2 * n):
                M[i][j] -= factor * M[col][j]
 
    # Lấy phần bên phải chính là A⁻¹
    inv = [row[n:] for row in M]
    return inv
 