
# Licitação Data Analyzer

### Análise de Contratos de Licitação utilizando Python e Estruturas de Dados

Este projeto visa facilitar a **análise** e **manipulação** de contratos de licitação em grandes volumes de dados JSON, utilizando **Python** e **Árvores Binárias**. Ele implementa consultas otimizadas, auditoria automática de contratos e tratamento de dados inconsistentes, proporcionando eficiência e escalabilidade.

## 🎯 Objetivos

- **Otimizar a consulta de contratos** por **valores**, **vigências** e **modalidades**.
- **Lidar com grandes volumes de dados JSON** sem perda de performance, utilizando **árvores binárias**.
- **Implementar auditoria automática** para identificar inconsistências em datas e listar contratos com **aditivos** de acréscimo e prorrogações.

## 🚀 Funcionalidades

- **Consultas otimizadas** por valor e vigência dos contratos.
- **Auditoria automatizada**: Identifica contratos com problemas de data (ex.: vigência de início maior que a de fim).
- **Relatórios em tempo real**: Geração automática de relatórios de contratos próximos ao vencimento, com aditivos ou com valores acima de determinado limite.
- **Tratamento de dados inconsistentes**: Lidando com entradas inválidas no JSON.

## 🛠️ Ferramentas e Tecnologias

- **Python**: Linguagem principal usada para manipulação e análise dos contratos.
- **Árvores Binárias**: Utilizadas para organizar e consultar contratos de forma eficiente.
- **Bibliotecas Nativas**: Uso de `json` para manipulação de dados e `datetime` para tratamento de datas.

## 📊 Resultados

- **Consultas aceleradas**: Relatórios em tempo real, gerando insights sobre contratos com base em valor, vigência e modalidade.
- **Auditoria automatizada**: Deteção automática de problemas em contratos.
- **Escalabilidade**: Capaz de lidar com grandes volumes de contratos, pronto para integração com bases públicas e privadas.

## 🏗️ Estrutura do Projeto

```plaintext
.
├── contratos.json          # Arquivo JSON contendo os dados dos contratos
├── contratos.py            # Script principal para processamento dos contratos
├── README.md               # Documentação do projeto
```

## 📝 Como Usar

1. **Clonar o repositório**:
    ```bash
    git clone https://github.com/seuusuario/licitação-analyzer.git
    ```

2. **Executar o script**:
    Certifique-se de ter o Python 3 instalado e execute o script para iniciar o processamento:
    ```bash
    python contratos.py
    ```

3. **Personalizar**:
    - Modifique o arquivo `contratos.json` para adicionar seus próprios contratos.
    - Ajuste os parâmetros no script para gerar relatórios personalizados.


---

**Licença**: Este projeto está licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
