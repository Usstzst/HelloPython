class Turtle:
              color='green'
              weight=10
              legs=4
              shell=True
              mouth='大嘴'
              
              def climb(self):
                            
                            print('我正在努力地向前爬...')
              def run(self):
                            print('我在飞')
              def bite(self):
                            print('我在咬')
              def eat(self):
                            print('我在吃')
              def sleep(self):
                            print('我在睡')

              
              
class Ball:
              def setName(self,name,age):
                            self.name=name
                            self.age=age
              def kick(self):
                            print('我叫 %s , 谁在踢我？！ ' % self.name)
                            print('我的年龄是：'+str(self.age))
class Potato():
              def __init__(self,name):
                            self.name=name
              def kick(self):
                            print('我叫 %s , 谁在踢我？！ ' % self.name)

                            

class Restaurant():

              
              def __init__(self,restaurant_name,cuisine_type):
                            
                            self.restaurant_name = restaurant_name
                            self.cuisine_type = cuisine_type
                            self.served_number=0
                            
              def describe_restaurant(self):
                            print('餐馆名字为：'+self.restaurant_name)
                            print('顾客类型为： '+self.cuisine_type)
              def open_restaurant(self):
                            print('餐馆正在营业！')
              def update_number(self,number):
                            self.served_number = number
                            print('在'+ str(self.restaurant_name) +'就餐的人数为：'+str(self.served_number))
              def set_number_served(self,number):
                            self.served_number=number
                            print('设置就餐人数为：'+str(self.served_number))
              def increment_number_served(slef,number):
                            self.served_number +=number


              


class Dog():
              def __init__(self,name,age):
                            self.name=name
                            self.age=age
              def sit(self):
                            print(self.name.title()+' is now sitting!')
              def roll_over(self):
                            print(self.name.title()+' rolled over!')
                            






class Car():
              def __init__(self,make,model,year):
                            self.make=make
                            self.model=model
                            self.year=year
                            self.odometer_reading=0
              def get_descriptive_name(self):
                            long_name=str(self.year)+' '+self.make+' '+self.model
                            return long_name.title()
              def read_odometer(self):
                            print('This car has '+str(self.odometer_reading)+' miles on it')

              def update_odometer(self,mileage):
                            if mileage >= self.odometer_reading:
                                          self.odometer_reading=mileage
                            else:
                                          print('You can\'t roll back an odometer')
              def increment_odometer(self,miles):
                            self.odometer_reading +=miles

class Battery():
              def __init__(self,battery_size=70):
                            self.battery_size=battery_size

              def describe_battery(self):
                            print('This car has a '+str(self.battery_size)+ '-kwh battery.')
              def get_range(self):
                            
                            if self.battery_size == 70:
                                          range = 240
                            elif self.battery_size == 85:
                                          range = 270
                            message = 'This car can go approximately ' +str(range)
                            message +=' miles on a full charge.'
                            print(message)
                            
              def upgrage_battery(self):
                            if self.battery_size != 85:
                                          self.battery_size=85
                                          print('电池容量为：'+str(self.battery_size))
                                          


class ElectricCar(Car):
              def __init__(self,make,model,year):
                            super().__init__(make,model,year)
                            self.battery=Battery()
                            
                            


class User():
              def describe_user(self,first_name,last_name,login_attempts):
                            self.first_name=first_name
                            self.last_name=last_name
                            self.login_attempts=login_attempts
                            
                            print('姓名： '+self.first_name)
                            print('姓名： '+self.last_name)
              def greet_user(self):
                            print('%s , 祝您生活愉快！' %self.first_name)
                            print('%s , You are beautiful', self.last_name)
              def increment_login_attempts(self):
                            self.login_attempts +=1
                            print('登陆次数：'+str(self.login_attempts))
              def reset_login_attempts(self):
                            self.login_attempts = 0
                            print('重置之后登陆次数为：'+str(self.login_attempts))



class CapStr(str):
              def __new__(cls,string):
                            string = string.upper()
                            return str.__new__(cls,string)




##class C:
##              def __init__(self,size=10):
##                            self.size=size
##              def getSize(self):
##                            return self.size
##              def setSize(self,value):
##                            self.size=value
##              def delSize(self):
##                            del self.size
##              x=property(getSize,setSize,delSize)
##              
                            


              
class C:
              def __getattribute__(self,name):
                            print('getattribute')
                            return super().__getattribute__(name)
              def __setattr__(self,name,value):
                            print('setattr')
                            super().__setattr__(name,value)
              def __delattr__(self,name):
                            print('delattr')
                            super().__delattr__(name)
              def __getattr__(self,name):
                            print('getattr')
              


"""  摄氏度和华氏度之间的转换 """

class Celsius:
              def __init__(self,value=26.0):
                            self.value = float(value)
              def __get__(self,instance,owner):
                            return self.value
              def __set__(self,instance,value):
                            self.value=float(value)

class Fahrenheit:
              def __get__(self,instance,owner):
                            return instance.cel*1.8+32
              def __set__(self,instance,value):
                            instance.cel=(float(value)-32)/1.8

class Temperature:
              cel=Celsius()
              fah=Fahrenheit()


"""   编写不可变列表  """

class CountList:
              def __init__(self,*args):
                            self.values=[x for x in args]
                            self.count={}.fromkeys(range(len(self.values)),0)

              def __len__(self):
                            return len(self.values)
              def __getitem__(self,key):
                            self.count[key] +=1
                            return self.values[key]


"""  迭代器  """

class Fibs:
              def __init__(self,n=20):
                            self.a=0
                            self.b=1
                            self.n=n
              def __iter__(self):
                            return self
              def __next__(self):
                            self.a,self.b = self.b,self.a+self.b
                            if self.a>self.n:
                                          raise StopIteration
                            return self.a


def c2f(cel):
              fah=cel*1.8+32
              return fah

def f2c(fah):
              cel=(fah-32)/1.8
              return cel

def test():
              print('测试，0 摄氏度 = %.2f 华氏度' %c2f(0))
              print('测试，0 华氏度 = %.2f 摄氏度' %f2c(0))


##   作为模块导入到其他程序中时，用来做判断，避免重复。__name__属性的值是当前程序名（文件名） __main__指的是导入文件的名
##   if __name__ == '__main__'

test()


