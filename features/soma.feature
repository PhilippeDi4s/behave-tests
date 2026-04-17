# language: pt
Funcionalidade: Somar dois números

  Cenário: Soma de dois números inteiros positivos
    Dado que eu tenho dois números: 10 e 20
    Quando eu os somo
    Então o resultado deve ser 30

  Cenário: Soma de dois números inteiros negativos
    Dado que eu tenho dois números: -5 e -15
    Quando eu os somo
    Então o resultado deve ser -20

  Cenário: Soma de um número positivo com um negativo
    Dado que eu tenho dois números: 10 e -3
    Quando eu os somo
    Então o resultado deve ser 7

  Cenário: Soma com o elemento neutro (zero)
    Dado que eu tenho dois números: 0 e 50
    Quando eu os somo
    Então o resultado deve ser 50

  Cenário: Soma de dois números decimais (float)
    Dado que eu tenho dois números: 1.5 e 2.5
    Quando eu os somo
    Então o resultado deve ser 4.0

  Cenário: Soma de números com muitas casas decimais
    Dado que eu tenho dois números: 0.1 e 0.2
    Quando eu os somo
    Então o resultado deve ser 0.3

  Cenário: Soma de números extremamente grandes (Big Int)
    Dado que eu tenho dois números: 1000000000000 e 1000000000000
    Quando eu os somo
    Então o resultado deve ser 2000000000000

  Cenário: Validar erro ao somar número com string
    Dado que eu tenho dois números: 10 e "5"
    Quando eu os somo
    Então o sistema deve retornar um erro de tipo TypeError

  Cenário: Validar erro ao somar valores nulos (None)
    Dado que eu tenho dois números: None e 10
    Quando eu os somo
    Então o sistema deve retornar um erro de tipo ValueError

  Cenário: Soma de dois zeros
    Dado que eu tenho dois números: 0 e 0
    Quando eu os somo
    Então o resultado deve ser 0