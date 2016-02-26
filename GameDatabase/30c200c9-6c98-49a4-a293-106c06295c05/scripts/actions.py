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
DuplicateColor = "#5c3521"
PlayColor = "#FFA6F7" # Yellow
usedplotcolor = "#99ffff"
GameURL = "http://octgn.gamersjudgement.com/wordpress/agot2/"
FAQ_URL = "https://images-cdn.fantasyflightgames.com/filer_public/03/43/034309e6-c3a2-4575-8062-32ede5798ef8/gt01_rules-reference-web.pdf"
#add
MilitaryIcon = ("MilitaryIcon", "7e9610d4-c06d-437d-a5e6-100000000001")
IntrigueIcon = ("IntrigueIcon", "0cabfb36-01b4-46c4-bb2a-42889fb63e8b")
PowerIcon = ("PowerIcon", "a6b9db40-b0ad-4b22-b049-5837c4ece904")

countmil = 0
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
			card.target(False)
	notify("{} stands all their cards.".format(me))

def announceMil(group, x = 0, y = 0):
	mute()
	global countmil
	stealth = ""
	notify("**{} declares a MIL challenge.**".format(me))
	list = []
	for card in table:
		card.highlight = None
		card.target(False)
		if card.type == "Character" and card.controller == me and card.isFaceUp and (card.Military == "Yes" or card.markers[MilitaryIcon] > 0) and card.orientation == 0 and card.filter == None:
			list.append(card)
	if len(list) == 0:
		whisper("No more card can eclares a MIL challenge.")
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
			if c.model != "a8854084-67e5-4955-89db-3d9cb1337789":
				if c.model == "09903f79-6155-4a63-9b52-e10fb2e69898":
					f = c.name+str(c.position)
					for cards in table:
						if cards.model == "99a12a9c-6e83-43bd-8947-0cc47ffcd02a" and cards.controller == me:
							attach = eval(getGlobalVariable("attachmodify"))
							if attach.has_key(cards._id):
								if attach(cards._id) == c._id and countmil == 1:
									c.orientation = 0
								else:c.orientation = 1
				elif c.model != "09903f79-6155-4a63-9b52-e10fb2e69898" :c.orientation = 1
				if re.search(r'stealth',c.keywords,re.I):   #stealth
					stealth = "0"
		notify("**{} declares MIL attackers.**".format(me))
		if stealth == "0":
			choice = confirm("Character with the stealth keyword has been declared as an attacker, do you want to chooses its stealth target?")
			if choice == True:
				notify("{} is ready to use the stealth keyword.".format(me))
			else:
				notify("{} renounces the use of the stealth keyword.".format(me))
			stealth = "1"
	else:
		whisper("You must declare at least 1 character to attack.")
	countmil += 1

def announceInt(group, x = 0, y = 0):
	mute()
	stealth = ""
	notify("**{} declares an INT challenge.**".format(me))
	list = []
	for card in table:
		card.highlight = None
		card.target(False)
		if card.type == "Character" and card.controller == me and card.isFaceUp and (card.Intrigue == "Yes" or card.markers[IntrigueIcon] > 0) and card.orientation == 0 and card.filter == None:
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
			if re.search(r'stealth',c.keywords,re.I):   #stealth
				stealth = "0"
		notify("**{} declares INT attackers.**".format(me))
		if stealth == "0":
			choice = confirm("Character with the stealth keyword has been declared as an attacker, do you want to chooses its stealth target?")
			if choice == True:
				notify("{} is ready to use the stealth keyword.".format(me))
			else:
				notify("{} renounces the use of the stealth keyword.".format(me))
			stealth = "1"
	else:
		whisper("You must declare at least 1 character to attack.")

