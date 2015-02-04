# -*- coding: utf-8 -*-

import shell
import userbin
prog=[]
def scrip():
        pg = []
        while 1:   # глобальный цикл инторпритатора
            a = raw_input('shell# ')

            if a == 'exit':
              break
            if 'run' in a :
               f = open('st.pas','w') # запись  текста программы в tmp.pas
               str1 =  '''
                program st;
                uses crt;
                var a,b,c,d,e,f,g,h:string;
                    i,j,k,m,n,o,p,q : integer;
                    r,s,t,u,v,w : real;
                    x,y,z: boolean;
                BEGIN
                '''


               f.write(str1 + '\n')
               for i in pg:
                 f.write(i+'\n')
               f.write('END.')
               f.close()
               shell.ran1()
               pg = []
               continue
            if a != '':
               pg.append(a)

while 1:   # глобальный цикл инторпритатора
    a = raw_input('> ')
    if 'user' in a:
      userbin.run()
      a = ''
    if 'shell' ==  a:
            scrip()
            prog = []
    if a != '':
       prog.append(a)
    if a == 'exit':
      break
    if ('end.' in a) or ('END.' in a) or ('End.' in a):
      f = open('tmp.pas','w') # запись  текста программы в tmp.pas

      for i in prog:
        f.write(i+'\n')

      f.close()
      shell.ran()
      prog = []

    #print a
