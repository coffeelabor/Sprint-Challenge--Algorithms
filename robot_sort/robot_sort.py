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
        """
        # Fill this out
        print('test')
        self.swap_item()
        print(f'base swap position:item: {self._position} {self._item}')
        while self._light == "OFF":
            print('while light off start')
            print(f'list now: {self._list}')

            print(f'position: {self._position}')
            while self.can_move_left():
                print("moving left")
                self.move_left()
                print('moved left')
            self.set_light_on()
            print(f'light turned on: {self._light}')
            print(f'position:item: {self._position} {self._item}')

            self.swap_item()
            print('item picked up')
            print(f'position:item: {self._position} {self._item}')
            print(f'list now: {self._list}')
            while self.can_move_right():
                print('moving right')
                self.move_right()
                if self.compare_item() == 1:
                    print(f'robot is holdin a larger item')
                    self.swap_item()
                    print(f'list now in right if: {self._list}')
                print('moved right')
                self.set_light_off()
            # if self._position == len(self._list - 1) and self._list[-1] == None:
            #     self.set_light_on
            # if self.swap_item() == None:
            #     if self.can_move_right() == False:
            #         self.swap_item()
            #         self.set_light_on
            #     self.move_right()
            # if self.compare_item() == 1:
            #     print('comparing')
            #     self.swap_item()
            #     print('swapped')
            #     self.set_light_off()
            #     print('light on in if')
            #     print(f'list now: {self._list}')
            # self.set_light_on()
            # print(f'Light should be on {self._light}')
            # elif self.compare_item == -1:
            #     self.move_left
            #     self.swap_item
            # self.set_light_off


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1,
         45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)


'''
###Understand
-the robot can move left or right 1 at a time and stops at either end of the list
-it will swap whatever item it has with whatever is in front of it
-it can tell if an item is smaller, larger or equal to the item its holding by returning -1,1, or 0
-The robot has a boolean value in the form of a 'light' that turns on or off
-it kinda seems like a bubble sort

###Planning
def bubble_sort(arr):
    done = True
    while done:
        done = False
        for i in range(0, len(arr)-1):
            if arr[i] > arr[i+1]:
                # swap
                arr[i], arr[i+1] = arr[i+1], arr[i]
                done = True
    return arr

-Maybe it should all be in a while loop for light off
    -another while for can_move left true
        -move left
        -check if it can move left
    -turn light on(set_light_on)
    -It will start at the index of 0 of a list
    -Then it will pick up the first item (index 0). 
    -if it can move right it will by index of 1
        -move_right
    -it will compare the item its holding to the item in front of it
        -if the item in front is 1(larger) compare_item == 1 it will swap items 
            -swap_item
        -if can_move_right is false then is should drop the item
    -I will need to end the loop
        -I can check if none is in the last item of the array
        -I can set the light on to break the loop
##################################
while light_is_on is False:
    while can_move_left:
        move_left
    set_light_on
    swap_item
    while can_move_right:
        move_right
        if compare_item == 1:
            swap_item
        elif compare_item == -1:
            move_left
            swap_item
        set_light_off
#########################
if can_move_right not True:
            swap_item
            set_light_off
########################

-Im going to need to be able to drop the item

-its light will be off
-while set_light_off
    -set_light_on
    -for loop for i in range(0, len(arr)-1):


    -It will check if it can move left or right

##########################################
while self.light_is_on is False:
            print('while light test')
            while self.can_move_left:
                self.move_left
            self.set_light_on
            print(f'light: {self._light}')
            self.swap_item
            while self.can_move_right:
                self.move_right
            if self.compare_item == 1:
                self.swap_item
            # elif self.compare_item == -1:
            #     self.move_left
            #     self.swap_item
            self.set_light_off

#########################################
print('test')
        self.swap_item()
        print(f'base swap position:item: {self._position} {self._item}')
        while self._light == "OFF":
            print('while light off start')
            print(f'list now: {self._list}')
            self._position
            print(f'position: {self._position}')
            while self.can_move_left():
                print("moving left")
                self.move_left()
                print('moved left')
            self.set_light_on()
            print(f'light turned on: {self._light}')
            print(f'position:item: {self._position} {self._item}')
            if self.swap_item() == None:
                if self.can_move_right() == False:
                    self.swap_item()
                    self.set_light_on
                self.move_right()
            self.swap_item()
            print('item picked up')
            print(f'position:item: {self._position} {self._item}')
            print(f'list now: {self._list}')
            while self.can_move_right():
                print('moving right')
                self.move_right()
                if self.compare_item() == 1:
                    print(f'robot is holdin a larger item')
                    self.swap_item()
                    print(f'list now in right if: {self._list}')
                print('moved right')
                self.set_light_off()


'''
