import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# App configuration
st.set_page_config(page_title="Math Concept Visualizer", layout="centered")

# Title and intro
st.title("📐 Mathematics Concept Visualizer")
st.write("Interactive plots to help understand core math topics visually.")

# Sidebar for topic selection
topic = st.sidebar.selectbox(
    "Choose a Topic", 
    ["Algebra - Linear Graph", "Calculus - Derivative", "Trigonometry - Sine Wave"]
)

# Algebra Visualization: Linear Graph
if topic == "Algebra - Linear Graph":
    st.subheader("Linear Function: y = mx + b")
    m = st.slider("Choose slope (m)", -10, 10, 1)
    b = st.slider("Choose y-intercept (b)", -10, 10, 0)

    x = np.linspace(-10, 10, 400)
    y = m * x + b

    fig, ax = plt.subplots()
    ax.plot(x, y, label=f"y = {m}x + {b}")
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.grid(True)
    ax.legend()
    st.pyplot(fig)

# Calculus Visualization: Derivative
elif topic == "Calculus - Derivative":
    st.subheader("Function and its Derivative")
    func_input = st.text_input("Enter a function f(x):", "x**2")

    x = sp.Symbol('x')
    try:
        f = sp.sympify(func_input)
        f_prime = sp.diff(f, x)

        f_lambdified = sp.lambdify(x, f, modules='numpy')
        f_prime_lambdified = sp.lambdify(x, f_prime, modules='numpy')

        x_vals = np.linspace(-10, 10, 400)
        y_vals = f_lambdified(x_vals)
        y_prime_vals = f_prime_lambdified(x_vals)

        fig, ax = plt.subplots()
        ax.plot(x_vals, y_vals, label=f"f(x) = {func_input}")
        ax.plot(x_vals, y_prime_vals, label=f"f'(x) = {sp.simplify(f_prime)}", linestyle='--')
        ax.axhline(0, color='black', linewidth=0.5)
        ax.axvline(0, color='black', linewidth=0.5)
        ax.grid(True)
        ax.legend()
        st.pyplot(fig)
    except:
        st.error("Invalid function! Please enter a valid mathematical expression using x.")

# Trigonometry Visualization: Sine Wave
elif topic == "Trigonometry - Sine Wave":
    st.subheader("Sine Wave: y = A sin(Bx)")
    A = st.slider("Amplitude (A)", 1, 10, 1)
    B = st.slider("Frequency (B)", 1, 10, 1)

    x = np.linspace(0, 4 * np.pi, 400)
    y = A * np.sin(B * x)

    fig, ax = plt.subplots()
    ax.plot(x, y, label=f"y = {A} sin({B}x)")
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.grid(True)
    ax.legend()
    st.pyplot(fig)
