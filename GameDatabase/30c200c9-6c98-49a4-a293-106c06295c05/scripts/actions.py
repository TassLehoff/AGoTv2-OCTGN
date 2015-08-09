#-*- coding: utf-8 -*-  
#coding=utf-8 
#---------------------------------------------------------------------------
# Constants
#---------------------------------------------------------------------------
Gold = ("Gold", "4e8046ba-759b-428c-917f-7e9268a5af90") #The GUID from markers.o8g
Power = ("Power", "d115ea96-ed05-4bf7-ba22-a34c8675c676") #The GUID from markers.o8g
STR_Up = ("STR_Up", "7898d5a0-1d59-42b2-bbfb-5051cc420cd8") #The GUID from markers.o8g
Burn = ("Burn", "c272aa0c-f283-4ff5-b545-a5a3f150e6da") #The GUID from markers.o8g
TokenRed = ("TokenRed", "6238a357-41b7-4bca-b394-925fc1b2caf8") #The GUID from markers.o8g
TokenBlue = ("TokenBlue", "99452bc7-d95b-4c54-8577-41d98dd3e30b") #The GUID from markers.o8g
MilitaryColor = "#ae0603" #A shade of red from the Military Icon
IntrigueColor = "#006b34" #A shade of green from the Intrigue Icon
PowerColor = "#1a4d8f" #A shade of blue from the Power Icon
GameURL = "https://drive.google.com/folderview?id=0BzUduMHRwqG0fk55b3hiX2d6aEN3Tk9VTGpOQWQxMlNfOGc2cUxnbUltWExRMjlsamlTWHc&usp=sharing#list"
#FAQ_URL = "http://www.fantasyflightgames.com/ffg_content/agotlcg/support/FAQ-TR-updates/AGoT-FAQ.pdf"

    
#---------------------------------------------------------------------------
# Table group actions
#---------------------------------------------------------------------------
def googleDriveWebsite(group, x = 0, y = 0):
    mute()

    openUrl("{}".format(GameURL))
    
def faqWebsite(group, x = 0, y = 0):
    mute()
    
    openUrl("{}".format(FAQ_URL))
    
def flipCoin(group, x = 0, y = 0):
    mute()
    n = rnd(1, 2)
    if n == 1:
        notify("**{} flips heads.**".format(me))
    else:
        notify("**{} flips tails.**".format(me))
        
def sixSided(group, x = 0, y = 0):
    mute()
    n = rnd(1,6)
    notify("**{} rolls a {} on a 6-sided die.**".format(me, n))
    
def twelveSided(group, x = 0, y = 0):
    mute()
    n = rnd(1,12)
    notify("**{} rolls a {} on a 12-sided die.**".format(me, n))
    
def xSided(group, x = 0, y = 0):
    mute()
    sides = askInteger("Roll a how many sided die? (minimum 3)", 3)
    if sides == None: return
    elif sides < 3:
        whisper("Please choose a number greater than or equal to 3.")
        return
    else:
        n = rnd(1,sides)
        notify("**{} rolls a {} on a {}-sided die.**".format(me, n, sides))

def cancelAllHighlight(group, x = 0, y = 0):
    mute()
    for card in group:
        card.target(False)
        if card.controller == me:
            card.highlight = None

def turnDone(group, x = 0, y = 0):
    mute()
    notify("**{} is done.**".format(me))
    table.create("73a6655b-60b6-4080-b428-f4e0099e0f77",0,0)

def restoreAll(group, x = 0, y = 0): 
    mute()
    myCards = (card for card in table
                if card.controller == me)
    for card in myCards:
        if card.isFaceUp:
            card.orientation &= ~Rot90
            card.highlight = None
    notify("{} stands all their cards.".format(me))

def announceMil(group, x = 0, y = 0):
    mute()
    notify("**{} declares a MIL challenge.**".format(me))

def announceInt(group, x = 0, y = 0):
    mute()
    notify("**{} declares an INT challenge.**".format(me))

def announcePow(group, x = 0, y = 0):
    mute()
    notify("**{} declares a PWR challenge.**".format(me))

def holdOn(group, x = 0, y = 0):
    mute()
    notify("**Please wait.  {} has an action/question.**".format(me))

