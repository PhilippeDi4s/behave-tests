from behave import given, when, then
from soma import somar

@given('que eu tenho dois números: {num1} e {num2}')
def definir_numeros(context, num1, num2):
    context.num1 = int(num1)
    context.num2 = int(num2)

@when('eu os somo')
def somar_numeros(context):
    try:
        context.resultado = somar(context.num1, context.num2)
    except Exception as e:
        context.error = TypeError(e)

@then('o resutado deve ser {resultado_esperado}')
def verificar_resultado(context, resultado_esperado):
    assert context.resultado == int(resultado_esperado)

@then('o sistema deve retornar um erro de tipo')
def verificar_erro(context):
    assert isinstance(context.error, TypeError)