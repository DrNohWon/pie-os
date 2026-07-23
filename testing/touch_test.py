import sys
import os

ROOT = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

sys.path.insert(
    0,
    ROOT
)


from pie_core.input import TouchInput


touch = TouchInput()


print("P.I.E. TOUCH TEST")
print("Touch screen...")


while True:

    event = touch.read()

    if event:

        print(event)
