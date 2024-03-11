class Dog:
    dog_id = 0
    def __init__(self, name, breed, age, sex, is_hungry=False):
        self.name = name
        self.breed = breed
        self.age = age
        self.sex = sex
        self.activity = "idle" if self.age > 3 else "playing"
        self.is_hungry = is_hungry
        self.__thinking_of = ["treats", "cuddles"]
        self.id = Dog.dog_id
        Dog.dog_id +=1
        self.tricks = set()

    def bark(self):
        sound = "bork" if self.age > 1 else "bark"
        if self.is_hungry:
            sound =  "Woof, woof"
        return f"{sound}!!!"

    def share_thoughts(self):
        return self.__thinking_of

    def learn_trick(self, s):
        self.tricks.add(s)

    @staticmethod
    def eat(item):
        return f"I ate some {item}, and it was delicious"

    def __str__(self):
        return f"{self.name} is a {self.age} year old {self.sex} {self.breed}"
    def __hash__(self):
        return self.id

    def __add__(self, other):
        if self.age < 1 or other.age < 1 or self.sex == other.sex:          raise ValueError("These dogs can't couple")
        offspring_breed = "Mutt" if self.breed != other.breed else self.breed
        import random
        offspring_sex = random.choice(["male", "female"])
        return Dog(None, offspring_breed, 0, offspring_sex)

struppi = Dog("Struppi", "Foxterrier", 7, "male", True)

print(struppi.bark())            # "Woof, woof!!!"
print(struppi.share_thoughts())  # ["treats", "cuddles"] 
#print(d.__thinking_of) # AttributeError
print(struppi.id)            # 0
lassie = Dog("Lassie", "Collie", 10, "female")
print(lassie.id)           # 1
fido = Dog("Fido", "Mutt", 2, "male")
print(fido.id)           # 2
print(Dog.dog_id)      # 3

puppy = struppi + lassie
puppy.name = "Knuffi"
print(puppy)

puppy.learn_trick("sit")



