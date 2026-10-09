#monthly sales dashboard
import numpy as np

# 3 products (rows) aur 12 months (columns) ki sales data ka 2D array
sales = np.array([
    [1200, 1500, 1300, 1600, 1700, 1900, 2100, 2000, 1800, 2200, 2400, 2600],  # Product 1 (Jan-Dec)
    [800,  950,  900,  1100, 1050, 1200, 1300, 1250, 1150, 1400, 1500, 1650],  # Product 2 (Jan-Dec)
    [500,  600,  550,  700,  750,  800,  850,  820,  780,  900,  950,  7000]   # Product 3 (Jan-Dec)
])
print(sales)
ys=np.sum(sales,axis=1)
print("Yearly Sales")
print(ys)
prod=["A","B","C"]
for i in range(3):
    print(f'product {prod[i]}:{ys[i]}')
bs=np.argmax(ys)
print("Best Selling Product")
print(ys[bs])
print(f'{prod[bs]}:{ys[bs]}')
hs=np.max(sales,axis=0)
print("High sales month",np.argmax(hs)+1)# ye index no dega aur index 0 se start hota h to plus one kar diya h 

print(hs[np.argmax(hs)])

   