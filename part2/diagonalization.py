import numpy as np
import math

def jacobi_eigenvalue_algorithm(A, tol=1e-9, max_iterations=1000):
    """
    Tìm giá trị riêng và vector riêng của ma trận đối xứng bằng phương pháp Jacobi.
    Trả về D (các giá trị riêng) và P (ma trận vector riêng).
    """
    n = len(A)
    # Khởi tạo D là bản sao của A, P là ma trận đơn vị
    D = [[A[i][j] for j in range(n)] for i in range(n)]
    P = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]

    def max_off_diagonal(mat):
        max_val = 0.0
        p, q = 0, 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                if abs(mat[i][j]) > max_val:
                    max_val = abs(mat[i][j])
                    p, q = i, j
        return max_val, p, q

    for _ in range(max_iterations):
        max_val, p, q = max_off_diagonal(D)
        if max_val < tol:
            break

        theta = 0.5 * math.atan2(2 * D[p][q], D[q][q] - D[p][p])

        c = math.cos(theta)
        s = math.sin(theta)

        # Cập nhật D và P
        for i in range(n):
            Pip, Piq = P[i][p], P[i][q]
            P[i][p] = c * Pip - s * Piq
            P[i][q] = s * Pip + c * Piq

            if i != p and i != q:
                Dip, Diq = D[i][p], D[i][q]
                D[i][p] = D[p][i] = c * Dip - s * Diq
                D[i][q] = D[q][i] = s * Dip + c * Diq

        Dpp, Dqq, Dpq = D[p][p], D[q][q], D[p][q]
        D[p][p] = c**2 * Dpp - 2*s*c*Dpq + s**2 * Dqq
        D[q][q] = s**2 * Dpp + 2*s*c*Dpq + c**2 * Dqq
        D[p][q] = D[q][p] = 0.0

    eigenvalues = [D[i][i] for i in range(n)]
    return eigenvalues, P

def verify_diagonalization(A, eigenvalues, P):
    """Kiểm chứng kết quả chéo hóa bằng NumPy."""
    print("\n--- KIỂM CHỨNG CHÉO HÓA ---")
    np_eigvals, np_eigvecs = np.linalg.eig(A)
    
    eigvals_sorted = np.sort(eigenvalues)
    np_eigvals_sorted = np.sort(np_eigvals)
    
    is_close_vals = np.allclose(eigvals_sorted, np_eigvals_sorted)
    print(f"Giá trị riêng khớp với NumPy: {is_close_vals}")

    P_matrix = np.array(P)
    D_matrix = np.diag(eigenvalues)
    A_reconstructed = np.dot(P_matrix, np.dot(D_matrix, P_matrix.T))
    
    is_close_A = np.allclose(A, A_reconstructed)
    print(f"P * D * P^(-1) khớp với A gốc: {is_close_A}")

if __name__ == "__main__":
    # Ma trận SPD mẫu (từ kết quả Cholesky)
    A = [
        [4, 12, -16],
        [12, 37, -43],
        [-16, -43, 98]
    ]
    eigenvalues, P = jacobi_eigenvalue_algorithm(A)
    print("Giá trị riêng (Eigenvalues):", [round(v, 4) for v in eigenvalues])
    verify_diagonalization(A, eigenvalues, P)