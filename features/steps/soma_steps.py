from behave import given, when, then
from soma import somar

@given('que eu tenho dois números: {num1} e {num2}')
def definir_numeros(context, num1, num2):
    context.num1 = int(num1)
    context.num2 = int(num2)

@when('eu os somo')
def somar_numeros(context):
    context.resultado = somar(context.num1, context.num2)

@then('o resutado deve ser {resultado_esperado}')
def verificar_resultado(context, resultado_esperado):
    assert context.resultado == int(resultado_esperado)