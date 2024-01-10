import monkey
def print1(self):
    print("This is the Modified Text that needs to be Displayed")

monkey.MP.monkey_patching = print1
obj1 = monkey.MP()
obj1.monkey_patching()

