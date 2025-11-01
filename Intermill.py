import sys

def can_finish(mills, w, T):
    total = 0.0
    for p, t in mills:
        useful = T - 2.0 * t
        if useful > 0:
            total += p * useful
            if total >= w:   # temprano corta, evita overflow
                return True
    return total >= w

def solve():
    data = sys.stdin.read().strip().split()
    it = iter(data)
    n = int(next(it)); w = float(next(it))
    mills = []
    min_time_single = None
    for _ in range(n):
        p = float(next(it)); t = float(next(it))
        mills.append((p, t))
        candidate = 2.0 * t + (w / p)
        if min_time_single is None or candidate < min_time_single:
            min_time_single = candidate

    # Cota superior segura: enviar todo el trigo al mejor molino individual
    lo = 0.0
    hi = min_time_single

    for _ in range(100):  # suficiente para 1e-9
        mid = (lo + hi) / 2.0
        if can_finish(mills, w, mid):
            hi = mid
        else:
            lo = mid

    print(f"{hi:.7f}")

if __name__ == "__main__":
    solve()
