import collider2
from particle2 import Particle
import pprint

collider2.MODE = 'pp'

ptcs = [ Particle(1, 2),
         Particle(2, 1) ]


pprint.pprint(ptcs)

pprint.pprint(sorted(ptcs))

collider2.MODE = 'ee'

pprint.pprint(ptcs)

pprint.pprint(sorted(ptcs))
