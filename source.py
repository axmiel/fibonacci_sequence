fib_seq = [0,1]
#expected input is positive integers
stop_loop = int(input("how many numbers frob fibonacci sequence should I generate: " ))

if stop_loop == 0:
    print("There are no numbers in the sequence")
elif stop_loop == 1:
    print(fib_seq[0])
else:
    for i in range(stop_loop-2):
        next_number = (fib_seq[i] + fib_seq[i + 1])
        fib_seq.append(next_number)
        print(next_number)
