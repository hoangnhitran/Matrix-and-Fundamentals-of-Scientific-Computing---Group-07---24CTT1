import warnings
import numpy as np

PIVOT_EPS  = 1e-12   
PIVOT_WARN = 1e-6   
RESID_WARN = 1e-6

def back_substitution(U, c):
    n = len(U)
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        if abs(U[i][i]) < PIVOT_EPS:
            raise ValueError(
                f"Phần tử đường chéo U[{i}][{i}] = {U[i][i]:.2e} "
                "gần bằng 0 — hệ suy biến, không thể thế ngược."
            )
        s = c[i]
        for j in range(i + 1, n):
            s -= U[i][j] * x[j]
        x[i] = s / U[i][i]
    return x

def gaussian_eliminate(A, b):
    """
    Khử Gauss với partial pivoting để giải  A · x = b.
 
    Tham số
    -------
    A : list[list[float]] — ma trận hệ số n×n
    b : list[float]       — vector vế phải độ dài n
 
    Trả về
    ------
    U          : list[list[float]] — ma trận tam giác trên sau khử
    c          : list[float]       — vector vế phải sau biến đổi
    x          : list[float] | None — nghiệm (None nếu không duy nhất)
    swap_count : int  — số lần hoán đổi hàng
    pivot_cols : list[int] — danh sách chỉ số cột pivot
 
    Cảnh báo (RuntimeWarning)
    -------------------------
    • Khi không tìm được pivot tại một cột → hệ không có nghiệm duy nhất.
    • Khi pivot nhỏ hơn PIVOT_WARN → hệ có thể ill-conditioned.
    """
    n = len(A)
    # Tạo ma trận tăng cường [A | b]
    M = [A[i][:] + [b[i]] for i in range(n)]
    swap_count = 0
    pivot_cols = []
    row = 0
 
    for col in range(n):
        # ── Tìm pivot (partial pivoting) ───────────────────────────────────
        pivot = row
        max_val = abs(M[row][col])
        for i in range(row + 1, n):
            if abs(M[i][col]) > max_val:
                max_val = abs(M[i][col])
                pivot = i
 
        # ── Kiểm tra pivot ─────────────────────────────────────────────────
        if max_val < PIVOT_EPS:
            warnings.warn(
                f"Không tồn tại pivot tại cột {col} "
                f"(|max| = {max_val:.2e}). "
                "Hệ không có nghiệm duy nhất (vô nghiệm hoặc vô số nghiệm).",
                RuntimeWarning,
                stacklevel=2,
            )
            continue   # biến tự do — bỏ qua cột này
 
        if max_val < PIVOT_WARN:
            warnings.warn(
                f"Pivot tại cột {col} rất nhỏ "
                f"(|pivot| = {max_val:.2e}). "
                "Hệ có thể ill-conditioned — kết quả số có thể mất chính xác.",
                RuntimeWarning,
                stacklevel=2,
            )
 
        # ── Hoán đổi hàng ──────────────────────────────────────────────────
        if pivot != row:
            M[row], M[pivot] = M[pivot], M[row]
            swap_count += 1
 
        pivot_cols.append(col)
 
        # ── Khử các hàng bên dưới ──────────────────────────────────────────
        for i in range(row + 1, n):
            factor = M[i][col] / M[row][col]
            for j in range(col, n + 1):
                M[i][j] -= factor * M[row][j]
 
        row += 1
        if row == n:
            break
 
    U = [r[:-1] for r in M]
    c = [r[-1]  for r in M]
 
    # Thế ngược chỉ khi có đủ pivot (hệ có nghiệm duy nhất)
    x = None
    if row == n:
        x = back_substitution(U, c)
 
    return U, c, x, swap_count, pivot_cols 
