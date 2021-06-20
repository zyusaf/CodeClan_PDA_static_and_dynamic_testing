### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:

# No colon after else and needs a == after card.value

  def check_for_ace(self, card):
    if card.value = 1:
      return True
    else
      return False
   
# Says dif instead of def and also no comma between card1 and card2, and return card should say card1

  dif highest_card(self, card1 card2):
  if card1.value > card2.value:
    return card
  else:
    return card2
  
# total has no value, return needs to be outside the four loop, add a space after "total of" change + str(total)

def cards_total(self, cards):
  total
  for card in cards:
    total += card.value
    return "You have a total of" + total
  
```
