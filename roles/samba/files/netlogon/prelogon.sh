#!/bin/bash
#
# Generate logon script for windows (or dos)
#
# parameters :
# %m (machine netbios name) %U (user) %a (architecture) %g (group) %L (server)
# $1                        $2        $3                $4         $5

#--------------------------- ERRORS LOG --------------------------------------- 
# for the new files
umask 022

SAMBA_DIR=/var/lib/samba/

# if you need the errors messages
exec 2>>"$SAMBA_DIR/logon_script.err"
# if you prefer the errors messages by machine name, comment the preceding line
# and uncomment :
#exec 2>>"$SAMBA_DIR/var/logon_script.$1.err"

# if you need SHELL DEBUG, in the errors messages file, uncomment :
#set -x

#--------------------------- FUNCTIONS ---------------------------------------- 
# end of line in windows world : CR+NL
# echo -n "WINDOWS_COMMAND"; echo -e '\r'
# do the trick.
# use "write" to write in the logon script
write () { echo -n "$@"; echo -e '\r'; }

#--------------------------- VARIABLES ----------------------------------------
CLIENT_MACHINE="$1"
USER="$2"
SYSTEM_TYPE="$3"
GROUP="$4"
GROUPNAME=$(echo "$GROUP" | sed -e 's/[0-9]//g')
SERVER_NAME="$5"
echo "$1 $2 $4 $4 $5">>"$SAMBA_DIR/logon_script.err"

SUFFIX=bat

#--------------------------- HEADER -------------------------------------------
SCRIPT="$SAMBA_DIR/netlogon/$GROUP.$SUFFIX"

# this redirection mean all the standard output go in the logon script
exec 1>"$SCRIPT"

# to hidden the script, (need "map hidden = yes", see in "man smb.conf")
chmod o+x "$SCRIPT"

#--------------------------- BODY ---------------------------------------------
write "@ECHO off"

write "ECHO."
write "ECHO Type : $SYSTEM_TYPE."
write "ECHO."
write "ECHO Computer : $CLIENT_MACHINE - User : $USER - Group : $GROUP."
write "ECHO."

# perhaps some tools used in the logon script are on the server
# write "PATH %path%;\\\\$SERVER_NAME\parameters\bin"

# set the workstation time at the server time
write "NET TIME \\\\$SERVER_NAME /set /yes"

# perhaps you need non persistent connexion
# write "NET USE /persistent:no"

# mount the home share

# command depend on client machine
# case "$CLIENT_MACHINE" in
# pc1)
# 	write "....."
# 	write "....."
# 	;;
# pc2)
# 	write "....."
# 	;;
# *)
# # other PCs
# 	write "....."
# esac

# mount depend on user
if [ "$USER" = jan ] || [ "$USER" = ania]; then
    write "net use y: \\\\$SERVER_NAME\\prace /yes"
    write "net use q: \\\\$SERVER_NAME\\serwer_homes /yes"
else
    write "NET USE z: \\\\$SERVER_NAME\\$GROUPNAME /yes"
fi

# mount depend on group


# command depend on system type
# if [ "$SYSTEM_TYPE" = Win95 ]; then
# 	.....
# fi
#
# if [ "$SYSTEM_TYPE" = WinNT ]; then
# 	.....
# fi

#--------------------------- IN OUR CLASSROOMS --------------------------------
# example : clients are named xxYYcZZ and printers xxYYpZZ
# xx: building prefix, YY: classroom number, ZZ: identifier numbers
# xxYY est the classroom

# common share by classroom
write "NET USE k: \\\\$SERVER_NAME\\informatyka /yes"


