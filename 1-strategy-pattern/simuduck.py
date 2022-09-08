class Duck: #abstract class
  def __init__(self):
    self.quack_behavior = None
    self.fly_behavior = None

  def set_fly_behavior(self, fly_behavior):
    self.fly_behavior =  fly_behavior
  
  def set_quack_behavior(self, quack_behavior):
    self.quack_behavior = quack_behavior

  def fly(self):
    self.fly_behavior.fly()
  
  def quack(self):
    self.quack_behavior.quack()


class FlyBehavior: # interface
  def fly(self):
    pass


class FlyWithWings(FlyBehavior):
  def fly(self):
    print("Flying with wings")


class FlyNoWay(FlyBehavior):
  def fly(self):
    print("Can't fly without wings")


class QuackBehavior:
  def quack(self):
    pass


class Quack(QuackBehavior):
  def quack(self):
    print("QUACK")


class Squeak(QuackBehavior):
  def quack(self):
    print("SQUEAK")


class MallordDuck(Duck):
  def __init__(self):
    super().__init__()
    self.quack_behavior = Quack()
    self.fly_behavior = FlyWithWings()



duck = MallordDuck()
duck.quack()
duck.fly()

duck.set_fly_behavior(FlyNoWay())
duck.fly()