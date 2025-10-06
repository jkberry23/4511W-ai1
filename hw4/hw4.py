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
    print("-------------------------")
    ttprob = sat_interface.KB(["~A C",
                                "~A A",
                                "~C ~A A",
                                "~B ~C",
                                "C B",
                                "~C B ~A",
                                "C ~B",
                                "C A"])
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

def salt():
    '''Propositions:
        CPS: The Caterpillar stole the salt
        CCS: The Cheshire Cat stole the salt
        BLS: Bill the Lizard stole the salt
        CPL: The Caterpillar lied
        CCL: The Cheshire Cat lied
        BLL: Bill the Lizard lied
    '''
    print("A salt and battery")
    print("-------------------------")
    ttprob = sat_interface.KB(["CPS CCS BLS",
                                "~CPS ~CCS",
                                "~CPS ~BLS",
                                "~CCS ~BLS",
                                "CPL CCL BLL",
                                "~CPL ~CCL ~BLL",
                                "~BLS ~CPL",
                                "CPL BLS",
                                "CCL ~CCS",
                                "~CCL CCS",
                                "BLL ~CPL",
                                "CPL ~BLL"])
    entailed = []
    if ttprob.test_literal("CPL") == False:
        entailed.append('~CPL')
        print("The Caterpillar told the truth")
    if ttprob.test_literal("~CPL") == False:
        entailed.append('CPL')
        print("The Caterpillar lied")
    if ttprob.test_literal("CCL") == False:
        entailed.append('~CCL')
        print("The Cheshire Cat told the truth")
    if ttprob.test_literal("~CCL") == False:
        entailed.append('CCL')
        print("The Cheshire Cat lied")
    if ttprob.test_literal("BLL") == False:
        entailed.append('~BLL')
        print("Bill the Lizard told the truth")
    if ttprob.test_literal("~BLL") == False:
        entailed.append('BLL')
        print("Bill the Lizard lied")
    if ttprob.test_literal("CPS") == False:
        entailed.append('~CPS')
        print("The Caterpillar did not steal the salt")
    if ttprob.test_literal("~CPS") == False:
        entailed.append('CPS')
        print("The Caterpillar stole the salt")
    if ttprob.test_literal("CCS") == False:
        entailed.append('~CCS')
        print("The Cheshire Cat did not steal the salt")
    if ttprob.test_literal("~CCS") == False:
        entailed.append('CCS')
        print("The Cheshire Cat stole the salt")
    if ttprob.test_literal("BLS") == False:
        entailed.append('~BLS')
        print("Bill the Lizard did not steal the salt")
    if ttprob.test_literal("~BLS") == False:
        entailed.append('BLS')
        print("Bill the Lizard did not steal the salt")
    print("-------------------------")
    return entailed

def prize():
    '''Propositions:
        RP: The prize is in the red box
        GP: The prize is in the green box
        BP: The prize is in the blue box
        RT: The red box's statement is true
        GT: The green box's statement is true
        BT: The blue box's statement is true
    '''
    print("Prize Box")
    print("-------------------------")
    ttprob = sat_interface.KB(["RP GP BP",    #prize must be in a box
                                "~RP ~GP",    #prize must not be in more than one box
                                "~RP ~BP",
                                "~GP ~BP",
                               "RT GT BT",    #a message is true
                                "~RT ~GT",    #not more than one message is true
                                "~RT ~BT",
                                "~GT ~BT",
                               "RT ~RP",
                               "~RT RP",
                               "BT BP",
                               "~BT ~BP",
                               "~GT ~RP",
                               "GT RP"])
    entailed = []
    if ttprob.test_literal("RP") == False:
        entailed.append('~RP')
        print("The prize is not in the red box")
    if ttprob.test_literal("~RP") == False:
        entailed.append('RP')
        print("The prize is in the red box")
    if ttprob.test_literal("BP") == False:
        entailed.append('~BP')
        print("The prize is not in the blue box")
    if ttprob.test_literal("~BP") == False:
        entailed.append('BP')
        print("The prize is in the blue box")
    if ttprob.test_literal("GP") == False:
        entailed.append('~GP')
        print("The prize is not in the green box")
    if ttprob.test_literal("~GP") == False:
        entailed.append('GP')
        print("The prize is in the green box")
    if ttprob.test_literal("RT") == False:
        entailed.append('~RT')
        print("The message on the red box is false")
    if ttprob.test_literal("~RT") == False:
        entailed.append('RT')
        print("The message on the red box is true")
    if ttprob.test_literal("BT") == False:
        entailed.append('~BT')
        print("The message on the blue box is false")
    if ttprob.test_literal("~BT") == False:
        entailed.append('BT')
        print("The message on the blue box is true")
    if ttprob.test_literal("GT") == False:
        entailed.append('~GT')
        print("The message on the green box is false")
    if ttprob.test_literal("~GT") == False:
        entailed.append('GT')
        print("The message on the green box is true")
    
    print("-------------------------")
    return entailed

def main():
    tt1()
    tt2()
    salt()
    prize()

if __name__ == '__main__':
    main()
