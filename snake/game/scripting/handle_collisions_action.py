import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point
from game.casting.score import Score
from game.casting.snake import Snake


class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the snake collides
    with the food, or the snake collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False
        self._score = Score()
        # self._snake = Snake()

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_segment_collision(cast)
            self._handle_game_over(cast)

    # def _handle_opponent_collision(self, cast):
    #     """Updates the score and ends the game if the opponents collide with each other.
    #
    #     Args:
    #         cast (Cast): The cast of Actors in the game.
    #     """
    #     score1 = cast.get_first_actor("player_1_scores")
    #     score2 = cast.get_first_actor("player_2_scores")
    #
    #     snake1 = cast.get_first_actor("player_1")
    #     snake2 = cast.get_first_actor("player_2")
    #     head1 = snake1.get_head()
    #     segments1 = snake1.get_segments()[1:]
    #     head2 = snake2.get_head()
    #     segments2 = snake2.get_segments()[1:]
    #
    #     # all_segments = []
    #     #
    #     # length1 = len(segments1)
    #     # length2 = len(segments2)
    #     #
    #     # total_segments = length1 + length2
    #
    #     # if len(all_segments) < total_segments:
    #     #     print("inside if statement")
    #     #     for segment in segments2:
    #     #         print(f"inside append for loop 1")
    #     #         all_segments.append(segment)
    #     #
    #     #     for segment in segments1:
    #     #         print(f"inside append for loop 2")
    #     #         all_segments.append(segment)
    #
    #     for segment in segments2:
    #         print(f"inside collision for loop 1")
    #         if head1.get_position().equals(segment.get_position()):
    #             # points = food.get_points()
    #             # snake.grow_tail(points)
    #             # score1.add_points(1, "one")
    #             # food.reset()
    #             print(f"head 1 hit segments2")
    #             self._is_game_over = True
    #     for segment in segments1:
    #         print(f"inside collision for loop 2")
    #         if head2.get_position().equals(segment.get_position()):
    #             # points = food.get_points()
    #             # snake.grow_tail(points)
    #             # score1.add_points(1, "one")
    #             # food.reset()
    #             print(f"head 2 hit segments1")
    #             self._is_game_over = True
    
    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the snake collides with one of its segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        snake1 = cast.get_first_actor("player_1")
        snake2 = cast.get_first_actor("player_2")
        head1 = snake1.get_head()
        head2 = snake2.get_head()
        segments1 = snake1.get_segments()[1:]
        segments2 = snake2.get_segments()[1:]

        for segment in segments2:
            if head1.get_position().equals(segment.get_position()):
                print(f"head 1 hit segments2")
                self._is_game_over = True
        for segment in segments1:
            if head2.get_position().equals(segment.get_position()):
                print(f"head 2 hit segments1")
                self._is_game_over = True

    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the snake and food white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            snake1 = cast.get_first_actor("player_1")
            segments1 = snake1.get_segments()
            # this should be the opposite snake
            snake2 = cast.get_first_actor("player_2")
            segments2 = snake2.get_segments()

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            message.set_text("Game Over!")
            message.set_position(position)
            cast.add_actor("messages", message)

            for segment in segments1:
                segment.set_color(constants.WHITE)
            for segment in segments2:
                segment.set_color(constants.WHITE)