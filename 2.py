# 0-100之间所有的偶数之和

i =0
result = 0
while i<=100:
    if i % 2 ==0: #奇数为 i % 2 != 0
        result +=i
    i += 1    
print(result)