# connenct4_SmartAgent
This modified version of connect-4 is played on a 7x7 grid as follows: Starting from the initial position illustrated below, players take turns moving one piece of their colour by a number of squares as explained below, either horizontally or vertically.  No jumping is allowed. White plays first. Pieces can only move to unoccupied squares. The winner is the first player to form a 2x2 square of four pieces. In addition, pieces create an "impedance" field in the immediate (8-squares) neighbourhood around them, affecting the number of squares an opponent piece can move. The following table describes the number of squares a piece can move given the number of opponent pieces in its neighbourhood:
<img width="557" alt="Screen Shot 2023-10-19 at 4 04 29 PM" src="https://github.com/julesgransden/COnenct4_SmartAgent/assets/78057184/b3f9035b-7cfc-4bba-8ca1-8cddb585655d">

I designed a heuristic evaluation function that assessed game states' quality without exploring the entire game tree.
This function considered factors such as position control, strategic advantage, and win/delay-defeat likelihood.
Behavior Implementation:

My agent exhibited specific behaviors:
When victory was imminent, I aimed to win as quickly as possible.
When defeat was approaching, I played defensively to delay the inevitable.
Rationale for Evaluation Function:

I provided a rationale for my heuristic evaluation function, explaining how each factor contributed to decision-making.
Comparison with Part I:

I assessed performance by comparing the new evaluation function to the one used in Part I. This analysis considered average node visits for both minimax and alpha-beta algorithms.
Computational Tradeoffs:

I discussed the computational tradeoffs of using a more complex evaluation function, highlighting memory and time considerations.
Game Logs:

I included game logs for scenarios (a) and (c) with a depth cutoff of 4, demonstrating how two agents utilizing my heuristic played against each other.
Code Implementation:

My code for the Dynamic Connect-4 game agent respects assignment specifications and operates without significant errors.
By incorporating these enhancements in Part II, I've made my game agent smarter, which is clearly explained in this README. This should help others understand my work and the improvements I've made in this assignment.
