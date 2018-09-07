import os ,shutil
src = "/home/nama/testpy"
des = "/home/nama/pytest"
for item in os.listdir(src):
    s = os.path.join(src , item)
    d = os.path.join(des , item)
    if os.path.isdir(s):
        shutil.copytree(s ,d , False , None)
    else:
        shutil.copy2(s ,d)
