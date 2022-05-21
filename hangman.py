import random

class Hangman():
  def __init__(self):
    self.lis=set(["python", "java", "swift", "javascript"])
    #self.nuk_eshte=0
    self.mat_won,self.mat_lost=0,0
    self.alphabet=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
  def store_win_loss(self):
    self.value=random.choice(tuple(self.lis))
    self.hiden_value=list("-"*len(self.value))
    self.control=8
    self.store_does_not_find=""
  def input_control_lenght(self):
      if len(self.user) !=1:
        print("Please, input a single letter.")
        return True

  def input_control_lowercase(self):
      if self.user not in self.alphabet:
        print("Please, enter a lowercase letter from the English alphabet.")
        return True

  def letter_if_not(self):
    if self.user in self.store_does_not_find:
      print("You've already guessed this letter")
    else:
      if (self.user not in self.value):
                  # nuk_eshte+=1
                  # if nuk_eshte==1:
                      print(f"That letter doesn't appear in the word.  # {self.control} attempts")
                      self.store_does_not_find+=self.user
                      self.control-=1
                  # else:
                  #     print(f"No improvements.  # {control} attempts")
                  #     control-=1
      if (self.user in self.hiden_value):
          print(f"You've already guessed this letter.")
          #control-=1

  def letter_if_exists(self):
        global nuk_eshte    
        for i in range(len(self.value)):
          if self.user in self.value[i]:
              #nuk_eshte=0
              self.hiden_value[i]=self.user

  def printimi_hiden(self):
        for el in self.hiden_value:
          print(el,end="")
        print()

  def kontrolli_nese_gjehet(self):
        if "-" not in self.hiden_value:
          print(f"You guessed the word {self.value}!\nYou survived!")
          self.mat_won+=1
          return True

  def nuk_u_gjet(self):
    if self.control==0:
      print("You lost!")
      self.mat_lost+=1

  def handgamn(self):
    
    while self.control>0:
      if self.kontrolli_nese_gjehet()==True:
        break
      self.printimi_hiden()
      self.user=input("Input a letter:  ")
      if (self.input_control_lenght() == True):
        pass
      elif (self.input_control_lowercase() == True):
        pass
      else:
        self.letter_if_not()
        self.letter_if_exists()
    self.nuk_u_gjet()

  def menu(self):
      print("H A N G M A N\n")
      while True:
        inp = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ')
        if inp == "play":
          loja.store_win_loss()
          self.handgamn()
        if inp == "results":
          print(f"You won: {self.mat_won} times\nYou lost: {self.mat_lost} times")
        if inp == "exit":
          break

if __name__ == "__main__":
    loja = Hangman()
    loja.store_win_loss()
    loja.menu()
