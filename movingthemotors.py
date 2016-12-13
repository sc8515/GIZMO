import classesforthecode
steppermotor = classesforthecode.StepperMotor()
servomotor = classesforthecode.ServoMotor()
current_pos = 0
movement = 0
currentpos_list = [0] #include the initial position which is 0.
numberslist = [0,5,2,2,1,8,5,9] #needs to be modified for each different example.
numbersqueue= classesforthecode.Queue()
for i in numberslist:
   numbersqueue.enqueue(i)
numbersqueue.enqueue(0) #includes 0 at the end of the queue so the mechanism always finishes at the start.
while not numbersqueue.isEmpty():
    i = numbersqueue.dequeue()
    current_pos = currentpos_list[-1] #get the current position as the last i used.
    if i > current_pos:
        movement = int(i - current_pos)
        print "HIGHER"
        for n in range(movement): # move as many times as the difference between postions
            steppermotor.Forwards()
            print "forwards"
        steppermotor.TurnOffMotors()
        servomotor.Hit()
        servomotor.TurnOff()
        print "hit"
    elif i < current_pos:
        movement = int(current_pos - i)
        print "LOWER"
        for n in range(movement):
            steppermotor.Backwards()
            print "backwards"
        steppermotor.TurnOffMotors()
        servomotor.Hit()
        servomotor.TurnOff()
        print "hit"
    else: #means i = current_pos
        movement = 0 #do not move stepper motor
        print "SAME"
        servomotor.Hit()
        servomotor.TurnOff()
        print "hit"

    currentpos_list.append(i)
