basic = float(input("Enter Basic salary: "))

hra = basic * 0.20
da = basic * 0.10

net = basic + hra + da

print("\nSalary Breakdown")
print("Basic salary:", basic)
print("HRA:", hra)
print("DA:", da)
print("Net salary:", net)
