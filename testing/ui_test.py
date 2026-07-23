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


from pie_ui.engine import UIEngine


ui = UIEngine()

ui.run()
