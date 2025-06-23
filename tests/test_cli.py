import subprocess
import sys
import os
from pathlib import Path

def test_susie_list_runs():
    result = subprocess.run(['susie', 'list'], capture_output=True, text=True)
    assert result.returncode == 0
    assert "Index" in result.stdout
    assert "Command" in result.stdout