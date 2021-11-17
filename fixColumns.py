# Arregla la estructura d elos archivos para facilitar su manejo
import pandas as pd
import numpy as np
import sys
print('iniciando proceso')
f = int(sys.argv[2])
file_name = sys.argv[1]
I = pd.read_csv(file_name, index_col=0)
I = I.loc[[f]].values.flatten()
O = pd.DataFrame(np.reshape(I, (int(I.size/4), 4)))
O.to_csv('fixed_' + file_name, header=["x", "theta", "volt", "time"])
print('proceso completado')