def announcePow(group, x = 0, y = 0):
	mute()
	stealth = ""
	notify("**{} declares a POW challenge.**".format(me))
	list = []
	for card in table:
		card.highlight = None
		card.target(False)
		if card.type == "Character" and card.controller == me and card.isFaceUp and (card.Power == "Yes" or card.markers[PowerIcon] > 0) and card.orientation == 0 and card.filter == None:
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
			if re.search(r'stealth',c.keywords,re.I):   #stealth
				stealth = "0"
		notify("**{} declares POW attackers.**".format(me))
		if stealth == "0":
			choice = confirm("Character with the stealth keyword has been declared as an attacker, do you want to chooses its stealth target?")
			if choice == True:
				notify("{} is ready to use the stealth keyword.".format(me))
			else:
				notify("{} renounces the use of the stealth keyword.".format(me))
			stealth = "1"
	else:
		whisper("You must declare at least 1 character to attack.")

def holdOn(group, x = 0, y = 0):
	mute()
	notify("**Please wait.  {} has an action/question.**".format(me))

def announceOpp(group, x = 0, y = 0):
	mute()
	notify("**{} responds: Opposed/Defend.**".format(me))
	choiceList = ['Military', 'Intrigue', 'Power', 'No defenders']
	colorList = ['#ae0603' ,'#006b34','#1a4d8f','#D8D8D8']
	choice = askChoice("Which challenge do you want to defend?", choiceList,colorList)
	if choice == 1:
		defMil(table)
	elif choice == 2:
		defInt(table)
	elif choice == 3:
		defPow(table)
	elif choice == 4:
		notify("{} declares no defenders.".format(me))
	else:return
	
def defMil(group, x = 0, y = 0):
	mute()
	list = []
	for card in table:
		card.target(False)
		if card.type == "Character" and card.controller == me and card.isFaceUp and (card.Military == "Yes" or card.markers[MilitaryIcon] > 0) and card.orientation == 0 and card.filter == None:
			list.append(card)
	dlg = cardDlg(list)
	dlg.title = "These cards are in your table:"
	dlg.text = "Declares characters to defend."
	dlg.min = 1
	dlg.max = len(list)
	cards = dlg.show()
	if cards != None:
		for c in cards:
			c.target(True)
			c.highlight = MilitaryColor
			c.orientation = 1
		notify("**{} declares MIL defenders.**".format(me))
	else:
		notify("{} declares no defenders.".format(me))

def defInt(group, x = 0, y = 0):
	mute()
	list = []
	for card in table:
		card.target(False)
		if card.type == "Character" and card.controller == me and card.isFaceUp and (card.Intrigue == "Yes" or card.markers[IntrigueIcon] > 0) and card.orientation == 0 and card.filter == None:
			list.append(card)
	dlg = cardDlg(list)
	dlg.title = "These cards are in your table:"
	dlg.text = "Declares characters to defend."
	dlg.min = 1
	dlg.max = len(list)
	cards = dlg.show()
	if cards != None:
		for c in cards:
			c.target(True)
			c.highlight = IntrigueColor
			c.orientation = 1
		notify("**{} declares INT defenders.**".format(me))
	else:
		notify("{} declares no defenders.".format(me))

def defPow(group, x = 0, y = 0):
	mute()
	list = []
	for card in table:
		card.target(False)
		if card.type == "Character" and card.controller == me and card.isFaceUp and (card.Power == "Yes" or card.markers[PowerIcon] > 0) and card.orientation == 0 and card.filter == None:
			list.append(card)
	dlg = cardDlg(list)
	dlg.title = "These cards are in your table:"
	dlg.text = "Declares characters to defend."
	dlg.min = 1
	dlg.max = len(list)
	cards = dlg.show()
	if cards != None:
		for c in cards:
			c.target(True)
			c.highlight = PowerColor
			c.orientation = 1
		notify("**{} declares POW defenders.**".format(me))
	else:
		notify("{} declares no defenders.".format(me))
		
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
		notify('{} kneels {}.'.format(me, card.name))
	else:
		notify('{} stands {}.'.format(me, card.name))

