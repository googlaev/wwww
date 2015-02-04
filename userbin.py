# -*- coding: utf-8 -*-
import os
import subprocess
import shlex
def run():
    '''# реализация пользовательского режима'''
    while 1:
        a = raw_input('user# ')
        list_com = os.listdir('./user/bin')
        if a in list_com:
            for i in list_com:
                if a == i:
                    runbim(a)
        elif 'man' in a: #== a.split(' ')[0]:
            reade_man(a)
        elif 'exit' in a:
            break
        elif 'ls' in a:

            for i in list_com:
                print i
        else:
            print 'not comand'

def runbim(comand):
    '''запуск пользовательских программам '''
    cmd = './user/bin/' + comand
    args = shlex.split(cmd)
    p = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    result = p.communicate()[0]
    print result

def reade_man(man):
    '''вывод документации по пользовательским программам '''

    man = man.split(' ')
    list_man = os.listdir('./user/doc')
    for i in list_man:
        if man[1]+'.txt' == i:
            f = open('./user/doc/'+i)
            for l in f:
                 print l.rstrip()
