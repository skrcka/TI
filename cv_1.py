import matplotlib.pyplot as plt
import numpy as np

# Define the range for n
n = np.linspace(1, 10, 400)
n_int = np.arange(1, 11)

# Define the functions
functions = {
    'a': n,
    'b': n**2,
    'c': n**3,
    'd': np.sqrt(n) * 3 * n,
    'e': n**2 * np.log2(n),
    'f': np.log2(n),
    'g': np.log10(n),
    'h': (np.log2(n))**2,
    'i': 2**n,
    'j': n**n,
    'k': n**(np.log2(n)),
    'l': (np.log2(n))**n,
    'm': 2 * np.sqrt(n),
    'n': 2**n_int,
    'o': 2**(n_int+1),
    'p_even': 2**n_int[n_int % 2 == 0],
    'p_odd': n_int[n_int % 2 == 1]**2
}

colors = plt.cm.viridis(np.linspace(0, 1, len(functions)))

# Create a new figure for the adjusted plot
plt.figure(figsize=(14, 8))

# Functions a to l, m, which are continuous
for (label, func), color in zip(functions.items(), colors):
    if label != 'n' and label != 'o' and label != 'p_even' and label != 'p_odd':
        plt.plot(n, func, label=label, color=color)


# Functions n, o, p which are discrete, with their own distinct colors
plt.scatter(n_int, functions['n'], label='n', color='magenta')
plt.scatter(n_int, functions['o'], label='o', color='cyan')
plt.scatter(n_int[n_int % 2 == 0], functions['p_even'], label='p (n even)', color='yellow')
plt.scatter(n_int[n_int % 2 == 1], functions['p_odd'], label='p (n odd)', color='orange')

# Make the plot readable
plt.yscale('log')
plt.xlabel('n')
plt.ylabel('Function value')
plt.title('Graphs of Various Functions with Distinct Colors')
plt.legend()
plt.grid(True, which="both", ls="--")

# Show the plot
plt.show()