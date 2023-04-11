import time
print(f"Contagem regressiva para fogos de artifícios: ")
for c in range(10, -1, -1):
    print(c)
    time.sleep(1)
print(f"BOOM")