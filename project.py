import random


def goal_function(goal_number):
    first_dice = random.randint(1, 6)
    second_dice = random.randint(1, 6)
    sum = first_dice + second_dice
    while sum != goal_number:
        first_dice = random.randint(1, 6)
        second_dice = random.randint(1, 6)
        sum = first_dice + second_dice
        print(f"The sum of two dice is {first_dice} + {second_dice} = {sum}")
        if sum == 7:
            print("You lose")
            break
        if sum == goal_number:
            print("You won")


def main():
    player_wins_numbers = [7, 11]
    player_loses_numbers = [2, 3, 12]
    goal_numbers = [4, 5, 6, 8, 9, 10]
    first_dice = random.randint(1, 6)
    second_dice = random.randint(1, 6)
    sum_of_two_dice = first_dice + second_dice
    print(f"The sum of two dice is {first_dice} + {second_dice} = {sum_of_two_dice}")
    if sum_of_two_dice in player_wins_numbers:
        print("You won")
    if sum_of_two_dice in player_loses_numbers:
        print("You lose")
    if sum_of_two_dice in goal_numbers:
        print(f"Now your goal number is {sum_of_two_dice}")
        goal_function(sum_of_two_dice)


if __name__ == "__main__":
    main()
