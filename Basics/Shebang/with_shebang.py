#! /usr/bin/python3
"""
#! is a shebang character sequence
after that absolute path of the interpreter
This will let the shell understand that this has to be interpreted using python3 from the path mentioned so
we don't have to explicitly mention   " python3 file_name.py "    to execute.
We can just use " ./file_name.py " to execute.

In scripting languages # is considered as a comment but #! is a special sequence which will be understood
by the shell itself.

In some cases executable permission won't be available for files by default so use " chmod +x filename.py " command
to give executable permission before executing.

This works only on linux platforms. Sorry windows users :(

"""
print("Life is beautiful")