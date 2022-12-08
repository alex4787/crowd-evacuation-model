from mvc import View

#Game variables
agent_count = 500
floor = 50

#test params
#test = 'capacity'
test = None
count = 10

view = View()

if test:
    for i in range(count):
        view.runPyGame(agent_count, floor, test)
else:
    view.runPyGame(agent_count, floor, test)
