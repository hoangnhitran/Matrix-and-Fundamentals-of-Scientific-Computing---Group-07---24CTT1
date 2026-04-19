import sys
import os
import math
import warnings

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

from part1.gaussian import gaussian_eliminate
from part2.decomposition import cholesky_decomposition

def check_diagonally_dominant(A):
    """Kiểm tra điều kiện hội tụ: Ma trận chéo trội chặt hàng."""
    n = len(A)
    for i in range(n):
        diag = abs(A[i][i])
        off_diag = sum(abs(A[i][j]) for j in range(n) if j != i)
        if diag <= off_diag:
            return False
    return True

def forward_substitution(L, b):
    """Thế tiến giải Ly = b (với L là ma trận tam giác dưới)."""
    n = len(L)
    y = [0.0] * n
    for i in range(n):
        s = b[i]
        for j in range(i):
            s -= L[i][j] * y[j]
        y[i] = s / L[i][i]
    return y

def backward_substitution_transpose(L, y):
    """Thế ngược giải L^T x = y."""
    n = len(L)
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        s = y[i]
        for j in range(i + 1, n):
            s -= L[j][i] * x[j] 
        x[i] = s / L[i][i]
    return x

def gauss_solve(A, b):
    """1. Giải hệ Ax = b bằng khử Gauss có Partial Pivoting (Từ Phần 1)."""
    _, _, x, _, _ = gaussian_eliminate(A, b)
    if x is None:
        raise ValueError("Hệ phương trình không có nghiệm duy nhất.")
    return x

def cholesky_solve(A, b):
    """2. Giải hệ Ax = b bằng phân rã Cholesky."""
    L = cholesky_decomposition_solver(A)
    y = forward_substitution(L, b)
    x = backward_substitution_transpose(L, y)
    return x

def gauss_seidel_solve(A, b, max_iters=1000, tol=1e-9):
    """3. Giải hệ Ax = b bằng phương pháp lặp Gauss-Seidel."""
    # Kiểm tra điều kiện hội tụ theo đúng barem điểm
    if not check_diagonally_dominant(A):
        warnings.warn("Ma trận không chéo trội chặt. Gauss-Seidel có thể không hội tụ!", RuntimeWarning)

    n = len(A)
    x = [0.0] * n 

    for it in range(max_iters):
        max_diff = 0.0
        for i in range(n):
            s1 = sum(A[i][j] * x[j] for j in range(i))
            s2 = sum(A[i][j] * x[j] for j in range(i + 1, n))
            
            new_xi = (b[i] - s1 - s2) / A[i][i]
            diff = abs(new_xi - x[i])
            if diff > max_diff:
                max_diff = diff
            x[i] = new_xi
            
        if max_diff < tol:
            return x, it + 1
            
    warnings.warn(f"Gauss-Seidel không hội tụ sau {max_iters} vòng lặp.")
    return x, max_iters
