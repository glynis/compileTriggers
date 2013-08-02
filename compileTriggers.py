# This script takes the ecode column from an eventlist (which contains buttonpress information)
# and a list of target triggers (which contains condition information),
# and outputs an updated version of the ecode column including both buttonpress and condition information.
# Created by Glynis MacMillan on 11/30/2012 


import os

start = int(raw_input('Starting from Subject#:'))
end = int(raw_input('Up to Subject#:'))

print('########## Separate ecode column from eventlist ##########')

for s in range(start,end+1):
    subj=str(s)
    with open('s'+subj+'.txt') as f_in:
        with open('s'+subj+'_column.txt', 'w') as f_out:
            for line in f_in:
                if line[0] != '#' and len(line.split()) > 0 :
                    f_out.write(line.split()[2]+'\n')
                # else: print 'passing by', line....

print('########## Combine ecode and target triggers ##########')

for s in range(start,end+1):
    subj=str(s)
    print('Subject#'+subj+' ...')
    
    trigrFilename = 'Subject'+subj+'_triggers.txt'
    trigr = open(trigrFilename, 'r')
    triggerfull = trigr.read()
    trigger = triggerfull.strip('\n')
    trigger_split = trigger.split('\n')

    ecodeFilename ='s'+subj+'_column.txt'
    ecode = open(ecodeFilename, 'r')
    eventcodefull = ecode.read()
    eventcode = eventcodefull.strip('\n')
    ecode_split = eventcode.split('\n')
               
    ready = False
    counter = 0 # this counts how many lines were copied from triggers_split
    count250ecode = 0 # this counts how many lines (in ecode/eventlist) are 250+

    lengthEcode = len(ecode_split)
    
    with open('s'+subj+'_buttonpress.txt', 'w') as out:
        for i in xrange(lengthEcode):
            if i == lengthEcode-1:
                outline = ecode_split[i]
            else:
                outline = ecode_split[i] + '\n' 
            if ready and int(ecode_split[i]) < 250:
                outline = trigger_split[counter]
                counter +=1
            elif not ready and int(ecode_split[i]) == 9:
                ready = True
                print('ready')
                counter += 1 # this assumes that '9' replaces the first experiment triggers for all subjects
            out.write(outline)
            
        if counter == len(trigger_split):
            print('DONE. All lines in '+trigrFilename+' are used.')
        else:
            print('DONE. WARNING: Not all lines in '+trigrFilename+' are used.')
        
print('########## Check length of ecode and new trigger list ##########')

for s in range(start,end+1):
    subj=str(s)
    print('Subject#'+subj+' ...')

    button = open('s'+subj+'_buttonpress.txt', 'rU')
    buttonpress = button.read()
    button_split = buttonpress.split('\n') # MacOS will not read the \n inserted earlier as a linebreak, need rU instead.
    ecode = open('s'+subj+'_column.txt', 'rU')
    eventcode = ecode.read()
    ecode_split = eventcode.split('\n')

    ready = False
    
    if len(button_split) == len(ecode_split):
        for i in range(len(button_split)):
            if not ready and (button_split[i] == '9'):
                ready = True
                print('ready')
            elif (ecode_split[i] == '1'):
                if (button_split[i] != '1'):
                    print('Aborted: Mismatch first detected in line# '+str(i))
                    break
        else:
            print('okay')
    else:
        print(button, ecode)
        print(len(button_split), len(ecode_split))
        print('difference: ' + len(button_split)-len(ecode_split))
        print('Aborted: Not equal length.')


