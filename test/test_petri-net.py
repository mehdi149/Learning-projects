import snakes.plugins
snakes.plugins.load('gv', 'snakes.nets', 'nets')
from nets import *
n = PetriNet('N') 
n.add_place(Place('p00', [0]))
n.add_transition(Transition('t10'))
n.add_place(Place('p11'))
n.add_transition(Transition('t01'))
n.add_input('p00', 't10', Variable('x'))
n.add_output('p11', 't10', Expression('x+1'))
n.add_input('p11', 't01', Variable('y'))
n.add_output('p00', 't01', Expression('y-1'))
def draw_place (place, attr) :
    attr['label'] = place.name.upper()
    attr['color'] = '#FF0000'
def draw_transition (trans, attr) :
    if str(trans.guard) == 'True' :
        attr['label'] = trans.name
    else :
        attr['label'] = '%s\n%s' % (trans.name, trans.guard)
n.draw(',net-with-colors.png',place_attr=draw_place, trans_attr=draw_transition)