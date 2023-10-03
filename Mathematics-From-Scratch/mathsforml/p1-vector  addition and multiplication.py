def vector_add(v1,v2):
    if len(v1)!=len(v2):
        raise ValueError('size must be same')
    return [x+y for x,y in zip(v1,v2)]

def vector_mul(v1,s):
    return [x*s for x in v1]

v1=[1,2,3]
v2=[4,5,6]
print(vector_add(v1,v2))
print(vector_mul(v1,2))
