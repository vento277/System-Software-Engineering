# System-Software-Engineering
CPEN 333 is a 3rd year computer engineering project course offered by the University of British Columbia.

*Course Description: Operating systems principles, real-time systems, principles of concurrent and multi-threaded programming, information structures, introduction to object oriented analysis, design, and modeling using UML, testing of software systems.*

## Tic-Tac-Toe
### Optimal Strategy for the Computer
#### If the Computer Starts:

1. **Take the Corner:**
   - **If the User Responds with the Center:**
     - Take the diagonally opposite corner.
     - Continue defending to force a draw or capitalize on any mistakes to win.
   - **If the User Responds with Anything Other Than the Center:**
     - This leads to a guaranteed win. Take the corner that is not diagonal but has the user’s cell in between to force them to block the space in between.
     - Take the center, setting up a two-way winning scenario.

#### If the User Starts:

1. **If the User Starts with the Center:**
   - Take any corner.
   - Continue defending to force a draw or win if the user makes a mistake.

2. **If the User Starts with a Non-Center Move:**
   - Take the center.
   - Continue defending to force a draw or win if the user makes a mistake.

3. **Blocking a Two-Way Winning Scenario:**
   - If the user plays two edge moves and takes a corner on their third move, this could create a two-way winning possibility. This must be blocked.
