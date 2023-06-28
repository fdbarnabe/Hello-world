import requests

a = input(f"qual o seu nome de usuário: ")

req = requests.get(f"https://api.github.com/users/{a}")

if (req.status_code == 200):
    print("sucesso")
    user = req.json()
    print(user["name"])
    file = open("user.json", "w")
    file.write(req.text)
    
else:
    print(req.status_code)
    print("deu ruim")
