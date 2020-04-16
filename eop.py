# eop program for python

### global ###
MAX_LINE_LEN = 1024
profile_data_nitems = 0
##############

#########################################################

### subst ###
def subst(s, c1, c2):
    return s.replace(c1, c2)
#############

### get_line ###
def get_line(fp):
    return subst(fp.readline(MAX_LINE_LEN + 1),"\n", "")
################

### new_profile ###
def new_profile(profile_list):
    print(profile_list) #debug
###################

### cmd_quite ###
def cmd_quite():
    print("bye.")
    exit()
#################

### exec_command ###
def exec_command(cmd_list):

    if cmd_list[0] == "%Q":
        cmd_quite()
    elif cmd_list[0] == "%C":
        print("%C command process")
    elif cmd_list[0] == "%P":
        print("%P command process")
    elif cmd_list[0] == "%R":
        print("%R command process")
    elif cmd_list[0] == "%W":
        print("%W command process")
    else:
        print("Invalid command")     
#######################

### parse_line ###
def parse_line(line):
    if line.find("%") == 0:
        cmd_list = line.split(" ")
        exec_command(cmd_list)
    else :
        profile_list = line.split(",")
        new_profile(profile_list)
##################

##### main #####
def main():
    f = open('lang.txt', 'r')
    line = get_line(f)

    while line:
        parse_line(line)
        line = get_line(f)
    f.close()
################

##決まり文句？(ggったら出てきた)##
if __name__ == "__main__":
    main()

