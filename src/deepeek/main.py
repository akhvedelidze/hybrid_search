#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from deepeek.crew import Deepeek

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'Does Benin have a centralized entry/exit system that records cross-border movement of travelers and captures relevant biographic and biometric data from individuals ? ?'
        
    }
    
    try:
        Deepeek().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


run ()