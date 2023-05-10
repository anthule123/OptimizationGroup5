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

#Bài 2
# %%
import numpy as np

def f(x, y):
    return 5*x**2 + y**2

def gradient_f(x, y):
    return np.array([10*x, 2*y])


# %%
x0 = np.array([1, 1])

# %%
class GradientDescentFindMin:
    def __init__(self, f, gradient_f, x0, learning_rate=0.1, epsilon=1e-5, max_iterations=100):
        self.f = f
        self.gradcient_f = gradient_f
        self.x0 = x0
        self.learning_rate = learning_rate
        self.epsilon = epsilon
        self.max_iterations = max_iterations
    
        self.y = f(x0[0], x0[1])
        self.i = 0
        
    
    def solve_fix_step_length(self):
        x = self.x0[0]
        y = self.x0[1]
        for i in range(self.max_iterations):
            current_gradient = self.gradient_f(x, y)
            x -= self.learning_rate * current_gradient[0]
            y -= self.learning_rate * current_gradient[1]
            if np.linalg.norm(current_gradient) < self.epsilon:
                break
        return x, y
    def solve_backtrack_step_length(self, contraction_factor=0.5, alpha=0.5):
        x = self.x0[0]
        y = self.x0[1]
        for i in range(self.max_iterations):
            current_gradient = self.gradient_f(x, y)
            t = self.learning_rate
            if np.linalg.norm(current_gradient) < self.epsilon:
                break
            for j in range(self.max_iterations):
                next_x = x - self.learning_rate * current_gradient[0]
                next_y = y - self.learning_rate * current_gradient[1]
                if self.f(next_x, next_y) > self.f(x, y) - alpha *t* np.linalg.norm(current_gradient)**2 :
                    t = t*contraction_factor
                else:
                    x = next_x
                    y = next_y
                    break
            
        return x, y
    
            

# %%
gradientSolver = GradientDescentFindMin(f=f, gradient_f=gradient_f, x0=x0)
#tính thời gian
import time
start = time.time()
solve_fix_step_length = gradientSolver.solve_fix_step_length()
end = time.time()
print('Thời gian chạy thuật toán fix step length : ', end-start)
print(solve_fix_step_length)    



# %%
gradientSolver = GradientDescentFindMin(f=f, gradient_f=gradient_f, x0=x0)
start = time.time()
solve_backtrack_step_length = gradientSolver.solve_backtrack_step_length()
end = time.time()
print('Thời gian chạy thuật toán backtrack step length : ', end-start)
print(solve_backtrack_step_length)

# %%




#Bài 3
#3.1
import numpy as np
def f(x_1, x_2):
    return (1.5 - x_1 + x_1 * x_2)**2 + (2.25 - x_1 + x_1 * x_2**2)**2 + (2.625 - x_1 + x_1 * x_2**3)**2
def getGrad_f(x_1, x_2):
    partialDerivation_x_1 = 2 * (x_2 - 1) * (x_1 * x_2 - x_1 + 1.5) + 2 * (x_2**2 - 1) * (x_1 * x_2**2 - x_1 + 2.25) + 2 * (x_2**3 - 1) * (x_1 * x_2**3 - x_1 + 2.625)
    partialDerivation_x_2 = 2 * x_1 * (x_1 * x_2 - x_1 + 1.5) + 4 * (x_1 * x_2**2 - x_1 + 2.25) * x_1 * x_2 + 6 * (x_1 * x_2**3 - x_1 + 2.625) * x_1 * x_2**2
    return np.array([partialDerivation_x_1, partialDerivation_x_2])
class GradientDescentWithBacktracking:
    def __init__(self, f, getGrad_f, x_0, alpha, beta,
                 shrinkFactor, epsilon = 10**(-4), maxIteration = 1000):
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
            while (self.f(x - t_Initital * currentGrad_f[0],
                         y - t_Initital * currentGrad_f[1]) > 
            self.f(x, y) - self.beta * t_Initital * 
            np.linalg.norm(currentGrad_f)**2):
                t_Initital = t_Initital * self.shrinkFactor
            # Tinh x_k
            x = x - t_Initital * currentGrad_f[0]
            y = y - t_Initital * currentGrad_f[1]
            currentStep = currentStep + 1
            # Dieu kien dung epsilon.
            if np.linalg.norm(currentGrad_f) <= self.epsilon:
                break
        # print(currentStep)
        print(self.f(x, y))
        return np.array([x, y])
