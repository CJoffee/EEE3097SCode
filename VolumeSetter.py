import subprocess
import sys

subprocess.call(["amixer", "set", "PCM","--", sys.argv[1] + "%"])
