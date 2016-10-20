def main():
  a=[]
  b=[]
  c=0
  product=1
  for i in range(1,216):
    a.append(i)
    a.reverse()
  for i in a:
    product=i*product
  product=str(product)
  for i in range(0,len(product)):
    b.append(product[i])
  for i in b:
    i=int(i)
    c=c+i
  print c
main()