def flipcard(card, x = 0, y = 0):
	mute()
	if card.isFaceUp:
		notify("{} turns {} face down.".format(me, card))
		card.isFaceUp = False
		card.orientation &= ~Rot90
	else:
		card.isFaceUp = True
		notify("{} turns {} face up.".format(me, card))
		#duplicate
		if len(me.piles['Plot Deck']) == 7:
			uniquecards = []
			uniquecardsinex = []
			for u in table:
				if u.name == card.name and u.filter == None and u.index != card.index:
					if u.name not in uniquecards:
						if u.controller == me and u.unique == "Yes":
							uniquecards.append(u.name)
							uniquecardsinex.append(u.index)
							cx, cy = u.position
			if uniquecards != []:
				if card.name == uniquecards[0] and card.index not in uniquecardsinex and card.controller == me:
					if me.isInverted:x,y = attachat(cx-8,cy-8,table)
					else:x,y = attachat(cx+8,cy+8,table)
					if me.isInverted: 
						card.moveToTable(x,y)
					else:
						card.moveToTable(x,y)
					notify("{} plays {}'s duplicate.".format(me,card))
					card.sendToBack()
					card.filter = "#005c3521"

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
	if drawAmount == None: drawAmount = askInteger("Draw how many cards?", 2)
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
	notify("{} randomly moves {} from their discard to their hand.".format(me, card))

#---------------------------------------------------------------------------
# New actions
#---------------------------------------------------------------------------
# New Table group actions
#---------------------------------------------------------------------------
def setup(group, x = 0, y = 0):
	mute()
	if not confirm("Confirm to setup?"): return
	var = me.getGlobalVariable("setupOk")
	if var != "0":
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
		table.create("656f69c4-c506-4014-932b-9dff4422f09e",-320,100)
	notify("**{} is ready to setup**".format(me))
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
	placesetupcards()

def placesetupcards():
	mute()
	list = []
	for p in me.hand:list.append(p)
	dlg=cardDlg(list)
	dlg.title = "Choose your setup cards."
	dlg.text = "You may place up to 8 gold cost worth cards as setup cards. To mulligan, close the window without choosing any cards."
	dlg.min = 0
	dlg.max = len(list)
	cards = dlg.show()
	uniquecards = [] #Duplicates
	cost = 0
	limit = 0
	countcards=20
	place = "OK"
	if cards != None:
		for placecard in cards:
			if placecard.unique != "Yes":
				cost += int(placecard.cost)
			elif placecard.unique == "Yes" and placecard.name not in uniquecards:
				uniquecards.append(placecard.name)
				cost += int(placecard.cost)
			if re.search(r'limit',placecard.keywords,re.I):   #keyword limit
				limit += 1
			if placecard.type == "Event":
				confirm("You may only place character, location, and attachment cards.")
				place = "NOTOK"
			if placecard.type == "Attachment":
				if not confirm("Each attachment must be attached to a valid target under its owner’s control."):
					place = "NOTOK"
		if cost > 8:
			confirm("You may only place up to 8 gold cost.")
			place = "NOTOK"
		if limit > 1:
			confirm("You may only place up 1 limited card.")
			place = "NOTOK"
		if place == "NOTOK":
			placesetupcards()
		if place == "OK":
			for card in cards:
				if me.isInverted:
					card.moveToTable(countcards,-100,True)
				else:
					card.moveToTable(countcards,0,True)
				countcards=countcards-80
				card.peek()
			for drawcard in me.deck.top(7-len(me.hand)):
				drawcard.moveTo(me.hand)
			notify("{} is ready to begin.".format(me))
	else:
		if me.getGlobalVariable("setupOk") == "2":
			placesetupcards()
		else:
			mulligan(me.hand)
			me.setGlobalVariable("setupOk","2")
			placesetupcards()

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
			card.target(False)
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
	for c in table: 
		if c.Type == "Plot" and c.controller == me:
			if len(me.piles['Plot Deck']) > 0:
				c.filter = "#0099ffff"
				x, y = c.position
				if me.isInverted:c.moveToTable(x, y-20)
				else:c.moveToTable(x, y+20)
			else:
				if c.filter == usedplotcolor:
					c.moveTo(me.piles['Plot Deck'])
				else:
					c.filter = "#0099ffff"
	me.counters['Reserve'].value = 0
	me.counters['Initiative'].value = 0
	me.counters['Str'].value = 0
	me.setGlobalVariable("turn", "0")
	global countmil
	countmil = 0
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
				if card.Initiative and int(card.Initiative) != 0:
					if card.Unique != "Yes":
						person.counters['Initiative'].value += int(card.Initiative)
					elif card.name not in uniquecards:
						uniquecards.append(card.name)
						person.counters['Initiative'].value += int(card.Initiative)	
		for card in plotlist:
			person.counters['Initiative'].value += int(card.plotInitiative)
			break
		plotlist.reverse()
		if person.counters['Initiative'].value < 0:person.counters['Initiative'].value = 0
		notify("{}'s Initiative value is {}.".format(person,person.counters['Initiative'].value))
	return

