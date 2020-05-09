from vpParcela import valorPresenteParcela, taxaIofDiario, strToDate
from datetime import date, timedelta

def taxaIofDiario(contrato):
    if contrato['tipoPessoa'] == 'PF':
        return 0.000082
    elif contrato['tipoPessoa'] == 'PJ':
        if contrato['simplesNacional'] is True:
            return 0.0000137
        else:
            return 0.000041

def strToDate(dateInString):
    return date(int(dateInString[6:]),int(dateInString[3:5]),int(dateInString[:2]))

def quebraDivida(contrato, strDataDeVisualizacao):
    dataDeVisualizacao = strToDate(strDataDeVisualizacao)
    dataDividaUltimoEvento = strToDate(contrato['dataInicioContrato'])
    valorDividaPrincipal = contrato['valorEmprestado']
    valorDividaJurosRemuneratorios = 0

    transferenciasAteADataDeVisualizacao = []
    for parcela in contrato['parcelas']:
        for transferencia in parcela['transferencias']:
            if strToDate(transferencia['dataTransferencia']) <= dataDeVisualizacao:
                transferenciasAteADataDeVisualizacao.append(transferencia)

    parcelasAteADataDeVisualizacao = []
    for parcela in contrato['parcelas']:
        if strToDate(parcela['dataContratual']) <= dataDeVisualizacao:
            parcelasAteADataDeVisualizacao.append(parcela)

    # Isso daqui eu não consigo fazer agora, mas em algum momento vou precisar
    # sortDaMaisAntigaAMaisRecente(transferenciasAteADataDeVisualizacao)

    for transferencia in transferenciasAteADataDeVisualizacao:
        # Logo antes de considerar a transferencia
        valorDividaJurosRemuneratorios = valorDividaJurosRemuneratorios + (valorDividaPrincipal + valorDividaJurosRemuneratorios)*(pow(1 + contrato['taxaDeJurosRemuneratoriosAoMes'], (strToDate(transferencia['dataTransferencia']) - dataDividaUltimoEvento).days/30) - 1)

        # Logo depois de considerar a transferencia
        valorDividaJurosRemuneratorios = valorDividaJurosRemuneratorios - transferencia['valorTransferenciaJuros'] - transferencia['valorTransferenciaJurosAdicionais']
        valorDividaPrincipal = valorDividaPrincipal - transferencia['valorTransferenciaPrincipal']
        dataDividaUltimoEvento = strToDate(transferencia['dataTransferencia'])

    # Acruando da última transferência à data de visualização
    valorDividaJurosRemuneratorios = valorDividaJurosRemuneratorios + (valorDividaPrincipal + valorDividaJurosRemuneratorios)*(pow(1 + contrato['taxaDeJurosRemuneratoriosAoMes'], (dataDeVisualizacao - dataDividaUltimoEvento).days/30) - 1)

    # Agora temos o valor do principal e dos juros remuneratórios da dívida para a data de visualização.
    # Só falta diferenciar entre "juros remuneratórios regulares" e "juros remuneratórios adicionais" e calcular os outros encargos
    quebrasValoresParcelasPassadasNaDataDeVisualizacao = []
    for parcela in parcelasAteADataDeVisualizacao:
        quebrasValoresParcelasPassadasNaDataDeVisualizacao.append(valorPresenteParcela(contrato, parcela, strDataDeVisualizacao))

    valorDividaIof = 0
    for quebraValorParcela in quebrasValoresParcelasPassadasNaDataDeVisualizacao:
        valorDividaIof = valorDividaIof + quebraValorParcela['valorIofAtraso']

    valorDividaMultaMoratoria = 0
    for quebraValorParcela in quebrasValoresParcelasPassadasNaDataDeVisualizacao:
        valorDividaMultaMoratoria = valorDividaMultaMoratoria + quebraValorParcela['valorMultaMoratoria']

    valorDividaJurosMoratorios = 0
    for quebraValorParcela in quebrasValoresParcelasPassadasNaDataDeVisualizacao:
        valorDividaJurosMoratorios = valorDividaJurosMoratorios + quebraValorParcela['valorJurosMoratorios']

    valorDividaJurosRemuneratoriosAdicionais = 0
    for quebraValorParcela in quebrasValoresParcelasPassadasNaDataDeVisualizacao:
        valorDividaJurosRemuneratoriosAdicionais = valorDividaJurosRemuneratoriosAdicionais + quebraValorParcela['valorJurosRemuneratoriosAdicionais']

    valorDividaTarifa = 0
    for quebraValorParcela in quebrasValoresParcelasPassadasNaDataDeVisualizacao:
        valorDividaTarifa = valorDividaTarifa + quebraValorParcela['valorTarifaASerPaga']

    valorDividaJurosRemuneratoriosRegulares = valorDividaJurosRemuneratorios - valorDividaJurosRemuneratoriosAdicionais
    quebraValorDivida = {'valorDividaPrincipal': valorDividaPrincipal,
                        'valorDividaJurosRemuneratoriosRegulares': valorDividaJurosRemuneratoriosRegulares,
                        'valorDividaJurosRemuneratoriosAdicionais': valorDividaJurosRemuneratoriosAdicionais,
                        'valorDividaJurosMoratorios': valorDividaJurosMoratorios,
                        'valorDividaIof': valorDividaIof,
                        'valorDividaMultaMoratoria': valorDividaMultaMoratoria,
                        'valorDividaTarifa': valorDividaTarifa}

    return quebraValorDivida
