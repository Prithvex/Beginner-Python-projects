# Text to HandWriting

import pywhatkit as pw

txt= """ Kab tak doosron ki kahaani mein
Side character bane rahoge?
Kabhi apni film ke hero bhi ban jao"""

pw.text_to_handwriting(txt, "demo1.png", [0, 0 , 138])
print("END")