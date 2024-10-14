import json


def load_contracts_from_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        contracts_json = json.load(file)
        return contracts_json['data']


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def convert_to_number(value):
    if isinstance(value, str):
        value = value.replace('.', '').replace(',', '.')
        try:
            return float(value)
        except ValueError:
            return 0
    return value


def insert_by_value(root, node):
    if root is None:
        return node
    
    node_value = convert_to_number(node.data['Valor'])
    root_value = convert_to_number(root.data['Valor'])
    
    if node_value < root_value:
        if root.left is None:
            root.left = node
        else:
            root.left = insert_by_value(root.left, node)
    else:
        if root.right is None:
            root.right = node
        else:
            root.right = insert_by_value(root.right, node)
    
    return root

def create_node(contract):
    return Node(contract)

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(f"Contrato: {root.data['Número']}, Valor: {root.data['Valor']}")
        inorder_traversal(root.right)

def count_nodes(root):
    if root is None:
        return 0
    else:
        return 1 + count_nodes(root.left) + count_nodes(root.right)


def count_contracts_by_secretary(root, secretary):
    if root is None:
        return
    secretary_ = root.data['Secretária']
    if secretary_ in secretary:
        secretary[secretary_] += 1
    else:
        secretary[secretary_] = 1
    count_contracts_by_secretary(root.left, secretary)
    count_contracts_by_secretary(root.right, secretary)


def compare_values_by_modality(root, modality):
    if root is None:
        return
    modality_ = root.data['Modalidade']
    valor = convert_to_number(root.data['Valor'])
    if modality_ in modality:
        modality[modality_].append(valor)
    else:
        modality[modality_] = [valor]
    compare_values_by_modality(root.left, modality)
    compare_values_by_modality(root.right, modality)



def buscar_contratos_com_data_invalida(root):
    if root is None:
        return
    vigencia_inicio = convert_to_date(root.data['Vigência inicio'])
    vigencia_fim = convert_to_date(root.data['Vigência fim'])
    if vigencia_inicio > vigencia_fim:
        print(f"Título: Contrato Nº {root.data['Número']} | Data inválida: Início: {root.data['Vigência inicio']}, Fim: {root.data['Vigência fim']}")
    buscar_contratos_com_data_invalida(root.left)
    buscar_contratos_com_data_invalida(root.right)


def total_value_by_secretary(root, secretary_totals):
    if root is None:
        return
    secretary_ = root.data['Secretária']
    valor = convert_to_number(root.data['Valor'])
    if secretary_ in secretary_totals:
        secretary_totals[secretary_] += valor
    else:
        secretary_totals[secretary_] = valor
    total_value_by_secretary(root.left, secretary_totals)
    total_value_by_secretary(root.right, secretary_totals)


file_path = 'C:/Users/caduc/Documents/analisededados/contratos/contratos.json'
contracts_data = load_contracts_from_json(file_path)

root_value = None

for contract in contracts_data:
    new_node = create_node(contract)
    root_value = insert_by_value(root_value, new_node)

print("\nÁrvore final em ordem:")
inorder_traversal(root_value)


total_nodes = count_nodes(root_value)
print(f"\nTotal de contratos na árvore: {total_nodes}")


# Exemplo de uso
secretary = {}
count_contracts_by_secretary(root_value, secretary)
print(secretary)

secretarybyvalue = {}
total_value_by_secretary(root_value,secretarybyvalue)
print(secretarybyvalue)


modality = {}
compare_values_by_modality(root_value, modality)
for modalidade, valores in modality.items():
    media_valor = sum(valores) / len(valores)
    print(f"\nModalidade: {modalidade} | Média dos valores: R$ {media_valor:.2f}")