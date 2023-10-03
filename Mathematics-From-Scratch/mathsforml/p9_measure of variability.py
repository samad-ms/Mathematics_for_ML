x = [1, 2, 3, 4, 5]
x_=sum(x)/len(x)

rangeX=max(x)-min(x)
varienceX=sum((x[i]-x_)**2 for i in range(len(x)))/(len(x)-1)
sd_X=varienceX**0.5

print(rangeX)
print(varienceX)
print(sd_X)