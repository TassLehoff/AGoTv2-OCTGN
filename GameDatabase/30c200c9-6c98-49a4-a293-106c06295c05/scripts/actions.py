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
GameURL = "http://tinyurl.com/op4me9g"
FAQ_URL = "http://www.fantasyflightgames.com/ffg_content/agotlcg/support/FAQ-TR-updates/AGoT-FAQ.pdf"


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

def setup(group, x = 0, y = 0):
	mute()
	if not confirm("Are you sure to setup ?"): return
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
	notify("**{} is ready**".format(me))

#---------------------------------------------------------------------------
# Table card actions
#---------------------------------------------------------------------------
def displayCardText(card, x = 0, y = 0):
	mute()
	
	notify('{} - Card Text:'.format(card.name))
	notify('{}'.format(card.Text))

def displayErrata(card, x = 0, y = 0):
	mute()
	
	notify('{} - Errata Text:'.format(card.name))
	notify('{}'.format(card.ErrataText))
	
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

def countincome(card, x=0, y=0):
	mute()
	if not confirm("Is this your revealing plot?"): return
	if card.Type == "Plot" and card.controller == me:
		for incomecard in table:
			if incomecard.goldincome and incomecard.controller == me:
				me.counters['Gold'].value += int(incomecard.goldincome)
		me.counters['Gold'].value += int(card.plotgoldincome)
		card.markers[Gold] += me.counters['Gold'].value
		notify("{} counts income {} gold.".format(me,me.counters['Gold'].value))
	else:
		return

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
	else : 	card.moveToTable(0,160)
	notify("{} plays {} for {} Gold (Cost reduced by {}).".format(me,card,cost,reduc))
	me.counters['Gold'].value -= cost
	for incomecard in table:
		if incomecard.controller == me and incomecard.markers[Gold] > 0:
			incomecard.markers[Gold] -= cost

#------------------------------------------------------------------------------
# Pile Actions
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
			if NeutralCount<16:
					notify("Your Agenda is[{}]".format(card.name))
			else:
					notify("Your Agenda is[{}],You include {} neutral cards in your deck, which is not permitted.".format(card.name, NeutralCount, me))
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
	
