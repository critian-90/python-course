def conversioncriptomoneda(bitcoin, ethereum, litecoin):
    ltcEUR = 104.50
    btcEUR = 6500.81
    ethEUR = 493.35
    totalEUR = (bitcoin*btcEUR)+(ethereum*ethEUR)+(litecoin*ltcEUR)
    return totalEUR

print (f'{conversioncriptomoneda}')