def fp(group, x = 0, y = 0):
	mute()
	getInit(table)
	recalcPower(table)
	maxInit = -1
	minPower = -1
	winners = []
	numPlayers = len(players)
	for i in range(numPlayers):
		if players[i].counters['Initiative'].value > maxInit:
			maxInit = players[i].counters['Initiative'].value
			minPower = players[i].counters['Power'].value
			winners = []
			winners.append(i)
		elif players[i].counters['Initiative'].value == maxInit:
			if minPower < 0 or players[i].counters['Power'].value < minPower:
				minPower = players[i].counters['Power'].value
				winners = []
				winners.append(i)
			elif players[i].counters['Power'].value == minPower:
				winners.append(i)
	if len(winners) == 1:
		winner = players[winners[0]]
		notify("{} wins the initiative.".format(winner))
	else:
		n = rnd(0, len(winners) - 1)
		winner = players[winners[n]]
		notify("{} randomly wins the initiative.".format(winner))
	notify("**{} decides who is the first player.**".format(winner))
	setGlobalVariable("firstplay","{}".format(winner._id))
	# if there are more than 2 players, move the FP token manually
	if numPlayers == 2:
		if not confirm("Continue to decide who is the first player?"): return
		decidefirstplayer(table)
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
	maxSTR = 0
	winner = -1
	numPlayers = len(players)
	for i in range(numPlayers):
		person = players[i]
		person.counters['Str'].value = 0
		personCards = (card for card in table
						if card.controller == person)
		uniquecards = []
		# exclude knelt unique characters
		for card in personCards:
			if card.isFaceUp and card.orientation == Rot90:
				if card.Strength and card.Unique == "Yes":
					if card.name not in uniquecards:
						uniquecards.append(card.name)
		personCards = (card for card in table
						if card.controller == person)
		for card in personCards:
			if card.isFaceUp:
				if card.orientation != Rot90:
					str = 0
					if card.Strength:
						if card.Unique != "Yes":
							str += int(card.Strength)
						elif card.name not in uniquecards:
							uniquecards.append(card.name)
							str += int(card.Strength)
					if card.markers[STR_Up] > 0:
						str += card.markers[STR_Up]
					if card.markers[Burn] > 0:
						str -= card.markers[Burn]
					if str > 0:
						person.counters['Str'].value += str
				if card.dominance and int(card.dominance) > 0:
					if card.Unique != "Yes":
						person.counters['Str'].value += int(card.dominance)
					elif card.name not in uniquecards:
						uniquecards.append(card.name)
						person.counters['Str'].value += int(card.dominance)
				if card.markers[Gold] > 0:
					person.counters['Str'].value += card.markers[Gold]
		if person.counters['Str'].value > maxSTR:
			maxSTR = person.counters['Str'].value
			winner = i
		elif person.counters['Str'].value == maxSTR:
			winner = -1
		notify("{}'s total for dominance is {}.".format(person,person.counters['Str'].value))
	if not confirm("Confirm to proceed?"): return
	if winner == -1:
		notify("No one wins dominance.")
	else:
		notify("{} wins the dominance.".format(players[winner]))
		for housecard in table:
			if housecard.type == "Faction" and housecard.controller == players[winner]:
				addPower(housecard)
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
	countstr = 0
	winplayer = []
	for person in players:
		if countstr < person.counters['Str'].value:
			countstr = person.counters['Str'].value
			winplayer = person
	notify("{} win such challenge.".format(winplayer))

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
			if len(me.piles['Plot Deck']) == 0:
				for card in table:
						if card.Type == "Plot" and card.controller == me and card.filter == usedplotcolor:
							card.moveTo(me.piles['Plot Deck'])
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
	
	notify('{} - ErrataText:'.format(card.position))
	notify('{} - ErrataText:'.format(card.filter))
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
	list = []
	attach = eval(getGlobalVariable("attachmodify"))
	if card.type == "Plot":
		card.moveTo(me.piles['Used Plot Pile'])
		notify("{} move {} to used plot pile.".format(me, card))
	elif card.type == "Faction" or card.type ==  "Agenda":
		whisper("You can't discard {} card.".format(card.type))
	elif card.type == "Internal":
		whisper("You can't discard {}.".format(card.name))
	elif card.type == "Attachment":
		for dcard in table:
			if dcard.name == card.name and dcard.filter == DuplicateColor and dcard.controller == me:
				list.append(dcard)
		if len(list) > 0:
			choiceList = ['Disc Attachment', 'Disc Duplicate']
			colorList = ['#ae0603' ,'#D8D8D8']
			choice = askChoice("Which pass do you want to action?", choiceList,colorList)
			if choice == 2:
				list[0].moveTo(me.piles['Discard pile'])
				notify("{} discard {}'s duplicate.".format(me,card))
				return
			elif choice == 1:
				for disccard in list:
					disccard.moveTo(me.piles['Discard pile'])
					notify("{} discard {}'s duplicate.".format(me,card))
		for cardc in table:
			if attach.has_key(card._id):
				if attach[card._id] == cardc._id:
					del attach[card._id]
					setGlobalVariable("attachmodify",str(attach))
					#rollback
					if card.model == "4dd074aa-af6c-4897-b7b2-bff3493bcf9e" and cardc.model == "df79718d-b01d-4338-8907-7b6abff58303":cardc.markers[MilitaryIcon] -= 1#096
					if re.search('\+\d\sSTR', card.Text) and card.model != "9e6bf142-159b-4a3b-9d4c-d8bf233a6f0c" and card.model != "4c8a114e-106c-4460-846b-28f73914fc11":
						stradd = re.search('\+\d\sSTR', card.Text).group()
						cardc.markers[STR_Up] -= int(stradd[1])
					if re.search('\[INT]\sicon', card.Text):cardc.markers[IntrigueIcon] -= 1
					if re.search('\[POW]\sicon', card.Text):cardc.markers[PowerIcon] -= 1
					if re.search('\[MIL]\sicon', card.Text) and cardc.model != "4dd074aa-af6c-4897-b7b2-bff3493bcf9e":cardc.markers[MilitaryIcon] -= 1
		card.moveTo(me.piles['Discard pile'])
		notify("{} discard {}.".format(me, card))
	elif card.type == "Character":
		for d in attach:
			if attach[d] == card._id:
				for cardd in table:
					if cardd._id == d:
						if cardd.Text.find('Terminal.') == -1 and cardd.Keywords.find('Terminal.') == -1:cardd.moveTo(me.hand)
						else:cardd.moveTo(me.piles['Discard pile'])
						del attach[d]
						setGlobalVariable("attachmodify",str(attach))
		card.moveTo(me.piles['Discard pile'])
		notify("{} discard {}.".format(me, card))
	elif card.type == "Event":
		card.moveTo(me.piles['Discard pile'])
		notify("{} discard {}.".format(me, card))
	elif card.type == "Location":
		for dcard in table:
			if dcard.name == card.name and dcard.filter == DuplicateColor and dcard.controller == me:
				list.append(dcard)
		if len(list) > 0:
			choiceList = ['Disc Location', 'Disc Duplicate']
			colorList = ['#ae0603' ,'#D8D8D8']
			choice = askChoice("Which pass do you want to action?", choiceList,colorList)
			if choice == 2:
				list[0].moveTo(me.piles['Discard pile'])
				notify("{} discard {}'s duplicate.".format(me,card))
				return
			elif choice == 1:
				for disccard in list:
					disccard.moveTo(me.piles['Discard pile'])
					notify("{} discard {}'s duplicate.".format(me,card))
		card.moveTo(me.piles['Discard pile'])
		notify("{} discard {}.".format(me, card))
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
	elif len(me.piles['Plot Deck']) == 7 and card.Type == "Attachment" and card.isFaceUp == True:
		play(card)
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
	if len(me.piles['Plot Deck']) != 7:
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
			list = []
			for targetcard in table:
				if targetcard.targetedBy == me:
					if targetcard.Keywords == 'No attachments.':
						whisper("{} cannot be attached.".format(targetcard))
						targetcard.target(False)
					elif re.search(r'\[(.*) or (.*)] character only.', card.Text,re.I):
						if targetcard.Traits.find('Lord') != -1 or targetcard.Traits.find('Lady') != -1:
							list.append(targetcard)
							targetcard.target(False)
						else:
							whisper("{} can only be attached to [Lord or Lady] characters.".format(card))
							targetcard.target(False)
					elif re.search(r'\[(.*)] character only.', card.Text,re.I):
						chaonly = re.search(r'\[(.*)] character only.', card.Text,re.I).group(1)
						if targetcard.Faction.find(chaonly) != -1 or targetcard.Traits.find(chaonly) != -1:
							list.append(targetcard)
							targetcard.target(False)
						else:
							whisper("{} can only be attached to [{}] characters.".format(card,chaonly))
							targetcard.target(False)
					else:
						list.append(targetcard)
						targetcard.target(False)
				if len(list) == 1:cards=list
			if list == []:
				whisper("You must targeted(use Shift+mouse left button) a card which you want to attach to.")
				return
			if len(list) > 0:
				if len(list) > 1:
					dlg = cardDlg(list)
					dlg.title = "These cards can be attached:"
					dlg.text = "Choose a card to attach."
					cards = dlg.show()
				if cards != None:
					for choose in cards:
						if len(me.piles['Plot Deck']) != 7:
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
						attach = eval(getGlobalVariable("attachmodify"))
						if not attach.has_key(card._id):
							attach[card._id] = choose._id
						else:attach[card._id].append(choose._id)
						setGlobalVariable("attachmodify",str(attach))
						if card.model == "4dd074aa-af6c-4897-b7b2-bff3493bcf9e" and choose.model == "df79718d-b01d-4338-8907-7b6abff58303":choose.markers[MilitaryIcon] += 1#096
						if re.search('\+\d\sSTR', card.Text) and card.model != "9e6bf142-159b-4a3b-9d4c-d8bf233a6f0c" and card.model != "4c8a114e-106c-4460-846b-28f73914fc11":
							stradd = re.search('\+\d\sSTR', card.Text).group()
							choose.markers[STR_Up] += int(stradd[1])
						if re.search('\[INT]\sicon', card.Text):choose.markers[IntrigueIcon] += 1
						if re.search('\[POW]\sicon', card.Text):choose.markers[PowerIcon] += 1
						if re.search('\[MIL]\sicon', card.Text) and card.model != "4dd074aa-af6c-4897-b7b2-bff3493bcf9e":choose.markers[MilitaryIcon] += 1
						card.sendToBack()
						card.highlight = PlayColor
						if len(me.piles['Plot Deck']) == 7:
							notify("{} plays {} and attachs to {}.".format(me,card,choose))
						else:
							notify("{} plays {} and attachs to {} for {} Gold (Cost reduced by {}).".format(me,card,choose,cost,reduc))
				else:
					whisper("Attachment cards must be attached to another card or game element.")
					return
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
		card.filter = "#005c3521"
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

