/*We just got home from a trip to South America, specifically Colombia, Peru, and Brazil. There's some leftover cash in:

🇨🇴 Colombian pesos
🇵🇪 Peruvian soles
🇧🇷 Brazilian reais
Create a currency.py program that asks the user for the amount they have in pesos, soles, and reais and calculates the total in USD.

Make sure to Google the current exchange rates!*/

# Write code below 💖
co=int(input("Enter co:"))
pe=int(input("Enter pe:"))
br=int(input("Enter br:"))

co_to_usd = co * 0.000241
pe_to_usd = pe * 0.273
br_to_usd = br * 0.175
print("conversion from co to usd is",co_to_usd)
print("conversion from pe to usd is",pe_to_usd)
print("conversion from br to usd is",br_to_usd)
total_sum = co_to_usd + pe_to_usd + br_to_usd
print("Total sum is",total_sum)
