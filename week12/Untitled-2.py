class Ewomazino:

    def __init__(self, name, age, hobbies, nationality, gender):

        #public instance variable
        self.name = name
        self.age = age

        #private instance variable
        self.__hobbies = hobbies
        self.__nationality = nationality
        self.__gender = gender


    #getter method
    def get_hobbies(self):
        return self.__hobbies
    
    def get_nationality(self):
        return self.__nationality
    
    def get_gender(self):
        return self.__gender
    
    def set_nationality(self, nationality):
        self.__nationality = nationality


zizi = Ewomazino("Ewoma", 17, "dancing", "Nigerian", "Female")
mazino = Ewomazino(18, "sleeping")
#acces public variables directly
print("Name: ",zizi.name)
print("Age: ", zizi.age)

#access private variables
print("hobbies: ",zizi.get_hobbies())
print("nationality: ",zizi.get_nationality())
print("gender: ",zizi.get_gender())






