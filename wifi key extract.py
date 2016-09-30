import os
print "[####################################]"
print "[wifi key extracter by jayaram yalla ]"
print "[++++++++++++++++++++++++++++++++++++]"
print "[https://linkedin.com/jayaramyalla   ]"
print "[++++++++++++++++++++++++++++++++++++]"
print "[https://twitter.com/jayaramyalla    ]"
print "[####################################]"

hotspot=os.popen('''netsh wlan show profiles | find "All User Profile     :"''').read().replace("    All User Profile     : ","").split("\n")
cmd='''netsh wlan show profile name="%s" key="clear" | find "Key Content"'''
print "\n\n\n"
for i in hotspot:
    cmd2=cmd % i
    p=os.popen(cmd2).read().replace("    Key Content            :","").replace("\n","")
    print i+":"+p

raw_input("press enter to exit")


#code by jayaram yalla
#https://linkedin.com/jayaramyalla
#https://twitter.com/jayaramyalla
