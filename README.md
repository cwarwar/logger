# Logger

Api em python + mongoDB para gerenciar logs com um formato pré estabelecido 

## Pré requisitos
Ter o docker compose instalado

## Rodando o projeto
Via terminal, acesse o diretório docker dentro do projeto e execute o seguinte comando:
```
docker-compose up
```

## Rodando os testes
Os testes rodam automaticamente assim que o container é instanciado


### Requests
O projeto rodará no seguinte endereço:
http://127.0.0.1:8888

curl -X POST http://127.0.0.1:8888/log/parse -F "file=@/arquivo.txt"

curl http://127.0.0.1:8888/log/parse