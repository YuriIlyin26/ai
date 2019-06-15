import logging

#------------------------------------------------------------------------------
#   binary search in list
def binSearch(list, what):
    logging.debug("list: {}, what: {}".format(list,what))
    if len(list) == 0:
        raise ValueError("No index. List is empty")
    left = 0
    right = len(list)-1
    step = 1

    while True:
        mid = int( (right+left)/2 )
        logging.debug("left: {}, right: {}, middle: {}, step: {}".format(left, right, mid, step))
        if list[mid] == what:
            return mid
        elif list[mid] < what:
            if mid == left:
                if list[right] == what:
                    return right
                else:
                    raise ValueError("No exact index, nearest indexes are {} and {}".format(left,right))
            left = mid
        else:
            if mid == right:
                if list[left] == what:
                    return left
                else:
                    raise ValueError("No exact index, nearest indexes are {} and {}".format(left,right))
            right = mid
        step += 1

    return None


if __name__ == '__main__':
#    logging.basicConfig( level=logging.DEBUG)
    list = [11, 31, 5, 15, 10, 12, 22, 9, 2, 4]
    list.sort()
    for what in range(0,list[-1]+1):
        try:
            index = binSearch(list, what)
            print( "Found index={} for value={}".format(index,what))
        except ValueError as e:
            print( "Not found index for value={}, error={}".format(what, e))
