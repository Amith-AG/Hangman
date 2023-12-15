# feature branch
import random
from word import word
import string
def get_valid_word():
    words=random.choice(word)
    if '-'in words or ' 'in words:
        words=random.choice(word)
    return words.upper()
def hangman():
     lives=10
     words=get_valid_word()
     word_letter=set(words)
     alpha=set(string.ascii_uppercase)
     used_letter=set()
     while len(word_letter)>0 and lives>0:
         print(f"lives:{lives} ")
         print("you have entered: "'',' '.join(used_letter))
         w=[letter if letter in used_letter else '-' for letter in words]
         print(' '.join(w))
         user_letter=input('enter the letter ').upper()
         if user_letter in alpha and used_letter:
             used_letter.add(user_letter)
             if user_letter in word_letter:
                 word_letter.remove(user_letter)
             else:
                lives=lives-1
         elif user_letter in used_letter:
             print("you have already enter the letter try again")
         else:
             print("inavalid input try again!!!")
        
             
hangman()
   
        

