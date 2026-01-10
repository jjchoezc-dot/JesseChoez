class CuentaBancaria:
    def __init__(self, saldo_inicial=0):
        self._saldo = saldo_inicial  # Protegido

    def depositar(self, monto):
        if monto > 0:
            self._saldo += monto

    def obtener_saldo(self):
        return self._saldo


cuenta = CuentaBancaria(100)
cuenta.depositar(50)
print(cuenta.obtener_saldo())  # Output: 150
