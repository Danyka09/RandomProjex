import time
from datetime import datetime, timedelta
#decorators are used to enhance functions, for example timing the length

def timer_dec(base_fn):
    def enhanced_fn(*args, **kwargs): # *args packs positional arguments into args tuple
        #                   **kwargs collects keyword arguments into kwargs dictionary
        start_time = time.time()
        result = base_fn(*args, **kwargs) # *args unpacks tuple into individual arguments
        #               **kwargs unpacks a dictionary into keyword arguments
        end_time = time.time()
        print(f"Task time: {end_time - start_time} seconds")
        return result #putting it into a variable and making it return makes returns like in matcha work
    return enhanced_fn

@timer_dec
def brew_tea(tea_type, steep_time):
    print(f"Brewing {tea_type} tea...")
    time.sleep(steep_time)
    print("Tea is ready!")

@timer_dec
def make_matcha():
    print("Brewing matcha...")
    time.sleep(1)
    print("Matcha is ready!")
    return f"Drink matcha by {datetime.now() + timedelta(minutes=30)}"

#how to run decorator, multiple ways
    # timer_dec(brew_tea)
#we can make a variable out of it
    # dec_brew_tea = timer_dec(brew_tea) #no parentheses ()
    # dec_brew_tea()
#we can also make it the same so that when the original function gets called it automatically has the decorator
    # brew_tea = timer_dec(brew_tea) #no parentheses ()
    # brew_tea()
#howerver the best way is to use the @ syntax at the top of the function

brew_tea("green", 1) #args
brew_tea(tea_type="purple", steep_time=0.67) #kwargs
print(make_matcha())

