#  MJH One-Bit Machine Type 01
#
#    by Michael John Hawks (so far)
#      language: Python 3
#    2020/02/18  17:36
#  
#############################################################################  
#  
#  INTRODUCTION
#  
#  This PYTHON3 program emulates an imaginary one-bit "computer" that
#  implements the "ob1" programming language ("ob1" is discussed later).
#  
#          "ob1" = One-Bit machine (type 1) programming language
#          ... affectionately nicknamed "Obi-Wan Kenobi"
#
#  Briefly, this implementation of "ob1" consists of a 16 x 16 bit data
#  field, a one bit flag, and a data-field pointer. That's it.
#
#  (Theoretically, "ob1" could operate within a data field extending infinitely
#  in all directions. Wow man. That blows my mind.)
#  
#  One could say that user input and output are memory-mapped because the
#  entire data field and flag are always on display and the user can
#  set/reset any of the bits and flag as well as move the data-field
#  pointer around. The virtual computer reacts to what it finds
#  in the data field.
#  
#  The "ob1" user program (supplied by the user by creating a separate file
#  on a text editor) can best be visualized as a separate reel of punched
#  paper tape that can be read forward or backward. The program is NOT
#  stored in the data field.
#  
#  Use any standard text editor to prepare a program file and call it
#  anything you want (I use an *.ob1 extention for my files but you don't
#  have to if you don't want to).
#  
#  Details of the "ob1" programming language will be discussed later.
#  
#############################################################################  
#  
#  USER INTERFACE
#  
#  When you first run this program the initial message tells you how big the
#  Python 3 display window should be. If you don't see all the asterisks
#  adjust the size of the display window until you do.
#  
#  Hit <ENTER> to move on.
#  
#  Next you are presented with a visual representation of the 16x16 bit data
#  field and you are given the opportunity to DO THINGS. Here's what you
#  can do:
#  
#  To load a user "ob1" program, enter the "path/filename" in quotes.
#      NOTE: If your "ob1" program is in the same folder as
#            "MJH One-Bit Machine Type 01 - b001.py",
#            there's a good chance you won't need a pathname.
#      ALSO: If "MJH One-Bit Machine Type 01 - b001.py" doesn't like
#            your program, it'll complain and you'll hear about it!
#  
#  To run that program, hit <ENTER>.
#
#  While a program isn't running you can do these things:
#  
#  Enter "s" to step through the program one instrution at a time
#      (this isn't as interesting as you might hope... BORING!).
#  
#  To exit the "ob1" program merely load a different one.
#  
#  Enter "l" to move the data pointer left
#  Enter "r" to move the data pointer right
#  Enter "u" to move the data pointer up
#  Enter "d" to move the data pointer down
#  Enter "h" to move the data pointer to "HOME" position (bottom left)
#  
#  Enter "0" to set the indicated bit in the data field to "0"
#  Enter "1" to set the indicated bit in the data field to "1"
#  Enter "f" to toggle the flag bit
#  
#  Enter "q" to quit the user interface and exit.
#  
#############################################################################  
#  BUT WAIT!!! THERE'S MORE YOU CAN DO!!!
#############################################################################  
#  
#  To move the data pointer a given number of spaces, enter the direction
#  and the number of desired spaces.
#  
#  i.e.
#  
#  "l12" moves the data pointer 12 spaces left.
#  "r14" moves the data pointer 14 spaces right.
#  "u7" moves the data pointer up 7 spaces.
#  "d3" moves the data pointer down 3 spaces.
#  
#  "r3659" moves the data pointer right as far as it's allowed to go.
#      No error occurs.
#  
#  To place a STRING of binary bits into the data field, merely position
#      the data pointer and enter a string of "0"s and "1"s.
#  
#  i.e.
#  
#  "10011101" puts that bit string in the data field starting with
#      wherever the data pointer is. If the string is too long to fit,
#      it'll just put in what it can (no error).
#  
#  HINT: There is no command to clear a row or the entire screen.
#      But if you wish to clear a row, position the data pointer on the
#      leftmost bit and enter "000000000000000000000000000000000000000".
#      Due to the repeating keyboard, it's easy to come up with a long
#      string of "0"s.
# 
#############################################################################  
#  HEY LOOK! HERE'S SOMETHING ELSE YOU CAN DO!!!
#############################################################################
#  
#  To change the appearance of the bits in the data field, enter
#  
#  "z<character 0><character 1>".
#
#  So by entering "z.X", the "0" bits will instead be displayed as "."
#  and the "1" bits will be displayed as "X".
#
#  To return to the standard "0" and "1" display, enter "z" all by itself.  
#  
#############################################################################  
#############################################################################  
#
#  The "ob1" programming language
#  
#############################################################################  
#############################################################################  
#
#  ob1
#  
#  Instruction Set & Mnemonics
#  (Eight-Bits per Instruction)
#  
#  Headers:
#  
#      0000
#       thru
#      0111 - (not used, undefined)
#  
#      1000,bbbb - tag,
#      1001,bbbb - adv,
#      1010,bbbb - ret,
#      1011,bbbb - exec,
#      1100,bbbb - ifd0,
#      1101,bbbb - ifd1,
#      1110,bbbb - iff0,
#      1111,bbbb - iff1,
#  
#  Operations:
#  
#      bbbb,0000 - r
#      bbbb,0001 - l
#      bbbb,0010 - u
#      bbbb,0011 - d
#      bbbb,0100 - h
#      bbbb,0101 - x
#      bbbb,0110 - sk
#      bbbb,0111 - ex
#      bbbb,1000 - df
#      bbbb,1001 - dc
#      bbbb,1010 - d0
#      bbbb,1011 - d1
#      bbbb,1100 - fd
#      bbbb,1101 - fc
#      bbbb,1110 - f0
#      bbbb,1111 - f1
#  
#  Headers:
#  
#   tag,
#  Merely serves as a tag to identify a place in the program. Tag id
#  can be 0 through 15. No operation is executed.
#  
#   adv,
#  Advance program to the next "tag," with the same id as proclaimed
#  by the "adv," instruction (0 through 15).
#  
#   ret,
#  Retreat program to the previous "tag," with the same id as
#  proclaimed by the "ret," instruction (0 through 15).
#  
#   exec,
#  Always and unconditionally perform the indicated operation.
#  
#   ifd0,
#  Only perform the indicated operation if the current data bit is
#  reset to "0".
#  
#   ifd1,
#  Only perform the indicated operation if the current data bit is
#  set to "1".
#  
#   iff0,
#  Only perform the indicated operation if the flag bit is reset to "0".
#  
#   iff1,
#  Only perform the indicated operation if the flag bit is set to "1".
#  
#  
#  Operations:
#  
#   r - Move data pointer one position to the right
#   l - Move data pointer one position to the left
#   u - Move data pointer one position up
#   d - Move data pointer one position down
#   h - Move data pointer to "HOME" position - (0,0) or bottom left
#   x - HALT program execution (HALT advances to the next program
#         instruction then gives control back to the user)
#   sk - SKIP the next instruction
#   ex - EXCHANGE data bit and flag
#   df - Load data bit with flag bit.
#   dc - Compliment data bit
#   d0 - Reset data bit to "0"
#   d1 - Set data bit to "1"
#   fd - Load flag with data bit
#   fc - Compliment flag
#   f0 - Reset flag to "0"
#   f1 - Set flag to "1"
#
#  Line numbers and comments:
#  
#  Line numbers can precede the "@" character.
#      The "@" character and anything preceding it will be ignored.
#  Comments can follow the "#" sign.
#      The "#" character and anything following it will be ignored.
#  
#  Blank (or empty) lines (or lines filled with spaces) are ignored.
#  
#############################################################################  
#############################################################################  
#  
#  EXAMPLE "ob1" PROGRAMS:
#  
#############################################################################  
#     ####  This ob1 program advances the data pointer to the right 
#     ####  until a "1" bit is encountered. If no "1" is found
#     ####  a run-time error occurs.
#     tag,0    #  This identifies the beginning of the search loop
#     ifd0,sk  #  Does the current bit equal "0"? If so skip next instruction
#     adv,1    #  If not, advance program to "tag,1" (the exit point)
#     exec,r   #  Move data pointer right (If out of bounds an error occurs!)
#     ret,0    #  Go back to "tag,0" and repeat loop
#     tag,1    #  This is the exit point
#############################################################################  
#     ####  This ob1 program copies the first three bits of the bottom line
#     ####  into the line above it.
#     000 @  exec,h   #  Moves data pointer to the far bottom left of field
#     #  Do bit 1:
#     001 @  exec,fd  #  Copy the indicated bit into the flag
#     002 @  exec,u   #  Move data pointer up
#     003 @  exec,df  #  Copy the flag bit into the indicated position
#     004 @  exec,d   #  Move data pointer down
#     005 @  exec,r   #  Move data pointer right
#     #  Do bit 2:
#     006 @  exec,fd  #  Copy the indicated bit into the flag
#     007 @  exec,u   #  Move data pointer up
#     008 @  exec,df  #  Copy the flag bit into the indicated position
#     009 @  exec,d   #  Move data pointer down
#     010 @  exec,r   #  Move data pointer right
#     #  Do bit 3:
#     011 @  exec,fd  #  Copy the indicated bit into the flag
#     012 @  exec,u   #  Move data pointer up
#     013 @  exec,df  #  Copy the flag bit into the indicated position
#     #  Exit point of program
#############################################################################
############################################################################# 
#  
#  Have fun!
#  
#############################################################################
#############################################################################
#  
# 
print()
print('******************************************************************')
print('*                                                                *')
print('*                                                                *')
print('*                                                                *')
print('*                                                                *')
print('*                                                                *')
print('*                                                                *')
print('*                                                                *')
print('*                                                                *')
print('*                                                                *')
print('*                                                                *')
print('*                                                                *')
print('*                                                                *')
print('*                                                                *')
print('*                                                                *')
print('*                                                                *')
print('*                                                                *')
print('*                                                                *')
print('*                                                                *')
print('*                                                                *')
print('*                                                                *')
print('*                                                                *')
print('*                                                                *')
print('*                                                                *')
print('*                                                                *')
print('*                                                                *')
print('*                                                                *')
print('*                                                                *')
print('*                                                                *')
print('*                                                                *')
print('*                                                                *')
print('*                                                                *')
print('*                                                                *')
print('*                                                                *')
print('*                                                                *')
print('*  "MJH One-Bit Machine Type 01"                                 *')
print('*  should run in a window at least 66 characters wide            *')
print('*  and 40 characters high for best results.                      *')
print('*                                                                *')     
dummy = input('*****  Hit <ENTER> to continue.  *********************************')

