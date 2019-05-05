#!/usr/bin/env python3
import random
"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def __init__(self):
        self.count = 0

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def __init__(self):
        self.count = 0

    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def __init__(self):
        self.count = 0

    def move(self):
        choice = input("rock, paper or scissors?")
        while choice.lower() not in moves:
            choice = input("rock, paper or scissors?")
        return choice.lower()


class ReflectPlayer(Player):
    def __init__(self):
        self.count = 0
        self.mimic = "rock"

    def learn(self, my_move, their_move):
        self.mimic = their_move
        return self.mimic

    def move(self):
        return self.mimic


class CyclePlayer(Player):
    def __init__(self):
        self.count = 0
        self.cycle = "rock"

    def learn(self, my_move, their_move):
        if my_move == "rock":
            self.cycle = "paper"
        elif my_move == "paper":
            self.cycle = "scissors"
        elif my_move == "scissors":
            self.cycle = "rock"

    def move(self):
        return self.cycle


""" beats fucntion used to determine the winner"""


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        if beats(move1, move2) is True:
            print("Player1 won")
            self.p1.count += 1
        elif move1 == move2:
            print("This is a tie")
        else:
            print("player2 won")
            self.p2.count += 1
        print(f"Score is Player1: {self.p1.count} vs Player2: {self.p2.count}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        game_number = input("How many rounds do you want to play?")
        while "." in game_number or float(game_number) <= 0:
            game_number = input("please enter a valid integer")

        print(f"Game start! You have {game_number} rounds, let's go!")
        for round in range(int(game_number)):
            print(f"Round {round}:")
            self.play_round()
        if self.p1.count > self.p2.count:
            print("<<The final result: Player1 won!>>")
        elif self.p1.count == self.p2.count:
            print("<<The final result: Tie!>>")
        elif self.p1.count < self.p2.count:
            print("<<The final result: Player2 won!>>")
        print("Game over!")


if __name__ == '__main__':
    player_1 = HumanPlayer()
    player_2 = RandomPlayer()
    game = Game(player_1, player_2)
    game.play_game()
 
