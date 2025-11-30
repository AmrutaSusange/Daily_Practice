def fact_loop(n):
    result = 1
    for i in range(2, n+1):
        result = result*i
    return result

def fact(num):
    if num ==0 or num == 1:
        return 1
    return num * fact(num-1)

if __name__ == "__main__":
    print(fact(5))
    print(fact_loop(5))