def announceUO(group, x = 0, y = 0):
    mute()
    notify("**{} responds: Unopposed.**".format(me))

def announceOpp(group, x = 0, y = 0):
    mute()
    notify("**{} responds: Opposed/Defend.**".format(me))
    
def scoop(group, x = 0, y = 0):
    mute()
    
    if not confirm("Scoop your side of the table?"): return
    
    var = me.getGlobalVariable("setupOk")
    var="0"
    me.setGlobalVariable("setupOk", var)
    
    for c in me.hand: 
        if not c.Type == "Faction" and not c.Type == "Agenda":
            c.moveTo(me.Deck)           
    for c in me.piles['Discard Pile']: c.moveTo(me.Deck)
    for c in me.piles['Dead Pile']: c.moveTo(me.Deck)

    myCards = (card for card in table
            if card.owner == me)

    for card in myCards:
        if card.Type == "Faction": 
            card.moveTo(me.hand)
        elif card.Type == "Agenda":
            card.moveTo(me.hand)
        elif card.Type == "Plot": 
            card.moveTo(me.piles['Plot Deck'])
        else: 
            card.moveTo(me.Deck)

    notify("{} scoops their side of the table.".format(me))


#---------------------------------------------------------------------------
# Table card actions
#---------------------------------------------------------------------------

    
def cardLookup(card, x = 0, y = 0):
    mute()
    
    if card.isFaceUp:
        webSite = ""
        webSite += "http://www.cardgamedb.com/index.php/GoT/gotcardsearch.html?ft=0"
        webSite += "&name={}".format(card.name)
        webSite += "&type={}".format(card.Type)
        openUrl("{}".format(webSite))
    else:
        whisper("Card must be face up to use this feature.")
    
def kneel(card, x = 0, y = 0):
    mute()
    card.orientation ^= Rot90
    if card.orientation & Rot90 == Rot90:
        notify('{} kneels {}.'.format(me, card))
    else:
        notify('{} stands {}.'.format(me, card))

def flipcard(card, x = 0, y = 0):
    mute()
    if card.isFaceUp:
        notify("{} turns {} face down.".format(me, card))
        card.isFaceUp = False
        card.orientation &= ~Rot90
    else:
        card.isFaceUp = True
        notify("{} turns {} face up.".format(me, card))

def addPower(card, x = 0, y = 0):
    mute()
    notify("{} adds a Power to {}.".format(me, card))
    card.markers[Power] += 1
    me.counters['Power'].value += 1
    
def addSTR_Up(card, x = 0, y = 0):
    mute()
    card.markers[STR_Up] += 1
    
def addBurn(card, x = 0, y = 0):
    mute()
    card.markers[Burn] += 1

def addRedToken(card, x = 0, y = 0):
    mute()
    card.markers[TokenRed] += 1
    
def addBlueToken(card, x = 0, y = 0):
    mute()
    card.markers[TokenBlue] += 1
   
def subPower(card, x = 0, y = 0):
    mute()
    notify("{} subtracts a Power to {}.".format(me, card))
    card.markers[Power] -= 1 
    me.counters['Power'].value -= 1
    
def subSTR_Up(card, x = 0, y = 0):
    mute()
    card.markers[STR_Up] -= 1
    
def subBurn(card, x = 0, y = 0):
    mute()
    card.markers[Burn] -= 1
    
def subRedToken(card, x = 0, y = 0):
    mute()
    card.markers[TokenRed] -= 1
    
def subBlueToken(card, x = 0, y = 0):
    mute()
    card.markers[TokenBlue] -= 1
    
def addMilitaryHighlight(card, x = 0, y = 0):
    mute()
    card.highlight = MilitaryColor
    card.target(False)
    
def addIntrigueHighlight(card, x = 0, y = 0):
    mute()
    card.highlight = IntrigueColor
    card.target(False)
    
def addPowerHighlight(card, x = 0, y = 0):
    mute()
    card.highlight = PowerColor
    card.target(False)

def cancelHighlight (card, x = 0, y = 0):
    mute()
    card.highlight = None
    card.target(False)

#---------------------------
#movement actions
#---------------------------

#------------------------------------------------------------------------------
# Hand Actions
#------------------------------------------------------------------------------

