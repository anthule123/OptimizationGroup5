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
            v = np.linalg.solve(current_hess, current_gradient)
            for j in range(self.max_iterations):
                next_x = x - t * v[0]
                next_y = y - t* v[1]
                if (self.niceFunction.f(next_x, next_y) > 
                    self.niceFunction.f(x, y) + self.beta *t* 
                    current_gradient @ v ):
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
sol1 = newtonSolver.gradient_descent_backtracking_linesearch()
print(sol1)
beale_function(sol1[0], sol1[1])


# %%
newtonSolverB = NewtonFindMin(nice_beale_function, B)
sol2 = newtonSolverB.gradient_descent_backtracking_linesearch()
print(sol2)
beale_function(sol2[0], sol2[1])


# %%
sol3 = newtonSolver.newton_backtracking_linesearch()
print(sol3)
beale_function(sol1[0], sol1[1])



# %%
sol4 = newtonSolverB.newton_backtracking_linesearch()
print(sol4)
beale_function(sol2[0], sol2[1])


