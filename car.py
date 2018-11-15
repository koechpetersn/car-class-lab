class Car():
    def __init__(self,car_type,num_of_doors,num_of_wheels=4,name = 'General',model = 'GM',speed = 0,):
        self.name = name
        self.model = model
        self.car_type = car_type
        self.num_of_doors = num_of_doors
        self.num_of_wheels = num_of_wheels
        self.speed = speed

    def car_doors(self):
      if self.name == "Porsche" or self.name == "Koenigsegg" or self.car_type != 'saloon':
        num_of_doors = 2
        return 'The number of doors is %d'%num_of_doors
        
      else:
        num_of_doors = 4
        return 'The number of doors is %d'%num_of_doors



    def car_wheels(self):
      if self.car_type == "saloon":
        no_of_wheels = 4
        return 'The number of wheels is %d'%no_of_wheels
            
      else:
        no_of_wheels = 8
        return 'The number of wheels is %d'%no_of_wheels
    
    def is_saloon(self):
        if self.car_type == "saloon":
            return True
        else:
            self.car_type = 'It is a Trailer'
            return False,self.car_type

    def drive(self,moving_speed):
        self.moving_speed = moving_speed
        parked_speed = self.speed
        
        total_speed = parked_speed + moving_speed
        return 'The moving speed is %d'%total_speed



