val_venda = float(input('Informe o valor total da venda: R$'))
pag_desc = val_venda - (val_venda*(10/100))
print('O total a pagar com 10 porcento de desconto é R$ %.2f'%pag_desc)
print('O valor parcelado em 3 x sem juros é R$ %.2f'%(val_venda/3))
print('A comissão do vendedor na venda a vista é R$ %.2f'%(pag_desc - (pag_desc*(95/100))))
print('A comissão do vendedor na venda parcelada é R$ %.2f'%(val_venda - (val_venda*(95/100))))
