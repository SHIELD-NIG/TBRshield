from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import GyroDriveBase
from pybricks.tools import wait, StopWatch

tempo      = StopWatch()
hub        = PrimeHub()
esquerdo   = Motor(Port.F, Direction.COUNTERCLOCKWISE)
direito    = Motor(Port.B)
garra      = Motor(Port.C, Direction.COUNTERCLOCKWISE)
sobe       = Motor(Port.D)
mover      = GyroDriveBase(esquerdo, direito, 68.8, 113)
sensoresq  = ColorSensor(Port.A)
sensordir  = ColorSensor(Port.E)


Color.YELLOW = Color(h=20,s=72,v=69)
Color.RED    = Color(h=352,s=83,v=48)
Color.GREEN  = Color(h=135,s=62,v=52)
Color.NONE   = Color(h=220,s=19,v=20)
Color.BLACK  = Color(h=330,s=17,v=15)

sensoresq.detectable_colors((Color.BLACK, Color.NONE, Color.YELLOW, Color.RED, Color.GREEN))
sensordir.detectable_colors((Color.BLACK, Color.NONE, Color.YELLOW, Color.RED, Color.GREEN))

def seleciona(cor):
    if cor == Color.RED:
        return("R")
    if cor == Color.GREEN:
        return("G")
    if cor == Color.YELLOW:
        return("Y")  

def andar(distancia, velocidade=240):
    mover.settings(velocidade, 900, 203, 913)
    mover.straight(distancia*10)

def curva(graus):
    mover.turn(graus)

def subir():
    sobe.run_time(10000,850, wait=False)

def descer():
    sobe.run_time(-1000, 850,)

def abre():
    garra.run_time(320, 800)

def fecha():
     garra.run_time(-1000, 1000)

def segueAte(cor, velocidade=200):
    while (sensordir.color() != cor) and (sensoresq.color() != cor):
        mover.drive(velocidade, 0)
    mover.stop()
try:
    curva(90)
    andar(40)
    curva(-90)
    subir()
    andar(-68,350)
    curva(-90)

    cores = [Color.RED, Color.GREEN, Color.YELLOW]

    while (sensordir.color() not in cores) and (sensoresq.color() not in cores):
        mover.drive(200,0)
    mover.stop()
    andar(1.3)

    if sensordir.color() not in cores:
        cor3 = seleciona(sensoresq.color())
    else:
        cor3 = seleciona(sensordir.color())

    andar(-3)
    curva(-90)

    while (sensordir.color() not in cores) and (sensoresq.color() not in cores):
        mover.drive(200,0)
    mover.stop()
    andar(1.3)

    if sensordir.color() not in cores:
        cor2 = seleciona(sensoresq.color())
    else:
        cor2 = seleciona(sensordir.color())

    if cor3 != 'G' and cor2 != 'G':
        cor1 = 'G'
    elif cor3 != 'Y' and cor2 != 'Y':
        cor1 = 'Y'
    elif cor3 != 'R' and cor2 != 'R':
        cor1 = 'R'

    sequencia = f'{cor1}{cor2}{cor3}'
    print(f'A sequência é {sequencia}') 

    andar(-70, 300)
    curva(-90)
    descer()

    # Início das rotinas

    if sequencia == 'RGY':
        segueAte(Color.RED)
        fecha()
        subir()
        andar(-30)
        curva(90)
        segueAte(Color.BLACK)
        andar(12)
        curva(-90)
        andar(10)
        descer()
        abre()
        subir()
        wait(500)
        andar(-15)
        curva(90)
        andar(-34)
        curva(-90)
        andar(32.2)
        descer()
        curva(90)
        segueAte(Color.YELLOW)
        andar(-1.5)
        fecha()
        subir()
        andar(-10)
        curva(90)
        andar(40)
        curva(-90)
        andar(31)
        curva(90)
        andar(20)
        descer()
        abre()
        subir()
        wait(500)
        andar(-20)
        curva(-90)
        andar(-30)
        curva(-90)
        descer()
        segueAte(Color.RED,250)
        curva(-90)
        segueAte(Color.GREEN)
        fecha()
        subir()
        andar(-10)
        curva(-90)
        andar(35)
        curva(90)
        andar(-110,320)

finally:
    print('O programa foi executado em: ', tempo.time()/1000, 's')
