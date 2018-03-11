# dice roll entropy functions to create a qrl mnemonic, ideally using a polyhedral dice..

import words    #qrl mnemonic words for lookup

# sided dice doesnt count 0, but we must. therefore binary range is 0-(x-1), dice is 1-x
def sides_to_bin(sides):
    sides -= 1
    if len(bin(sides+1)[2:]) == len(bin(sides)[2:]):
        return len(bin(sides)[2:])-1
    return len(bin(sides)[2:])


class Mnemonic():

    def __init__(self, sides=100, words=34, bits=12):
        self.sides = sides
        self.words = words
        self.bits = bits
        self.seed_bits = bits*words
        self.bits_per_roll = sides_to_bin(sides)
        self.range = 2**self.bits_per_roll
        self.rolls_per_word = bits/self.bits_per_roll
        self.rolls_per_mnemonic = self.rolls_per_word*words
        self.mnemonic = []
        return

    def rolls_to_int(self):
        rolls = []
        print 'Number of rolls: ', self.rolls_per_word
        for x in range (self.rolls_per_word):
            print 'Roll: ' ,x+1, '  Enter dice value (1 - ', self.range, '): '
            roll = int(raw_input())
            if roll < 1 or roll > self.range:
                print 'Error, roll outside acceptable range (1 - ', self.range, ' )'
                return False
            rolls.append(roll-1)
        word = self.r_to_int(rolls)
        #print 'word_int lookup', word
        return word

    def r_to_int(self, rolls):
        word = ''
        if type(rolls) != list:
            return False
        rolls.reverse()
        for r in rolls:
            word = word + bin(r)[2:].zfill(self.bits_per_roll)
        return int(word, 2)

    def int_to_word(self, intw):
        return words.words[intw]

    def rolls_to_word(self):
        return self.int_to_word(self.rolls_to_int())

    def rolls_to_mnemonic(self):
        mnemonic = []
        print 'Prepare to roll your', self.sides, 'sided dice ', self.rolls_per_mnemonic, ' times, to create a ', self.words, ' mnemonic phrase..'
        for x in range(self.words):
            print 'Word number ', x+1, ' of ', self.words, ':'
            w = self.rolls_to_int()
            if w == False:                      # give one chance per word to user error
                w = self.rolls_to_int()
            if w == False:
                print 'Error, you must follow rules to create mnemonic correctly, please run script again.'
                return
            mnemonic.append(self.int_to_word(w))
        self.mnemonic = mnemonic
        return self.mnemonic

#generate a qrl mnemonic using a dice

def gen_mnemonic():
    print 'Enter the number of sides of the dice:'
    m = Mnemonic(sides=int(raw_input()))
    print m.rolls_to_mnemonic()

if __name__ == '__main__':
    print 'QRL mnemonic phrase dice generator...'
    gen_mnemonic()