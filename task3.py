
class Eveniterator:
    def __init__(self,limit):
        self.limit=limit
        self.num=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.num <= self.limit:
            result=self.num
            self.num+=2
            return result
        else:
            raise StopIteration
object=Eveniterator(8)
for n in object:
    print(n)


# num = int(input("Enter the number: "))

# if num % 2 == 0:
#     print("even")
# else:
#     print("odd")