def listComprehension():
    """List comprehension example
    """
    inpt = ['x', 'y', 'z']

    print([j * i for j in inpt for i in range(1, 5)])
    print([j * i for j in range(1, 5) for i in inpt])
    print([[[j] for j in range(i, i + 3)] for i in range(2, 5)])
    print([[j for j in range(i, i + 4)] for i in range(2, 6)])
    print([(i, j) for i in range(1, 4) for j in range(1, 4)])


def testFilterFunction(var):
    """
    Filter call this function.
    :param var:
    :return:
    """
    if var >= 18:
        return True
    return False


def testReduceFunction(var1, var2):
    """
    Reduce function call.
    :param var:
    :return:
    """
    return var1 + var2


def myFilter(funName, list_var):
    """
    My Filter function.
    :param funName: Function name use for filter.
    :param list_var: List of variable.
    :return: list - return list
    """
    return_list_var = list()
    if isinstance(list_var, list):
        for element in list_var:
            val = funName(element)
            if val:
                return_list_var.append(element)
    return return_list_var


def myReduce(funName, list_name):
    """
    My Reduce Function.
    :param funName: Function name use for filter.
    :param list_name: List of variable.
    :return: return single value.
    """
    val = None
    if isinstance(list_name, list):
        val = list_name[0]
        for element in list_name[1:]:
            val = funName(val, element)
    return val


if __name__ == '__main__':
    print('Assignment qa1.1')
    print(myFilter(testFilterFunction, [18, 4, 19, 21, 91, 27, 24, 7, 60]))
    print('Assignment qa1.2')
    print(myReduce(testReduceFunction, [18, 4, 19, 21, 91, 27, 24, 7, 60]))
    print('Assignment qa2')
    listComprehension()
