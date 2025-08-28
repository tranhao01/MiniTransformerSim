import matplotlib.pyplot as plt

# Generate Fibonacci sequence first 10 numbers
fib = [0, 1]
for _ in range(8):
    fib.append(fib[-1] + fib[-2])

plt.figure()
plt.plot(range(len(fib)), fib)
plt.xlabel('Index')
plt.ylabel('Fibonacci Number')
plt.title('Fibonacci Sequence (first 10 numbers)')
plt.grid(True)
plt.savefig('fibonacci_chart.png')
