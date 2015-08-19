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
WaitColor = "#D8D8D8" # Grey
GameURL = "http://octgn.gamersjudgement.com/wordpress/agot2/"
FAQ_URL = "https://images-cdn.fantasyflightgames.com/filer_public/03/43/034309e6-c3a2-4575-8062-32ede5798ef8/gt01_rules-reference-web.pdf"


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

def addGold(card, x = 0, y = 0):
	mute()
	notify("{} adds a Gold to {}.".format(me, card))
	card.markers[Gold] += 1
	me.counters['Gold'].value += 1
    
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
    
def subGold(card, x = 0, y = 0):
    mute()
    notify("{} subtracts a Gold to {}.".format(me, card))
    card.markers[Gold] -= 1
    me.counters['Gold'].value -= 1
    
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

#---------------------------------------------------------------------------
# New actions
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
	checkdeck()
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
	if me.hasInvertedTable(): 
		table.create("656f69c4-c506-4014-932b-9dff4422f09e",300,-200)
	else:
		table.create("656f69c4-c506-4014-932b-9dff4422f09e",-280,100)
	notify("**{} is ready**".format(me))
	if me._id == 1:
		if me.hasInvertedTable(): 
			table.create("73a6655b-60b6-4080-b428-f4e0099e0f77",380,-100)
		else:
			table.create("73a6655b-60b6-4080-b428-f4e0099e0f77",-360,0)


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
			discAmount = askInteger("How many cards to discard?", len(me.hand)-me.counters['Reserve'].value) 
		if discAmount == None: return
		for index in range(0,discAmount):
			cardList = []
			for c in me.hand:
				cardList.append(c)
			c=askCard(cardList)
			if c != None:
				c.moveTo(me.piles['Discard pile'])
				notify("{} discard {}.".format(me, c.name))
				count += 1
			else:return
	else:
		notify("Hand size is ok.")
	for c in table: 
		if c.Type == "Plot" and c.controller == me:
			if len(me.piles['Plot Deck']) > 0:
				c.moveTo(me.piles['Used Plot Pile'])
			else:
				shuffleToPlot(me.piles['Used Plot Pile'])
				c.moveTo(me.piles['Used Plot Pile'])
	me.counters['Reserve'].value = 0
	me.counters['Initiative'].value = 0
	me.counters['Str'].value = 0
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
					setGlobalVariable("firstplay","{}".format(me._id))
				else:
					notify("**{} flips heads,and wins the initiative.**".format(players[1]))
					notify("**{} decides who is the first player.**".format(players[1]))
					setGlobalVariable("firstplay","{}".format(players[1]._id))
			if players[0].counters['Power'].value > players[1].counters['Power'].value:
				notify("**{} wins the initiative.**".format(players[1]))
				notify("**{} decides who is the first player.**".format(players[1]))
				setGlobalVariable("firstplay","{}".format(players[1]._id))
			if players[0].counters['Power'].value < players[1].counters['Power'].value:
				notify("**{} wins the initiative.**".format(players[0]))
				notify("**{} decides who is the first player.**".format(players[0]))
				setGlobalVariable("firstplay","{}".format(me._id))
		elif players[0].counters['Initiative'].value > players[1].counters['Initiative'].value:
			notify("{} wins the initiative.".format(players[0]))
			notify("**{} decides who is the first player.**".format(players[0]))
			setGlobalVariable("firstplay","{}".format(me._id))
		else:
			notify("{} wins the initiative.".format(players[1]))
			notify("**{} decides who is the first player.**".format(players[1]))
			setGlobalVariable("firstplay","{}".format(players[1]._id))
		if not confirm("Continue to decide who is the first player?"): return
		decidefirstplayer(table)
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

def revealplot(group, x = 0, y = 0):
	mute()
	me.piles['Plot Deck'].addViewer(me)
	list = []
	for card in me.piles['Plot Deck']: list.append(card)
	card=askCard(list)
	if card != None:
		if me.hasInvertedTable(): 
			card.moveToTable(120,-80)
		else:
			card.moveToTable(-120,0)
		card.isFaceUp = False
		count = 0
		for p in table:
			if p.type == "Plot":
				count += 1
		if count == len(players):
			flipplotcard(card)
			d = (card for card in table 
					if card.type == "Plot" and card.controller != me)
			for c in d:
				remoteCall(players[1], "flipplotcard", c)
			if not confirm("Continue to calculate initiative?"): return
			fp(table)
	else:
		return

		
def decidefirstplayer(group, x = 0, y = 0):
	mute()
	if getGlobalVariable("firstplay") == "{}".format(me._id):  
		askfirstplayer(table)
	else: 
		remoteCall(players[1], "askfirstplayer", table)     


