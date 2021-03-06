
import random

class FileHandler:

    def __init__(self):
        self.answer = ''

        #read 'WordDB.txt' file
        self.words = []
        f = open('wordDB.txt', 'r')
        lines = f.readlines()
        f.close()

        self.count = 0
        for line in lines:
            word = line.rstrip()
            self.words.append(word)
            self.count += 1

        print("%d words in DB" %self.count)

    def randFromDB(self):
        r = random.randrange(self.count)
        self.answer = self.words[r]
        return self.answer

    def CorrectInput(self):
        Dic = ['a', 'b', 'c', 'd', 'e','f','g','h','i','j','k','l',
               'm','n','o','p','q','r','s','t','u','v','w','x','y','z']
        return Dic
