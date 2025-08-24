# Pong
Pong Game in Python (Turtle Graphics)  A simple recreation of the classic Pong game using Python's built-in `turtle` module.   Two players compete to reach a target score — with bouncing physics, paddle control, increasing ball speed, and a dynamic scoreboard!

## 📸 Preview

---

## 🎮 Features

- Two-player paddle controls:
  - `W` / `S` keys for left paddle
  - `Up` / `Down` keys for right paddle
- Real-time ball physics with bounce behavior
- Paddle collision detection (boundary-based, not segment-based)
- Ball speed increases after every successful paddle hit
- Dynamic scoreboard with custom end score
- Game-over screen triggers once winning score is reached

---

## 🧠 How It Works

- **OOP Design**: Four classes are used:
  - `Ball` – handles ball movement, bounce, speed logic
  - `Paddle` – creates paddles and allows them to move
  - `Score` – manages and displays the score
  - `Main` – sets up the game and handles interactions
- **Collision Detection**:
  - Uses bounding box logic instead of `.distance()` for higher accuracy
- **Speed Scaling**:
  - Ball increases speed slightly after every paddle hit
  - Resets to default speed after scoring

---

## 🛠️ How to Run

Make sure you have Python 3 installed.

git clone https://github.com/your-username/pong-game-python.git
cd pong-game-python
python main.py
✅ Completed Features
 Paddle creation and movement

 Ball bouncing on top/bottom

 Paddle-ball collision

 Scoring system

 Scoreboard display

 Winning score input via popup

 Ball speed scaling

 Game reset after score

🛠️ To Improve / Fix
⏳ Add countdown before game starts

🔊 Add sound effects

🧠 AI opponent mode

📱 Mobile-friendly adaptation

🧪 Unit testing and cleanup

Improvements on ball and the paddle collision. change distance method to manually calculates coordination. 

🧰 Built With
Python 3 or higher

turtle graphics module (built-in, no extra dependencies)

🙏 Acknowledgments
This project was built as a fun exercise to learn OOP with turtle, practice collision logic, and simulate retro arcade mechanics.
