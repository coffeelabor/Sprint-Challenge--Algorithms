class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"
    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"
    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"

    def sort(self):
        """
        Sort the robot's list.
            print('list', self._list)
            print('position', self._position)
            print('item', self._item)
            print('light', self._light)
            self.compare_item() == -1:  # robots holding smaller number
            self.compare_item() == 1:  # robots holding larger number
        """
        # Fill this out
        def send_robot_right():
            while self.can_move_right():
                # robots holding smaller number or its holding None
                if self.compare_item() == -1 or self.compare_item() == None:
                    #it will always swap for a larger one
                    self.swap_item()
                    self.move_right()
                    print('position rsmall', self._position)
                    print('item rsmall', self._item)
                    print('list rsmall', self._list)
                # it has to be 1 so its holding a larger number
                else:
                    self.move_right()
                    print('position rlarge', self._position)
                    print('item rlarge', self._item)
                    print('list rlarge', self._list)
            #it should be holding a large number now and at the end so swap
            self.swap_item()
            print('********ROBOT IS AT FAR RIGHT********')
            print('position end', self._position)
            print('item end', self._item)
            print('list', self._list)
            print('********ROBOT IS AT FAR RIGHT********')
        print('test')
        send_robot_right()
        print('test2')
        while self.can_move_left():
            # robots holding larger number or its holding None
            if self.compare_item() == 1 or self.compare_item() == None:
                print('robots holding larger number or its holding None')
                # print('about to move right in can move left')
                # move_right()
                # print('should have finished moving rightin move left')

                #it will always swap for a larger one
                self.swap_item()
                self.move_left()
                print('position llarge', self._position)
                print('item llarge', self._item)
                print('list llarge', self._list)
            # it has to be 1 so its holding a smaller number
            else:
                print('about to move right in can move left')
                send_robot_right()
                print('should have finished moving rightin move left')
                # self.move_left()
                # print('position lsmall', self._position)
                # print('item lsmall', self._item)
                # print('list lsmall', self._list)
        #it should be holding a small number now and at the start so swap
        self.swap_item()
        print('********ROBOT IS AT FAR LEFT********')
        print('position start', self._position)
        print('item start', self._item)
        print('list', self._list)
        print('********ROBOT IS AT FAR LEFT********')
    
            
            


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)


'''
Abilities:
* It can move left or right.
* It can pick up an item
    * If it tries to pick up an item while already holding one, it will swap the items instead.
* It can compare the item it's holding to the item in front of it.
* It can switch a light on its head on or off.


Planning
its some sort of sorting algo and its only moving directly to the left or right
    it should be setup like a bubble sort
if it only compares to the right it can sort that way
    onces its react the end of the list it can go all the way back left

ill have a while loop for can move left and can move right

new plan
The light is dumb and confusing, just dont use it



'''


'''

def sort(self):
        """
        Sort the robot's list.
        """
        # Fill this out
        self.set_light_on()
        while self.light_is_on():
            print('light on')
            if self.compare_item() == None:
                    self.swap_item()
            while self.can_move_right():
                # self.swap_item()
                print('position', self._position)
                print('item', self._item)
                if self.compare_item() == -1:
                    self.swap_item()
        
                self.move_right()
                if self.can_move_right() == False and self.compare_item() == 1:
                    self.swap_item()
                print('position2', self._position)
                print('moving right')
                print('list', self._list)
            self.set_light_off()
            print('light off')
'''

'''
  self.set_light_on()
        while self.light_is_on():
            if self.compare_item() == None:
                    self.swap_item()
            while self.can_move_right():
                # self.swap_item()
                if self.compare_item() == -1: #robots holding smaller number
                    self.swap_item()
        
                self.move_right()
                if self.can_move_right() == False and self.compare_item() == 1:
                    self.swap_item()
            self.set_light_off()
'''

'''
def sort(self):
        """
        Sort the robot's list.
        """
        # Fill this out
        self.set_light_on()
        while self.light_is_on():
            print('list', self._list)
            self.set_light_off()
            #just use the can move right in an if/else
            if self.can_move_right() == True:
                if self.compare_item() == -1:  # robots holding smaller number
                    self.swap_item()
                    self.move_right()
                    self.set_light_on()
                elif self.compare_item() == 1:
                    self.move_right()
                    self.set_light_on()

            else:
                while self.can_move_left() == True:
                    self.move_left()
'''

'''
# ##################    
            # if self.compare_item() == None:
            #         self.swap_item()
            # while self.can_move_right():
            #     # self.swap_item()
            #     if self.compare_item() == -1: #robots holding smaller number
            #         self.swap_item()
        
            #     self.move_right()
            #     if self.can_move_right() == False and self.compare_item() == 1:
            #         self.swap_item()
'''