def func_get_number(this_str):
    try:
        if len(this_str) > 1:
                z = int(this_str[1 :])
        else:
                z = 1
        return z
    except ValueError:
        print("????")
        return 0

def func_data_bits(this_str):
    old_str = mem[memy]
    new_str = old_str[ : memx * 3]
    bad_error = "So far, so good."
    i=0
    while i < len(this_str):
        bit_str = this_str[i]
        if bit_str == "0" or bit_str == "1":
            new_str = new_str + " " + bit_str + " "
        else:
            bad_error = "TROUBLE!"
        i += 1
    new_str = new_str + old_str[(i + memx) * 3 : ]
    new_str = new_str[ : 48]
    if bad_error == "TROUBLE!":
        new_str = old_str
        print("?????")
    return new_str

def func_read_prog(filename):
    bad_error = 0
    
    try:
        prog_file = open(filename[1 : -1], "r")
    
        xline = prog_file.readline()
        
        line_number = 0
        bad_error = 0    

        while xline != "":
            print(xline[:-1])
            line_number += 1
            workline = xline.upper()[:-1]
            
            if workline != "":         
                if workline.find("#") >= 0:
                    workline = workline[ : workline.find("#")]
                if workline.find("@") >= 0:
                    workline = workline[workline.find("@") + 1 : ]
                    
                workline = workline.strip()

                if workline != "":
                    xcode = 0
                    comma = workline.find(",")
                    if comma == -1:
                        print("No comma")
                        bad_error = 1
                        break
                    chunk = workline[:comma]
                    if chunk == "TAG":
                        xcode = 128
                    elif chunk == "ADV":
                        xcode = 144
                    elif chunk == "RET":
                        xcode = 160
                    elif chunk == "EXEC":
                        xcode = 176
                    elif chunk == "IFD0":
                        xcode = 192
                    elif chunk == "IFD1":
                        xcode = 208
                    elif chunk == "IFF0":
                        xcode = 224
                    elif chunk == "IFF1":
                        xcode = 240
                    else:
                        print("Unknown header")
                        bad_error = 2
                        break
                
                    chunk = workline[comma + 1 :]
                    if chunk == "R":
                        xcode = xcode + 0
                    elif chunk == "L":
                        xcode = xcode + 1
                    elif chunk == "U":
                        xcode = xcode + 2
                    elif chunk == "D":
                        xcode = xcode + 3
                    elif chunk == "H":
                        xcode = xcode + 4
                    elif chunk == "X":
                        xcode = xcode + 5
                    elif chunk == "SK":
                        xcode = xcode + 6
                    elif chunk == "EX":
                        xcode = xcode + 7
                    elif chunk == "DF":
                        xcode = xcode + 8
                    elif chunk == "DC":
                        xcode = xcode + 9
                    elif chunk == "D0":
                        xcode = xcode + 10
                    elif chunk == "D1":
                        xcode = xcode + 11
                    elif chunk == "FD":
                        xcode = xcode + 12
                    elif chunk == "FC":
                        xcode = xcode + 13
                    elif chunk == "F0":
                        xcode = xcode + 14
                    elif chunk == "F1":
                        xcode = xcode + 15
                    else:
                        try:
                            trial_number = int(chunk)
                            if (trial_number > 15) or (trial_number < 0):
                                
                                print("Numeric expression out of range")
                                bad_error = 3
                                break
                            else:
                                xcode = xcode + trial_number
                        except:
                            print("Instruction or number expected")
                            bad_error = 4
                            break

                    #print("#! >>>",xcode) ###  I'm commenting this
                    #                      ###   print line out because
                    #                      ###   it clutters the screen
                    #                      ###  and nobody cares anyway!
                    
                    proglist.append(xcode)
            xline = prog_file.readline()
            
        prog_file.close()

        print(">>>",filename)
        if bad_error != 0:
            print(">>> Error", bad_error, "in line", line_number)
        else:
            print(">>> Successful Program Load")
    except:
        print(">>>",filename,"can't be opened.")
        bad_error = 5
    return bad_error

