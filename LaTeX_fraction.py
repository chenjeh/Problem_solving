# 2025/11/16
# https://quera.org/problemset/148639?tab=description

def frac(state:int, val:int=1) -> str :
    if state == 1 :
        return val
    else :
        return str(val) + "+" + "\\frac{" + f"{frac(state-1, 2*val)}" + "}{" + f"{frac(state-1, 2*val+1)}" + "}"

x = int(input())
print(frac(x))