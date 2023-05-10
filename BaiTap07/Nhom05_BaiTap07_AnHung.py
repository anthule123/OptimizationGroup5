"""
    Thông tin các thành viên trong nhóm 5:
    1. Lê Thị Thu An, 18001975, K63 TN Toán học.
    2. Thiều Đình Minh Hùng, 21000006, K66 TN Toán học.
    Danh sách các bài tập:
"""
# Bài tập 3
# Beale function. f(x_1,x_2) = (1.5 - x_1 + x_1 x_2)^2 + (2.25 - x_1 + x_1 x_2^2)^2 + (2.625 - x_1 + x_1 x_2^3)^2
# Points A(0,0) and B(-4,3).
# 1. Lập trình thuật toán gradient descent với backtracking line search tìm điểm cực tiểu của f với các thông số sau
# • Giá trị bước ban đầu cho thuật toán backtracking line search $\bar{\alpha}= 1$.
# • Điểm xuất phát cho thuật toán gradient descent lần lượt là x_0 = A và x_0 = B.
# • Thuật toán dừng khi số bước lặp vượt quá 1000 hoặc ∥∇f(x_k)∥ ≤ 10^{−4} với x_k là tọa độ tại bước thứ k của thuật toán.
# 2. Hãy lập trình thuật toán Newton với backtracking tìm nghiệm cực tiểu của f dùng tiêu chuẩn dừng như trên.
# 3. So sánh tốc độ và chất lượng nghiệm của các thuật toán đã lập trình ở trên.

# 1. Lập trình thuật toán gradient descent với backtracking line search tìm điểm cực tiểu của f
# Thiết lập hàm $f$ và vector gradient của hàm $f$.
import numpy as np
def f(x_1, x_2):
    return (1.5 - x_1 + x_1 * x_2)**2 + (2.25 - x_1 + x_1 * x_2**2)**2 + (2.625 - x_1 + x_1 * x_2**3)**2
def getGrad_f(x_1, x_2):
    partialDerivation_x_1 = 2 * (x_2 - 1) * (x_1 * x_2 - x_1 + 1.5) + 2 * (x_2**2 - 1) * (x_1 * x_2**2 - x_1 + 2.25) + 2 * (x_2**3 - 1) * (x_1 * x_2**3 - x_1 + 2.625)
    partialDerivation_x_2 = 2 * x_1 * (x_1 * x_2 - x_1 + 1.5) + 4 * (x_1 * x_2**2 - x_1 + 2.25) * x_1 * x_2 + 6 * (x_1 * x_2**3 - x_1 + 2.625) * x_1 * x_2**2
    return np.array([partialDerivation_x_1, partialDerivation_x_2])
class GradientDescentWithBacktracking:
    def __init__(self, f, getGrad_f, x_0, alpha, beta, shrinkFactor, epsilon = 10**(-4), maxIteration = 1000):
        # Cac thong so beta va shrinkFactor se duoc su dung cho buoc backtracking tim t_k ve sau.
        self.f = f
        self.getGrad_f = getGrad_f
        self.x_0 = x_0
        self.alpha = alpha
        self.beta = beta
        self.shrinkFactor = shrinkFactor
        self.epsilon = epsilon
        self.maxIteration = maxIteration
        self.y = f(x_0[0], x_0[1])
        self.index = 0
        return None
    def solveWithBacktracking(self):
        x = self.x_0[0]
        y = self.x_0[1]
        currentStep = self.index
        for k in range(self.maxIteration):
            # Tinh gradient cua f tai x_k.
            currentGrad_f = self.getGrad_f(x, y)
            # Tinh do dai buoc t_k.
            t_Initital = self.alpha
            while self.f(x - t_Initital * currentGrad_f[0], y - t_Initital * currentGrad_f[1]) > self.f(x, y) - self.beta * t_Initital * np.linalg.norm(currentGrad_f)**2:
                t_Initital = t_Initital * self.shrinkFactor
            # Tinh x_k
            x = x - t_Initital * currentGrad_f[0]
            y = y - t_Initital * currentGrad_f[1]
            currentStep = currentStep + 1
            # Dieu kien dung epsilon.
            if np.linalg.norm(currentGrad_f) <= self.epsilon:
                break
        # print(currentStep)
        return np.array([x, y])
# Truong hop x_0 = A.
GradientDescentModelA = GradientDescentWithBacktracking(f, getGrad_f, np.array([0, 0]), 1, 0.5, 0.5)
print(GradientDescentModelA.solveWithBacktracking())
# Truong hop x_0 = B.
GradientDescentModelB = GradientDescentWithBacktracking(f, getGrad_f, np.array([-4, 3]), 1, 0.5, 0.5)
print(GradientDescentModelB.solveWithBacktracking())
            