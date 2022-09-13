def get_high_card(hand):

    card_vals={

    "1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"T":10,"J":11,"Q":12,"K":13,"A":14

    }

    keys_list=list(card_vals.keys())

    values_list=list(card_vals.values())

    face_values=[]

    card_values=hand.split()

    num_vals=[h[0]for h in card_values]

    for i in range(len(num_vals)):

        faces=card_vals[num_vals[i]]

        face_values.append(faces)

    high_card=max(face_values)

    high_card_num=max(face_values)

    high_card_location=values_list.index(high_card)

    high_card=keys_list[high_card_location]

    return high_card_num

def get_pairs(hand):

    pair_list=[]

    card_vals=hand.split()

    faces_vals=[h[0]for h in card_vals]

    for i in range(len(faces_vals)):

        if faces_vals.count(faces_vals[i])>1:

            pair_list.append(faces_vals[i])

    count=0

    if len(pair_list)==0:

        count=count

        return count #no pairs

    if len(pair_list)==2:

        count=1

        return count #one pair

    if len(pair_list)==3 and len(set(pair_list))==1:

        count=3

        return count #three of a kind

    if len(pair_list)==4 and len(set(pair_list))==2:

        count=2

        return count #two pairs

    if len(pair_list)==4 and len(set(pair_list))==1:

        count=5

        return count #four of a kind

    if len(pair_list)==5 and len(set(pair_list))==2:

        count=4

        return count #full house

    else:

        return False


def get_max(hand):

    card_vals={

    "1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"T":10,"J":11,"Q":12,"K":13,"A":14

    }

    card_values=hand.split()

    num_val_list=[]

    num_values=[h[0]for h in card_values]

    for i in range(len(num_values)):

        num_val=card_vals[num_values[i]]

        num_val_list.append(num_val)

    Max=max(num_val_list)

    return Max 


def get_straight(hand):

    card_vals={

    "1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"T":10,"J":11,"Q":12,"K":13,"A":14

    }

    card_values=hand.split()

    num_val_list=[]

    num_values=[h[0]for h in card_values]

    for i in range(len(num_values)):

        num_val=card_vals[num_values[i]]

        num_val_list.append(num_val)

    Max=max(num_val_list)

    Min=min(num_val_list)

    Sum=0 

    for i in range(Min,Max+1):

        Sum+=i

    if sum(num_val_list)==Sum:

        return True

    else:

        return False

def get_flush(hand):

    card_valuess=hand.split()

    suits=[h[1]for h in card_valuess]

    if len(set(suits))==1:

        return True

    else:

        return False

def get_straight_flush(hand):

    if get_straight(hand) and get_flush(hand):

        return True 

    else:

        return False

def get_royal_flush(hand):

    if get_flush(hand) and get_straight(hand) and get_max(hand)==14:

        return True

    else:

        return False


def score_hand(hand):

    if get_royal_flush(hand):

        score=24

        return score

    if get_straight_flush(hand):

        score=23

        return score

    if get_pairs(hand)==5:

        score=22

        return score

    if get_pairs(hand)==4:

        score=21

        return score

    if get_flush(hand):

        score=20

        return score

    if get_straight(hand):

        score=19

        return score

    if get_pairs(hand)==3:

        score=18

        return score

    if get_pairs(hand)==2:

        score=17

        return score

    if get_pairs(hand)==1:

        score=16

        return score

    else:

        score=get_max(hand)

        return score

def get_type(hand):

    if get_royal_flush(hand):

        hand_type='royal flush'

        return hand_type

    if get_straight_flush(hand):

        hand_type ='straight flush'

        return hand_type

    if get_pairs(hand)==5:

        hand_type='four of a kind'

        return hand_type

    if get_pairs(hand)==4:

        hand_type='full house'

        return hand_type

    if get_flush(hand):

        hand_type='flush'

        return hand_type

    if get_straight(hand):

        hand_type='straight'

        return hand_type

    if get_pairs(hand)==3:

        hand_type='three of a kind'

        return hand_type

    if get_pairs(hand)==2:

        hand_type='two pairs'

        return hand_type

    if get_pairs(hand)==1:

        hand_type='one pair'

        return hand_type

    else:

        hand_type='high card'

        return hand_type

num_of_hands=int(input("Number of hands: "))

i=0

Hands=[]

Scores=[]

for i in range(num_of_hands):
    hand=str(input('Hand: '))
    score=score_hand(hand)
    Hands.append(hand)
    Scores.append(score)

max_val=max(Scores)

index=Scores.index(max_val)

best_hand=Hands[index]

Hands.pop(index)

Hands.append(best_hand)

print('\n')

print(best_hand,'- Best Hand -',get_type(best_hand))

for i in range(len(Hands)-1):

    print(Hands[i],'-',get_type(Hands[i]))
