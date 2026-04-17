from behave import given, when, then
from soma import somar
from converter_num import converter_num

@given('que eu tenho dois números: {num1} e {num2}')
def definir_numeros(context, num1, num2):
    context.error = None
    try:
        context.num1 = converter_num(num1)
        context.num2 = converter_num(num2)
    except Exception as e:
         context.error = TypeError(e)

@when('eu os somo')
def somar_numeros(context):
    if context.error is None:
        try:
            context.resultado = somar(context.num1, context.num2)
        except Exception as e:
            context.error = e

@then('o resultado deve ser {resultado_esperado}')
def verificar_resultado(context, resultado_esperado):
    esperado = converter_num(resultado_esperado)
    assert round(context.resultado, 10) == round(esperado, 10)

@then('o sistema deve retornar um erro de tipo')
def verificar_erro(context):
    assert isinstance(context.error, TypeError)