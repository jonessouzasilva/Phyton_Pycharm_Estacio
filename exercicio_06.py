def conta_numeros(n):
 if n == 0: return 1 # 0 é par
 elif n%2 == 0: return 1 + conta_numeros(n-1)
 else: return conta_numeros(n-1)