def randomDiscard(group):
    mute()
    card = group.random()
    if card == None: return
    card.moveTo(me.piles['Discard pile'])
    notify("{} randomly discards {}.".format(me, card))
 
def discardMany(group):
    count = 0
    discAmount = None
    
    mute()
    if len(group) == 0: return
    if discAmount == None: discAmount = askInteger("Randomly discard how many cards?", 2)
    if discAmount == None: return
    
    for index in range(0,discAmount):
        card = group.random()
        if card == None: break
        card.moveTo(me.piles['Discard pile'])
        count += 1
        notify("{} randomly discards {}.".format(me,card))
    notify("{} randomly discards {} cards.".format(me, count))

def mulligan(group):
    count = None
    draw = None
    mute()
    
    if not confirm("Are you sure you want to Mulligan?"): return
    if draw == None: draw = askInteger("How many cards would you like to draw for your Mulligan?", len(me.hand))
    if draw == None: return
    
    for card in group:
        card.moveToBottom(me.deck)
            
    me.deck.shuffle()
        
    for card in me.deck.top(draw):
        card.moveTo(me.hand)
    notify("{} mulligans and draws {} new cards.".format(me, draw))

def play(card, x=0, y=0):
    mute()
    if card.cost == "" : 
        whisper("You can't play this card")
        return
    if card.Cost == "X": cost=askInteger("How much do you want to pay to play {} ? ".format(card.name),0)
    else : cost=int(card.Cost)
    reduc=askInteger("Reduce Cost by ?",0)
    if reduc == None or cost == None: return
    if reduc>cost: reduc=cost
    cost-=reduc
    if me.counters['Gold'].value < cost :
        whisper("You don't have enough Gold to pay for {}.".format(card.name))
        return      
    if me.hasInvertedTable(): card.moveToTable(0,-288)
    else :  card.moveToTable(0,160)
    notify("{} plays {} for {} Gold (Cost reduced by {}).".format(me,card,cost,reduc))
    me.counters['Gold'].value -= cost
    for incomecard in table:
        if incomecard.controller == me and incomecard.markers[Gold] > 0:
            incomecard.markers[Gold] -= cost

#------------------------------------------------------------------------------
# Pile Actions
#------------------------------------------------------------------------------

def shuffle(group):

    group.shuffle()

def draw(group):
    mute()
    if len(group) == 0: return
    group[0].moveTo(me.hand)
    notify("{} draws a card.".format(me))
    
def drawRandom(group):
    mute()
    
    card = group.random()
    if card == None: return
    card.moveTo(me.hand)
    notify("{} randomly draws a plot card.".format(me))

def drawMany(group):
    drawAmount = None
    
    mute()
    if len(group) == 0: return
    if drawAmount == None: drawAmount = askInteger("Draw how many cards?", 7)
    if drawAmount == None: return
    
    if len(group) < drawAmount:
        drawAmount = len(group)
    
    for card in group.top(drawAmount):
        card.moveTo(me.hand)
    notify("{} draws {} cards.".format(me, drawAmount))
 
def discardManyFromTop(group):
    count = 0
    discAmount = None
    
    mute()
    if len(group) == 0: return
    if discAmount == None: discAmount = askInteger("Discard how many from top?", 4)
    if discAmount == None: return
    
    for index in range(0,discAmount):
        card = group.top()
        card.moveTo(me.piles['Discard pile'])
        count += 1
        if len(group) == 0: break
    notify("{} discards {} cards from the top of their Deck.".format(me, count))
    
def reshuffle(group):
    count = None
    
    mute()
    if len(group) == 0: return
    if not confirm("Are you sure you want to reshuffle the {} back into your Deck?".format(group.name)): return
    
    myDeck = me.deck
    for card in group:
        card.moveTo(myDeck)
    myDeck.shuffle()
    notify("{} shuffles thier {} back into their deck.".format(me, group.name))
    
def moveOneRandom(group):
    mute()
    if len(group) == 0: return
    if not confirm("Are you sure you want to move one random card from your {} to your Hand?".format(group.name)): return
    
    card = group.random()
    if card == None: return
    card.moveTo(me.hand)
    notify("{} randomly moves {} from their discard to thier hand.".format(me, card.name))



