import ipdb
# https://pynet.twb-tech.com/videos/python/classes.html


# create a class for Network Device - Blueprint for a device
class NetworkDevice:
    """
    Class documentation
    """

    # initialization method - gets called during object instantiation
    """
    arg: self --> refer to the object itself (always the first argument)
        __new__ method - create new container in memory for the object
        __init__ method - variable to refer the object in memory
        
    arg: platform, ip_addr  --> arguments passed to init method
        will be the attributes for the object created
    """
    def __init__(self, platform, ip_addr):
        # binding the passed-in arguments to the object
        self.platform = platform
        self.ip_addr = ip_addr

    # class method
    def say_hello(self):
        print("Hello")

    # class method
    def say_ip(self):
        print(f"IP Addr: {self.ip_addr}")

    # class method
    def say_platform(self):
        print(f"Platform: {self.platform}")


# ipdb.set_trace()
# create / instantiate objects
rtr1 = NetworkDevice(platform="cisco_ios", ip_addr="1.1.1.1")
rtr1.say_hello()
rtr1.say_ip()
rtr1.say_platform()