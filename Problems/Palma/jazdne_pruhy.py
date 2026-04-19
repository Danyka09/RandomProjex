import turtle
tabula = turtle.Screen() # okay so this was copied from my code cause i forgot it
pero = turtle.Turtle()
pero.hideturtle()
pero.speed(0)

def symbol_v_smere(dlzka_symbolu):
    pero.dot(dlzka_symbolu/7)
    pero.rt(90)
    pero.fd(dlzka_symbolu)
    pero.fd(-dlzka_symbolu)
    pero.lt(90)

def symbol_proti_smere(dlzka_symbolu):
    pero.lt(90)
    pero.fd(-dlzka_symbolu)
    pero.dot(dlzka_symbolu/7)
    pero.fd(dlzka_symbolu)
    pero.rt(90)

def kresli_znacku(dlzka_symbolu, pocet_v_smere, pocet_proti):
    for i in range(2):
        pero.fd(dlzka_symbolu/5 * (pocet_proti + pocet_v_smere + 1))
        pero.rt(90)
        pero.fd(dlzka_symbolu * 1.4)
        pero.rt(90)

    pero.penup()
    pero.fd(dlzka_symbolu/5)
    pero.rt(90)
    pero.fd(dlzka_symbolu * 0.2)
    pero.lt(90)
    pero.pendown()

    for i in range(pocet_proti):
        symbol_proti_smere(dlzka_symbolu)
        pero.penup()
        pero.fd(dlzka_symbolu / 5)
        pero.pendown()

    for i in range(pocet_v_smere):
        symbol_v_smere(dlzka_symbolu)
        pero.penup()
        pero.fd(dlzka_symbolu/5)
        pero.pendown()

kresli_znacku(100,3,2)

turtle.mainloop()
# done in 29 minutes 45 seconds