#------------------------------------------------------------------------------
# New Actions
#---------------------------------------------------------------------------
# New Table group actions
#---------------------------------------------------------------------------

def setup(group, x = 0, y = 0):
    mute()
    if not confirm("Confirm to setup?"): return
    var = me.getGlobalVariable("setupOk")
    if var == "1":
        notify("You already did your Setup")
        return
    if len(me.hand) == 0:
        notify("You need to load a deck first") 
        return
    var="1"
    me.setGlobalVariable("setupOk", var)
    notify("**{} has started setup, please wait**".format(me))
    checkdeck(me.deck)
    for c in me.hand: 
        if c.Type == "Faction":
            if me.hasInvertedTable(): 
                c.moveToTable(300,-100)         
            else:
                c.moveToTable(-280,0)
        if c.Type == "Agenda":
            if me.hasInvertedTable(): 
                c.moveToTable(220,-100)         
            else:
                c.moveToTable(-200,0)
    me.deck.shuffle()
    for card in me.deck.top(7):
        card.moveTo(me.hand)
    table.create("73a6655b-60b6-4080-b428-f4e0099e0f77",0,0)
    notify("**{} is ready**".format(me))

def endturn(group, x = 0, y = 0): 
    count = 0
    discAmount = None
    mute()
    if not confirm("Are you sure to end this turn?"): return
    myCards = (card for card in table  #restore all cards
            if card.controller == me)
    for card in myCards:
        if card.isFaceUp:
            card.orientation &= ~Rot90
            card.highlight = None
    me.counters['Gold'].value = 0  #reset gold counters
    goldcard = (card for card in table
            if card.controller == me)
    for card in goldcard: 
        card.markers[Gold] = 0
    getreserve(group)
    if len(me.hand) > me.counters['Reserve'].value:  #check reserve
        if discAmount == None: 
            notify("The number of cards in {}'s hand is more than your reserve.You should discard {} cards.".format(me, len(me.hand)-me.counters['Reserve'].value))
            discAmount = askInteger("Randomly discard how many cards?", len(me.hand)-me.counters['Reserve'].value) 
        if discAmount == None: return
        for index in range(0,discAmount):
            card = me.hand.random()
            if card == None: break
            card.moveTo(me.piles['Discard pile'])
            count += 1
            notify("{} randomly discards {}.".format(me,card))
    else:
        notify("You can keep all of your cards in hand.")
    for c in table: 
        if c.Type == "Plot" and c.controller == me:
            c.moveTo(me.piles['Used Plot Pile'])
    me.counters['Reserve'].value = 0
    me.counters['Initiative'].value = 0
    me.setGlobalVariable("turn", "0")
    notify("{} is ready for a new turn.".format(me))

def countincome(group, x=0, y=0):
    mute()
    if me.getGlobalVariable("turn") == "0":
        uniquecards = []
        for incomecard in table:
            if incomecard.isFaceUp:
                if incomecard.goldincome and incomecard.controller == me:
                    if incomecard.Unique != "Yes":
                        me.counters['Gold'].value += int(incomecard.goldincome)
                    elif incomecard.Unique == "Yes" and incomecard.name not in uniquecards:
                        uniquecards.append(incomecard.name)
                        me.counters['Gold'].value += int(incomecard.goldincome)
        for plotcard in table:
            if plotcard.type == "Plot" and plotcard.controller == me:
                me.counters['Gold'].value += int(plotcard.plotgoldincome)
                plotcard.markers[Gold] += me.counters['Gold'].value
        notify("{} counts income {} gold.".format(me,me.counters['Gold'].value))
        me.setGlobalVariable("turn", "1")
        return
    else:
        notify("You have already counted income.")

def getreserve(group, x=0, y=0):
    mute()
    for person in players:
        person.counters['Reserve'].value = 0
        personCards = (card for card in table
                        if card.controller == person)
        uniquecards = []
        for card in personCards:
            if card.isFaceUp:
                if card.Reserve and int(card.Reserve) > 0:
                    if card.Unique != "Yes":
                        person.counters['Reserve'].value += int(card.Reserve)
                    elif card.name not in uniquecards:
                        uniquecards.append(card.name)
                        person.counters['Reserve'].value += int(card.Reserve)   
                elif card.type == "Plot":
                    person.counters['Reserve'].value += int(card.plotReserve)
        notify("{}'s Reserve value is {}.".format(person,person.counters['Reserve'].value))
    return

