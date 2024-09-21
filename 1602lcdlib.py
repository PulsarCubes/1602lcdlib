import machine
import utime

#this assumes you are using a non-i2c 1602 and are using the pins listed
#code based off of how2electronics.com's guide (https://how2electronics.com/interfacing-16x2-lcd-display-with-raspberry-pi-pico/)

class LCD:
    def __init__(self, rs,e,d4,d5,d6,d7):
        self.rs = machine.Pin(rs, machine.Pin.OUT)
        self.e = machine.Pin(e, machine.Pin.OUT)
        self.d4 = machine.Pin(d4, machine.Pin.OUT)
        self.d5 = machine.Pin(d5, machine.Pin.OUT)
        self.d6 = machine.Pin(d6, machine.Pin.OUT)
        self.d7 = machine.Pin(d7, machine.Pin.OUT)
    def pulseE(self):
        self.e.value(1)
        utime.sleep_us(40)
        self.e.value(0)
        utime.sleep_us(40)
    def send2LCD4(self,BinNum):
        self.d4.value((BinNum & 0b00000001) >> 0)
        self.d5.value((BinNum & 0b00000010) >> 1)
        self.d6.value((BinNum & 0b00000100) >> 2)
        self.d7.value((BinNum & 0b00001000) >> 3)
        self.pulseE()
    def send2LCD8(self,BinNum):
        self.d4.value((BinNum & 0b00010000) >> 4)
        self.d5.value((BinNum & 0b00100000) >> 5)
        self.d6.value((BinNum & 0b01000000) >> 6)
        self.d7.value((BinNum & 0b10000000) >> 7)
        self.pulseE()
        self.d4.value((BinNum & 0b00000001) >> 0)
        self.d5.value((BinNum & 0b00000010) >> 1)
        self.d6.value((BinNum & 0b00000100) >> 2)
        self.d7.value((BinNum & 0b00001000) >> 3)
        self.pulseE()
    def setUpLCD(self):
        self.rs.value(0)
        self.send2LCD4(0b0011)
        self.send2LCD4(0b0011)
        self.send2LCD4(0b0011)
        self. send2LCD4(0b0010)
        self.send2LCD8(0b00101000)
        self.send2LCD8(0b00001100)
        self.send2LCD8(0b00000110)
        self.send2LCD8(0b00000001)
        utime.sleep_ms(2)
    def clearLCD(self):
        self.setUpLCD()
        self.rs.value(1)
    def writetolcd(self,string):
        for x in str(string):
            self.send2LCD8(ord(x))
    def lcdnewline(self,length):
        for _ in range(40-length):
            self.send2LCD8(0x80)
    def split_string(self,string):
        if 16 < len(string):
            first_part = string[:16]
            second_part = string[16:]
            return first_part, second_part
        else:
            return string, ""
    def splitstringdisplay(self,string):
        first, second = self.split_string(string)
        self.writetolcd(first)
        self.lcdnewline(len(first))
        self.writetolcd(second)















if __name__ == "__main__":
    lcd=LCD(16,17,18,19,20,21)
    lcd.clearLCD()
    lcd.splitstringdisplay('this library is written by PulsarCubes')

