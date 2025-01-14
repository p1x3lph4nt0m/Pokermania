import random
from base import Base

class Bot(Base):
    def declare_action(self, valid_actions, hole_card, round_state):
        # Randomly chooses between "fold", "call", and "raise"

        action = random.choice(valid_actions)

        amount = action.get("amount")
        if isinstance(amount, dict):
            amount = amount.get("min", 0)
        return action["action"], int(amount or 0)

    def receive_game_start_message(self, game_info):
        pass

    def receive_round_start_message(self, round_count, hole_card, seats):
        pass

    def receive_street_start_message(self, street, round_state):
        pass

    def receive_game_update_message(self, new_action, round_state):
        pass

    def receive_round_result_message(self, winners, hand_info, round_state):
        pass