# Truong hop x_0 = A.
GradientDescentModelA = GradientDescentWithBacktracking(f, getGrad_f, np.array([0, 0]), 1, 0.5, 0.5)
print(GradientDescentModelA.solveWithBacktracking())
# Truong hop x_0 = B.
GradientDescentModelB = GradientDescentWithBacktracking(f, getGrad_f, np.array([-4, 3]), 1, 0.5, 0.5)
print(GradientDescentModelB.solveWithBacktracking())

print(getGrad_f(2.5,3))
#3.2
# %%
import numpy as np
import sympy as sp


def beale_function(x, y):
    #f(x_1,x_2) = (1.5 - x_1 + x_1 x_2)^2 + (2.25 - x_1 + x_1 x_2^2)^2 + (2.625 - x_1 + x_1 x_2^3)^2
    return (1.5 - x + x*y)**2 + (2.25 - x + x*y**2)**2 + (2.625 - x + x*y**3)**2

# %%
from sympy import symbols, diff, lambdify
class NiceFunction:
    def __init__(self, f):
        self.f = f
        self.x = sp.Symbol('x')
        self.y = sp.Symbol('y')
        self.f_x = sp.diff(f(self.x,self.y), self.x)
        self.f_x_lamb = sp.lambdify((self.x, self.y), self.f_x, 'numpy')
        self.f_y = sp.diff(f(self.x,self.y), self.y)
        self.f_y_lamb = sp.lambdify((self.x, self.y), self.f_y, 'numpy')
        self.gradient_f_sym = np.array([self.f_x_lamb, self.f_y_lamb])
        self.f_xx = sp.diff(self.f_x, self.x)
        self.f_xx_lamb = sp.lambdify((self.x, self.y), self.f_xx, 'numpy')
        self.f_yy = sp.diff(self.f_y, self.y)
        self.f_yy_lamb = sp.lambdify((self.x, self.y), self.f_yy, 'numpy')
        self.f_xy = sp.diff(self.f_x, self.y)
        self.f_xy_lamb = sp.lambdify((self.x, self.y), self.f_xy, 'numpy')
        self.f_yx = sp.diff(self.f_y, self.x)
        self.f_yx_lamb = sp.lambdify((self.x, self.y), self.f_yx, 'numpy')
        self.hessian_f_lamb = np.array([[self.f_xx_lamb, self.f_xy_lamb],[self.f_yx_lamb, self.f_yy_lamb]])
    def gradient_f(self, val_x, val_y):
        #thay số vào đạo hàm
        ans = np.array([0.0,0.0])
        ans[0] = self.f_x_lamb(val_x, val_y)
        ans[1] = self.f_y_lamb(val_x, val_y)
        return ans

    def hessian_f(self, val_x, val_y):
        ans = np.array([[0.0,0.0],[0.0,0.0]])
        for i in range(2):
            for j in range(2):
                ans[i][j] += self.hessian_f_lamb[i][j](val_x, val_y)
        return ans
                 
        

# %%
niceFunction = NiceFunction(beale_function)
print(niceFunction.f)
print(niceFunction.gradient_f_sym)
print(niceFunction.gradient_f(2.5,3))
#print(niceFunction.hessian_f_sym)


# %%
from sympy import symbols, diff, lambdify

# Define the function f(x)
x = symbols('x')
f = x**2 + 2*x - 1

# Compute the derivative of f(x)
df = diff(f, x)

# Create a lambda function from f(x) and df/dx
f_lam = lambdify(x, f, 'numpy')
df_lam = lambdify(x, df, 'numpy')

# Evaluate the derivative at x = 2
x_val = 2.375
df_val = df_lam(x_val)

print(df_val)


# %%
from sympy import symbols, diff, lambdify
from sympy.abc import x, y

# Define the function f(x, y)
f = x**2 + 2*x*y + y**2

# Compute the partial derivatives of f(x, y)
df_dx = diff(f, x)
df_dy = diff(f, y)

# Create a lambda function from f(x, y), df/dx and df/dy
f_lam = lambdify((x, y), f, 'numpy')
df_dx_lam = lambdify((x, y), df_dx, 'numpy')
df_dy_lam = lambdify((x, y), df_dy, 'numpy')

# Evaluate the partial derivatives at (x, y) = (1, 2)
x_val = 1.7
y_val = 2.898
df_dx_val = df_dx_lam(x_val, y_val)
df_dy_val = df_dy_lam(x_val, y_val)

print(df_dx_val, df_dy_val)


# %%
def trial_function(x,y):
    return (x+y)**2 + y**3 + x*y
