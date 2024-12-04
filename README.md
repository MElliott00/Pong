This code implements a simple Pong game using the `turtle` module in Python. The game features two paddles, a ball, and a scoring system. Here's a breakdown of the main components:
1. **Setup**:
   - The game window is created with a black background, a title, and a size of 800x600 pixels.
   - The screen updates are turned off for smoother animation.

2. **Paddles**:
   - Two paddles (A and B) are created using turtle objects, positioned on the left and right sides of the screen.
   - The paddles are white squares stretched to a size of 5x1.

3. **Ball**:
   - A ball is created as a white circle, starting at the center of the screen.
   - The ball has initial movement speeds set for both the x and y directions.

4. **Score**:
   - Scores for both players are initialized to zero.
   - A pen turtle is used to display the scores at the top of the screen.

5. **Paddle Movement**:
   - Functions are defined to move the paddles up and down by 30 pixels.
   - Keyboard bindings are set up to control the paddles (W/S for the left paddle, Up/Down for the right paddle).

6. **Game Loop**:
   - The main game loop continuously updates the screen and moves the ball.
   - The ball bounces off the top and bottom edges of the screen.
   - When the ball goes past a paddle, the score is updated, and the ball is reset to the center.
   - The ball bounces off the paddles when it collides with them.

7. **Game Over**:
   - The game ends when either player reaches a score of 5.
   - A message is displayed indicating the winner.