def askfirstplayer(group, x = 0, y = 0):
	mute()
	choiceList = ['{}'.format(getGlobalVariable("AID")),'{}'.format(getGlobalVariable("BID"))]
	choice = askChoice("Decide who is First player.", choiceList)
	if choice == 1:
		notify("**{} is firstplayer.**".format(getGlobalVariable("AID")))
		setGlobalVariable("firstplay","True")
		f = (card for card in table  
			if card.name == "1st Player Token")
		for card in f:
			if card.controller == me:    
				moveFP(card)
			else:                        
				remoteCall(players[1], "moveFP", card)
	elif choice == 2:
		notify("**{} is firstplayer.**".format(getGlobalVariable("BID")))
		setGlobalVariable("firstplay","False")
		f = (card for card in table  
			if card.name == "1st Player Token")
		for card in f:
			if card.controller == me:   
				moveFP(card)
			else:                       
				remoteCall(players[1], "moveFP", card)
	else:
		return

#---------------------------------------------------------------------------
# New Table card actions
#---------------------------------------------------------------------------
def displayCardText(card, x = 0, y = 0):
	mute()
	
	notify('{} - Card Text:'.format(card.name))
	notify('{}'.format(card.Text))


def displayErrata(card, x = 0, y = 0):
	mute()
	
	notify('{} - ErrataText:'.format(card.name))
	if card.ErrataText:
		notify('{}'.format(card.ErrataText))
	else:
		notify('')

def remove(card, x = 0, y = 0):
	mute()
	if card.type == "Internal":
		notify("You can't remove {} from the game".format(card.name))
	else:
		if not confirm("Confirm to remove this card from game."): return
		card.delete()
		notify('{} remove {} from the game'.format(me, card.name))

def cardLookup(card, x = 0, y = 0):
	mute()
	
	if card.isFaceUp:
		webSite = ""
		webSite += "http://www.cardgamedb.com/index.php/agameofthrones2ndedition/a-game-of-thrones-2nd-edition-cards?&advanced=false&tx="
		webSite += "{}".format(card.name)
		webSite += "&txf=Name&or=name&vw=spoiler"
		openUrl("{}".format(webSite))
	else:
		whisper("Card must be face up to use this feature.")

def disc(card, x = 0, y = 0):
	mute()
	if card.type == "Plot":
		card.moveTo(me.piles['Used Plot Pile'])
		notify("{} move {} to used plot pile.".format(me, card.name))
	elif card.type == "Faction" or card.type ==  "Agenda":
		notify("You can't discard {} card.".format(card.type))
	elif card.type == "Internal":
		notify("You can't discard {}.".format(card.name))
	else:
		card.moveTo(me.piles['Discard pile'])
		notify("{} discard {}.".format(me, card.name))

def defaultAction(card, x = 0, y = 0):
	mute()
	# Default for Done button is playerDone
	if card.Type == "Internal": 
		if card.name == "Done Token":
			DoneButton(card)
		if card.name == "1st Player Token":
			moveFP(card)
	elif card.Type == "Plot":
		countincome(table)
	elif not card.isFaceUp: #Face down card - flip
		flipcard(card, x, y)
	else:
		kneel(card, x, y)

def moveFP(card):
	mute()
	if getGlobalVariable("firstplay") == "True":
		if me.hasInvertedTable(): 
			card.moveToTable(380,-100)
		else:
			card.moveToTable(-360,0)
	elif getGlobalVariable("firstplay") == "False":
		if me.hasInvertedTable(): 
			card.moveToTable(-360,0)
		else:
			card.moveToTable(380,-100)
	else:
		return

def DoneButton(card):
	mute()
	notify("**{} is done.**".format(me))
	card.highlight = None
	if len(players) > 1:
		d = (card for card in table 
				if card.name == "Done Token" and card.controller != me)
		for c in d:
			remoteCall(players[1], "addWaitHighlight", c)
	
def addWaitHighlight(card):
	mute()
	card.highlight = WaitColor
	card.target(False)

def flipplotcard(card):
	mute()
	if card.isFaceUp:
		return
	else:
		card.isFaceUp = True
		notify("{} reveals {}.".format(me, card.name))
	
#------------------------------------------------------------------------------
# New Hand Actions
#------------------------------------------------------------------------------
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
	else : 	card.moveToTable(0,160)
	card.target(True)
	notify("{} plays {} for {} Gold (Cost reduced by {}).".format(me,card,cost,reduc))
	me.counters['Gold'].value -= cost
	for incomecard in table:
		if incomecard.controller == me and incomecard.markers[Gold] > 0:
			incomecard.markers[Gold] -= cost
			
