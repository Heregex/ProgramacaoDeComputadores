N = int(input())

ced_100 = N//100
N = N - (100*ced_100)
print(ced_100, "nota(s) de R$ 100,00")

ced_50 = N//50
N = N - (50*ced_50)
print(ced_50, "nota(s) de R$ 50,00")

ced_20 = N//20
N = N - (20*ced_20)
print(ced_20, "nota(s) de R$ 20,00")

ced_10 = N//10
N = N - (10*ced_10)
print(ced_10, "nota(s) de R$ 10,00")

ced_5 = N//5
N = N - (5*ced_5)
print(ced_5, "nota(s) de R$ 5,00")

ced_2 = N//2
N = N - (2*ced_2)
print(ced_2, "nota(s) de R$ 2,00")

ced_1 = N//1
N = N - (1*ced_1)
print(ced_1, "nota(s) de R$ 1,00")