import app
import os
import subprocess

# print(app)
# help(app)
# print(id(help(app)))
# print(app)
# os.kill(id(app), 9)

# os.kill(id(help(app)), 9)

# p1 = subprocess.Popen([app])

pid = app.os.getpid()
help('app')

p1 = subprocess.Popen([app])
p1.terminate()
# app.__doc__
# app._doc_