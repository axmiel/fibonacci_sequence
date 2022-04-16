fib_seq = [0,1]

stop_loop = int(input("how many numbers frob fibonacci sequence should I generate" ))
for i in range(stop_loop-2):
    fib_seq.append(fib_seq[i] + fib_seq[i + 1])
print(fib_seq)
