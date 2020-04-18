# dice
polyhedral dice mnemonic phrase generator


For those who are completely paranoid about random number generation, it is possible to create entropy for a seed or mnemonic by rolling a dice. The more sides the dice has the more bits of entropy may be gathered with each roll, resulting in fewer rolls to complete a mnemonic.

The functions work for any sided dice, but I would recommend a polyhedral dice (e.g. 100 sided) which allows 6 bits of entropy per roll to be harvested.

For the QRL mnemonic (34 words, first 2 words (24 bits) are the extended seed descriptor, 32x12 bits per word thereafter, 408 bits required in total) this translates to 64 dice rolls to complete a mnemonic phrase.

Usage: 
    python dice.py
    
