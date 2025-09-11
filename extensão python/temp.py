# %%
import numpy as np
import matplotlib.pyplot as plt
import time
import random

n=20

x=np.zeros(n)
y=np.zeros(n)

for i in range(n):
    x[i]=i
    y[i]=random.gauss(0,1)

grafico=plt.subplot(111)

for i in range(n):
    grafico.plot(x[0:i],y[0:i])
    plt.pause(0.6)

# %%

# %%
pessoa1 = {
    "nome": "paulo",
    "idade": 65,
    "cidade": "porto alegre",
    "profissao": "matematico"
}
print(pessoa1.get("pais", "brasil"))
# %%