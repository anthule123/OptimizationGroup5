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



