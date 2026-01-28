print(f"if_2 __name__: {__name__}")
#were running file 2; file 2 __name__ == __main__

import if_1
# since file 1 is being run as a module from file 2; __name__ does not == __main__
                                                    # __name__ == if_1
print(if_1)