def getInit(group, x = 0, y = 0):
    mute()
    for person in players:
        person.counters['Initiative'].value = 0
        personCards = (card for card in table
                        if card.controller == person)
        uniquecards = []
        for card in personCards:
            if card.isFaceUp:
                if card.Initiative and int(card.Initiative) > 0:
                    if card.Unique != "Yes":
                        person.counters['Initiative'].value += int(card.Initiative)
                    elif card.name not in uniquecards:
                        uniquecards.append(card.name)
                        person.counters['Initiative'].value += int(card.Initiative) 
                elif card.type == "Plot":
                    person.counters['Initiative'].value += int(card.plotInitiative)
        notify("{}'s Initiative value is {}.".format(person,person.counters['Initiative'].value))
    return

def fp(group, x = 0, y = 0):
    mute()
    if len(players) == 2:
        getInit(table)
        if players[0].counters['Initiative'].value == players[1].counters['Initiative'].value:
            notify("{}'s initiative value is same as {}.".format(players[0],players[1]))
            recalcPower(table)
            if players[0].counters['Power'].value == players[1].counters['Power'].value:
                if not confirm("Are you sure to decide who wins the initiative randomly?"): return
                n = rnd(1, 2)
                if n == 1:
                    notify("**{} flips heads,and wins the initiative.**".format(players[0]))
                    notify("**{} decides who is the first player.**".format(players[0]))
                else:
                    notify("**{} flips heads,and wins the initiative.**".format(players[1]))
                    notify("**{} decides who is the first player.**".format(players[1]))
            if players[0].counters['Power'].value > players[1].counters['Power'].value:
                notify("**{} wins the initiative.**".format(players[1]))
                notify("**{} decides who is the first player.**".format(players[1]))
            if players[0].counters['Power'].value < players[1].counters['Power'].value:
                notify("**{} wins the initiative.**".format(players[0]))
                notify("**{} decides who is the first player.**".format(players[0]))
        elif players[0].counters['Initiative'].value > players[1].counters['Initiative'].value:
            notify("{} wins the initiative.".format(players[0]))
            notify("**{} decides who is the first player.**".format(players[0]))
        else:
            notify("{} wins the initiative.".format(players[1]))
            notify("**{} decides who is the first player.**".format(players[1]))
    else:
        notify("Only supported for Joust format.")
        return

def recalcPower(group, x = 0, y = 0):
    mute()
    index = 0
    for person in players:
        person.counters['Power'].value = 0
        personCards = (card for card in table
                        if card.controller == person)
        for card in personCards:
            if card.markers[Power] > 0:
                person.counters['Power'].value += card.markers[Power]
        notify("{} has a total of {} power.".format(person.name,person.counters['Power'].value))

def dominance(group, x=0, y=0):
    mute()
    for person in players:
        person.counters['Str'].value = 0
        personCards = (card for card in table
                        if card.controller == person)
        uniquecards = []
        for card in personCards:
            if card.isFaceUp:
                if card.orientation != Rot90:
                    if card.Strength and int(card.Strength) > 0:
                        if card.Unique != "Yes":
                            person.counters['Str'].value += int(card.Strength)
                        elif card.name not in uniquecards:
                            uniquecards.append(card.name)
                            person.counters['Str'].value += int(card.Strength)
                    if card.markers[STR_Up] > 0:
                        person.counters['Str'].value += card.markers[STR_Up]
                    if card.markers[Burn] > 0:
                        person.counters['Str'].value -= card.markers[Burn]
                if card.dominance and int(card.dominance) > 0:
                    if card.Unique != "Yes":
                        person.counters['Str'].value += int(card.dominance)
                    elif card.name not in uniquecards:
                        uniquecards.append(card.name)
                        person.counters['Str'].value += int(card.dominance)
                if card.markers[Gold] > 0:
                    person.counters['Str'].value += card.markers[Gold]
        notify("{}'s total for dominance is {}.".format(person,person.counters['Str'].value))
    if not confirm("Confirm to proceed?"): return
    if len(players) == 2:
        if players[0].counters['Str'].value == players[1].counters['Str'].value:
            notify("No one wins dominance.")
        elif players[0].counters['Str'].value > players[1].counters['Str'].value:
            notify("{} wins the dominance.".format(players[0]))
            for housecard in table:
                if housecard.type == "Faction" and housecard.controller == players[0]:
                    addPower(housecard)
        else:
            notify("{} wins the dominance.".format(players[1]))
            for housecard in table:
                if housecard.type == "Faction" and housecard.controller == players[1]:
                    addPower(housecard)
    else:
        notify("Only supported for Joust format.")
    return

