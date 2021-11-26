

from typing import Dict, List, Tuple


class Turing:
      
      def __init__(self, sigma: Tuple[str], gamma: Tuple[str], Q: Tuple[str], 
                  transicion:Dict[Tuple[str,str],Tuple[str,str,str]],B: str, q0: str, F: Tuple[str]) -> None:
            
            self.sigma = sigma
            self.gamma = gamma
            self.Q = Q
            self.transicion = transicion
            self.B = B
            self.q0 = q0
            self.F = F
      
      def Comenzar(self, entrada: List[str], ptr = 0) -> Tuple[list[str], bool]:
            
            cinta = entrada.copy()
            puntero = ptr
            q = self.q0
            while True:
                  if puntero < 0:
                        return self.Limpiar(puntero), False
                  if puntero == len(cinta):
                        cinta.append(self.B)
                  estado = (q,cinta[puntero])
                  if estado in self.transicion:
                        estadoC, valor, direccion = self.transicion[estado]
                        cinta[puntero] = valor
                        puntero += 1 if direccion == "R" else -1
                        q = estadoC
                  else:
                        return self.Limpiar(cinta), q in self.F
                  
      def Limpiar(self, entrada: List[str]) -> List[str]:
            if entrada[-1] != self.B:
                  return entrada
            ind = len(entrada) - 1
            for i in range(ind, -1, -1):
                  if entrada[i] != self.B:
                        ind = i + 1
                        break
            else:
                  return []
            return entrada[:ind]
                  