import smbus

class MCP:

    def __init__(self):
        self.bus = smbus.SMBus(1)

        self.DEVICE = 0x20
        IODIRA = 0x00
        IODIRB = 0x01

        self.bus.write_byte_data(self.DEVICE, IODIRA, 0x00)
        self.bus.write_byte_data(self.DEVICE, IODIRB, 0x00)    


    def output(self, s):
        bin = s[1:]
        reg = s[0]

        if reg == 'A':
            inreg = '0x12'
        elif reg == 'B':
            inreg = '0x13'

        else:
            print('The input register is not valid')

        try:
            if(len(bin)) != 8:
                print('The input binary sequence is not valid')
            
            hexcode = hex(int(bin, 2))
        except:
            print('The input binary sequence is not valid')

        try:
            self.bus.write_byte_data(self.DEVICE, int(inreg, 16), int(hexcode, 16))

        except Exception as e:
            print('Something went wrong! Parsed with error message: ', e)


mcp = MCP()

mcp.output('A00000100')
mcp.output('B00010000')








        
        
