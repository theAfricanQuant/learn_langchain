# Learning LangChain
# in 20234
# (c) Ricky Macharm, MScFE
# https://www.SisengAI.com
#
#

"""This module extracts information from your `.env` file.
"""
from pathlib import Path
from pydantic import BaseSettings

def return_full_path(filename: str = ".env") -> str:
    """Returns the correct path of the `.env` file using the current working directory."""
    # Get the current working directory
    cwd = Path.cwd()
    # Join the current working directory with the filename
    full_path = cwd / filename
    return str(full_path)

class Settings(BaseSettings):
    """Uses pydantic to define settings for project."""

    OPENAI_API_KEY: str
    HUGGINGFACEHUB_API_TOKEN: str

    class Config:
        env_file = return_full_path(".env")

# Create instance of `Settings` class that will be imported
# in lesson notebooks and the other modules for application.
settings = Settings()
