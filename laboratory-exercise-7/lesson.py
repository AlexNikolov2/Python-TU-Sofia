'''
class Child(Parent) - the way class are extended in Python. That's how inheritance works.
!!! super() - this way we use methods from the parent class.
super.<method> - that's the way it happens.
pass - it doesn't inherit any shit 

how we use constructor from inherited class:

--parent class
    def __init__(self, arguments):
--child class
    def __init__(self, arguments, child arguments):
        super().__init__(arguments from parent class)
'''