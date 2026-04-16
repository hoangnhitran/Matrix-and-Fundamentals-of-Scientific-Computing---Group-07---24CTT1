PIVOT_EPS = 1e-12

def determinant(A):
    """
    Tính định thức det(A) qua khử Gauss với partial pivoting.
 
    det(A) = (−1)^s · ∏ U[i][i]
    với s = số lần hoán đổi hàng.
 
    Tham số
    -------
    A : list[list[float]] — ma trận vuông n×n
 
    Trả về
    ------
    det : float
 
    Ngoại lệ
    --------
    ValueError nếu A không vuông.
    """
    n = len(A)
    if any(len(row) != n for row in A):
        raise ValueError("determinant() chỉ áp dụng cho ma trận vuông.")
 
    # Khử Gauss trên bản sao (b giả bằng 0, không dùng)
    M = [A[i][:] for i in range(n)]
    swap_count = 0
 
    for col in range(n):
        # Tìm pivot
        pivot = col
        max_val = abs(M[col][col])
        for i in range(col + 1, n):
            if abs(M[i][col]) > max_val:
                max_val = abs(M[i][col])
                pivot = i
 
        if max_val < PIVOT_EPS:
            return 0.0   # Ma trận suy biến → det = 0
 
        if pivot != col:
            M[col], M[pivot] = M[pivot], M[col]
            swap_count += 1
 
        for i in range(col + 1, n):
            factor = M[i][col] / M[col][col]
            for j in range(col, n):
                M[i][j] -= factor * M[col][j]
 
    # det = (−1)^s · tích các phần tử đường chéo
    det = (-1) ** swap_count
    for i in range(n):
        det *= M[i][i]
    return det
 