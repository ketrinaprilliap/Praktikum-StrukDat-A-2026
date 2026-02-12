class Person:
    def __init__(self, nama, jenis_kelamin, umur):
        self.nama = nama
        self.jenis_kelamin = jenis_kelamin
        self.umur = umur

Person1 = Person("Ketrin", "perempuan", 19)

class Karyawan(Person):
    def __init__(self, nama, jenis_kelamin, umur, gaji ):
        super().__init__(nama, jenis_kelamin, umur)
        self._gaji = gaji

    def get_gaji(self):
        return self._gaji

Karyawan1 = Karyawan("Masen", "laki-laki", 20, 4000000)

class Rekening:
    def __init__(self, no_rekening, PIN):
        self.no_rekening = no_rekening
        self.__PIN = PIN

    def get_PIN(self):
        return self.__PIN

    def set_PIN(self, PIN):
        if PIN > 0:
            self.__PIN = PIN
        else:
            print("PIN tidak boleh berangka negatif")

Rekening1 = Rekening("123456789", 230467)

print(Person1.nama, Person1.jenis_kelamin, Person1.umur)
print(Karyawan1.nama, Karyawan1.get_gaji())
print(Rekening1.get_PIN(), Rekening1.set_PIN(4046))
print(Rekening1.get_PIN())



    