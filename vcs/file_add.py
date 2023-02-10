# h3avren

import sys

with open('.vcs/vcs_stage.vcs', 'a') as file:
    for i in sys.argv[1:]:
        file.write( i + "\n")