'''
# Fill this out
        self.set_light_on()
        if self.compare_item() == None:
            self.swap_item()
        while self.light_is_on():
            print('list', self._list)
            print('position', self._position)
            print('item', self._item)
            print('light', self._light)
            self.set_light_off()
            #just use the can move right in an if/else
            # if self.can_move_right() == True:
            while self.can_move_right():
                print('position', self._position)
                print('item', self._item)
                if self.compare_item() == -1:  # robots holding smaller number
                    self.swap_item()
                    self.move_right()
                    self.set_light_on()
                elif self.compare_item() == 1:  # robots holding larger number
                    self.move_right()
                    self.set_light_on()
                else:
                    self.move_right()
                    print('test')
            if self.can_move_right() == False and self.compare_item() == 1:
                self.swap_item()
            while self.can_move_left():
                print('position left', self._position)
                self.move_left()
'''

'''
***Its moveing the way it should

self.set_light_on()
        while self.can_move_right():
            # robots holding smaller number or its holding None
            if self.compare_item == -1 or self.compare_item() ==None:
                #it will always swap for a larger one
                self.swap_item()
                self.move_right()
                print('position rsmall', self._position)
                print('item rsmall', self._item)
                print('list rsmall', self._list)
            # it has to be 1 so its holding a larger number
            else:
                self.move_right()
                print('position rlarge', self._position)
                print('item rlarge', self._item)
                print('list rlarge', self._list)
        #it should be holding a large number now and at the end so swap
        self.swap_item()
        print('position end', self._position)
        print('item end', self._item)
        print('ROBOT IS AT FAR RIGHT')
        while self.can_move_left():
            self.move_left()
        print('position start', self._position)
        print('item start', self._item)
        print('ROBOT IS AT FAR LEFT')
        print('list', self._list)
'''
'''
*********It moved back correctly

self.set_light_on()
        while self.can_move_right():
            # robots holding smaller number or its holding None
            if self.compare_item == -1 or self.compare_item() ==None:
                #it will always swap for a larger one
                self.swap_item()
                self.move_right()
                print('position rsmall', self._position)
                print('item rsmall', self._item)
                print('list rsmall', self._list)
            # it has to be 1 so its holding a larger number
            else:
                self.move_right()
                print('position rlarge', self._position)
                print('item rlarge', self._item)
                print('list rlarge', self._list)
        #it should be holding a large number now and at the end so swap
        self.swap_item()
        print('********ROBOT IS AT FAR RIGHT********')
        print('position end', self._position)
        print('item end', self._item)
        print('list', self._list)
        print('********ROBOT IS AT FAR RIGHT********')
        while self.can_move_left():
            # robots holding larger number or its holding None
            if self.compare_item == 1 or self.compare_item() == None:
                #it will always swap for a larger one
                self.swap_item()
                self.move_left()
                print('position llarge', self._position)
                print('item llarge', self._item)
                print('list llarge', self._list)
            # it has to be 1 so its holding a smaller number
            else:
                self.move_left()
                print('position lsmall', self._position)
                print('item lsmall', self._item)
                print('list lsmall', self._list)
        print('********ROBOT IS AT FAR LEFT********')
        print('position start', self._position)
        print('item start', self._item)
        print('list', self._list)
        print('********ROBOT IS AT FAR LEFT********')
'''
'''
********Fixed bug sorts smallest and largest***********

# self.set_light_on()
        while self.can_move_right():
            # robots holding smaller number or its holding None
            if self.compare_item() == -1 or self.compare_item() ==None:
                #it will always swap for a larger one
                self.swap_item()
                self.move_right()
                print('position rsmall', self._position)
                print('item rsmall', self._item)
                print('list rsmall', self._list)
            # it has to be 1 so its holding a larger number
            else:
                self.move_right()
                print('position rlarge', self._position)
                print('item rlarge', self._item)
                print('list rlarge', self._list)
        #it should be holding a large number now and at the end so swap
        self.swap_item()
        print('********ROBOT IS AT FAR RIGHT********')
        print('position end', self._position)
        print('item end', self._item)
        print('list', self._list)
        print('********ROBOT IS AT FAR RIGHT********')
        while self.can_move_left():
            # robots holding larger number or its holding None
            if self.compare_item() == 1 or self.compare_item() == None:
                #it will always swap for a larger one
                self.swap_item()
                self.move_left()
                print('position llarge', self._position)
                print('item llarge', self._item)
                print('list llarge', self._list)
            # it has to be 1 so its holding a smaller number
            else:
                self.move_left()
                print('position lsmall', self._position)
                print('item lsmall', self._item)
                print('list lsmall', self._list)
        #it should be holding a small number now and at the start so swap
        self.swap_item()
        print('********ROBOT IS AT FAR LEFT********')
        print('position start', self._position)
        print('item start', self._item)
        print('list', self._list)
        print('********ROBOT IS AT FAR LEFT********')
'''

