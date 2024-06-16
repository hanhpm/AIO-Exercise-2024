def md_nre(y: float, y_hat: float, n: int, p: int) -> float:
    root_y = y ** (1/n)
    root_y_hat = y_hat ** (1/n)
    difference = root_y - root_y_hat

    loss = abs(difference) ** p

    return loss

print(md_nre(y=100, y_hat=99.5, n=2, p=1))
print(md_nre(y=50, y_hat=49.5, n=2, p=1))
print(md_nre(y=20, y_hat=19.5, n=2, p=1))
print(md_nre(y=0.6, y_hat=0.1, n=2, p=1))