def challenge(group, x=0, y=0):
    mute()
    choiceList = ['Military', 'Intrigue', 'Power']
    choice = askChoice("To which challenge do you want to calculate? ", choiceList)
    for person in players:
        person.counters['Str'].value = 0
        personCards = (card for card in table
                        if card.controller == person)
        uniquecards = []
        for card in personCards:
            if card.isFaceUp:
                if choice == 1 and card.highlight == MilitaryColor:
                    if card.Strength and int(card.Strength) > 0:
                        if card.Unique != "Yes":
                            person.counters['Str'].value += int(card.Strength)
                        elif card.name not in uniquecards:
                            uniquecards.append(card.name)
                            person.counters['Str'].value += int(card.Strength)
                    if card.markers[STR_Up] > 0:
                        person.counters['Str'].value += card.markers[STR_Up]
                    if card.markers[Burn] > 0:
                        person.counters['Str'].value -= card.markers[Burn]
                elif choice == 2 and card.highlight == IntrigueColor:
                    if card.Strength and int(card.Strength) > 0:
                        if card.Unique != "Yes":
                            person.counters['Str'].value += int(card.Strength)
                        elif card.name not in uniquecards:
                            uniquecards.append(card.name)
                            person.counters['Str'].value += int(card.Strength)
                    if card.markers[STR_Up] > 0:
                        person.counters['Str'].value += card.markers[STR_Up]
                    if card.markers[Burn] > 0:
                        person.counters['Str'].value -= card.markers[Burn]
                elif choice == 3 and card.highlight == PowerColor:
                    if card.Strength and int(card.Strength) > 0:
                        if card.Unique != "Yes":
                            person.counters['Str'].value += int(card.Strength)
                        elif card.name not in uniquecards:
                            uniquecards.append(card.name)
                            person.counters['Str'].value += int(card.Strength)
                    if card.markers[STR_Up] > 0:
                        person.counters['Str'].value += card.markers[STR_Up]
                    if card.markers[Burn] > 0:
                        person.counters['Str'].value -= card.markers[Burn]
        notify("{}'s total strength for such challenge is {}.".format(person,person.counters['Str'].value))
    
def challengeAnnounce(group, x=0, y=0):
    mute()
    choiceList = ['Military', 'Intrigue', 'Power', 'No challenge and Pass']
    choice = askChoice("Which challenge do you want to initiate?", choiceList)
    if choice == 1:
        announceMil(table)
    elif choice == 2:
        announceInt(table)
    elif choice == 3:
        announcePow(table)
    elif choice == 4:
        notify("{} has no challenge to initiate.".format(me))
    else:return

#def chooseplot(group, x=0, y=0):
#   mute()
#   cardList = []
#   for card in me.piles['Plot Deck']:
#       cardList.append(card.name)
#   choice = askChoice("Choose a card.",cardList)
#   notify("****")

