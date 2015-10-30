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
PlayColor = "#FFFF00" # Yellow
GameURL = "http://octgn.gamersjudgement.com/wordpress/agot2/"
FAQ_URL = "https://images-cdn.fantasyflightgames.com/filer_public/03/43/034309e6-c3a2-4575-8062-32ede5798ef8/gt01_rules-reference-web.pdf"

import re

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
	list = []
	for card in table:
		if card.type == "Character" and card.controller == me and card.isFaceUp:
			list.append(card)
	dlg = cardDlg(list)
	dlg.title = "These cards are in your table:"
	dlg.text = "Declares at least 1 character to attack."
	dlg.min = 1
	dlg.max = len(list)
	cards = dlg.show()
	if cards != None:
		for c in cards:
			c.target(True)
			c.highlight = MilitaryColor
			c.orientation = 1
		notify("**{} declares MIL attackers.**".format(me))
	else:
		whisper("You must declare at least 1 character to attack.")

def announceInt(group, x = 0, y = 0):
	mute()
	notify("**{} declares an INT challenge.**".format(me))
	list = []
	for card in table:
		if card.type == "Character" and card.controller == me and card.isFaceUp:
			list.append(card)
	dlg = cardDlg(list)
	dlg.title = "These cards are in your table:"
	dlg.text = "Declares at least 1 character to attack."
	dlg.min = 1
	dlg.max = len(list)
	cards = dlg.show()
	if cards != None:
		for c in cards:
			c.target(True)
			c.highlight = IntrigueColor
			c.orientation = 1
		notify("**{} declares INT attackers.**".format(me))
	else:
		whisper("You must declare at least 1 character to attack.")

