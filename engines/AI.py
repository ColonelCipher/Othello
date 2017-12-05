import gym
import tflearn
from board import print_moves
from engines import Engine

class AIEngine(Engine):
    def get_move(self, board, color, move_num=None, time_remain=None, time_opponent=None):
        
