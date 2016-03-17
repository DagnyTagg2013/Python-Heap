import sys
from Heaps.binheap import BinHeap

def main(args):

    # CASE 0:  CTOR
    print 'Hello2!'
    bh = BinHeap()
    print 'Hello3!'

    # CASE 1:  INITIALIZE 1
    bh.buildHeap([9])
    bh.printContents()

    # CASE 2:  INITIALIZE 10 @ max external capacity
    bh.buildHeap([9,5,6,2,3,11,30,45,15,50])
    bh.printContents()

    # CASE 3:  Testing External Cache-Control
    newStreamElement = 88;
    bh.insert(newStreamElement);

    bh.printContents()


# ATTENTION:  main entrypoint, for Python to emulate Java main entrypoint
if __name__ == '__main__':
    main(sys.argv)