def announcePow(group, x = 0, y = 0):
	mute()
	notify("**{} declares a PWR challenge.**".format(me))
	list = []
	for card in table:
		if card.type == "Character" and card.controller == me and card.isFaceUp:
			list.append(card)
	dlg = cardDlg(list)
	dlg.title = "These cards are in your table:"
	dlg.text = "Declares at least 1 character to attack."
	dlg.min = 1
	dlg.max = len(list)
	cards = dlg.show()
	if cards != None:
		for c in cards:
			c.target(True)
			c.highlight = PowerColor
			c.orientation = 1
		notify("**{} declares POW attackers.**".format(me))
	else:
		whisper("You must declare at least 1 character to attack.")

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
	me.counters['Gold'].value = 0  #reset all counters
	me.counters['Power'].value = 0
	me.counters['Reserve'].value = 0
	me.counters['Initiative'].value = 0
	me.counters['Str'].value = 0
	me.setGlobalVariable("turn", "0")
	
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
	notify("{} randomly moves {} from their discard to thier hand.".format(me, card))

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
		whisper("You already did your Setup")
		return
	if len(me.hand) == 0:
		whisper("You need to load a deck first") 
		return
	var="1"
	me.setGlobalVariable("setupOk", var)
	notify("**{} has started setup, please wait**".format(me))
	for c in me.hand: 
		if c.Type == "Faction":
			if me.isInverted: 
				c.moveToTable(300,-100)			
			else:
				c.moveToTable(-280,0)
		if c.Type == "Agenda":
			if me.isInverted: 
				c.moveToTable(220,-100)			
			else:
				c.moveToTable(-200,0)
	me.deck.shuffle()
	for card in me.deck.top(7):
		card.moveTo(me.hand)
	if me.isInverted: 
		table.create("656f69c4-c506-4014-932b-9dff4422f09e",300,-200)
	else:
		table.create("656f69c4-c506-4014-932b-9dff4422f09e",-280,100)
	notify("**{} is ready**".format(me))
	if me._id == 1:
		if me.isInverted: 
			table.create("73a6655b-60b6-4080-b428-f4e0099e0f77",380,-100)
		else:
			table.create("73a6655b-60b6-4080-b428-f4e0099e0f77",-360,0)
	if getGlobalVariable("numplayer") == "2":
		n = rnd(1, 2)
		if n == 1:
			notify("**Seven Gods decide {} is the firstplayer.**".format(getGlobalVariable("AID")))
		else:
			setGlobalVariable("firstplay","False")
			f = (card for card in table  
					if card.name == "1st Player Token")
			for card in f:
				if card.controller == me:    
					moveFP(card)
				else:                        
					remoteCall(players[1], "moveFP", card)
			notify("**Seven Gods decide {} is the firstplayer.**".format(getGlobalVariable("BID")))


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
			whisper("The number of cards in {}'s hand is more than your reserve.You should discard {} cards.".format(me, len(me.hand)-me.counters['Reserve'].value))
			discAmount = askInteger("How many cards to discard?", len(me.hand)-me.counters['Reserve'].value) 
		if discAmount == None: return
		dlg = cardDlg([c for c in me.hand])
		dlg.title = "These cards are in your hand:"
		dlg.text = "Choose {} cards to discard.".format(discAmount)
		dlg.min = discAmount
		dlg.max = discAmount
		cards = dlg.show()
		if cards != None:
			for card in cards:
				card.moveTo(me.piles['Discard pile'])
				notify("{} discard {}.".format(me, card))
		else:return
	else:
		notify("Hand size is ok.")
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
		plotlist = [card for card in table
						if card.controller == me and card.type == "Plot"]
		plotlist.reverse()
		for plotcard in plotlist:
			me.counters['Gold'].value += int(plotcard.plotgoldincome)
			plotcard.markers[Gold] += me.counters['Gold'].value
			break
		notify("{} counts income {} gold.".format(me,me.counters['Gold'].value))
		plotlist.reverse()
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
		plotlist = [card for card in table
						if card.controller == person and card.type == "Plot"]
		plotlist.reverse()
		uniquecards = []
		for card in personCards:
			if card.isFaceUp:
				if card.Reserve and int(card.Reserve) > 0:
					if card.Unique != "Yes":
						person.counters['Reserve'].value += int(card.Reserve)
					elif card.name not in uniquecards:
						uniquecards.append(card.name)
						person.counters['Reserve'].value += int(card.Reserve)	
		for card in plotlist:
			person.counters['Reserve'].value += int(card.plotReserve)
			break
		plotlist.reverse()
		notify("{}'s Reserve value is {}.".format(person,person.counters['Reserve'].value))
	return

def getInit(group, x = 0, y = 0):
	mute()
	for person in players:
		person.counters['Initiative'].value = 0
		personCards = (card for card in table
						if card.controller == person)
		plotlist = [card for card in table
						if card.controller == person and card.type == "Plot"]
		plotlist.reverse()
		uniquecards = []
		for card in personCards:
			if card.isFaceUp:
				if card.Initiative and int(card.Initiative) > 0:
					if card.Unique != "Yes":
						person.counters['Initiative'].value += int(card.Initiative)
					elif card.name not in uniquecards:
						uniquecards.append(card.name)
						person.counters['Initiative'].value += int(card.Initiative)	
		for card in plotlist:
			person.counters['Initiative'].value += int(card.plotInitiative)
			break
		plotlist.reverse()
		notify("{}'s Initiative value is {}.".format(person,person.counters['Initiative'].value))
	return

