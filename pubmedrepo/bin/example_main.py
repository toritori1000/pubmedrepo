from pubmed.example_mod import ExampleMod
from pubmed.package1.example_mod2 import ExampleMod2

print("I am a driver program from main.")

clsobj = ExampleMod()
print("Add result:", clsobj.add())

clsobj2 = ExampleMod2()
print("Compose result: ", clsobj2.compose())
