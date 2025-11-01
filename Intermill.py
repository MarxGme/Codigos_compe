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
    max_t = 0
    min_p = None
    for _ in range(n):
        p = float(next(it)); t = float(next(it))
        mills.append((p, t))
        if t > max_t: max_t = t
        if min_p is None or p < min_p: min_p = p

    # Cota superior segura: todo el viaje más el tiempo si solo usáramos el molino más lento
    lo = 0.0
    hi = 2.0 * max_t + (w / min_p) + 1.0  # margen

    for _ in range(100):  # suficiente para 1e-9
        mid = (lo + hi) / 2.0
        if can_finish(mills, w, mid):
            hi = mid
        else:
            lo = mid

    print(f"{hi:.7f}")

if __name__ == "__main__":
    solve()
