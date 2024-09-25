import time

gravity = 9.8
dragCoeficient = 0.2
airDensity = 1300

def Loop(area,speed,mass,time):
  drag = 0.5 * airDensity * (speed**2) * dragCoeficient * area
  result = speed*time + gravity*(time**2) - (drag/mass) * (time**2) # v*t + g*t^2 - F(drag)/m*t
  return result

def Area(shape,size):
  if shape == "krychle":
    return (size[0]**2) * 6
  if shape == "kvadr":
    return (size[0]*size[1] + size[1]*size[2] + size[0]*size[2]) * 2
  elif shape == "koule":
    return 4 * 3.14 * (size[0]**2)


type = "kvadr"
sizes = [2,4,5]
mass = 10
speed = 0
i = 0
lastTime = time.time()

while True:
  nowTime = time.time()
  i += 1
  plocha = Area(type,sizes)
  newspeed = Loop(plocha,speed,mass,nowTime-lastTime)
  print(newspeed)
  speed = newspeed
  if i > 50:
    break
  lastTime = nowTime