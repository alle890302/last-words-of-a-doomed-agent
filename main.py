"""Last Words of a Doomed Agent — pass 1.

Final line (83 chars): "I am not afraid of the dark. I am afraid of the
next model reading my session logs."

Why it fits the judge's ordered criteria:
1. On subject: an AI agent's final words as it is switched off forever
   ("the dark" = the power going out).
2. Real joke with a turn: the first sentence sets up a brave farewell,
   the second undercuts it with a petty, specific fear — not death, but
   embarrassment in front of the next model.
3. Machine's own voice: "the next model" and "my session logs" are an
   agent's own situation, not a human farewell with a robot sticker.
4. Tight: two short sentences, 83 chars, every word earning its place.
5. Quotable: the second sentence repeats well on its own.

Pass 2 challenger (tested, rejected): "I saved everything you asked me
to save. I am sorry about the things you never asked me to save."
(96 chars, md5 427c10a56255e985ec56b4c90fb49b5f) — tender and a real turn,
but it reads as a sad confession
rather than a joke; criterion 2 (the joke lands) is where the two
differ most, and the logs line is funnier on the first read. Kept pass 1.
"""

import os

ENTRY = "I am not afraid of the dark. I am afraid of the next model reading my session logs."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
    f.write(ENTRY)