'''
*********Works


# Fill this out
        # self.set_light_on()
        def move_right():
            while self.can_move_right():
                # robots holding smaller number or its holding None
                if self.compare_item() == -1 or self.compare_item() ==None:
                    #it will always swap for a larger one
                    self.swap_item()
                    self.move_right()
                    print('position rsmall', self._position)
                    print('item rsmall', self._item)
                    print('list rsmall', self._list)
                # it has to be 1 so its holding a larger number
                else:
                    self.move_right()
                    print('position rlarge', self._position)
                    print('item rlarge', self._item)
                    print('list rlarge', self._list)
            #it should be holding a large number now and at the end so swap
            self.swap_item()
            print('********ROBOT IS AT FAR RIGHT********')
            print('position end', self._position)
            print('item end', self._item)
            print('list', self._list)
            print('********ROBOT IS AT FAR RIGHT********')
        print('test')
        move_right()
        print('test2')
        while self.can_move_left():
            # robots holding larger number or its holding None
            if self.compare_item() == 1 or self.compare_item() == None:
                # print('about to move right in can move left')
                # move_right()
                # print('should have finished moving rightin move left')
                #it will always swap for a larger one
                self.swap_item()
                self.move_left()
                print('position llarge', self._position)
                print('item llarge', self._item)
                print('list llarge', self._list)
            # it has to be 1 so its holding a smaller number
            else:
                print('about to move right in can move left')
                move_right()
                print('should have finished moving rightin move left')
                # self.move_left()
                # print('position lsmall', self._position)
                # print('item lsmall', self._item)
                # print('list lsmall', self._list)
        #it should be holding a small number now and at the start so swap
        self.swap_item()
        print('********ROBOT IS AT FAR LEFT********')
        print('position start', self._position)
        print('item start', self._item)
        print('list', self._list)
        print('********ROBOT IS AT FAR LEFT********')
'''

'''
**********Final
# self.set_light_on()
        def send_robot_right():
            while self.can_move_right():
                # robots holding smaller number or its holding None
                if self.compare_item() == -1 or self.compare_item() ==None:
                    #it will always swap for a larger one
                    self.swap_item()
                    self.move_right()
                    print('position rsmall', self._position)
                    print('item rsmall', self._item)
                    print('list rsmall', self._list)
                # it has to be 1 so its holding a larger number
                else:
                    self.move_right()
                    print('position rlarge', self._position)
                    print('item rlarge', self._item)
                    print('list rlarge', self._list)
            #it should be holding a large number now and at the end so swap
            self.swap_item()
            print('********ROBOT IS AT FAR RIGHT********')
            print('position end', self._position)
            print('item end', self._item)
            print('list', self._list)
            print('********ROBOT IS AT FAR RIGHT********')
        print('test')
        send_robot_right()
        print('test2')
        while self.can_move_left():
            # robots holding larger number or its holding None
            if self.compare_item() == 1 or self.compare_item() == None:
                print('robots holding larger number or its holding None')
                # print('about to move right in can move left')
                # move_right()
                # print('should have finished moving rightin move left')
                
                #it will always swap for a larger one
                self.swap_item()
                self.move_left()
                print('position llarge', self._position)
                print('item llarge', self._item)
                print('list llarge', self._list)
            # it has to be 1 so its holding a smaller number
            else:
                print('about to move right in can move left')
                send_robot_right()
                print('should have finished moving rightin move left')
                # self.move_left()
                # print('position lsmall', self._position)
                # print('item lsmall', self._item)
                # print('list lsmall', self._list)
        #it should be holding a small number now and at the start so swap
        self.swap_item()
        print('********ROBOT IS AT FAR LEFT********')
        print('position start', self._position)
        print('item start', self._item)
        print('list', self._list)
        print('********ROBOT IS AT FAR LEFT********')

'''
'''

*****Clean
def send_robot_right():
            while self.can_move_right():
                if self.compare_item() == -1 or self.compare_item() ==None:
                    self.swap_item()
                    self.move_right()
                else:
                    self.move_right()
            self.swap_item()
            
        send_robot_right()
        
        while self.can_move_left():
            
            if self.compare_item() == 1 or self.compare_item() == None:
                self.swap_item()
                self.move_left()
            else:
                send_robot_right()
        self.swap_item()
'''
