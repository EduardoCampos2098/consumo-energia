📝- Primeiro Projeto - Programa de cálculo mensal de gasto energético.

Este projeto em Python foi criado para praticar o ciclo **Entrada → Processamento → Saída**. 
O programa pede informações fáceis, como o **nome do eletrodoméstico**, seu **consumo em Watts** e o **tempo de uso**. Com as informações preenchidas, ele retorna o consumo enegético e gasto monetário aproximado, respectivamente em kWh e R$ (valor fixo de 0.80). Assim, é possivel criar uma noção média de gastos com energia ao final do mês.
Fómulas resposável pela síntese de resultados:
consumo_elétrico_mensal = (potência * tempo * 30) / 1000 #kWh
cálculo_monetário = (consumo_elétrico_mensal * 0.80) #reais (R$)

<div style="display: inline_block"><br>
  <img align="center" alt="Python" height="40" width="40"
src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg">
<img align=center height="40" width="40" src="https://imgs.search.brave.com/Dn4Zk9BXCLsW_fT_OJiWdmIwHx_rHK3IrJSUEEDG7f4/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9zdGF0/aWMudmVjdGVlenku/Y29tL3N5c3RlbS9y/ZXNvdXJjZXMvdGh1/bWJuYWlscy8wNjUv/NzQyLzI4MC9zbWFs/bC9hLWJsYWNrLWdp/dGh1Yi1pY29uLWlu/LWEtY2lyY2xlLWZy/ZWUtcG5nLnBuZw">
<img align=center height="40" width="40" src="https://imgs.search.brave.com/VGjmArJqQEZj48vS4UcTxmw0ivDE9UbsRBhX1McIJ1I/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9jZG4u/aWNvbnNjb3V0LmNv/bS9pY29uL3ByZW1p/dW0vcG5nLTI1Ni10/aHVtYi9zaGllbGQt/aWNvbi1zdmctZG93/bmxvYWQtcG5nLTEw/NjMyNTI5LnBuZz9m/PXdlYnAmdz0xMjg">
<img align=center height="40" width="40" src="https://imgs.search.brave.com/6ear6naP-JI50z1BKchIfCyu-WKtLHwUsNO-g2XPbCE/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9zdGF0/aWMudmVjdGVlenku/Y29tL3N5c3RlbS9y/ZXNvdXJjZXMvdGh1/bWJuYWlscy8wMzUv/NTg1Lzc2OC9zbWFs/bC9lbmVyZ3ktZWZm/aWNpZW5jeS1saW5l/LWljb24tc3ltYm9s/LWlsbHVzdHJhdGlv/bi1mcmVlLXBuZy5w/bmc">