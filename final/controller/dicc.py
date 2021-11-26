from typing import List, Tuple
from controller.maquina import Turing
from collections import defaultdict
import regex


class Diccionario:
    def __init__(self, path: str) -> None:
        self.sets = {}
        self.lists = {}
        self.funciones = defaultdict(dict)
        self.maquina = {}
        self.guardar = 0

        with open(path, mode="r") as file:
            self.Cargar(file.read())

    def Cargar(self, code: str) -> None:
        funcionRegex = regex.compile(r"^(\w+)\((\w+),(\w+)\)=\((\w+),(\w+),(\w+)\)$")
        setRegex = regex.compile(r"^(\w+)=\{(?:(\w+),)*(\w+)?\}$")
        maquinaRegex = regex.compile(
            r"^(\w+)=\((\w+),(\w+),(\w+),(\w+),(\w+),(\w+),(\w+)\)$"
        )
        listaRegex = regex.compile(r"^(\w+)=\[(?:(\w+),)*(\w+)?\]$")

        for line in code.replace(" ", "").split():
            if line[0] == "#":
                continue
            elif funcionRegex.match(line):
                match = funcionRegex.match(line)
                funcionName = match.group(1)
                funcionParametro = (match.group(2), match.group(3))
                funcionRetorna = (match.group(4), match.group(5), match.group(6))
                if funcionParametro in self.funciones[funcionName]:
                    raise Exception(
                        f"Parametro {funcionParametro} duplicado duplicado en la "
                        + "transicion de funcion {funcionName}"
                    )
                self.funciones[funcionName][funcionParametro] = funcionRetorna
            elif setRegex.match(line):
                match = setRegex.match(line)
                setName = match.group(1)
                setElemento = tuple(match.captures(2) + match.captures(3))
                if len(set(setElemento)) != len(setElemento):
                    raise Exception(f"Duplicacion en set {setName}")
                if setName in self.sets:
                    raise Exception(f"simbolo duplicado {setName}")
                self.sets[setName] = set(setElemento)
            elif maquinaRegex.match(line):
                match = maquinaRegex.match(line)
                maquinaName = match.group(1)
                maquinaComponente = (
                    match.group(2),
                    match.group(3),
                    match.group(4),
                    match.group(5),
                    match.group(6),
                    match.group(7),
                    match.group(8),
                )
                if maquinaName in self.maquina:
                    raise Exception(f"maquina duplicada {maquinaName}")
                self.maquina[maquinaName] = maquinaComponente
                self.Checar(maquinaName)
            elif listaRegex.match(line):
                match = listaRegex.match(line)  #!AQUI
                listName = match.group(1)
                listElemento = match.captures(2) + match.captures(3)
                print(listElemento, " ELEMOT EN LISTA OG")
                if listName in self.lists:
                    raise Exception(f"Lista duplicada {listName}")
                self.lists[listName] = listElemento
            elif line[0] == "!":
                self.Run(line)
            else:
                raise Exception(f'Unknown command: "{line}"')

    def Checar(self, name: str) -> None:
        n_sigma, n_gamma, n_Q, n_f, B, q0, n_F = self.maquina[name]

        if n_sigma not in self.sets:
            raise Exception(f"Set {n_sigma} en la maquina {name} no existe D:")
        sigma = self.sets[n_sigma]
        if n_gamma not in self.sets:
            raise Exception(f"Set {n_gamma} en la maquina {name} no existe D:")
        gamma = self.sets[n_gamma]
        if n_Q not in self.sets:
            raise Exception(f"Set {n_Q} en la maquina {name} no existe D:")
        Q = self.sets[n_Q]
        if n_F not in self.sets:
            raise Exception(f"Set {n_F} en la maquina {name} no existe D:")
        F = self.sets[n_F]
        if n_f not in self.funciones:
            raise Exception(
                f"Funcion de Transicion {n_f} en la maquina {name} no existe D:"
            )
        f = self.funciones[n_f]

        dif = F.difference(Q)
        if len(dif) != 0:
            raise Exception(
                f"el estado {dif} en la maquina {name} en el estado fina set {n_F} no se encontro ese estado {n_Q}"
            )
        inters = Q.intersection(gamma)
        if len(inters) != 0:
            raise Exception(
                f"Simbolo  {inters} en la maquina {name} son simbolo y estado"
            )

        if q0 not in Q:
            raise Exception(f"Estado inicial {q0} en la maquina {name} no existe {n_Q}")

        if len(gamma.union(sigma)) != len(gamma):
            raise Exception(
                f"El conjunto sigma {n_sigma} en la maquina {name} no es un subconjunto"
                + "'s"
                + f" {n_gamma} de gamma "
            )
        if B not in gamma:
            raise Exception(
                f"Simbolo blanco {B} en la maquina {name} no esta en {n_gamma} o en {n_gamma} y {n_sigma}"
            )

        for (q, a), (p, b, D) in f.items():
            if D not in ["R", "L"]:
                raise Exception(f"Direction {D} not in " + "{R, L}")
            if q not in Q:
                raise Exception(
                    f"Estado {q} en la maquina {name} en la transicion {n_f} no esta en el conjunto {n_Q}"
                )
            if p not in Q:
                raise Exception(
                    f"State {p} en la maquina {name} en la transicion {n_f} no esta en el conjunto {n_Q}"
                )
            if a not in gamma:
                raise Exception(
                    f"Symbol {a} en la maquina {name} en la transicion {n_f} no esta en el conjunto {n_gamma} o {n_sigma}"
                )
            if b not in gamma:
                raise Exception(
                    f"Symbol {b} en la maquina {name} en la transicion {n_f} no esta en el conjunto {n_gamma} o {n_sigma}"
                )

        self.maquina[name] = Turing(sigma, gamma, Q, f, B, q0, F)

    def Run(self, comando: str) -> None:
        run_regex = regex.compile(r"^!run\((\w+),(\w+)\)$")
        if run_regex.match(comando):
            match = run_regex.match(comando)
            m_name = match.group(1)
            l_name = match.group(2)
            if m_name not in self.maquina:
                raise Exception(
                    f'Machine {m_name} from run comando "{comando}" not exists'
                )
            machine = self.maquina[m_name]
            if l_name not in self.lists:
                raise Exception(
                    f'Array {l_name} from run comando "{comando}" not exists'
                )
            inp = self.lists[l_name]
            for sym in inp:
                if sym not in machine.sigma:
                    raise Exception(
                        f'Symbol {sym} from input array {l_name} in run comando "{comando}" not in machine {m_name} sigma set'
                    )
            machine.Comenzar(inp)
            print(machine.Comenzar(inp))
            a =str(len(machine.Comenzar(inp)[0])-1)
            archi1=open("controller\suma.txt","w")
            archi1.write(f"{a}") 
            self.guardar = len(machine.Comenzar(inp)[0])
        else:
            raise Exception(f'Unknown comando: "{comando}"')
    
    def Total(self):
            a = self.guardar
            print("DEF TOTAL XD ",a)
