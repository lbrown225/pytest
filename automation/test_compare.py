import main

def test_greater():
   num = 100
   assert num > 100

def test_greater_equal():
   num = 100
   assert num >= 100

def test_less():
   num = 100
   assert num < 200
def test_helloWorld():
   str = main()
   assert str == "Hello World"