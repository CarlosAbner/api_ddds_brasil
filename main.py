import requests

def linhas():
    print('*------------------------------------------------------------*')

print('*------------------------------------------------------------*')
print('   # digite um ddd para saber o nome do UF e suas cidades #')
print('*------------------------------------------------------------*')

class DDD:
    def ddd_uf(self, n):
        try:
            r = requests.get(f'https://brasilapi.com.br/api/ddd/v1/{str(n)}')
            r_requests = r.json()
            uf = r_requests['state']
            return f'O estado retorado foi {uf} \n'
        except:
            print('Números entre 11 e 98')


    def ddd_cidades(self, n):
        try:
            requi = requests.get(f'https://brasilapi.com.br/api/ddd/v1/{str(n)}')
            requi_json = requi.json()
            return f"e as cidades foram: \n{','.join(requi_json['cities'])} \nTotal de {len(requi_json['cities'])} cidade"
        except:
            print('Números entre 11 e 98')

objeto_r = DDD()

n = int(input('digite o ddd: '))
linhas()

print(objeto_r.ddd_uf(n))
print(objeto_r.ddd_cidades(n))