def fp(group, x = 0, y = 0):
	mute()
	if getGlobalVariable("numplayer") == "2":
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
	if getGlobalVariable("numplayer") == "2":
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
	colorList = ['#ae0603' ,'#006b34','#1a4d8f','#D8D8D8']
	choice = askChoice("Which challenge do you want to initiate?", choiceList,colorList)
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
	dlg=cardDlg([c for c in me.piles['Plot Deck']])
	dlg.title = "These cards are in your unused-plot pile:"
	dlg.text = "Select a plot card to reveal."
	cards = dlg.show()
	if cards != None:
		for card in cards:
			if me.isInverted: 
				card.moveToTable(120,-80,True)
			else:
				card.moveToTable(-120,0,True)
			me.setGlobalVariable("turn","1")
			list = [card for card in table
						if card.Type == "Plot" and card.controller == me]
			count = len(list)
			for p in list:
				if count > 1:
					p.moveTo(me.piles['Used Plot Pile'])
					count -= 1
				if count == 1:
					break
			if len(me.piles['Plot Deck']) == 0:
				shuffleToPlot(me.piles['Used Plot Pile'])
			if len(players) > 1:
				if me.getGlobalVariable("turn") == players[1].getGlobalVariable("turn") == "1":
					flipplotcard(card)
					d = (card for card in table 
							if card.type == "Plot" and card.controller != me)
					for c in d:
						remoteCall(players[1], "flipplotcard", c)
					if not confirm("Continue to calculate initiative?"): return
					fp(table)
			if len(players) == 1:
				flipplotcard(card)
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
	
	notify('{} - Card Text:'.format(card))
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
		whisper("You can't remove {} from the game".format(card.name))
	else:
		if not confirm("Confirm to remove this card from game."): return
		card.delete()
		notify('{} removes {} from the game'.format(me, card))

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
		notify("{} move {} to used plot pile.".format(me, card))
	elif card.type == "Faction" or card.type ==  "Agenda":
		whisper("You can't discard {} card.".format(card.type))
	elif card.type == "Internal":
		whisper("You can't discard {}.".format(card.name))
	else:
		card.moveTo(me.piles['Discard pile'])
		notify("{} discard {}.".format(me, card))

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
		if me.isInverted: 
			card.moveToTable(380,-100)
		else:
			card.moveToTable(-360,0)
	elif getGlobalVariable("firstplay") == "False":
		if me.isInverted: 
			card.moveToTable(-360,0)
		else:
			card.moveToTable(380,-100)
	else:
		return

def DoneButton(card):
	mute()
	notify("**{} is done.**".format(me))
	card.filter = None
	if len(players) > 1:
		d = (card for card in table 
				if card.name == "Done Token" and card.controller != me)
		for c in d:
			remoteCall(players[1], "addWaitHighlight", c)
	
def addWaitHighlight(card):
	mute()
	card.filter = WaitColor
	card.target(False)

def flipplotcard(card):
	mute()
	if card.isFaceUp:
		return
	else:
		card.isFaceUp = True
		notify("{} reveals {}.".format(me, card))
	me.setGlobalVariable("turn","0")
	
#------------------------------------------------------------------------------
# New Hand Actions
#------------------------------------------------------------------------------
def attachat(ax,ay,table):
	mute()
	for c in table:
		x,y = c.position
		if x == ax and y == ay:
			return attachat(x+12,y+12,table)
	return ax,ay

