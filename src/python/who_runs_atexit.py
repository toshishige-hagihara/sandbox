import atexit
import grp
from optparse import OptionParser
import os
import pwd
import sys

### Implementation
def change_user(name):
    pwent = pwd.getpwnam(name)
    os.setgid(pwent.pw_gid)
    groups = [g.gr_gid for g in grp.getgrall() if pwent.pw_name in g.gr_mem]
    if len(groups) > 0:
        os.setgroups(groups)
    os.setuid(pwent.pw_uid)

def show_current_user():
    print os.getuid(), os.getgid(), os.getgroups()

### Main
usage = '%prog USER'
parser = OptionParser(usage)
(options, args) = parser.parse_args()

if len(args) < 1:
    parser.print_help()
    sys.exit(1)

show_current_user()
atexit.register(show_current_user)
change_user(args[0])
show_current_user()
