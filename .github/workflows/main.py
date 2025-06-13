from fastapi import FastAPI
import time

app = FastAPI()

def fib(n: int):
    return n if n <= 1 else fib(n-1) + fib(n-2)

@app.get("/fib/{n}")
def get_fib(n: int):
    start = time.time()
    result = fib(n)
    return {
        "input": n,
        "result": result,
        "time_sec": round(time.time() - start, 2)
    }
