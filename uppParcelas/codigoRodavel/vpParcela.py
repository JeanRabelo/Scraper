def valorPresenteParcela(contrato, parcela, dataDeVisualizacao):
    resposta = {}
    valorParcelaAoInvestidorNoVencimentoASerPaga = parcela.valorParcela - parcela.valorParcelaTarifa
    valorTarifaASerPaga = parcela.valorParcelaTarifa

    valorMultaMoratoria = Null
    valorJurosMoratorios = 0
    valorIofAtraso = 0
    valorJurosRemuneratoriosAdicionais = 0
    dataUltimaTransferenciaParcela = parcela.data

    # Convencionou-se que vamos cobrar a multa moratória somente em cima do valor em aberto no dia do vencimento
    ehAPrimeiraTransferenciaEmAtraso = True
    sortDaMaisAntigaAMaisRecente(parcela.transferencias[])
    for Transferencia in parcela.transferencias[]: # Vamos passar por todas as transferências já realizadas para pagar essa parcela a fim de descobrir seu estado antes de calcular o valor dela
        if Transferencia.dataTransferencia <= dataDeVisualizacao:
            if Transferencia.dataTransferencia <= parcela.data: # pagamento adiantado
                fatorJurosTransferencia = (1 + contrato.taxaDeJurosRemuneratoriosAoMes)^((parcela.data - Transferencia.dataTransferencia) / 30)
                # O valor aux é o valor em aberto decrementado de todos os valores pagos adiantadamente a valor futuro, para podermos ter como referência a mesma base temporal, que é a data contratual do pagamento.
                valorAtualParcelaAoInvestidor = valorParcelaAoInvestidorNoVencimentoASerPaga/fatorJurosTransferencia
                valorTransferenciaAoInvestidor = min(Transferencia.valorTransferencia, valorAtualParcelaAoInvestidor)
                valorTransferenciaQuePagaTarifa = Transferencia.valorTransferencia - valorTransferenciaAoInvestidor

                valorAtualParcelaAoInvestidor = valorAtualParcelaAoInvestidor - valorTransferenciaAoInvestidor
                valorParcelaAoInvestidorNoVencimentoASerPaga = valorAtualParcelaAoInvestidor * fatorJurosTransferencia
                valorTarifaASerPaga = valorTarifaASerPaga - valorTransferenciaQuePagaTarifa
            elif Transferencia.dataTransferencia > parcela.data: # pagamento atrasado
                if ehAPrimeiraTransferenciaEmAtraso:
                    ehAPrimeiraTransferenciaEmAtraso = False
                    diasDesdeVencimento = Transferencia.dataTransferencia - parcela.data
                    valorMultaMoratoria = contrato.multaMoratoriaPercentual * valorParcelaAoInvestidorNoVencimentoASerPaga
        			valorJurosMoratorios = contrato.taxaDeJurosMoratoriosAoMes * valorParcelaAoInvestidorNoVencimentoASerPaga * diasDesdeVencimento / 30
                    valorIofAtraso = taxaIofDiario(contrato) * valorParcelaAoInvestidorNoVencimentoASerPaga * (max(min(contrato.inicio + 365 - parcela.data, diasDesdeVencimento), 0)) / 30
                    valorJurosRemuneratoriosAdicionais = valorParcelaAoInvestidorNoVencimentoASerPaga * ((1 + contrato.taxaDeJurosRemuneratoriosAoMes)^(diasDesdeVencimento / 30) - 1)
                else:
                    diasDesdeUltimaTransferencia = Transferencia.dataTransferencia - dataUltimaTransferenciaParcela
        			valorJurosMoratorios = valorJurosMoratorios + contrato.taxaDeJurosMoratoriosAoMes * valorParcelaAoInvestidorNoVencimentoASerPaga * diasDesdeUltimaTransferencia / 30
                    valorIofAtraso = valorIofAtraso + taxaIofDiario(contrato) * valorParcelaAoInvestidorNoVencimentoASerPaga * (max(min(contrato.inicio+365-dataUltimaTransferenciaParcela, diasDesdeUltimaTransferencia), 0)) / 30
                    valorJurosRemuneratoriosAdicionais = valorJurosRemuneratoriosAdicionais + (valorParcelaAoInvestidorNoVencimentoASerPaga + valorJurosRemuneratoriosAdicionais) * ((1 + contrato.taxaDeJurosRemuneratoriosAoMes)^(diasDesdeUltimaTransferencia / 30) - 1)

                valorAtualParcelaAoInvestidor = valorParcelaAoInvestidorNoVencimentoASerPaga + valorMultaMoratoria + valorJurosMoratorios + valorJurosRemuneratoriosAdicionais + valorIofAtraso
                valorTransferenciaAoInvestidor = min(Transferencia.valorTransferencia, valorAtualParcelaAoInvestidor)
                valorTransferenciaQuePagaTarifa = Transferencia.valorTransferencia - valorTransferenciaAoInvestidor

                valorTransferenciaAoInvestidorRestante = valorTransferenciaAoInvestidor

                Descontando a transferência ao investidor
                # A ORDEM DA ARRAY IMPORTA
                # Motivo da ordenação valorIofAtraso, valorJurosRemuneratoriosAdicionais, valorJurosMoratorios, valorMultaMoratoria:
                # 1-valorIofAtraso: Governo
                # 2-valorJurosRemuneratoriosAdicionais: para não acumular nos juros compostos do dia posterior. É a melhor opção para o tomador.
                # 3 e 4-valorJurosMoratorios, valorMultaMoratoria: a ordem importa pouco nesses 2.
                for divisao in [valorIofAtraso, valorJurosRemuneratoriosAdicionais, valorJurosMoratorios, valorMultaMoratoria]:
                    divisao = divisao - min(valorTransferenciaAoInvestidorRestante, divisao)
                    valorTransferenciaAoInvestidorRestante = valorTransferenciaAoInvestidorRestante - min(valorTransferenciaAoInvestidorRestante, divisao)

                valorDevidoAoInvestidorNaDataDeTransferencia = valorParcelaAoInvestidorNoVencimentoASerPaga + valorJurosRemuneratoriosAdicionais + valorJurosMoratorios + valorMultaMoratoria + valorIofAtraso
                valorParcelaAoInvestidorNoVencimentoASerPaga = valorParcelaAoInvestidorNoVencimentoASerPaga * (1 - (valorTransferenciaAoInvestidor/valorDevidoAoInvestidorNaDataDeTransferencia))
                valorTarifaASerPaga = valorTarifaASerPaga - valorTransferenciaQuePagaTarifa

                dataUltimaTransferenciaParcela = Transferencia.dataTransferencia

    if valorParcelaAoInvestidorNoVencimentoASerPaga + valorTarifaASerPaga < 0.01:
        resposta['valorPresenteParcelaComTarifa'] = 0
        resposta['valorPresenteParcelaSemTarifa'] = 0
        resposta['valorIofAtraso'] = 0
        resposta['valorJurosMoratorios'] = 0
        resposta['valorJurosRemuneratoriosAdicionais'] = 0
        resposta['valorMultaMoratoria'] = 0
        resposta['valorTarifaASerPaga'] = 0

    elif dataDeVisualizacao <= parcela.data: # parcela adiantada
        resposta['valorPresenteParcelaComTarifa'] = valorParcelaAoInvestidorNoVencimentoASerPaga/(1 + contrato.taxaDeJurosRemuneratoriosAoMes)^((parcela.data-dataDeVisualizacao) / 30) + valorTarifaASerPaga
        resposta['valorPresenteParcelaSemTarifa'] = valorParcelaAoInvestidorNoVencimentoASerPaga/(1 + contrato.taxaDeJurosRemuneratoriosAoMes)^((parcela.data-dataDeVisualizacao) / 30)
        resposta['valorIofAtraso'] = 0
        resposta['valorJurosMoratorios'] = 0
        resposta['valorJurosRemuneratoriosAdicionais'] = 0
        resposta['valorMultaMoratoria'] = 0
        resposta['valorTarifaASerPaga'] = valorTarifaASerPaga

    elif dataDeVisualizacao > parcela.data: # parcela em atraso
        if valorMultaMoratoria = Null:
            valorMultaMoratoria = contrato.multaMoratoriaPercentual * valorParcelaAoInvestidorNoVencimentoASerPaga

        # Os juros moratórios crescem de maneira simples e não composta
		valorJurosMoratorios = valorJurosMoratorios + contrato.taxaDeJurosMoratoriosAoMes * valorParcelaAoInvestidorNoVencimentoASerPaga * (dataDeVisualizacao - dataUltimaTransferenciaParcela) / 30
        valorIofAtraso = valorIofAtraso + taxaIofDiario(contrato) * valorParcelaAoInvestidorNoVencimentoASerPaga * (max(min(contrato.inicio + 365 - dataUltimaTransferenciaParcela, dataDeVisualizacao - dataUltimaTransferenciaParcela), 0)) / 30
        # Não há incidência de Juros Remuneratórios adicionais sobre o valor da tarifa cobrada pela up.p na parcela
        valorJurosRemuneratoriosAdicionais = valorJurosRemuneratoriosAdicionais + (valorParcelaAoInvestidorNoVencimentoASerPaga + valorJurosRemuneratoriosAdicionais) * ((1 + contrato.taxaDeJurosRemuneratoriosAoMes)^((dataDeVisualizacao - dataUltimaTransferenciaParcela) / 30) - 1)
        # É muito difícl extrair dessa função o valor de principal e juros remuneratórios regulares da parcela
        resposta['valorPresenteParcelaComTarifa'] = valorParcelaAoInvestidorNoVencimentoASerPaga + valorTarifaASerPaga + valorJurosRemuneratoriosAdicionais + valorMultaMoratoria + valorJurosMoratorios + valorIofAtraso
        resposta['valorPresenteParcelaSemTarifa'] = valorParcelaAoInvestidorNoVencimentoASerPaga + valorJurosRemuneratoriosAdicionais + valorMultaMoratoria + valorJurosMoratorios + valorIofAtraso
        # resposta['valorParcelaAoInvestidorNoVencimentoASerPaga'] = valorParcelaAoInvestidorNoVencimentoASerPaga
        resposta['valorIofAtraso'] = valorIofAtraso
        resposta['valorJurosMoratorios'] = valorJurosMoratorios
        resposta['valorJurosRemuneratoriosAdicionais'] = valorJurosRemuneratoriosAdicionais
        resposta['valorMultaMoratoria'] = valorMultaMoratoria
        resposta['valorTarifaASerPaga'] = valorTarifaASerPaga

    return resposta
