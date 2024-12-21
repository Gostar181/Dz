import colorama
import inspect



for metod in dir(colorama):
    print(metod)

print(inspect.ismodule(colorama))
print(inspect.isclass(colorama))