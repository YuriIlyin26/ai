import logging
import collections


# -----------------------------------------------------------------------------
#   storage for float values
class StorageFloatValues:
    def __init__(self):
        self.de = collections.deque([])

    # -----------------------------------------------------------------------------
    def add_value(self, value):
        logging.debug("add_value. value: {}".format(value))
        # first insert to the left or right if value is less than min or more than max
        if len(self.de) > 0:
            if value < self.de[0]:
                logging.debug("add_value. append left: {}".format(value))
                self.de.appendleft(value)
                return
            if value > self.de[-1]:
                logging.debug("add_value. append right: {}".format(value))
                self.de.append(value)
                return
        if len(self.de) == 0:
            self.de.append(value)
            return

        left_index = 0
        right_index = len(self.de) - 1
        while left_index < right_index:
            mid = int((left_index + right_index) / 2)
            if value < self.de[mid]:
                logging.debug("add_value. right_index: {} at {}".format(right_index,mid))
                right_index = mid
            if value >= self.de[mid]:
                logging.debug("add_value. left_index: {} at {}".format(left_index,mid))
                left_index = mid
            if right_index - left_index <= 1:
                logging.debug("add_value. insert: {} at {}".format(value,left_index+1))
                self.de.insert(left_index+1, value)
                return



    # -----------------------------------------------------------------------------
    def print_value(self):
        print(self.de)

    # -----------------------------------------------------------------------------
    def remove_min(self):
        self.de.popleft()

    # ------------------------------------------------------------------------------
    def remove_max(self):
        self.de.pop()

    # -----------------------------------------------------------------------------
    def remove_element(self,value):
        logging.debug("remove_element. value: {}".format(value))
        self.de.remove(value)

# ------------------------------------------------------------------------------
if __name__ == '__main__':
#    logging.basicConfig(level=logging.DEBUG)
    input_list = [111.3, 31.5, 5.1, 15.0, -10.0, 1.2, 5.1, 2200.9, -9.0, 2.0, 4.3]
    so = StorageFloatValues()
    for f in input_list:
        so.add_value(f)
    so.print_value()
    print( 'Remove min:')
    so.remove_min()
    so.print_value()
    print( 'Remove max:')
    so.remove_max()
    so.print_value()
    print( 'Remove existing element:')
    so.remove_element(5.1)
    so.print_value()
    try:
        print('Remove nonexistent element:')
        so.remove_element(100.0)
    except ValueError:
        pass

