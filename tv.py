
class Television(object):
    """A virtual tv"""
    
    def __init__(self, __channel, volume, is_on):
        ## setting constructor values
        self.__channel = __channel
        self.volume = volume
        self.is_on = is_on

    ##string statement shows status
    def __str__(self):
        if self.is_on == True:
            reply = "The TV is on channel "+str(self.__channel)+" and has a volume level of "+str(self.volume)+".\n"
        else:
            reply = "The TV is not currently on.\n"
        return reply

    ##turns the tv on/off with True/False statement
    def toggle_power(self):
        if self.is_on == True:
            self.is_on = False
        else:
            self.is_on = True

    ##Shows current channel
    def get_channel(self):
        print "The current channel: "+str(self.__channel)

    ##If TV is on, it will change the channel between 0-499
    def set_channel(self):
         if self.is_on == False:
            print "The television is currently off."
         else:
            while True:
                try:
                    change = raw_input("The available channels are 0-499. Which channel would you like to switch to? ")
                except:
                    print "Sorry, that's not an integer."
                else:
                    break
            if int(change) > 499 or int(change) < 0:
                print "This television only has channels 0-499."
            else:
                print "The channel has been switched to", change +"."
                self.__channel = int(change)

    ##Raises volume by 1 if TV is on
    def raise_volume(self):
        if self.is_on == False:
            print "The television is currently off."
        elif self.volume == 10:
            print "The television is already at max volume."
        else:
            print "The volume has been turned up by 1."
            self.volume += 1

    ##Lowers volume by 1 if TV is on
    def lower_volume(self):
        if self.is_on == False:
            print "The television is currently off."
        elif self.volume == 0:
            print "The television is already at the minimum volume."
        else:
            print "The volume has been turned down by 1."
            self.volume = self.volume - 1
       
#main
print "This program allows you to watch television.\n"
tv = Television(13, 4, True)

while True:
    print tv
    print "These are your menu choices:\n" \
      "0 - Exit\n"\
      "1 - Toggle Power\n"\
      "2 - Change Channel\n"\
      "3 - Raise Volume\n"\
      "4 - Lower Volume\n"

    ##getting user's choice
    while True:
        try:
            choice = int(raw_input("What would you like to do? "))
        except:
            print "That wasn't an integer."
        else:
            break

    ##Executing the chosen option
    if choice == 0:
        break
    elif choice == 1:
        tv.toggle_power()
    elif choice == 2:
        tv.get_channel()
        tv.set_channel()
    elif choice == 3:
        tv.raise_volume()
    elif choice == 4:
        tv.lower_volume()
    else:
        print "Sorry, that is not an available option.\n"

raw_input("\n\nPress the enter key to exit.")





    
