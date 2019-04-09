# Star wars planets

Api em python + mongoDB com intuito de gerenciar os planetas do universo de star wars 

## Pré requisitos
Ter o docker compose instalado

## Rodando o projeto
Via terminal, acesse o diretór 'docker' dentro do projeto e execute o seguinte comando:
```
docker-compose up
```

## Rodando os testes
Os testes rodam automaticamente assim que o container é instanciado


### Requests
O projeto rodará no seguinte endereço:
http://127.0.0.1:8888


/planets/getById/5af73ae1d6611a1e3c401a85D [GET]

/planets/getByName/teste7 [GET]

/planets/remove/5aeed967d6611a04e8371bfc [GET] || [DELETE]

/planets/getAll/0/7 [GET]

/planets/store [POST]
Body
name: xxxx
weather: xxxx
terrain: xxx