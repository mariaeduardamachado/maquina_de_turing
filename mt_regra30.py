def regra_30_tripla(left, center, right):
    tripla = left + center + right
    mapping = {
        "111": "0", "110": "0", "101": "0", "100": "1",
        "011": "1", "010": "1", "001": "1", "000": "0"
    }
    return mapping[tripla]


class MaquinaRegra30:
    def __init__(self, fita):
        if '|' not in fita:
            fita = fita + '|' + 'B' * 200

        self.fita = list(fita)
        self.head = 0

        self.start = self.fita.index('#') + 1
        self.end = self.fita.index('#', self.start)
        self.sep = self.fita.index('|')
        self.out_pos = 0

        self.validar_entrada()

    def validar_entrada(self):
        for c in self.fita[self.start:self.end]:
            if c not in ('0', '1'):
                raise ValueError(f"Erro: símbolo inválido '{c}'. A entrada só pode conter 0 e 1.")

    def ler_celula(self, idx):
        if idx < self.start or idx >= self.end:
            return '0'
        if self.fita[idx] in ('0', '1'):
            return self.fita[idx]
        return '0'

    def escrever_saida(self, bit):
        pos = self.sep + 1 + self.out_pos
        if pos >= len(self.fita):
            self.fita.extend(['B'] * 50)
        self.fita[pos] = bit
        self.out_pos += 1

    def executar(self):
        i = self.start
        while i < self.end:
            left = self.ler_celula(i - 1)
            center = self.ler_celula(i)
            right = self.ler_celula(i + 1)

            novo = regra_30_tripla(left, center, right)
            self.escrever_saida(novo)

            i += 1

        return ''.join(self.fita[self.sep+1:self.sep+1+self.out_pos])

    def fita_str(self):
        return ''.join(self.fita)


def exemplo_uso():
    entrada = "#10100#|"
    maquina = MaquinaRegra30(entrada)
    proxima = maquina.executar()

    print("Entrada: ", entrada)
    print("Próxima:", proxima)
    print("Fita completa:", maquina.fita_str())


if __name__ == "__main__":
    exemplo_uso()