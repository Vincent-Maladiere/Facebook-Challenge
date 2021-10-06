# Write any import statements here

def getUniformIntegerCountInInterval(A: int, B: int) -> int:

    # Write your code here
    total_uniform = 0
    all_uniforms = [int(str(jdx)*idx) for idx in range(1, 13) for jdx in range(1, 10)]
    for n in all_uniforms:
        if A <= n and n <= B:
            total_uniform += 1
    
    return total_uniform

def _getUniformIntegerCountInInterval(A: int, B: int) -> int:

    total_uniform = 0
    for n in range(A, B+1):
        total_uniform += 1
        n_digits = len(str(n))
        if n % int("1"*n_digits) == 0:
            total_uniform += 1
    
    return total_uniform