def play(card):
	mute()
	c = 0
	if card.cost == "" : 
		whisper("You can't play this card")
		return
	if card.Cost == "X": cost=askInteger("How much do you want to pay to play {} ? ".format(card.name),0)
	else : cost=int(card.Cost)
	uniquecards = []
	for u in table:
		if u.controller == me and u.unique == "Yes":
			uniquecards.append(u.name)
			if card.name in uniquecards: 
				cost=0
				c = 1   #Duplicates
				x,y = u.position
				break
	if c != 1:
		if card.type == "Attachment":
			if not confirm("Have you already targeted(use Shift+mouse left button) the object you want to attach?"):return
			list = []
			for targetcard in table:
				if targetcard.targetedBy == me:
					list.append(targetcard)
					targetcard.target(False)
			if len(list) > 0:
				dlg = cardDlg(list)
				dlg.title = "These cards can be attached:"
				dlg.text = "Choose a card to attach."
				cards = dlg.show()
				if cards != None:
					for choose in cards:
						reduc=askInteger("Reduce Cost by ?",0)
						if reduc == None or cost == None: return
						if reduc>cost: reduc=cost
						cost-=reduc
						if me.counters['Gold'].value < cost :
							whisper("You don't have enough Gold to pay for {}.".format(card))
							return		
						me.counters['Gold'].value -= cost
						for incomecard in table:
							if incomecard.controller == me and incomecard.markers[Gold] > 0:
								incomecard.markers[Gold] -= cost
						cx,cy = choose.position
						x,y = attachat(cx+15,cy+15,table)
						card.moveToTable(x,y)
						card.sendToBack()
						card.highlight = PlayColor
						notify("{} plays {} and attachs to {} for {} Gold (Cost reduced by {}).".format(me,card,choose,cost,reduc))
				else:
					whisper("Attachment cards must be attached to another card or game element.")
					return
			else:
				whisper("You must targeted(use Shift+mouse left button) a card which you want to attach to.")
		else:
			reduc=askInteger("Reduce Cost by ?",0)
			if reduc == None or cost == None: return
			if reduc>cost: reduc=cost
			cost-=reduc
			if me.counters['Gold'].value < cost :
				whisper("You don't have enough Gold to pay for {}.".format(card))
				return		
			if card.type == "Character":
				clist = [p for p in table
							if p.controller == me and p.type == "Character" and p.isFaceUp]
				if len(clist) > 0:
					clist.reverse()
					for character in clist:
						x, y = character.position
						break
					clist.reverse()
					if me.isInverted: card.moveToTable(x-80,y)
					else : 	card.moveToTable(x+80,y)
				else:
					if me.isInverted:card.moveToTable(20,-100)			
					else:card.moveToTable(-20,0)
			elif card.Type == "Location":
				clist = [p for p in table
							if p.controller == me and p.type == "Location" and p.isFaceUp]
				if len(clist) > 0:
					clist.reverse()
					for location in clist:
						x, y = location.position
						break
					clist.reverse()
					if me.isInverted: card.moveToTable(x-80,y)
					else : 	card.moveToTable(x+80,y)
				else:
					if me.isInverted:card.moveToTable(20,-220)			
					else:card.moveToTable(-20,120)
			else:
				if me.isInverted: card.moveToTable(150,-230)
				else: card.moveToTable(-130,130)
			card.highlight = PlayColor
			notify("{} plays {} for {} Gold (Cost reduced by {}).".format(me,card,cost,reduc))
			me.counters['Gold'].value -= cost
			for incomecard in table:
				if incomecard.controller == me and incomecard.markers[Gold] > 0:
					incomecard.markers[Gold] -= cost
	else:
		if me.isInverted: 
			card.moveToTable(x-8,y-8)
		else:
			card.moveToTable(x+8,y+8)
		notify("{} plays {}'s duplicate.".format(me,card))
		card.sendToBack()
			
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
			whisper("You have a card in your hand that is not a faction or an agenda, please put it in the appropriate deck.")
			
	if FactionCount != 1:
		ok = False
		whisper("You should have exactly 1 faction card in your hand.")
	if AgendaCount > 1:
		ok = False
		whisper("You can only use 1 agenda.")
		
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
		whisper("Your plot deck must contain exactly 7 cards.")
		
	for card in me.piles['Plot Deck']:
		if card.type != 'Plot':
			ok = False
			whisper("Your plot deck must contain only plots.")
			
		if card.faction != 'Neutral.' and FactionName not in card.faction:
			if card.loyal == 'Yes':
				ok = False
				notify("{}'s plot deck contains a loyal card from another faction.".format(me))
			if BannerFaction == '' or BannerFaction not in card.faction:
				ok = False
				notify("{}'s plot deck contains a card from an illegal faction.".format(me))
				
		counts[card.name] += 1
		
		if counts[card.name] > 1:
			if card.decklimit == '':
					limit = 2
			else:
				limit = int(card.decklimit)
				
			if counts[card.name] > limit:
				ok = False
				notify("{} has {} copies of {} in plot deck, but {} can has only {}.".format(me, counts[card.name], card,me, limit))
				
			if MultiplePlotName == '':
				MultiplePlotName = card.name
			else:
				ok = False
				notify("{} can has several copies of only 1 plot.".format(me))
	
	#Deck
	NeutralCount = 0
	BannerCount = 0
	me.deck.addViewer(me)
	
	if len(me.deck) < 60:
		ok = False
		notify("{}'s deck must contain at least 60 cards.".format(me))
	
	for card in me.deck:
		if card.type != "Character" and card.type != "Location" and card.type != "Attachment" and card.type != "Event":
			ok = False
			notify("{}'s deck must contain only characters, locations, attachments and events.".format(me))
	
		if card.faction == 'Neutral.':
			NeutralCount += 1
		elif FactionName not in card.faction:
			if card.loyal == 'Yes':
				ok = False
				notify("{}'s deck contains a loyal card from another faction.".format(me))
			elif BannerFaction == '' or BannerFaction not in card.faction:
				ok = False
				notify("{}'s deck contains a card from an illegal faction.".format(me))
			else:
				BannerCount += 1
				
		counts[card.name] += 1
		
		if card.decklimit == '':
			limit = 3
		else:
			limit = int(card.decklimit)
		
		if counts[card.name] > limit:
			ok = False
			notify("{} has {} copies of {} in deck, but {} can has only {}.".format(me,counts[card.name], card,me, limit))
	
	if AgendaName == 'Fealty' and NeutralCount > 15:
		ok = False
		notify("{}'s agenda is Fealty, so {} can has 15 neutral cards in deck, but {} have {}.".format(me,me,me, NeutralCount))
	elif BannerFaction != '' and BannerCount < 12:
		ok = False
		notify("{}'s agenda is {}, so {} must has at least 12 {} cards in deck, but {} have only {}".format(me, AgendaName, me,BannerFaction, me,BannerCount))
	
	me.deck.removeViewer(me)
	
	if ok:
		notify("Deck of {} is OK".format(me))
	else:
		notify("Deck of {} is NOT OK".format(me))
	
