def quebraDivida(contrato, dataDeVisualizacao):
    dataDividaUltimoEvento = contrato.dataInicio
    valorDividaPrincipal = contrato.valorEmprestado
    valorDividaJurosRemuneratorios = 0

    transferenciasAteADataDeVisualizacao = []
    for parcela in contrato.parcelas[]:
        for transferencia in parcela.transferencia:
            if transferencia.data <= dataDeVisualizacao:
                transferenciasAteADataDeVisualizacao.append(transferencia)

    parcelasAteADataDeVisualizacao = []
    for parcela in contrato.parcelas[]:
        if parcela.data <= dataDeVisualizacao:
            parcela.append(parcela)

    sortDaMaisAntigaAMaisRecente(transferenciasAteADataDeVisualizacao)

    for transferencia in transferenciasAteADataDeVisualizacao:
        # Logo antes de considerar a transferencia
        valorDividaJurosRemuneratorios = valorDividaJurosRemuneratorios + (valorDividaPrincipal + valorDividaJurosRemuneratorios)*((1 + contrato.taxaDeJurosRemuneratoriosAoMes)^((transferencia.data-dataDividaUltimoEvento)/30) - 1)

        # Logo depois de considerar a transferencia
        valorDividaJurosRemuneratorios = valorDividaJurosRemuneratorios - transferencia.valorTransferenciaJuros - transferencia.valorTransferenciaJurosAdicionais
        valorDividaPrincipal = valorDividaPrincipal - transferencia.valorTransferenciaPrincipal
        dataDividaUltimoEvento = transferencia.data

    # Acruando da última transferência à data de visualização
    valorDividaJurosRemuneratorios = valorDividaJurosRemuneratorios + (valorDividaPrincipal + valorDividaJurosRemuneratorios)*((1 + contrato.taxaDeJurosRemuneratoriosAoMes)^((dataDeVisualizacao-dataDividaUltimoEvento)/30) - 1)

    # Agora temos o valor do principal e dos juros remuneratórios da dívida para a data de visualização.
    # Só falta diferenciar entre "juros remuneratórios regulares" e "juros remuneratórios adicionais" e calcular os outros encargos
    quebrasValoresParcelasPassadasNaDataDeVisualizacao = []
    for parcela in parcelasAteADataDeVisualizacao:
        quebrasValoresParcelasPassadasNaDataDeVisualizacao.append(valorPresenteParcela(contrato, parcela, dataDeVisualizacao))

    valorDividaIof = 0
    for quebraValorParcela in quebrasValoresParcelasPassadasNaDataDeVisualizacao:
        valorDividaIof = valorDividaIof + quebraValorParcela.valorIof

    valorDividaMultaMoratoria = 0
    for quebraValorParcela in quebrasValoresParcelasPassadasNaDataDeVisualizacao:
        valorDividaMultaMoratoria = valorDividaMultaMoratoria + quebraValorParcela.valorMultaMoratoria

    valorDividaJurosMoratorios = 0
    for quebraValorParcela in quebrasValoresParcelasPassadasNaDataDeVisualizacao:
        valorDividaJurosMoratorios = valorDividaJurosMoratorios + quebraValorParcela.valorJurosMoratorios

    valorDividaJurosRemuneratoriosAdicionais = 0
    for quebraValorParcela in quebrasValoresParcelasPassadasNaDataDeVisualizacao:
        valorDividaJurosRemuneratoriosAdicionais = valorDividaJurosRemuneratoriosAdicionais + quebraValorParcela.valorJurosRemuneratoriosAdicionais

    valorDividaTarifa = 0
    for quebraValorParcela in quebrasValoresParcelasPassadasNaDataDeVisualizacao:
        valorDividaTarifa = valorDividaTarifa + quebraValorParcela.valorTarifa

    valorDividaJurosRemuneratoriosRegulares = valorDividaJurosRemuneratorios - valorDividaJurosRemuneratoriosAdicionais
    quebraValorDivida = {'valorDividaPrincipal': valorDividaPrincipal,
                        'valorDividaJurosRemuneratoriosRegulares': valorDividaJurosRemuneratoriosRegulares,
                        'valorDividaJurosRemuneratoriosAdicionais': valorDividaJurosRemuneratoriosAdicionais,
                        'valorDividaJurosMoratorios': valorJurosMoratorios,
                        'valorDividaIof': valorDividaIof,
                        'valorDividaMultaMoratoria': valorDividaMultaMoratoria,
                        'valorDividaTarifa': valorDividaTarifa}

    return quebraValorDivida
