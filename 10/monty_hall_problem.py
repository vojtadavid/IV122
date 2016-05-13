import random

repeat = 10000

#option=0 never change tour guess
#option=1 always change your guess
#option=2 randomly change your guess
def monty_hall(option=1):
    good_guess = 0
    for i in range(repeat):

        car_position = random.randint(0,2)
        choosen_pos = random.randint(0,2)
        host_pos = -1


        if (car_position==1 and choosen_pos==0) or (car_position==0 and choosen_pos==1):
            host_pos = 2
        if (car_position == 0 and choosen_pos == 2) or (car_position == 2 and choosen_pos == 0):
            host_pos = 1
        if (car_position == 1 and choosen_pos == 2) or (car_position == 2 and choosen_pos == 1):
            host_pos = 0

        if host_pos==-1:
            if random.randint(0,1):
                host_pos = (car_position +1)%3
            else:
                host_pos = (car_position -1)%3


        if option==1:
            s = set([0,1,2])
            s.remove(host_pos)
            s.remove(choosen_pos)
            choosen_pos = s.pop()

        # option 0 dont change your guess

        #option 2 randomly change your guess
        if option==2 and random.randint(0,1):
            s = set([0,1,2])
            s.remove(host_pos)
            s.remove(choosen_pos)
            choosen_pos = s.pop()

        if car_position==choosen_pos:
            good_guess+=1

    if option==1:
        print("always change your guess",good_guess/repeat)

    if option==2:
        print("randomly change your guess",good_guess/repeat)

    if option == 0:
        print("never change your guess", good_guess / repeat)


monty_hall(0)
monty_hall(1)
monty_hall(2)

# experimentalni vyhodnoceni ruznych strategii odpovida predpokladanym vysledkum
# jako nejvyhodnejsi strategie se jevi vzdy zmenit nas puvodni tip
# never change your guess 0.3348
# always change your guess 0.6666
# randomly change your guess 0.499



