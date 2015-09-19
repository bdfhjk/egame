import subprocess
import os
import sys

def start_brain():
    stdout.write('>>> Starting brain')
    grunt_process = subprocess.Popen(
            ['grunt --gruntfile=brain/Gruntfile.js'],
            shell=True,
            stdin=subprocess.PIPE,
            stdout=stdout,
            stderr=stderr,
        )

start_brain()
