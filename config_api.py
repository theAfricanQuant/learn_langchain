# Learning LangChain
# in 20234
# (c) Ricky Macharm, MScFE
# https://www.SisengAI.com
#
#

import os
OPENAI_API_KEY='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'
# I'm omitting all other keys
def set_environment():
    variable_dict = globals().items()
    for key, value in variable_dict:
        if "API" in key or "ID" in key:
            os.environ[key] = value