#------------------------------------------------------------------------------
# New Pile Actions
#------------------------------------------------------------------------------
def checkdeck():
	mute()
	notify (" -> Checking deck of {} ...".format(me))
	ok = True
	
	# Faction and agenda (should be in hand)
	FactionCount = 0
	AgendaCount = 0
	FactionName = ''
	AgendaName = ''
	BannerFaction = ''
	
	for card in me.hand:
		if card.type == 'Faction':
			FactionCount += 1
			FactionName = card.faction
		elif card.type == 'Agenda':
			AgendaCount += 1
			AgendaName = card.name
		else:
			ok = False
			notify("You have a card in your hand that is not a faction or an agenda, please put it in the appropriate deck.")
			
	if FactionCount != 1:
		ok = False
		notify("You should have exactly 1 faction card in your hand.")
	if AgendaCount > 1:
		ok = False
		notify("You can only use 1 agenda.")
		
	if AgendaName == "Banner of the Stag":
		BannerFaction = "Baratheon"
	elif AgendaName == "Banner of the Kraken":
		BannerFaction = "Greyjoy"
	elif AgendaName == "Banner of the Lion":
		BannerFaction = "Lannister"
	elif AgendaName == "Banner of the Sun":
		BannerFaction = "Martell"
	elif AgendaName == "Banner of the Watch":
		BannerFaction = "Night's Watch"
	elif AgendaName == "Banner of the Wolf":
		BannerFaction = "Stark"
	elif AgendaName == "Banner of the Dragon":
		BannerFaction = "Targaryen"
	elif AgendaName == "Banner of the Rose":
		BannerFaction = "Tyrell"
		
	#Plot deck
	MultiplePlotName = ''
	counts = collections.defaultdict(int)
	
	if len(me.piles['Plot Deck']) != 7:
		ok = False
		notify("Your plot deck must contain exactly 7 cards.")
		
	for card in me.piles['Plot Deck']:
		if card.type != 'Plot':
			ok = False
			notify("Your plot deck must contain only plots.")
			
		if card.faction != 'Neutral.' and FactionName not in card.faction:
			if card.loyal == 'Yes':
				ok = False
				notify("Your plot deck contains a loyal card from another faction.")
			if BannerFaction == '' or BannerFaction not in card.faction:
				ok = False
				notify("Your plot deck contains a card from an illegal faction.")
				
		counts[card.name] += 1
		
		if counts[card.name] > 1:
			if card.decklimit == '':
					limit = 2
			else:
				limit = int(card.decklimit)
				
			if counts[card.name] > limit:
				ok = False
				notify("You have {} copies of {} in your plot deck, but you can have only {}.".format(counts[card.name], card.name, limit))
				
			if MultiplePlotName == '':
				MultiplePlotName = card.name
			else:
				ok = False
				notify("You can have several copies of only 1 plot.")
	
	#Deck
	NeutralCount = 0
	BannerCount = 0
	me.deck.setVisibility('me')
	
	if len(me.deck) < 60:
		ok = False
		notify("Your deck must contain at least 60 cards.")
	
	for card in me.deck:
		if card.type != "Character" and card.type != "Location" and card.type != "Attachment" and card.type != "Event":
			ok = False
			notify("Your deck must contain only characters, locations, attachments and events.")
	
		if card.faction == 'Neutral.':
			NeutralCount += 1
		elif FactionName not in card.faction:
			if card.loyal == 'Yes':
				ok = False
				notify("Your deck contains a loyal card from another faction.")
			elif BannerFaction == '' or BannerFaction not in card.faction:
				ok = False
				notify("Your deck contains a card from an illegal faction.")
			else:
				BannerCount += 1
				
		counts[card.name] += 1
		
		if card.decklimit == '':
			limit = 3
		else:
			limit = int(card.decklimit)
		
		if counts[card.name] > limit:
			ok = False
			notify("You have {} copies of {} in your deck, but you can have only {}.".format(counts[card.name], card.name, limit))
	
	if AgendaName == 'Fealty' and NeutralCount > 15:
		ok = False
		notify("Your agenda is Fealty, so you can have 15 neutral cards in your deck but you have {}.".format(NeutralCount))
	elif BannerFaction != '' and BannerCount < 12:
		ok = False
		notify("Your agenda is {}, so you must have at least 12 {} cards in your deck, but you have only {}".format(AgendaName, BannerFaction, BannerCount))
	
	me.deck.setVisibility('None')
	
	if ok:
		notify("Deck of {} is OK".format(me))
	else:
		notify("Deck of {} is NOT OK".format(me))
	
def shuffleToPlot(group):
	mute()
	for card in group:
		card.moveTo(me.piles['Plot Deck'])
	notify("{} moved all used plots to their plot deck.".format(me))

#------------------------------------------------------------------------------
# New Events
#------------------------------------------------------------------------------
def on_load_deck(player, groups):
	mute()
	setGlobalVariable("firstplay","True")
	if player == me:
		if me._id == 1:
			setGlobalVariable("AID","{}".format(me))
		else:
			setGlobalVariable("BID","{}".format(me))
		setup(table)
