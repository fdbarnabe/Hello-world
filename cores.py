colorbold = {'red':'\033[1;31m',
    'green':'\033[1;32m',
    'yellow':'\033[1;33m',
    'blue':'\033[1;34m',
    'purple':'\033[1;35m',
    'cyan':'\033[1;36m',
    'gray':'\033[1;37m',
    'clean':'\033[m'}
colorunder = {'red':'\033[4;31m',
    'green':'\033[4;32m',
    'yellow':'\033[4;33m',
    'blue':'\033[4;34m',
    'purple':'\033[4;35m',
    'cyan':'\033[4;36m',
    'gray':'\033[4;37m'}
print(f"{colorbold['cyan']}Hello World{colorbold['clean']}.")
print(f"{colorunder['red']}Hello World.\033[m")
print(f"Hello World")