#!/usr/bin/env python

import subprocess
import sys
from pathlib import Path

if __name__ == "__main__":
    assert len(sys.argv) > 1, "Expected at least one dependency"

    for dependency in sys.argv[1:]:
        subprocess.run(["pip", "install", dependency])

        with (Path.cwd() / 'requirements.txt').open("a") as requirements_txt:
            try:
                pip_freeze = subprocess.Popen(("pip", "freeze"), stdout=subprocess.PIPE)
                output = subprocess.check_output(("grep", dependency), stdin=pip_freeze.stdout)
                requirements_txt.write(f"{output.decode().strip()}\n")
            except subprocess.CalledProcessError as e:
                print(f'Installing "{dependency}" failed ({e})')
                continue
