import mod1
import mod2
import collider
import pprint


print collider.MODE

from particle import Particle

ptcs = [ Particle(1, 2),
         Particle(2, 1) ]


pprint.pprint(ptcs)

pprint.pprint(sorted(ptcs))

collider.set_mode('ee')

pprint.pprint(ptcs)

pprint.pprint(sorted(ptcs))