def shuffleToPlot(group):
	mute()
	for card in group:
		card.moveTo(me.piles['Plot Deck'])
	notify("{} moved all used plots to their plot deck.".format(me))

def createTitles(group):
	mute()
	if len(shared.piles['Titles']) == 6:
		whisper("Melee titles are created.")
	else:
		for card in group:
			card.delete()
		group.create("feefb8d0-f4ed-4d27-b272-3b9e9ee11a5d")
		group.create("3c734e0d-d625-4553-9cf5-74051311eef5")
		group.create("f91c60a9-d506-45f3-b5de-3a51e23279d3")
		group.create("cb3a2844-1aa5-494c-9536-87b4b9bd4562")
		group.create("0ba59f59-b08c-4e8e-ab23-b5cf9e77d176")
		group.create("3b088db8-adeb-4728-9eb9-6817455da6dc")
		notify("{} created melee titles.".format(me))

def removeTitles(group):
	mute()
	card = group.random()
	if card == None: return
	card.delete()
	notify('{} removes a Title'.format(me))
	
def chooseTitle(card):
	mute()
	card.moveToTable(0,0,True)
	card.controller == me
	card.peek()
	notify('{} choose a Title'.format(me))
	
#------------------------------------------------------------------------------
# New Events
#------------------------------------------------------------------------------
def onloaddeck(args):
	mute()
	c = int(getGlobalVariable("numplayer"))+1
	setGlobalVariable("numplayer","{}".format(c))
	if me._id == 1:
		setGlobalVariable("AID","{}".format(me))
	else:
		setGlobalVariable("BID","{}".format(me))
	player = args.player
	if player==me:
		checkdeck()
		setup(table)