nice_trial_function = NiceFunction(trial_function)
print(nice_trial_function.f)
print(nice_trial_function.gradient_f_sym)
print(nice_trial_function.hessian_f_lamb)
#thay số vào hàm trong sympy


# %%
class NewtonFindMin:
    def __init__(self, niceFunction, x0, epsilon=1e-4, max_iterations=1000,
                 alpha = 0.5,
                 shrinking_factor = 0.5,
                 beta = 0.5,):
        self.niceFunction = niceFunction
        self.x0 = x0
        self.epsilon = epsilon
        self.max_iterations = max_iterations
        self.alpha = alpha
        self.shrinking_factor = shrinking_factor
        self.beta = beta
        
    def gradient_descent_backtracking_linesearch(self, contraction_factor=0.5):
        x = self.x0[0]
        y = self.x0[1]
        for i in range(self.max_iterations):
            currentGrad_f = self.niceFunction.gradient_f(x, y)
            # Tinh do dai buoc t_k.
            t_Initital = self.alpha
            while (self.niceFunction. f(x - t_Initital * currentGrad_f[0],
                                       y - t_Initital * currentGrad_f[1])>
                   self.niceFunction.f(x, y) - self.beta * t_Initital * 
                   np.linalg.norm(currentGrad_f)**2):
                t_Initital = t_Initital * contraction_factor
            # Tinh x_k
            x = x - t_Initital * currentGrad_f[0]
            y = y - t_Initital * currentGrad_f[1]

            # Dieu kien dung epsilon.
            if np.linalg.norm(currentGrad_f) <= self.epsilon:
                break
        return x, y
    def newton_backtracking_linesearch(self, contraction_factor=0.5):
        x = self.x0[0]
        y = self.x0[1]
        for i in range(self.max_iterations):
            current_gradient = self.niceFunction.gradient_f(x, y)
            t = self.alpha
            if np.linalg.norm(current_gradient) < self.epsilon:
                break
            current_hess = self.niceFunction.hessian_f(x, y)
            v = -np.linalg.solve(current_hess, current_gradient)
            h= v@current_gradient
            for j in range(self.max_iterations):
                next_x = x + t * v[0]
                next_y = y + t* v[1]
                if (self.niceFunction.f(next_x, next_y) > 
                    self.niceFunction.f(x, y) + self.beta *t* h):
                    t = t*contraction_factor
                else:
                    x = next_x
                    y = next_y
                    break
        return x, y 
        


# %%
nice_beale_function = NiceFunction(beale_function)
A = np.array([0,0])
B = np.array([-4,3])
newtonSolver = NewtonFindMin(nice_beale_function, A)
sol3 = newtonSolver.newton_backtracking_linesearch()
print(sol3)
beale_function(sol3[0], sol3[1])



# %%
newtonSolverB = NewtonFindMin(nice_beale_function, B)
sol4 = newtonSolverB.newton_backtracking_linesearch()
print(sol4)
beale_function(sol4[0], sol4[1])



#Bài 4
# %%
import gurobipy as gp
from gurobipy import GRB
import numpy as np

# %%
class LinearRegression:
    def __init__(self, data):
        self.data = data
        self.n = len(data)
        self.model = gp.Model('Linear Regression')
        #loại liên tục
        self.a = self.model.addVar(
                                  vtype=GRB.CONTINUOUS,
                                   name='a')
        self.b = self.model.addVar(
                                    vtype=GRB.CONTINUOUS,
                                    name='b')
    def setObjective(self):
        self.model.setObjective(
                                gp.quicksum(
                                    (self.data[i][1]-self.a*self.data[i][0]-self.b)**2 
                                    for i in range(self.n)),
                                GRB.MINIMIZE)
    def solve(self):
        self.setObjective()
        self.model.optimize()
        

# %%
#tạo dữ liệu độ dài 10, random quanh đường thẳng y = 2x 
data = [ [i, 2*i + np.random.normal(0, 1)] for i in range(10)]
data = np.array(data)
print(data)

# %%
linearRegression = LinearRegression(data)
linearRegression.solve()
print('a = ', linearRegression.a.x)
print('b = ', linearRegression.b.x)

# %%
#plot dữ liệu
import matplotlib.pyplot as plt
plt.scatter(data[:, 0], data[:, 1])
#x từ min(data[:, 0]) đến max(data[:, 0])
x = np.linspace(min(data[:, 0]), max(data[:, 0]), 100)
y = linearRegression.a.x*x + linearRegression.b.x
plt.plot(x, y, 'r')
plt.show()



