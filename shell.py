# -*- coding: utf-8 -*-

import subprocess
import shlex
def ran():
	''' компиляция и запуск временного файла tmp.pas'''
	cmd = 'fpc tmp.pas'
	args = shlex.split(cmd)
	p = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	result = p.communicate()[0]
	if 'Error' in result:
		print result
	else:
		cmd = './tmp'
		args = shlex.split(cmd)
		p = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
		result = p.communicate()[0]
		print result

def ran1():
	''' компиляция и запуск временного файла tmp.pas'''
	cmd = 'fpc st.pas'
	args = shlex.split(cmd)
	p = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	result = p.communicate()[0]
	if 'Error' in result:
		print result
	else:
		cmd = './st'
		args = shlex.split(cmd)
		p = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
		result = p.communicate()[0]
		print result



	'''
	cmd = 'fpc tmp.pas'
	PIPE = subprocess.PIPE
	p = subprocess.Popen(cmd, shell = True)
	p.wait()
	print '\n ----------OUTPUT---------\n'
	cmd = './tmp'
	p = subprocess.Popen(cmd, shell = True)
	p.wait()
	'''
