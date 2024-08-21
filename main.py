# Dice sum probability calculator
# Författare: Filip Nemlin
# Datum:2024-08-21

from pdb import Restart


def main():
    user_input = input("skriv två nummer på hur många sidor tärningarna ska ha, mellan 4 och 20. Använd ett mellanslag mellan numren").split(" ")

    dice1=str(user_input[0])
    dice2=str(user_input[1])
    sum=[]
    for a in range (1, dice1+1):
        for b in range (1, dice2+1):
            if a+b in sum:
                sum[a+b] +=1





if __name__ == "__main__":
    main()

