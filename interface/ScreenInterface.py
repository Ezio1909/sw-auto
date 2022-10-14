from abc import ABC,abstractmethod

class IScreen(ABC):
  @abstractmethod
  def click(self):
    pass