#------------------------------------------------------------------------------
# New Pile Actions
#------------------------------------------------------------------------------
def checkdeck(group):
    mute()
    notify (" -> Checking deck of {} ...".format(me))

    NeutralCount = 0
    LannisterCount = 0
    MartellCount = 0
    NightCount =0
    StarkCount=0
    TargaryenCount=0
    TyrellCount=0
    BaratheonCount=0
    GreyjoyCount=0
    for card in group:
        if card.faction=='Neutral.':
            NeutralCount += 1
        elif card.faction=='Lannister.':
            LannisterCount += 1
        elif card.faction=='Martell.':
            MartellCount += 1
        elif card.faction=="Night's Watch.":
            NightCount += 1
        elif card.faction=='Stark.':
            StarkCount += 1
        elif card.faction=='Targaryen.':
            TargaryenCount += 1
        elif card.faction=='Tyrell.':
            TyrellCount += 1
        elif card.faction=='Baratheon.':
            BaratheonCount += 1
        elif card.faction=='Greyjoy.':
            GreyjoyCount += 1

    for card in me.hand:
        if card.name == "Fealty":
            if NeutralCount>15:
                    notify("Your Agenda is[{}],You include {} neutral cards in your deck, which is not permitted.".format(card.name, NeutralCount, me))
            else:
                    notify("Your Agenda is[{}]".format(card.name))
            return
        elif card.name == "Banner of the Lion":
            if LannisterCount<12:
                    notify("Your Agenda is[{}],You include {} Lannister cards in your deck, which is not permitted.".format(card.name, LannisterCount, me))
            else:
                    notify("Your Agenda is[{}]".format(card.name))
            return
        elif card.name == "Banner of the Sun":
            if MartellCount<12:
                    notify("Your Agenda is[{}],You include {} Martell cards in your deck, which is not permitted.".format(card.name, MartellCount, me))
            else:
                    notify("Your Agenda is[{}]".format(card.name))
            return
        elif card.name == "Banner of the Watch":
            if NightCount<12:
                    notify("Your Agenda is[{}],You include {} Night's Watch cards in your deck, which is not permitted.".format(card.name, NightCount, me))
            else:
                    notify("Your Agenda is[{}]".format(card.name))
            return
        elif card.name == "Banner of the Wolf":
            if StarkCount<12:
                    notify("Your Agenda is[{}],You include {} Stark cards in your deck, which is not permitted.".format(card.name, StarkCount, me))
            else:
                    notify("Your Agenda is[{}]".format(card.name))
            return
        elif card.name == "Banner of the Dragon":
            if TargaryenCount<12:
                    notify("Your Agenda is[{}],You include {} Targaryen cards in your deck, which is not permitted.".format(card.name, TargaryenCount, me))
            else:
                    notify("Your Agenda is[{}]".format(card.name))
            return
        elif card.name == "Banner of the Rose":
            if TyrellCount<12:
                    notify("Your Agenda is[{}],You include {} Tyrell cards in your deck, which is not permitted.".format(card.name, TyrellCount, me))
            else:
                    notify("Your Agenda is[{}]".format(card.name))
            return
        elif card.name == "Banner of the Stag":
            if BaratheonCount<12:
                    notify("Your Agenda is[{}],You include {} Baratheon cards in your deck, which is not permitted.".format(card.name, BaratheonCount, me))
            else:
                    notify("Your Agenda is[{}]".format(card.name))
            return
        elif card.name == "Banner of the Kraken":
            if GreyjoyCount<12:
                    notify("Your Agenda is[{}],You include {} Grejoy cards in your deck, which is not permitted.".format(card.name, GreyjoyCount, me))
            else:
                    notify("Your Agenda is[{}]".format(card.name))
            return

    notify("You have no Agenda or Your Agenda is not in your hand")

def shuffleToPlot(group):
    mute()
    for card in group:
        card.moveTo(me.piles['Plot Deck'])
    notify("{} moved all used plots to their plot deck.".format(me))

#---------------------------------------------------------------------------
# New Table card actions
#---------------------------------------------------------------------------

def displayCardText(card, x = 0, y = 0):
    mute()
    
    notify('{} - Card Text:'.format(card.name))
    notify('{}'.format(card.Text))

    

def displayErrata(card, x = 0, y = 0):
    mute()
    
    notify('{} - Errata Text and FAQ:'.format(card.name))
    if card.ErrataText:
        notify('{}'.format(card.ErrataText))
    else:
        notify('NO Errata.')
        
def addGold(card, x = 0, y = 0):
    mute()
    notify("{} adds a Gold to {}.".format(me, card))
    card.markers[Gold] += 1
    me.counters['Gold'].value += 1
    
def subGold(card, x = 0, y = 0):
    mute()
    notify("{} subtracts a Gold to {}.".format(me, card))
    card.markers[Gold] -= 1
    me.counters['Gold'].value -= 1
