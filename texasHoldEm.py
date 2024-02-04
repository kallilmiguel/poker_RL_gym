import gym
from gym import spaces
import numpy as np
from numpy.random import default_rng
from poker_utils import evaluate_hand

class TexasHoldemEnv(gym.Env):
    """A simplified version of Texas Hold'em poker environment."""
    
    metadata = {'render.modes': ['human']}
    
    def __init__(self, num_players=2):
        super(TexasHoldemEnv, self).__init__()
        
        # Define the action space
        self.action_space = spaces.Discrete(4)  # 0: fold, 1: check, 2: raise, 3: all-in
        
        # Define the state space
        # This is a placeholder. You'll need to define a more complex structure
        # based on your game's requirements.
        self.observation_space = spaces.Dict({
            'phase': spaces.Discrete(4),  # 0: pre-flop, 1: flop, 2: turn, 3: river
            'player_cards': spaces.Tuple([spaces.Discrete(52) for _ in range(num_players)]),
            'table_cards': spaces.MultiDiscrete([52] * 5),
            'pot': spaces.Box(low=0, high=float('inf'), shape=(1,), dtype=np.float32),
            'bet': spaces.Box(low=0, high=float('inf'), shape=(1,), dtype=np.float32),
            'num_players': spaces.Discrete(num_players)  # Number of players
        })
        
        # Initialize state
        self.state = None
        self.num_players = num_players
        self.rng = default_rng()
        self.deck = list(range(52)) # deck of 52 cards, to see each card, just call the map_card function
        self.reset()
    
    def shuffle_and_deal(self):
        self.rng.shuffle(self.deck)

         # Deal two cards to each player
        self.state['player_cards'] = [self.deck[n*2:(n+1)*2] for n in range(self.num_players)]
        # Deal five cards to the table, simulated for all game phases
        self.state['table_cards'] = self.deck[self.num_players*2:self.num_players*2+5]



    def step(self, action):
        # Apply action, update the state of the environment, and calculate reward
        # Placeholder for your logic
        observation, reward, done, info = None, 0, False, {}
        return observation, reward, done, info

    def reset(self):
        # Reset the state of the environment to an initial state
        # Placeholder for your logic
        self.state = {
            'phase': 0,  # pre-flop
            'player_cards': [],  # This will be filled by shuffle_and_deal
            'table_cards': [],  # This will be filled by shuffle_and_deal
            'pot': 0.0,
            'bet': 0.0,
            'num_players': self.num_players  # Assuming you want to keep track of the number of players in the state
        }
        self.shuffle_and_deal()

        return self.state

    def render(self, mode='human'):
        # Render the environment to the screen
        for player in range(self.num_players):
            print(f" PLAYER {player + 1}")
            print(f" {self.map_card(self.state['player_cards'][player][0])} | {self.map_card(self.state['player_cards'][player][1])}")
        print("TABLE ")
        for table_card in self.state['table_cards']:
            print(self.map_card(table_card), end='|')
        print(f"\n\nPhase: {self.map_phase(self.state['phase'])}")
        print(f"Pot:{self.state['pot']}")
        print(f"Bet: {self.state['bet']}")
        
        return

    def close(self):
        # Perform any cleanup
        pass

    def map_card(self, card_number):
        suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        
        suit = suits[card_number // 13]
        rank = ranks[card_number % 13]
        return f"{rank} of {suit}"
    
    def map_phase(self, phase_number):
        
        phases = ['Pre-flop', 'Flop', 'Turn', 'River']
        return phases[phase_number]
    
    def player_table_cards(self, player_number):

        cards = list([*self.state['player_cards'][player_number], *self.state['table_cards']])
        return [self.map_card(card) for card in cards]