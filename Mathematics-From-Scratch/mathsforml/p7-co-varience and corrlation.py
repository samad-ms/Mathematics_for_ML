x = [1, 2, 3, 4, 5]
y = [2, 3, 4, 5, 6]

x_=sum(x)/len(x)
y_=sum(y)/len(y)


varienceY=sum((x[i]-x_)**2 for i in range(len(x)))/(len(x)-1)
varienceX=sum((x[i]-x_)**2 for i in range(len(x)))/(len(x)-1)
sd_X=varienceX**0.5
sd_Y=varienceY**0.5

cov=sum((x[i]-x_)*(y[i]-y_) for i in range(len(x)))/(len(x)-1)

cor=cov/(sd_X*sd_Y)

print(cov)
print(cor)












