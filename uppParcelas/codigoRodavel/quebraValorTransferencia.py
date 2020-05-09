def quebraTransferencia(contrato, dataTransferencia, valorTransferencia, parcela):
    valorQuebraDividaDataTransferencia = quebraDivida(contrato, dataTransferencia)
    valorQuebraParcelaDataTransferencia = valorPresenteParcela(contrato, parcela, dataTransferencia)

    # Caso a transferência tenha um valor maior do que o valor presente da parcela, retornar um erro
    checarSeATransferenciaÉMaiorQueAParcela

    valorQuebraTransferencia = {}

    # Preenchendo o valor do IOF com base no IOF da parcela
    valorQuebraTransferencia['valorTransferenciaIOFAtraso'] = min(valorTransferencia, valorQuebraParcelaDataTransferencia['valorIofAtraso'])
    valorTransferencia = valorTransferencia - min(valorTransferencia, valorQuebraParcelaDataTransferencia['valorIofAtraso'])

    # Preenchendo o valor dos Juros Remuneratórios Adicionais com base nos Juros Remuneratórios Adicionais da parcela
    valorQuebraTransferencia['valorJurosRemuneratoriosAdicionais'] = min(valorTransferencia, valorQuebraParcelaDataTransferencia['valorJurosRemuneratoriosAdicionais'])
    valorTransferencia = valorTransferencia - min(valorTransferencia, valorQuebraParcelaDataTransferencia['valorJurosRemuneratoriosAdicionais'])

    # Preenchendo o valor dos Juros Moratórios com base nos Juros Moratórios da parcela
    valorQuebraTransferencia['valorJurosMoratorios'] = min(valorTransferencia, valorQuebraParcelaDataTransferencia['valorJurosMoratorios'])
    valorTransferencia = valorTransferencia - min(valorTransferencia, valorQuebraParcelaDataTransferencia['valorJurosMoratorios'])

    # Preenchendo o valor da Multa Moratória com base na Multa Moratória da parcela
    valorQuebraTransferencia['valorMultaMoratoria'] = min(valorTransferencia, valorQuebraParcelaDataTransferencia['valorMultaMoratoria'])
    valorTransferencia = valorTransferencia - min(valorTransferencia, valorQuebraParcelaDataTransferencia['valorMultaMoratoria'])

    # Preenchendo o valor dos Juros Remuneratórios Regulares com base nos Juros Remuneratórios Regulares da dívida na data da parcela
    if dataTransferencia >= parcela.data: # Se a transferÊncia estiver em atraso ou pontual
        valorParcelaJurosRemuneratoriosRegularesNaTransferencia = parcela.valorParcelaJuros
    else: # Se a transferÊncia estiver adiantada
        valorParcelaJurosRemuneratoriosRegularesNaTransferencia = min(valorQuebraDividaDataTransferencia['valorDividaJurosRemuneratoriosRegulares'], valorQuebraParcelaDataTransferencia['valorPresenteParcelaSemTarifa'])

    valorQuebraTransferencia['valorTransferenciaJuros'] = min(valorTransferencia, valorParcelaJurosRemuneratoriosRegularesNaTransferencia)
    valorTransferencia = valorTransferencia - min(valorTransferencia, valorParcelaJurosRemuneratoriosRegularesNaTransferencia)

    # Preenchendo o valor do Principal com base no valor Regulares da dívida na data da parcela
    if dataTransferencia >= parcela.data: # Se a transferÊncia estiver em atraso ou pontual
        valorParcelaPrincipalNaTransferencia = parcela.valorTransferenciaPrincipal
    else: # Se a transferÊncia estiver adiantada
        valorParcelaPrincipalNaTransferencia = valorQuebraParcelaDataTransferencia['valorPresenteParcelaSemTarifa'] - valorParcelaJurosRemuneratoriosRegularesNaTransferencia

    valorQuebraTransferencia['valorTransferenciaPrincipal'] = min(valorTransferencia, valorParcelaPrincipalNaTransferencia)
    valorTransferencia = valorTransferencia - min(valorTransferencia, valorParcelaPrincipalNaTransferencia)

    # Preenchendo o valor da Tarifa com base no valor da Tarifa na data da parcela
    valorQuebraTransferencia['valorTarifaASerPaga'] = min(valorTransferencia, valorQuebraParcelaDataTransferencia['valorTarifaASerPaga'])

    return valorQuebraTransferencia
