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
        i = 0
        for elem in self.de:
            if value < elem:
                logging.debug("add_value. insert: {} at {}".format(value,i))
                self.de.insert(i, value)
                return
            i += 1

        self.de.append(value)

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
    input_list = [111.3, 31.5, 5.1, 15.0, -10.0, 1.2, 2200.9, -9.0, 2.0, 4.3]
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

