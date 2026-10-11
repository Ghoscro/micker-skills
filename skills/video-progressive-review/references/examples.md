# A mock UI recording

Question: “Which setting did the operator change?”

An overview of a 60-second synthetic recording has tile 4 at 15.0s and tile 5 at 20.0s. Tile 4 shows a settings dialog, but the selected value is too small to read. Extract the original frame at 15.0s; if the selection occurs between the two overview frames, review a short sequence from 14–20s. Report the visible before/after values with timestamps. If the sequence lacks the selection moment, report the observed change and keep the click mechanism unknown.

Other cases:

- A 2-second clip needs only a few frames; 12 tiles is a starting point, not a quota.
- An audio-only file has no visual frames. Use audio or transcript evidence appropriate to the question.
- If a tiny label remains unreadable in the original, mark it unreadable instead of inferring it from the thumbnail.
- A generated sheet that the agent never opened supplies extraction artifacts, not an inspected video.
- The absence of an error dialog in 12 sampled frames leaves its occurrence between samples unknown.