def func_format_progline(pcounter):

    if pcounter < 0 or pcounter >= len(proglist):
        return "#"
    else:
        header = int(proglist[pcounter] // 16)
        optype = int(proglist[pcounter] % 16)
        
        if header == 8:
            that_str = "tag,"
        elif header == 9:
            that_str = "adv,"
        elif header == 10:
            that_str = "ret,"    
        elif header == 11:
            that_str = "exec,"
        elif header == 12:
            that_str = "ifd0,"    
        elif header == 13:
            that_str = "ifd1,"
        elif header == 14:
            that_str = "iff0,"    
        elif header == 15:
            that_str = "iff1,"
        else:
            that_str = "#???,"

        if header < 11:
            that_str = that_str + str(optype)
        elif optype == 0:
            that_str = that_str + "r"
        elif optype == 1:
            that_str = that_str + "l"
        elif optype == 2:
            that_str = that_str + "u"        
        elif optype == 3:
            that_str = that_str + "d"        
        elif optype == 4:
            that_str = that_str + "h"
        elif optype == 5:
            that_str = that_str + "x"
        elif optype == 6:
            that_str = that_str + "sk"        
        elif optype == 7:
            that_str = that_str + "ex"
        elif optype == 8:
            that_str = that_str + "df"
        elif optype == 9:
            that_str = that_str + "dc"
        elif optype == 10:
            that_str = that_str + "d0"        
        elif optype == 11:
            that_str = that_str + "d1"
        elif optype == 12:
            that_str = that_str + "fd"
        elif optype == 13:
            that_str = that_str + "fc"
        elif optype == 14:
            that_str = that_str + "f0"        
        elif optype == 15:
            that_str = that_str + "f1"        
        else:
            that_str = that_str + "#?"
        return that_str



############################################################################
###                                                                      ###
###                               MAIN                                   ###
###                                                                      ###
############################################################################
    
print()
proglist = []
program_counter = -1
str_0="0"
str_1="1"
mem = []
memx = 0
memy = 0
flag = "0"
exception = "ok"
name = ""

i=0
while i < 16:
    mem = mem + [" 0 " * 16]
    i += 1

quit = 0

while quit == 0:
    print()
    print('To load a program, enter "path/filename" in quotes.')
    print('<ENTER>=run s=step l=left r=right u=up d=down h=home')
    print('0=reset_bit 1=set_bit f=toggle_flag q=quit')
    print('*** See comments in listing for more options ***')

    displayed_op = program_counter - 11
    i=15
    while i >= 0:
        displayed_op += 1
        this_str = mem[i]
        this_str = this_str.replace("0",str_0)
        this_str = this_str.replace("1",str_1)
        
        if i == 10:
            this_str = this_str + str(program_counter).rjust(6) + " >>>"
        else:
            this_str = this_str+ "          "
        print(this_str , func_format_progline(displayed_op))

        displayed_op += 1      
        if memy == i:
            this_str = ("   " * memx) + "*^*" + ("   " * (15 - memx))
        else:
            this_str = (" " * 48)
        print(this_str , "         ", func_format_progline(displayed_op))
        i -= 1

    print("******************** FLAG=" + flag +  " ********************           ######&")
    print(name)
    print(exception)

    exception = "ok"
    
    search_for_this = 0
    cmd = ""
    console_cmd = input()

    if console_cmd != "":
        cmd = console_cmd[0]
  
    if cmd == "l":  
        memx -= func_get_number(console_cmd)
        if memx < 0:
            memx = 0
        if memx > 15:
            memx = 15
    elif cmd == "r":
        memx += func_get_number(console_cmd)
        if memx < 0:
            memx = 0
        if memx > 15:
            memx = 15
    elif cmd == "u":
        memy += func_get_number(console_cmd)
        if memy < 0:
            memy = 0
        if memy > 15:
            memy = 15
    elif cmd == "d":
        memy -= func_get_number(console_cmd)
        if memy < 0:
            memy = 0
        if memy > 15:
            memy = 15
    elif console_cmd == "h":
        memx = 0
        memy = 0
    elif console_cmd == "f":
        if flag == "0":
            flag = "1"
        else:
            flag = "0"
    elif cmd == "0":
        mem[memy] = func_data_bits(console_cmd)
        
    elif cmd == "1":
        mem[memy] = func_data_bits(console_cmd)
    elif cmd == "z":
        this_str = console_cmd + "01"
        str_0 = this_str[1]
        str_1 = this_str[2]


##################################################################
        
    elif console_cmd == "s" or console_cmd == "":
        mode = "run"
        if console_cmd == "s":
            mode = "step"

        exception = "ok"

        if len(proglist) == 0:
            exception = "no program loaded"
        else:
            if program_counter < 0:
                exception = "what happened???"
            elif program_counter >= len(proglist):
                program_counter = 0
                exception = "ok"

        while exception == "ok":
               
            header = int(proglist[program_counter] / 16)
            opcode = int(proglist[program_counter] % 16)
            do_op = "no"
            exception = "ok"

            if header == 9 or header == 10:  ############ adv/ret
                
                if header == 9:      # adv
                    noodle = 1
                elif header == 10:   # ret
                    noodle = -1
                
                search_for_this = 128 + opcode # because (header of "tag") * 16 = 128
                trial_pc = program_counter
                proglist_length = len(proglist)
                
                keep_going = "yes"

                while keep_going == "yes":
                    trial_pc += noodle
                    if trial_pc < 0 or trial_pc >= proglist_length:
                        keep_going = "tag not found"
                        exception = "tag not found"
                    else:
                        if proglist[trial_pc] == search_for_this:
                            keep_going = "tag found"
                            program_counter = trial_pc - 1
                    
            elif header == 11:   # exec
                do_op = "yes"
            elif header == 12:   # ifd0
                if mem[memy][(3 * memx) + 1] == "0":
                    do_op = "yes"
                else:
                    do_op = "no"
            elif header == 13:   # ifd1
                if mem[memy][(3 * memx) + 1] == "1":
                    do_op = "yes"
                else:
                    do_op = "no"
            elif header == 14:   # iff0
                if flag =="0":
                    do_op = "yes"
                else:
                    do_op = "no"
            elif header == 15:   # iff1
                if flag =="1":
                    do_op = "yes"
                else:
                    do_op = "no"
            
            else:                # Includes tag
                do_op = "no"
            

            if do_op == "yes":
                if opcode == 0:      #### r
                    memx += 1
                    if memx > 15:
                        memx = 15
                        exception = "data pointer out of range"
                elif opcode == 1:    #### l
                    memx -= 1
                    if memx < 0:
                        memx = 0
                        exception = "data pointer out of range"
                elif opcode == 2:    #### u
                    memy += 1
                    if memy > 15:
                        memy = 15
                        exception = "data pointer out of range"
                elif opcode == 3:    #### d
                    memy -= 1
                    if memy < 0:
                        memy = 0
                        exception = "data pointer out of range"
                elif opcode == 4:    #### h
                    memx = 0
                    memy = 0
                elif opcode == 5:    #### x
                    exception = "halt"
                elif opcode == 6:    #### sk
                    program_counter += 1
                elif opcode == 7:    #### ex
                    old_flag = flag
                    flag = mem[memy][(3 * memx) + 1]

                    old_str = mem[memy]
                    new_str = old_str[ : 1 + (memx * 3)]
                    new_str = new_str + old_flag
                    new_str = new_str + old_str[(memx * 3) + 2 : ]
                    #new_str = new_str[ : 48]
                    mem[memy] = new_str
                    
                elif opcode == 8:    #### df
                    old_str = mem[memy]
                    new_str = old_str[ : 1 + (memx * 3)]
                    new_str = new_str + flag
                    new_str = new_str + old_str[(memx * 3) + 2 : ]
                    #new_str = new_str[ : 48]
                    mem[memy] = new_str
                    
                elif opcode == 9:    #### dc
                    data_bit = mem[memy][(3 * memx) + 1]
                    
                    if data_bit == "0":
                        data_bit = "1"
                    else:
                        data_bit = "0"

                    old_str = mem[memy]
                    new_str = old_str[ : 1 + (memx * 3)]
                    new_str = new_str + data_bit
                    new_str = new_str + old_str[(memx * 3) + 2 : ]
                    #new_str = new_str[ : 48]
                    mem[memy] = new_str

                elif opcode == 10:   #### d0
                    old_str = mem[memy]
                    new_str = old_str[ : 1 + (memx * 3)]
                    new_str = new_str + "0"
                    new_str = new_str + old_str[(memx * 3) + 2 : ]
                    #new_str = new_str[ : 48]
                    mem[memy] = new_str

                elif opcode == 11:   #### d1
                    old_str = mem[memy]
                    new_str = old_str[ : 1 + (memx * 3)]
                    new_str = new_str + "1"
                    new_str = new_str + old_str[(memx * 3) + 2 : ]
                    #new_str = new_str[ : 48]
                    mem[memy] = new_str

                elif opcode == 12:   #### fd
                    flag = mem[memy][(3 * memx) + 1]

                elif opcode == 13:   #### fc
                    if flag == "0":
                        flag = "1"
                    else:
                        flag = "0"
                        
                elif opcode == 14:   #### f0
                    flag = "0"
                elif opcode == 15:   #### f1
                    flag = "1"
                else:               #### undefined error (should never happen)
                    exception = "undefined error"

            if exception == "ok" or exception == "halt":
                program_counter += 1
                if program_counter >= len(proglist):
                    exception = "Program terminated normally"

            if mode == "step" and exception == "ok":
                exception = "step"

###################################################################


        
    elif console_cmd == "q":
        quit = 1
    elif cmd == '"':
        name = console_cmd
        proglist = []
        xxx = func_read_prog(console_cmd)
        if len(proglist) > 0:
            program_counter = 0
        else:
            program_counter = -1

        if xxx == 0:
            exception = "ok"
        else:
            exception = "problem loading program"
            name = ""

    else:
        print("?????")
