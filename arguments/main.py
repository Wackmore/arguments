# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line
mass = 0

def greet(name, template = "Hello, <name>!"):
        greet = template.replace("<name>",name)
        return greet

def force(mass=0,body="earth"):
        mass = int(mass)
        body = str(body)

        planets = {
        "mercury" : 3.7,
        "venus"   : 8.9,
        "earth"   : 9.8,
        "moon"    : 1.6,
        "mars"    : 3.7,
        "jupiter" : 23.1,
        "saturn"  : 9,
        "uranus"  : 8.7,
        "neptune" : 11,
        "pluto"   : 0.7
        }       # I am aware that pluto and the moon are not a planet ;)

        #bodywaight = planets.get(body)
        #force = mass*bodywaight
        force = mass * (planets.get(body))
        return force

def pull(m1,m2,d):
        forceconstant = 6.674*(10**-11)
        pull = forceconstant*(m1*m2)/(d**2)
        return pull

print(force(69))