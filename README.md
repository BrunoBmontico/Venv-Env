## -- COMO CONFIGURAR O VENV PARA O FUNCIONAMENTO CORRETO DO PROGRAMA --

1. Crie um ambiente virtual utilizando o comando no console que preferir: python -m venv nome_da_sua_venv.

2. Ative o seu ambiente virtual utilizando o comando:
    - CMD ou POWERSHELL: nome_da_sua_venv\Scripts\activate
    - BASH             : source nome_da_sua_venv/bin/activate              

3. Após ativar sua venv, instale todas as bibliotecas e dependencias exigidas no arquivo requirements.txt utilizando no console o comando: pip install -r requirements.txt

4. Antes de iniciar o programa será necessário definir a variavel de ambiente utilizando os seguintes códigos no console:
    - POWERSHELL: set-item -path "env:DATA_PATH" -value "caminho_do_arquivo\meses_vendas.csv"
    - CMD       : set DATA_PATH "caminho_do_arquivo\meses_vendas.csv"
    - BASH      : export DATA_PATH="caminho_do_arquivo\meses_vendas.csv"

5. Verifique se a variavel de ambiente foi criada com sucesso:
    - POWERSHELL: $env:DATA_PATH
    - CMD       : echo %DATA_PATH%
    - BASH      : echo $DATA_PATH

6. Caso a criação da variavel tenha ocorrido da maneira correta, rode o programa!
