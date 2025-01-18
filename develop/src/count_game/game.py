import random
from typing import List, Optional

class TurnInfo:
    def __init__(self, current_count: int, old_count: Optional[int], end_count: int):
        self.current_count = current_count
        self.old_count = old_count
        self.end_count = end_count

class Player:
    def __init__(self, logic: str, id: int):
        self.id = id
        self.logic = logic

    def play_turn(self, info: TurnInfo) -> int:
        # ASWIP: 詰みターンは必ず最適行動を行う．
        if info.current_count < info.end_count - 1:
            return info.end_count - info.current_count - 1

        # ランダム行動
        if self.logic == "random":
            return random.randint(1, 3)
        # 4 - (現在のカウント % 4) の数だけ取る
        elif self.logic == "smart":
            return 4 - info.current_count % 4
        # ミラーリング
        elif self.logic == "mirror":
            if info.old_count is None:
                return random.randint(1, 3)
            else:
                return info.old_count
        # Error
        else:
            raise ValueError("Invalid logic")

class CountGame:
    def __init__(self, players: list[Player]):
        # self.end_count = 30
        self.end_count = 49
        self.players = players

    def play_to_end(self):
        count = 0
        old_count = None
        while count < self.end_count:
            for player in self.players:
                player_count = player.play_turn(TurnInfo(count, old_count))
                print(f"Current {count}. Player {player.id} took {player_count}")
                count += player_count
                old_count = player_count
                print(f"New count {count}")

                if count >= self.end_count:
                    print(f"Player {player.id} loss!")
                    break

if __name__ == "__main__":
    players = [Player("random", 1), Player("mirror", 2)]
    game = CountGame(players)
    game.play_to_end()
    print("Game finished")