def movetobottom(card):
	mute()
	if len(card.group) < 2: return
	card.moveToBottom(card.group)
	notify("{} moves a card to bottom of {}'s {}'.".format(me,card.owner,card.group.name))

	
#------------------------------------------------------------------------------
# New Events
#------------------------------------------------------------------------------
def onloaddeck(args):
	mute()
	c = len(players)
	setGlobalVariable("numplayer","{}".format(c))
	if me._id == 1:
		setGlobalVariable("AID","{}".format(me))
	else:
		setGlobalVariable("BID","{}".format(me))
	setGlobalVariable("attachmodify", "{}")
	player = args.player
	if player==me:
		checkdeck()
		setup(table)
		
def onmoved(args):
	mute()
	index = 0
	for card in args.cards:
		attach = eval(getGlobalVariable("attachmodify"))
		if args.cards[index].type in ("Character","Attachment","Location") and args.toGroups[index].name == "Table" and args.fromGroups[index].name == "Table" and card.owner == me and card.filter != DuplicateColor:
			list = []
			list2 = []
			list3 = []
			for d in attach:
				if attach[d] == args.cards[index]._id:
					list.append(d)
			for dcard in table:
				if dcard.name == args.cards[index].name and dcard.filter == DuplicateColor and dcard.controller == me:
					list2.append(dcard._id)
			list.reverse()
			for cardatt in table:
				for listcard in table:
					if cardatt.controller == me and cardatt.name == listcard.name and  listcard._id in (list) and cardatt.filter == DuplicateColor:
						list3.append(cardatt)
			i = 12			
			if len(list) > 0:
				for cardindex in list:
					for carda in table:
						if carda._id == cardindex:
							x1,y1 = card.position
							if me.isInverted:carda.moveToTable(x1-i,y1-i)
							else:carda.moveToTable(x1+i,y1+i)
							carda.sendToBack()
							x2,y2 = carda.position
							i+=12
							k = 12
							for cardattd in list3:
								if cardattd.name == carda.name:
									if me.isInverted:cardattd.moveToTable(x2-k,y2+k)
									else:cardattd.moveToTable(x2+k,y2-k)
									cardattd.sendToBack()
									k+=12
			i = 12
			if args.cards[index].unique == "Yes":
				if len(list2) > 0:
					for cardindex in list2:
						for carda in table:
							if carda._id == cardindex:
								x1,y1 = card.position
								carda.moveToTable(x1-i,y1-i)
								carda.sendToBack()
								i+=12
		if card.type == "Attachment" and args.toGroups[index].name != "Table" and args.fromGroups[index].name == "Table" and card.owner == me:
			for card in table:
				if attach.has_key(args.cards[index]._id):
					if attach[args.cards[index]._id] == card._id:
						del attach[args.cards[index]._id]
						setGlobalVariable("attachmodify",str(attach))
					#rollback
						if args.cards[index].model == "4dd074aa-af6c-4897-b7b2-bff3493bcf9e" and card.model == "df79718d-b01d-4338-8907-7b6abff58303":card.markers[MilitaryIcon] -= 1#096
						if re.search('\+\d\sSTR', args.cards[index].Text) and card.model != "9e6bf142-159b-4a3b-9d4c-d8bf233a6f0c" and card.model != "4c8a114e-106c-4460-846b-28f73914fc11":
							stradd = re.search('\+\d\sSTR', args.cards[index].Text).group()
							card.markers[STR_Up] -= int(stradd[1])
						if re.search('\[INT]\sicon', args.cards[index].Text):card.markers[IntrigueIcon] -= 1
						if re.search('\[POW]\sicon', args.cards[index].Text):card.markers[PowerIcon] -= 1
						if re.search('\[MIL]\sicon', args.cards[index].Text) and args.cards[index].model != "4dd074aa-af6c-4897-b7b2-bff3493bcf9e":card.markers[MilitaryIcon] -= 1
			args.cards[index].resetProperties()
		if args.cards[index].type == "Character" and args.toGroups[index].name != "Table" and args.fromGroups[index].name == "Table" and card.owner == me:
			for d in attach:
				if attach[d] == args.cards[index]._id:
					for cardd in table:
						if cardd._id == d:
							if cardd.Text.find('Terminal.') == -1 and cardd.Keywords.find('Terminal.') == -1:cardd.moveTo(me.hand)
							else:cardd.moveTo(me.piles['Discard pile'])
							del attach[d]
							setGlobalVariable("attachmodify",str(attach))
		index += 1