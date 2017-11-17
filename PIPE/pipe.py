from subprocess import Popen, PIPE

p = Popen('less', stdin=PIPE, stdout=PIPE)
p.communicate('Line number %d.\n' % x)
