import numpy as np
import matplotlib.pyplot as plt

def center_of_gravity(x):
    '''
    Find the center of gravity of a vector, x.
    If x=[x0,x1,...,xn], then you should return
    c = ( 0*x0 + 1*x1 + 2*x2 + ... + n*xn ) / sum(x)
    where n = len(x)-1.
    
    Recommended method: use np.arange, np.dot, and np.sum.
    
    @param:
    x (array): a 1d numpy array
    
    @result:
    c (scalar): x's center of gravity
    '''
    n = len(x) - 1
    indices = np.arange(n + 1)
    c = np.dot(indices, x) / np.sum(x)
    return c

def matched_identity(x):
    '''
    Create an identity matrix that has the same number of rows as x has elements.
    Hint: use len(x), and use np.eye.
    
    @param:
    x (array): a 1d numpy array, of length N
    
    @result:
    I (array): a 2d numpy array: an NxN identity matrix
    '''
    N = len(x)
    I = np.eye(N)
    return I

def sine_and_cosine(t_start, t_end, t_steps):
    '''
    Create a time axis, and compute its cosine and sine.
    Hint: use np.linspace, np.cos, and np.sin
    
    @param:
    t_start (scalar): the starting time
    t_end (scalar): the ending time
    t_steps (scalar): length of t, x, and y
    
    @result:
    t (array of length t_steps): time axis, t_start through t_end inclusive
    x (array of length t_steps): cos(t)
    y (array of length t_steps): sin(t)
    '''
    t = np.linspace(t_start, t_end, t_steps)
    x = np.cos(t)
    y = np.sin(t)
    return t, x, y

# Grading block
if __name__ == "__main__":
    import importlib
    importlib.reload(homework5)
    
    # Test center_of_gravity
    x = [1, 2, 3, 2, 1]
    print('Center of Gravity:', homework5.center_of_gravity(x))  # Expected output: 2.0
    
    # Test matched_identity
    identity_matrix = homework5.matched_identity(x)
    print('Matched Identity Matrix:')
    print(identity_matrix)
    
    # Test sine_and_cosine
    theta, cos, sin = homework5.sine_and_cosine(0, np.pi, 20)
    
    f = plt.figure(figsize=(14, 4))
    s = f.subplots(1, 1)
    s.stem(theta, cos, 'r')
    s.stem(theta, sin, 'b')
    s.set_title('Sine and Cosine: Stem Plot', fontsize=24)
    s.set_xlabel('Theta (in radians)', fontsize=18)
    s.set_ylabel('sin(theta) and cos(theta)', fontsize=18)
    s.legend(['cosine', 'sine'], fontsize=18)
    
    plt.show()
