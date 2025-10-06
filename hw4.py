import sat_interface

def tt1():
    '''Propositions:
        A: Amy is a truth-teller
        B: Bob is a truth-teller
        C: Cal is a truth-teller

    return a list containing all entailed propositions or negated propositions
    '''
    print("Truth-tellers and liars I")
    print("-------------------------")
    ttprob = sat_interface.KB(["~A ~B",
                                "B A",
                                "~B ~C",
                                "C B",
                                "~C ~A",
                                "~C ~B",
                                "A B C"])

    entailed = []
    if ttprob.test_literal("A") == False:
        entailed.append('~A')
        print("Amy is a liar")
    if ttprob.test_literal("~A") == False:
        entailed.append('A')
        print("Amy is a truth-teller")
    if ttprob.test_literal("B") == False:
        entailed.append('~B')
        print("Bob is a liar")
    if ttprob.test_literal("~B") == False:
        entailed.append('B')
        print("Bob is a truth-teller")
    if ttprob.test_literal("C") == False:
        entailed.append('~C')
        print("Cal is a liar")
    if ttprob.test_literal("~C") == False:
        entailed.append('C')
        print("Cal is a truth-teller")
    print("-------------------------")
    return entailed

def tt2():
    '''Propositions:
        A: Amy is a truth-teller
        B: Bob is a truth-teller
        C: Cal is a truth-teller
    '''
    print("Truth-tellers and liars II")
    entailed = []
    # your code here!
    return entailed

def prize():
    '''Propositions:
        You tell me!
    '''
    print("Prize box")
    entailed = []

    return entailed


def salt():
    '''Propositions:
        You tell me!
    '''
    print("A salt and battery")
    entailed = []
    # your code here!
    return entailed

def main():
    tt1()
    tt2()
    salt()
    prize()

if __name__ == '__main__':
    main()
