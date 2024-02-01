# Learning LangChain
# in 20234
# (c) Ricky Macharm, MScFE
# https://www.SisengAI.com
#
#

import os
OPENAI_API_KEY='sk-IwillNeverUseThisKeyInARealApplication'
# I'm omitting all other keys
def set_environment():
    variable_dict = globals().items()
    for key, value in variable_dict:
        if "API" in key or "ID" in key:
            os.environ[key] = value
