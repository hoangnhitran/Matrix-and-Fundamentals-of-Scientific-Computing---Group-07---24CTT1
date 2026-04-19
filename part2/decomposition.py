import math
import numpy as np

def cholesky_decomposition(A):
    """
    Phân rã ma trận A thành L * L^T (A phải là ma trận đối xứng xác định dương).
    """
    n = len(A)
    L = [[0.0] * n for _ in range(n)]

    for j in range(n):
        # Tính các phần tử trên đường chéo chính: L_jj
        sum_k = sum(L[j][k] ** 2 for k in range(j))
        val = A[j][j] - sum_k
        
        if val <= 0:
            raise ValueError("Ma trận không phải là đối xứng xác định dương (Not SPD).")
            
        L[j][j] = math.sqrt(val)

        # Tính các phần tử nằm dưới đường chéo: L_ij (i > j)
        for i in range(j + 1, n):
            sum_k = sum(L[i][k] * L[j][k] for k in range(j))
            L[i][j] = (A[i][j] - sum_k) / L[j][j]

    return L

def verify_cholesky(A, L):
    """Kiểm chứng kết quả phân rã Cholesky bằng NumPy."""
    print("\n--- KIỂM CHỨNG PHÂN RÃ CHOLESKY ---")
    try:
        L_numpy = np.linalg.cholesky(A)
        L_matrix = np.array(L)
        A_reconstructed = np.dot(L_matrix, L_matrix.T)
        
        is_close_L = np.allclose(L, L_numpy)
        is_close_A = np.allclose(A, A_reconstructed)
        
        print(f"Ma trận L khớp với NumPy: {is_close_L}")
        print(f"L * L^T khớp với ma trận A gốc: {is_close_A}")
    except np.linalg.LinAlgError:
        print("NumPy đánh giá ma trận này không phải là SPD.")

if __name__ == "__main__":
    A = [
        [4, 12, -16],
        [12, 37, -43],
        [-16, -43, 98]
    ]
    print("Ma trận A gốc:")
    for row in A:
        print(row)
        
    L = cholesky_decomposition(A)
    print("\nMa trận tam giác dưới L:")
    for row in L:
        print([round(val, 4) for val in row])
        
    verify_cholesky(A, L)