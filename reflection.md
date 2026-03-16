# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- Hints change despite having the same guess input. For example it changes between "Go Lower" and "Go Higher" even when you have the same guess of, say "5"
- After finshing the first game and using all attempts, when you start a new game, the game freezes and you cannot enter more guesses. 
- The hints are off. When you input a number outside the range the hint still says "Go Higher". For example, if you enter 150, the hint says "Go Higher" even when the game says enter between 1 to 100
- the difficulty feature is off on the Hard level. The range is smaller than both easy and medium. It's expected to be a larger range since its hard

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project. 

Answer: Claude Code

- For the difficulty bug where the Hard range was too smalL (1-50), the AI changed it to 1-200 for a larger, harder range. 

- For the wrong hint direction bug, the AI first suggested that it was because secret was a string and wanted to convert it to integers. But this was only fixing the bug of hints flipping on same guess. So I referenced the lines which I though were the root cause, and it managed to fix it properly. It then suggested to flip guess > secret -> "Go LOWER!" to guess < secret -> "Go HIGHER!".This fixed the bug. 
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed? 

Answer:  I saved the edits and refreshed the app and tested them

- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.

Answer:
  platform darwin -- Python 3.14.2, pytest-9.0.2, pluggy-1.6.0 -- /Users/qhelanimoyo/Desktop/Projects/AI110-module1show-gameglitchinvestigator-starter/.venv/bin/python
cachedir: .pytest_cache
rootdir: /Users/qhelanimoyo/Desktop/Projects/AI110-module1show-gameglitchinvestigator-starter
collecting ... collected 5 items

tests/test_game_logic.py::test_winning_guess PASSED                      [ 20%]
tests/test_game_logic.py::test_guess_too_high PASSED                     [ 40%]
tests/test_game_logic.py::test_guess_too_low PASSED                      [ 60%]
tests/test_game_logic.py::test_hint_direction_too_high PASSED            [ 80%]
tests/test_game_logic.py::test_hint_direction_too_low PASSED             [100%]

============================== 5 passed in 0.01s ===============================

- Did AI help you design or understand any tests? How? 

Answer: Yes it explained how the edits fixed the bugs and provided more test cases to further solidify the judgements

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.

Answer:
In the original version, the st.session_state.secret line had no guard around it, so everytime it rerun it picked a brand new secret nuumber, including each time you hit Submit

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

Answer:

Streamlit - Imagine every time you click a button on a webpage, the entire Python script runs again from top to bottom, that's what Streamlit does. It reruns

Session State is a sticky notepad that survives reruns. Anything you store in st.session_state sticks around between clicks for the whole browser session. 


- What change did you make that finally gave the game a stable secret number?

Answer:
- Added the guard check so the secret is only generated once. 
Before (ran every rerun — new secret every click):
st.session_state.secret = random.randint(low, high)
After (only runs if no secret exists yet):
if "secret" not in st.session_state:
    st.session_state.secret = random.randint(low, high)

- Fixed the "New Game" button to use low/high from the selected difficulty instead of hardcoded 1, 100, and also reset status so the game doesn't freeze
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?

Answer:
- constant collaboration with the AI chatbot. The Plan feature is super useful to sort of plan and understand before executing

- What is one thing you would do differently next time you work with AI on a coding task?

Answer:
- to not just prompt and edit automatically without planning and asking first


- In one or two sentences, describe how this project changed the way you think about AI generated code

Answer:
- I now see AI generated code as useful, but at the same time not as useful if carried out without supervision
