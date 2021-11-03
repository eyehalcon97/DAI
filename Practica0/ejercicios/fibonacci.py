# ejercicios/fibonacci.py

f=open("numeroaleer.txt")
numero = int(f.read())
f.close()
resultado = [ 0 , 1]
for i in range(1,numero):
    resultado.append(resultado[i] + resultado[i-1])
    

f=open("numeroaescribir.txt","w+")
f.write(str(resultado[numero]))
f.close()