from optparse import OptionParser, OptionGroup

dict_characters = {}
dict_characters["A"] = ".-"
dict_characters["B"] = "-..."
dict_characters["C"] = "-.-."
dict_characters["D"] = "-.."
dict_characters["E"] = "."
dict_characters["F"] = "..-."
dict_characters["G"] = "--."
dict_characters["H"] = "...."
dict_characters["I"] = ".."
dict_characters["J"] = ".---"
dict_characters["K"] = "-.-"
dict_characters["L"] = ".-.."
dict_characters["M"] = "--"
dict_characters["N"] = "-."
dict_characters["O"] = "---"
dict_characters["P"] = ".--."
dict_characters["Q"] = "--.-"
dict_characters["R"] = ".-."
dict_characters["S"] = "..."
dict_characters["T"] = "-"
dict_characters["U"] = "..-"
dict_characters["V"] = "...-"
dict_characters["W"] = ".--"
dict_characters["X"] = "-..-"
dict_characters["Y"] = "-.--"
dict_characters["Z"] = "--.."
dict_characters["0"] = "-----"
dict_characters["1"] = ".----"
dict_characters["2"] = "..---"
dict_characters["3"] = "...--"
dict_characters["4"] = "....-"
dict_characters["5"] = "....."
dict_characters["6"] = "-...."
dict_characters["7"] = "--..."
dict_characters["8"] = "---.."
dict_characters["9"] = "----."
dict_characters["."] = ".-.-.-"
dict_characters[","] = "--..--"
dict_characters["/"] = "-..-."
dict_characters["?"] = "..--.."
dict_characters[" "] = "|"

class morse_converter(object):
    def __init__(self, wpm):
        self.wpm = wpm
        self.bps = wpm * 50. / 60 #--- PARIS has 50 bits
        self.initial_string = ""
        self.morse_string = ""
        self.bits_string = ""
        self.nbits = 0
        self.time_seconds = 0


    def __str__(self):
        line =  ""
        line += str("Original string: %s\n"   % (self.initial_string))
        line += str("Morse string:    %s\n"   % (self.morse_string))
        line += str("Bits string:     %s\n"   % (self.bits_string))
        line += str("Number of bits:  %d\n"   % (self.nbits))
        line += str("Time:            %.2f\n" % (self.time_seconds))
        return line

    
    def setString(self, initial_string):
        self.initial_string = initial_string

        #--- Translate to dots and dashes
        for c in self.initial_string:
            if c != " ":
                self.morse_string += dict_characters[c.upper()]
                self.morse_string += " "
            else:
                self.morse_string = self.morse_string[:-1]
                self.morse_string += dict_characters[c.upper()]
        self.morse_string = self.morse_string[:-1]

        #--- If space in the last character, restore last removed char
        if self.initial_string[-1]==" ":
            self.morse_string += "|"

        #--- Translate to time
        for char in self.morse_string:
            if char==".":
                self.bits_string += "=."
            if char=="-":
                self.bits_string += "===."
            if char==" ":
                self.bits_string = self.bits_string[:-1]
                self.bits_string += "..."
            if char=="|":
                self.bits_string = self.bits_string[:-1]
                self.bits_string += "......."
        self.bits_string = self.bits_string[:-1]

        #--- If space in the last character, restore last removed bit
        if self.initial_string[-1]==" ":
            self.bits_string += "."

        #--- Count bits
        for b in self.bits_string:
            self.nbits += 1
            self.time_seconds += 1./self.bps


    def getNBits(self):
        return self.nbits


    def getTime(self):
        return self.time_seconds


    def clean(self):
        self.initial_string = ""
        self.morse_string = ""
        self.bits_string = ""
        self.nbits = 0
        self.time_seconds = 0



if __name__=="__main__":

    usage = "usage: %prog [options]"
    parser = OptionParser(usage=usage)

    parser.add_option("-v","--verbose", action="store_true", dest="doVerbose", default=False, help="Set the program in verbose mode")
    parser.add_option("--wpm", action="store", type="string", default=30, help="Speed in WPM")
    parser.add_option("--text", action="store", type="string", default="", help="Text to convert")

    (options, args) = parser.parse_args()

    wpm  = float(options.wpm)
    text = options.text

    m = morse_converter(wpm)
    m.setString(text)
    print(m)
