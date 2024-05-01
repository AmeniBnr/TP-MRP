from functools import lru_cache

def fibo_iter(n):
  """this is a pure iterartive version of Fibonacci series. Complexity is O(n)."""
  a,b=1,1
  for _ in range(n-1):
    a,b=a+b,a
  return a

def fib_rec(n):
  """this is recursion based version of Fibonacci series. Complexity is terrible (exponential)"""
  return 1 if n<=1 else fib_rec(n-1)+fib_rec(n-2)

@lru_cache
def fib_rec2(n):
  """this is recursion based version of Fibonacci series. Complexity is now linear since each
  result is computed once.
  """
  return 1 if n<=1 else fib_rec2(n-1)+fib_rec2(n-2)

def fib_dynamic(n):
  """this is recursive version of Fibonacci series which explicitly uses dynamic programming."""
  def fib_dynamic_rec(v):
    nonlocal vals
    if v<=1:return 1
    elif vals[v]==0:
        vals[v]=fib_dynamic_rec(v-1)+fib_dynamic_rec(v-2)
    return vals[v]

  if n<=1:return 1
  vals=[0]*(n+1)
  fib_dynamic_rec(n)
  return vals[-1]
