# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
| --- | --- | --- | --- |
| Guess possible numbers | Give accurate feedback to input higher or lower numbers next | Answer was 97, first guess was 99 and was told to go higher, next 98 - higher, next 100 - lower, next 10 - lower, next 3 - lower, next 1 - lower, finally 0 - lower and lost the game | none |
| Click 'new game' button | New game would start | Secret changes and attempts restart but history will remain the same, it should also restart that | none |
| Deactive 'show hint' button and activate it again | Hint will disappear but then appear again | Hint disappears but wont appear again | none |
| Change difficulty mid game | User should not be able to change difficulty mid game, and if they do, it should restart a new game | The difficulty changes, but the game remains the same | `preventOverflow modifier is required by hide modifier in order to work, be sure to include it before hide!` |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
Claude
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
One small example is that I asked how to correctly format the table for the log table. 
one good: it help me when I asked why the comparison between guess and secret was almost never correct, I suspected it was because of the str - int comparisson, so I asked claude about it and it confirmed it and helped corrected it (where the guess is passed for comparisson). Then it help me with the hint wording, changing it to the appropiate one. If the guess was higher, it would return "go lower" and so
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
when i tried restarting the game correctly (including the history), this was the fix that AI recomended:
"if new_game:
    st.session_state.secret = random.randint(low, high)
    st.session_state.attempts = 1
    st.session_state.score = 0
    st.session_state.status = "playing"
    st.session_state.history = []
    guess_key = f"guess_input_{difficulty}"
    if guess_key in st.session_state:
        st.session_state[guess_key] = ""
    st.success("New game started.")
    st.rerun()"
but its not working, when I played the game again, and tried a couple times it would not let me restart the game:
streamlit.errors.StreamlitAPIException: st.session_state.guess_input_Normal cannot be modified after the widget with key guess_input_Normal is instantiated.

Traceback:
File "C:\Users\marit\OneDrive\Escritorio\ai110-module1show-gameglitchinvestigator-starter\app.py", line 135, in <module>
    st.session_state[guess_key] = ""
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^
File "C:\Users\marit\AppData\Roaming\Python\Python314\site-packages\streamlit\runtime\metrics_util.py", line 698, in wrapped_func
    result = non_optional_func(*args, **kwargs)
File "C:\Users\marit\AppData\Roaming\Python\Python314\site-packages\streamlit\runtime\state\session_state_proxy.py", line 114, in __setitem__
    get_session_state()[key] = value
    ~~~~~~~~~~~~~~~~~~~^^^^^
File "C:\Users\marit\AppData\Roaming\Python\Python314\site-packages\streamlit\runtime\state\safe_session_state.py", line 109, in __setitem__
    self._state[key] = value
    ~~~~~~~~~~~^^^^^
File "C:\Users\marit\AppData\Roaming\Python\Python314\site-packages\streamlit\runtime\state\session_state.py", line 608, in __setitem__
    raise StreamlitAPIException(
    ...<2 lines>...
    )
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
