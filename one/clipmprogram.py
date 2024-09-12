import pyperclip
from imageio.v3 import improps

TEXT = {'agree': """Yes, I agree. That sounds fine to me.""",
        'busy': """Sorry, can we do this later this week or next week?""",
        'upsell': """Would you consider making this a monthly donation?"""}

import sys
if len(sys.argv) < 2:
    print("Usage: python clipmprogram.py [keyphrase] - copy phrase text")
    sys.exit()

key_phrase = sys.argv[1]

if key_phrase in TEXT:
    pyperclip.copy(TEXT[key_phrase])
    print('Text for '+key_phrase+' copied to clipboard')
else:
    print("Thers is not text for "+key_phrase)