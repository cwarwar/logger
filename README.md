# Logger

Api em python + mongoDB para gerenciar logs com um formato pré estabelecido 

## Pré requisitos
Ter o docker compose instalado

## Rodando o projeto
Via terminal, acesse o diretório docker dentro do projeto e execute o seguinte comando:
```
docker-compose up
```

Para fazer o deploy utilize o diretório docker-prod para criação dos containers

## Rodando os testes
Os testes rodam automaticamente assim que o container é instanciado em modo de produção.
Caso queira executar os testes manualmente é só acessar o diretório '_tests' e digitar 'python {nomeDoArquivo.py}' 


### Requests
O projeto rodará no seguinte endereço:
http://127.0.0.1:8888

Esse endereço também fornece a listagem dos serviços, métodos, parâmetros e respostas.