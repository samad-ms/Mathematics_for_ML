x=[1,2,3,4,5]
y=[2,3,4,5,6]
x_=sum(x)/len(x)
y_=sum(y)/len(y)
sd_x=((sum((x[i]-x_)**2 for i in range(len(x))))/(len(x)-1))**0.5
sd_y=((sum((y[i]-y_)**2 for i in range(len(y))))/(len(y)-1))**0.5

cov=(sum((x[i]-x_)*(y[i]-y_) for i in range(len(x))))/(len(x)-1)
cor=cov/(sd_x*sd_y)
print(cov)
print(cor)
