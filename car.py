class Car():
    def __init__(self,name = 'General',model = 'GM',car_type = 'saloon',num_of_doors=4,num_of_wheels=4,speed = 0,):
        self.name = name
        self.model = model
        self.car_type = car_type
        self.num_of_doors = num_of_doors
        self.num_of_wheels = num_of_wheels
        self.speed = speed

    def car_doors(self):
      
      if self.name == "Porshe" or self.name == "Koenigsegg" or self.car_type == 'trailer':
        num_of_doors = 2
        return num_of_doors
        
        
      else:
        num_of_doors = 4
        return num_of_doors
        


    def car_wheels(self):
      if self.car_type == "saloon":
        no_of_wheels = 4
        return no_of_wheels
            
      else:
        no_of_wheels = 8
        return no_of_wheels
    
    def is_saloon(self):
        if self.car_type == "saloon":
            return True
        else:
            self.car_type = 'It is a Trailer'
            return False,self.car_type

    def car_speed(self,moving_speed):
        self.moving_speed = moving_speed
        parked_speed = self.speed
        
        total_speed = parked_speed + self.moving_speed
        return total_speed

    def drive(self,moving_speed):
        self.moving_speed = moving_speed
        return self

'''
opel = Car('Opel', 'Omega 3')
porshe = Car('Porshe', '911 Turbo')
print(opel.car_doors())
print(porshe.car_doors())

man = Car('MAN', 'Truck', 'trailer')
koenigsegg = Car('Koenigsegg', 'Agera R')
print(man.car_wheels())
print(koenigsegg.car_wheels())

man = Car('MAN', 'Truck', 'trailer')
print(man.car_speed(7))
'''




