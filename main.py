from node import *

def main():
    testinit()

def testinit():
    # 1
    head = node('T', None)
    head = node('K', head)
    head = node('N', head)
    head = node('I', head)
    head = node('L', head)

    # 2
    selection = head

    # 3
    selection = selection.getLink()
    selection = selection.getLink()
    selection = selection.getLink()

    # 4
    selection.addNodeAfter('E')

    # 5
    selection = selection.getLink()

    # 6
    selection.addNodeAfter('D')

    # 7
    selection = selection.getLink()

    # 8
    selection.addNodeAfter('L')

    # 9
    selection = selection.getLink()

    # 10
    selection.addNodeAfter('I')
    
    # 11
    selection = selection.getLink()

    # 12
    selection.addNodeAfter('S')

    # 13
    print("How many nodes does head contain? ", node.listLength(head))
    print("How many nodes does selection contain? ", node.listLength(selection))
    
    # 14
    tail = selection

    # 15
    tail = tail.getLink()
    tail = tail.getLink()

    # 16
    print("How many nodes does tail contain? ", node.listLength(tail))

    # 17
    selection.removeNodeAfter()
    selection.removeNodeAfter()

    # 18
    print("How many nodes does head contain? ", node.listLength(head))
    print("How many nodes does selection contain? ", node.listLength(selection))
    print("How many nodes does tail contain? ", node.listLength(tail))

    # 19
    head.removeNodeAfter()
    head.removeNodeAfter()

    # 20
    tail = tail.getLink()

    # 21
    print("How many nodes does head contain? ", node.listLength(head))
    print("How many nodes does selection contain? ", node.listLength(selection))
    print("How many nodes does tail contain? ", node.listLength(tail))

    # 22
    print("Head contains the letter", node.listSearch(head, "K").getData())
    print("Head contains the letter", node.listSearch(selection, "I").getData())

    # 23
    copy = node.listCopy(head)
    other_copy = node.listCopy(selection)
    print("Copy[0] contains", node.listLength(copy))
    print("Copy[1] contains", node.listLength(other_copy))

    # 24
    print("Copy[0] contains", node.listPosition(copy, 1).getData())
    print("Copy[1] contains", node.listPosition(other_copy, 1).getData())

    # 25
    for i in range(1,11):
        if (node.listPosition(head, i) != None):
            print("Head contains position", i)
        else:
            print("Head doesn't contain position", i)


if __name__ == '__main__':
    main()