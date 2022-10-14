
import interface.ScreenInterface
=======
from ..interface.ScreenInterface import IScreen


class test(IScreen):
  def __init__(self):
    print("testing")


x = test()