#-*- coding: utf-8 -*-  
#coding=utf-8 
#---------------------------------------------------------------------------
# Constants
#---------------------------------------------------------------------------
Gold = ("Gold", "4e8046ba-759b-428c-917f-7e9268a5af90") #The GUID from markers.o8g
Power = ("Power", "d115ea96-ed05-4bf7-ba22-a34c8675c676") #The GUID from markers.o8g
STR_Up = ("STR_Up", "7898d5a0-1d59-42b2-bbfb-5051cc420cd8") #The GUID from markers.o8g
STR_Sub = ("STR_Sub", "1be0aa4d-8f52-42d7-bc3f-798c9759ba5e") #The GUID from markers.o8g
Burn = ("Burn", "c272aa0c-f283-4ff5-b545-a5a3f150e6da") #The GUID from markers.o8g
TokenRed = ("TokenRed", "6238a357-41b7-4bca-b394-925fc1b2caf8") #The GUID from markers.o8g
TokenBlue = ("TokenBlue", "99452bc7-d95b-4c54-8577-41d98dd3e30b") #The GUID from markers.o8g
MilitaryColor = "#ae0603" #A shade of red from the Military Icon
IntrigueColor = "#006b34" #A shade of green from the Intrigue Icon
PowerColor = "#1a4d8f" #A shade of blue from the Power Icon
WaitColor = "#5c3521" # Grey
PlayColor = "#ffa6f7" # Yellow
showColor = "#ffa6f8"
miljudgecolor = "#000000" # black
milsavecolor = "#ff0000" # red
saveactioncolor = "#6aa84f" # green
countereventcolor = "#c0ff3e" #
usedplotcolor = "#99ffff"
sacrificecolor = "#a0522d"
interruptcolor = "#ffd700"
leavecolor = "#b03060"
leaveandabilitycolor = "#20124d"
leaveonlycolor = "#e06666"
activcolor = "#e06667"
abilitycolor = "#a32f5b"
Stealthcolor = "#ffffff"
cantchallengecolor = "#fffacd"
targetcardcolor = "#e69138"
cantselectcardclor = "#000000"
targetcardfilter = "#55e69138"
cantselectcardfilter = "#88000000"
sourcecardcolor = "#3d85c6"
sourcecardcfilter = "#773d85c6"
showtablecolor = "#000002"
showtablefilter = "#00000002"
standcolor = "#000003"
standfilter = "#00000003"
discfilter = "#00000004"

GameURL = "http://octgn.gamersjudgement.com/wordpress/agot2/"
FAQ_URL = "https://images-cdn.fantasyflightgames.com/filer_public/03/43/034309e6-c3a2-4575-8062-32ede5798ef8/gt01_rules-reference-web.pdf"
#add
MilitaryIcon = ("MilitaryIcon", "7e9610d4-c06d-437d-a5e6-100000000001")
IntrigueIcon = ("IntrigueIcon", "0cabfb36-01b4-46c4-bb2a-42889fb63e8b")
PowerIcon = ("PowerIcon", "a6b9db40-b0ad-4b22-b049-5837c4ece904")
subMilitaryIcon = ("subMilitaryIcon", "786f6eb1-22bf-4623-9423-7854f5f078d6")
subIntrigueIcon = ("subIntrigueIcon", "7dadfabe-8024-4d93-91a7-81c11a51ff24")
subPowerIcon = ("subPowerIcon", "d042dab3-176a-471e-a917-1041c64c6579")
poisonIcon = ("poisonIcon", "aba7e269-4096-4b60-b1c5-0ab97dd9caa0")
standIcon = ("standIcon", "353db31d-b5d7-4f17-9683-08b03151ff83")
betrayalIcon = ("betrayalIcon", "d042dab3-176a-471e-a917-1041c64c6579")
cardtmp = []

debugMode = False
countusedplot = 0
Heartsbaneused = 0
countmil = 1
challengetype = 0
winplayer = []
attacker = []
defender = []
unopposed = 0
otherplayer = []
mjfinish = 0
savepoint = 0
claimtmp = 0
timerIsRunning = False
savetarget = []
inserttarget = []
interruptpass = 0
interruptpasstmp = 0
interruptcancelplayer = []
saveactionplayer = []
interruptcancelcard = []
interruptcancellastcard = []
interruptcanceledcard = []
reducegold = 0
interruptcancelok = 1
interruptlib = {}
interruptlibtmp = {}
mainpass = ""
selectplayer = []
sessionpass = ""
interruptsessionpass = ""
interruptpasscounttmp = 0
selectedcard = []
liststeal = []
cardkilllist = []
smcount = 1
kbcount = 1
recount = 1
abilityattach = {}
leavecardtype = []
leavetablecard = []
reactionattach = {}
actionattach = {}
reactioncardlimit = {}
actioncardlimit = {}
keywordattach = []
intertreaction = 0
isinsertreaction = 0
interruptreaction = []
nextcardtmp = []
cardtoaction = []
dwtmpcard = []
plotcard = []
top5card = []
savetargettmp = []
inserttargettmp = []
interruptcancelcardtmp = []
interruptcancelplayertmp = []
interruptcanceledcardtmp = []
interruptcancellastcardtmp = []
interruptlibtmp = {}
interruptcanceloktmp = 1
saveactionplayertmp = []
mainpasstmp = ""
insertreactioncard = []
manualcard = []
interruptcardselect = []
listattach = []
aryaduplicate = []
#turnreset

usedplot = []

addiconmil_turn = []
addiconint_turn = []
addiconpow_turn = []
subiconmil_turn = []
subiconint_turn = []
subiconpow_turn = []
returntohand_turn = []
noprint_turn = []
disc_turn = []


import re
import time


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
	global attacker
	global challengetype
	global selectedcard
	global sessionpass
	global stealthcount
	stealth = ""
	stealthcount = 0
	if sessionpass != "milselectok":
		notify("**{} declares a MIL challenge.**".format(me))
		list = []
		for card in table:
			card.highlight = None
			card.target(False)
			if card.type == "Character" and card.controller == me and card.isFaceUp and checkchallengeicon(card,"milicon") and card.orientation == 0:
				list.append(card)
		if len(list) == 0:
			whisper("No more card can eclares a MIL challenge.")
		dlg = cardDlg(list)
		dlg.title = "These cards are in your table:"
		dlg.text = "Declares at least 1 character to attack."
		dlg.min = 1
		dlg.max = len(list)
		cards = dlg.show()
	else:cards = selectedcard
	if cards != None and cards != []:
		for c in cards:
			if getGlobalVariable("automode") != "1":
				c.target(True)
			c.highlight = MilitaryColor
			if c.model != "a8854084-67e5-4955-89db-3d9cb1337789":
				if c.model == "09903f79-6155-4a63-9b52-e10fb2e69898":
					for cards in table:
						if cards.model == "99a12a9c-6e83-43bd-8947-0cc47ffcd02a" and cards.controller == me:
							attach = eval(getGlobalVariable("attachmodify"))
							if attach.has_key(cards._id):
								if attach(cards._id) == c._id and countmil == 1:
									c.orientation = 0
								else:c.orientation = 1
				elif c.model != "09903f79-6155-4a63-9b52-e10fb2e69898":c.orientation = 1
				if re.search(r'stealth',c.keywords,re.I):   #stealth
					stealth = "0"
					stealthcount += 1
					if c.model == afterchallengereacion['Ghost'][1]:setGlobalVariable("cantchallenge", "1")
		notify("**{} declares MIL attackers.**".format(me))
		if getGlobalVariable("automode") == "1":
			attacker = me
			challengetype = 1
			remoteCall(otherplayer, "getattacker", [attacker,challengetype])
			sessionpass = ""
			selectedcard = []
			setGlobalVariable("selectmode", "0")
		if stealth == "0" and not check511():
			if checktablestealthcount(0):
				choice = confirm("Character with the stealth keyword has been declared as an attacker, do you want to chooses its stealth target?")
				if choice == True:
					stealthdict()
					notify("{} is ready to use the stealth keyword.".format(me))
					if getGlobalVariable("automode") == "1":
						selectstealth(table)
						return
				else:
					notify("{} renounces the use of the stealth keyword.".format(me))
			stealth = "1"
		if getGlobalVariable("automode") == "1":remoteCall(otherplayer, "challengedeficon", ["mil"])
			# if getGlobalVariable("mainstep") == "0":setGlobalVariable("mainstep", "1")
			# #checkafterchallengereacioncard(1)
			# b = str(int(me.getGlobalVariable("milcount"))+1)
			# me.setGlobalVariable("milcount",b)
		countmil += 1
	else:
		whisper("You must declare at least 1 character to attack.")

def announceInt(group, x = 0, y = 0):
	mute()
	global attacker
	global challengetype
	global stealthcount
	global selectedcard
	global sessionpass
	stealth = ""
	stealthcount = 0
	if sessionpass != "intselectok":
		notify("**{} declares an INT challenge.**".format(me))
		list = []
		for card in table:
			card.highlight = None
			card.target(False)
			if card.type == "Character" and card.controller == me and card.isFaceUp and checkchallengeicon(card,"inticon") and card.orientation == 0:
				list.append(card)
		dlg = cardDlg(list)
		dlg.title = "These cards are in your table:"
		dlg.text = "Declares at least 1 character to attack."
		dlg.min = 1
		dlg.max = len(list)
		cards = dlg.show()
	else:cards = selectedcard
	if cards != None and cards != []:
		for c in cards:
			if getGlobalVariable("automode") != "1":
				c.target(True)
			c.highlight = IntrigueColor
			c.orientation = 1
			if re.search(r'stealth',c.keywords,re.I):   #stealth
				stealth = "0"
				stealthcount += 1
		notify("**{} declares INT attackers.**".format(me))
		if getGlobalVariable("automode") == "1":
			attacker = me
			challengetype = 2
			remoteCall(otherplayer, "getattacker", [attacker,challengetype])
			sessionpass = ""
			selectedcard = []
			setGlobalVariable("selectmode", "0")
		if stealth == "0" and not check511():
			if checktablestealthcount(0):
				choice = confirm("Character with the stealth keyword has been declared as an attacker, do you want to chooses its stealth target?")
				if choice == True:
					stealthdict()
					notify("{} is ready to use the stealth keyword.".format(me))
					if getGlobalVariable("automode") == "1":
						selectstealth(table)
						return
				else:
					notify("{} renounces the use of the stealth keyword.".format(me))
			stealth = "1"
		if getGlobalVariable("automode") == "1":remoteCall(otherplayer, "challengedeficon", ["int"])
			# setGlobalVariable("mainstep", "1")
			# #checkafterchallengereacioncard(1)
			# b = str(int(me.getGlobalVariable("intcount"))+1)
			# me.setGlobalVariable("intcount",b)
	else:
		whisper("You must declare at least 1 character to attack.")

def announcePow(group, x = 0, y = 0):
	mute()
	global attacker
	global challengetype
	global stealthcount
	global selectedcard
	global sessionpass
	stealth = ""
	stealthcount = 0
	if sessionpass != "powselectok":
		notify("**{} declares a POW challenge.**".format(me))
		list = []
		for card in table:
			card.highlight = None
			card.target(False)
			if card.type == "Character" and card.controller == me and card.isFaceUp and checkchallengeicon(card,"powicon") and card.orientation == 0:
				list.append(card)
		dlg = cardDlg(list)
		dlg.title = "These cards are in your table:"
		dlg.text = "Declares at least 1 character to attack."
		dlg.min = 1
		dlg.max = len(list)
		cards = dlg.show()
	else:cards = selectedcard
	if cards != None and cards != []:
		for c in cards:
			if getGlobalVariable("automode") != "1":
				c.target(True)
			c.highlight = PowerColor
			c.orientation = 1
			if re.search(r'stealth',c.keywords,re.I):   #stealth
				stealth = "0"
				stealthcount += 1
		notify("**{} declares POW attackers.**".format(me))
		if getGlobalVariable("automode") == "1":
			attacker = me
			challengetype = 3
			remoteCall(otherplayer, "getattacker", [attacker,challengetype])
			sessionpass = ""
			selectedcard = []
			setGlobalVariable("selectmode", "0")
		if stealth == "0" and not check511():
			if checktablestealthcount(0):
				choice = confirm("Character with the stealth keyword has been declared as an attacker, do you want to chooses its stealth target?")
				if choice == True:
					stealthdict()
					notify("{} is ready to use the stealth keyword.".format(me))
					if getGlobalVariable("automode") == "1":
						selectstealth(table)
						return
				else:
					notify("{} renounces the use of the stealth keyword.".format(me))
			stealth = "1"
		if getGlobalVariable("automode") == "1":remoteCall(otherplayer, "challengedeficon", ["pow"])
			# setGlobalVariable("mainstep", "1")
			# #checkafterchallengereacioncard(1)
			# b = str(int(me.getGlobalVariable("powcount"))+1)
			# me.setGlobalVariable("powcount",b)
	else:
		whisper("You must declare at least 1 character to attack.")

def holdOn(group, x = 0, y = 0):
	mute()
	notify("**Please wait.  {} has an action/question.**".format(me))

def announceOpp(group, x = 0, y = 0):
	mute()
	global attacker
	global challengetype
	global defender
	global sessionpass
	if getGlobalVariable("automode") == "1":
		setGlobalVariable("mainstep", "3")
		if attacker == me:
			notify("You already are a attacker.")
			return
		if attacker != []:
			notify("**{} responds: Opposed/Defend.**".format(me))
			if challengetype == 1:
				choiceList = ['Military', 'No defenders']
				colorList = ['#ae0603' ,'#D8D8D8']
				choice = askChoice("Opposed or defend?", choiceList,colorList)
				if choice == 1:
					if getGlobalVariable("automode") != "1":
						defMil(table)
					else:
						targetTuple = ([card._id for card in table if card.type == "Character" and card.controller == me and card.isFaceUp and card.highlight != Stealthcolor and checkchallengeicon(card,"milicon") and card.orientation == 0], me._id) 
						setGlobalVariable("tableTargets", str(targetTuple))
						setGlobalVariable("selectmode", "2")
						if me.isInverted:table.create("584a37d7-5a30-4018-ae21-0ad325203fa0",-375,-250)
						else:table.create("584a37d7-5a30-4018-ae21-0ad325203fa0",-375,200)
						sessionpass = "mildefselect"
						notify("**{} into selectmode**".format(me))
				elif choice == 2:
					notify("{} declares no defenders.".format(me))
					defender = me
					remoteCall(otherplayer, "getdefender", [me])
					challengeaction(1)
			if challengetype == 2:
				choiceList = ['Intrigue', 'No defenders']
				colorList = ['#006b34' ,'#D8D8D8']
				choice = askChoice("Opposed or defend?", choiceList,colorList)
				if choice == 1:
					if getGlobalVariable("automode") != "1":
						defInt(table)
					else:
						targetTuple = ([card._id for card in table if card.type == "Character" and card.controller == me and card.isFaceUp and card.highlight != Stealthcolor and checkchallengeicon(card,"inticon") and card.orientation == 0], me._id) 
						setGlobalVariable("tableTargets", str(targetTuple))
						setGlobalVariable("selectmode", "2")
						if me.isInverted:table.create("584a37d7-5a30-4018-ae21-0ad325203fa0",-375,-250)
						else:table.create("584a37d7-5a30-4018-ae21-0ad325203fa0",-375,200)
						sessionpass = "intdefselect"
						notify("**{} into selectmode**".format(me))
				elif choice == 2:
					if getGlobalVariable("automode") == "1":
						c = 0
						for card in table:
							if str(card._id) in getGlobalVariable("bedefend") and card.controller == me and card.isFaceUp and checkchallengeicon(card,"powicon") and card.orientation == 0 and card.highlight != IntrigueColor:
								card.highlight = IntrigueColor
								card.orientation = 1
								c = 1
						if c == 0:notify("{} declares no defenders.".format(me))
						else:
							setGlobalVariable("bedefend","")
							notify("**{} declares INT defenders.**".format(me))
					else:
						notify("{} declares no defenders.".format(me))
					defender = me
					remoteCall(otherplayer, "getdefender", [me])
					challengeaction(1)
			if challengetype == 3:
				choiceList = ['Power', 'No defenders']
				colorList = ['#1a4d8f','#D8D8D8']
				choice = askChoice("Opposed or defend?", choiceList,colorList)
				if choice == 1:
					if getGlobalVariable("automode") != "1":
						defPow(table)
					else:
						targetTuple = ([card._id for card in table if card.type == "Character" and card.controller == me and card.isFaceUp and card.highlight != Stealthcolor and checkchallengeicon(card,"powicon") and card.orientation == 0], me._id) 
						setGlobalVariable("tableTargets", str(targetTuple))
						setGlobalVariable("selectmode", "2")
						if me.isInverted:table.create("584a37d7-5a30-4018-ae21-0ad325203fa0",-375,-250)
						else:table.create("584a37d7-5a30-4018-ae21-0ad325203fa0",-375,200)
						sessionpass = "powdefselect"
						notify("**{} into selectmode**".format(me))
				elif choice == 2:
					notify("{} declares no defenders.".format(me))
					defender = me
					remoteCall(otherplayer, "getdefender", [me])
					challengeaction(1)
			else:return
		else:notify("No challenge happened.")
	else:
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
	global defender
	global selectedcard
	global sessionpass
	if sessionpass != "mildefselectok":
		list = []
		for card in table:
			card.target(False)
			if card.type == "Character" and card.controller == me and card.isFaceUp and checkchallengeicon(card,"milicon") and card.orientation == 0:
				list.append(card)
		dlg = cardDlg(list)
		dlg.title = "These cards are in your table:"
		dlg.text = "Declares characters to defend."
		dlg.min = 1
		dlg.max = len(list)
		cards = dlg.show()
	else:cards = selectedcard
	if cards != None and cards != []:
		for c in cards:
			if getGlobalVariable("automode") != "1":
				c.target(True)
			c.highlight = MilitaryColor
			c.orientation = 1
		notify("**{} declares MIL defenders.**".format(me))
	else:
		notify("{} declares no defenders.".format(me))
	if getGlobalVariable("automode") == "1":
		setGlobalVariable("selectmode", "0")
		# defender = me
		# remoteCall(otherplayer, "getdefender", [defender])
		sessionpass = ""
		selectedcard = []
		#challengeaction(1)

def defInt(group, x = 0, y = 0):
	mute()
	global defender
	global selectedcard
	global sessionpass
	if sessionpass != "intdefselectok":
		list = []
		for card in table:
			card.target(False)
			if card.type == "Character" and card.controller == me and card.isFaceUp and checkchallengeicon(card,"inticon") and card.orientation == 0:
				list.append(card)
		dlg = cardDlg(list)
		dlg.title = "These cards are in your table:"
		dlg.text = "Declares characters to defend."
		dlg.min = 1
		dlg.max = len(list)
		cards = dlg.show()
	else:cards = selectedcard
	if cards != None and cards != []:
		for c in cards:
			if getGlobalVariable("automode") != "1":
				c.target(True)
			c.highlight = IntrigueColor
			c.orientation = 1
		if getGlobalVariable("automode") == "1":
			for card in table:
				if str(card._id) in getGlobalVariable("bedefend") and card.controller == me and card.isFaceUp and checkchallengeicon(card,"inticon") and card.orientation == 0 and card.highlight != IntrigueColor:
					card.highlight = IntrigueColor
					card.orientation = 1
			setGlobalVariable("bedefend","")
		notify("**{} declares INT defenders.**".format(me))
	else:
		if getGlobalVariable("automode") == "1":
			c = 0
			for card in table:
				if str(card._id) in getGlobalVariable("bedefend") and card.controller == me and card.isFaceUp and checkchallengeicon(card,"inticon") and card.orientation == 0 and card.highlight != IntrigueColor:
					card.highlight = IntrigueColor
					card.orientation = 1
					c = 1
			if c == 0:notify("{} declares no defenders.".format(me))
			else:
				setGlobalVariable("bedefend","")
				notify("**{} declares INT defenders.**".format(me))
	if getGlobalVariable("automode") == "1":
		setGlobalVariable("selectmode", "0")
		defender = me
		remoteCall(otherplayer, "getdefender", [defender])
		sessionpass = ""
		selectedcard = []
		#challengeaction(1)

def defPow(group, x = 0, y = 0):
	mute()
	global defender
	global defender
	global selectedcard
	global sessionpass
	if sessionpass != "powdefselectok":
		list = []
		for card in table:
			card.target(False)
			if card.type == "Character" and card.controller == me and card.isFaceUp and checkchallengeicon(card,"powicon") and card.orientation == 0:
				list.append(card)
		dlg = cardDlg(list)
		dlg.title = "These cards are in your table:"
		dlg.text = "Declares characters to defend."
		dlg.min = 1
		dlg.max = len(list)
		cards = dlg.show()
	else:cards = selectedcard
	if cards != None and cards != []:
		for c in cards:
			if getGlobalVariable("automode") != "1":
				c.target(True)
			c.highlight = PowerColor
			c.orientation = 1
		notify("**{} declares POW defenders.**".format(me))
	else:
		notify("{} declares no defenders.".format(me))
	if getGlobalVariable("automode") == "1":
		defender = me
		remoteCall(otherplayer, "getdefender", [defender])
		sessionpass = ""
		selectedcard = []
		#challengeaction(1)
		
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
	# if (card.model == "f97ccf1a-5b0d-490f-9968-78330e92171c" or card.model == "4c8a114e-106c-4460-846b-28f73914fc11") and card.orientation == 0:
	# 	if not confirm("Do you want to use {}'s ability?".format(card.name)): return
	# 	attach = card.name+str(card.position)
	# 	for cards in table:
	# 		f = cards.name+str(cards.position)
	# 		if attachmodify != {}:
	# 			if f == attachmodify[attach]:
	# 				if card.model == "4c8a114e-106c-4460-846b-28f73914fc11":#just for Heartsbane
	# 					global Heartsbaneused
	# 					cards.markers[STR_Up] += 3
	# 					card.orientation ^= Rot90
	# 					Heartsbaneused = 1	
	# 					return
	# 				if cards.orientation != 0:
	# 					cards.orientation ^= Rot90
	# 					card.orientation ^= Rot90
	# 				else:
	# 					notify("{} is standing, you cannot stand it.".format(cards))
	# 					return
	# else:notify("{} s already knelt.".format(card))
	# if card.model not in ("f97ccf1a-5b0d-490f-9968-78330e92171c" ,"4c8a114e-106c-4460-846b-28f73914fc11"):		
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

def addhousepow(ok = 1):
	for count in range(0,ok):
		for housecard in table:
			if housecard.type == "Faction" and housecard.controller == me:
				addPower(housecard)

def subhousepow(ok = 1):
	for count in range(0,ok):
		for housecard in table:
			if housecard.type == "Faction" and housecard.controller == me:
				subPower(housecard)


	
#---------------------------
#movement actions
#---------------------------

#------------------------------------------------------------------------------
# Hand Actions
#------------------------------------------------------------------------------

def randomDiscard(group=me.hand):
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
	
	if not confirm("Are you sure you want to Mulligan?"): return False
	if draw == None: draw = askInteger("How many cards would you like to draw for your Mulligan?", len(me.hand))
	if draw == None: return True
	
	for card in group:
		card.moveToBottom(me.deck)
			
	me.deck.shuffle()
		
	for card in me.deck.top(draw):
		card.moveTo(me.hand)
	notify("{} mulligans and draws {} new cards.".format(me, draw))
	
	return True

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
	if getGlobalVariable("marshalphase") != "0":
		if me.getGlobalVariable("firstdraw") != "0":me.setGlobalVariable("firstdraw","1")
	
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
	global winplayer
	global attacker
	global defender
	global unopposed
	global challengetype
	global otherplayer
	if getGlobalVariable("automode") != "1":
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
				c.moveToTable(-320,-100)			
			else:
				c.moveToTable(-320,10)
		if c.Type == "Agenda":
			if me.isInverted: 
				c.moveToTable(-240,-100)			
			else:
				c.moveToTable(-240,10)
	me.deck.shuffle()
	for card in me.deck.top(7):
		card.moveTo(me.hand)
	if me.isInverted: 
		table.create("656f69c4-c506-4014-932b-9dff4422f09e",-320,-175)
	else:
		table.create("656f69c4-c506-4014-932b-9dff4422f09e",-320,85)

	notify("**{} is ready to setup**".format(me))
	if me._id == int(getGlobalVariable("aside")):
		if me.isInverted: 
			table.create("73a6655b-60b6-4080-b428-f4e0099e0f77",380,-100)
		else:
			table.create("73a6655b-60b6-4080-b428-f4e0099e0f77",-160,8)
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
		remoteCall(players[1], "getotherplayer", me)
	winplayer = []
	attacker = []
	defender = []
	unopposed = 0
	challengetype = 0
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
	countcards = -60
	countcardss = -60
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
				if not checksetupattch(cards):
					confirm("Attachment card's target error.")
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
					card.moveToTable(countcardss,-100,True)
					countcardss=countcardss+80
				else:
					card.moveToTable(countcards,10,True)
					countcards=countcards+80
				card.peek()
			for drawcard in me.deck.top(7-len(me.hand)):
				drawcard.moveTo(me.hand)
			notify("{} is ready to begin.".format(me))
			if getGlobalVariable("automode") == "1":
				me.setGlobalVariable("setupOk","3")
				if len(players) == 1:
					remoteCall(me, "proccessetupcard", [table])
				else:
					if me.getGlobalVariable("setupOk") == players[1].getGlobalVariable("setupOk") == "3":
						remoteCall(me, "proccessetupcard", [1])
	else:
		if me.getGlobalVariable("setupOk") == "2":
			placesetupcards()
		else:
			isMulligan = mulligan(me.hand)
			if(isMulligan):
				me.setGlobalVariable("setupOk","2")
			placesetupcards()

def checksetupattch(cards):
	c = 0
	f = 1
	listat = []
	listc = []
	for card in cards:
		if card.type == "Character":
			if 'No attachments.' not in card.Keywords:
				c = 1
				listc.append(card)
		if card.type == "Attachment":
			listat.append(card)
			if card.Keywords == "Opponent’s character only.":
				c = 0
				break
	if len(listat) > 0:
		for atcard in listat:
			if re.search(r'(.*) or (.*) character only.', atcard.Text,re.I):
				f = 0
				for targetcard in listc:
					if targetcard.Traits.find('Lord') != -1 or targetcard.Traits.find('Lady') != -1:
						debug(targetcard)
						f = 1
			elif re.search(r'\[(.*)] character only.', atcard.Text,re.I):
				chaonly = re.search(r'\[(.*)] character only.', atcard.Text,re.I).group(1)
				f = 0
				for targetcard in listc:
					if chaonly in targetcard.Faction or targetcard.Traits.find(chaonly) != -1:
						f = 1
	debug(f)
	debug(c)
	if f == 1 and c == 1:return True

def proccessetupcard(count):
	mute()
	global listattach
	for card in table:
		if not card.isFaceUp and card.controller == me:
			flipcard(card)
			if card.type == "Attachment" and card.filter == None:
				listattach.append(card)
	if len(listattach) > 0:
		me.setGlobalVariable("setupOk","4")
		attatchcard(listattach)
	else:
		reordertable(table)
	if count == 1:remoteCall(players[1], "proccessetupcard", [2])

def attatchcard(listattach):
	mute()
	global sessionpass
	global cardtmp
	attachid = []
	if re.search(r'(.*) or (.*) character only.', listattach[0].Text,re.I):
		for targetcard in table:
			if targetcard.type == "Character" and targetcard.controller == me:
				if targetcard.Traits.find('Lord') != -1 or targetcard.Traits.find('Lady') != -1:
					attachid.append(targetcard._id)
	elif re.search(r'\[(.*)] character only.', listattach[0].Text,re.I):
		chaonly = re.search(r'\[(.*)] character only.', listattach[0].Text,re.I).group(1)
		for targetcard in table:
			if targetcard.type == "Character" and targetcard.controller == me:
				if chaonly in targetcard.Faction or targetcard.Traits.find(chaonly) != -1:
					attachid.append(targetcard._id)
	if attachid != []:selectlist = attachid
	else:selectlist = checkcardid(deck = table,cardtype = "Character",player = me)
	selectcardnext(selectlist,"attatchcardselect",table,listattach[0],me,1)
	#selectcardnext(selectlist,spass,deck = table,actioncard = [],)
	# targetTuple = ([card._id for card in table if card.Type in "Character" and card.controller == me], me._id)
	# me.setGlobalVariable("tableTargets", str(targetTuple))
	# setGlobalVariable("selectmode", "1")
	# sessionpass = "attatchcardselect"
	# if me.isInverted:table.create("584a37d7-5a30-4018-ae21-0ad325203fa0",-375,-250)
	# else:table.create("584a37d7-5a30-4018-ae21-0ad325203fa0",-375,200)
	# for card in table:
	# 	if card.type not in ("Internal","Agenda","Faction"):
	# 		if card._id not in targetTuple[0] and card._id != listattach[0]._id:
	# 			card.filter="#88000000"
	# notify("**{} into selectmode**".format(me))
	whisper("Please select a target for {}".format(listattach[0]))

def reordertable(group, x = 0, y = 0):
	mute()
	countcards = -60
	countcard = -60
	attach = eval(getGlobalVariable("attachmodify"))
	for card in table:
		if card.type == "Character" and card.controller == me and card.filter == None:
			if me.isInverted:
				card.moveToTable(countcards,-100,True)
			else:
				card.moveToTable(countcards,10,True)
			countcards=countcards+80
		if card.type == "Location" and card.controller == me and card.filter == None:
			if me.isInverted:
				card.moveToTable(countcard,-220,True)
			else:
				card.moveToTable(countcard,120,True)
			countcard=countcard+80
		list = []
		list2 = []
		list3 = []
		for d in attach:
			if attach[d] == card._id:
				list.append(d)
		for dcard in table:
			if dcard.name == card.name and dcard.filter == WaitColor and dcard.controller == me:
				list2.append(dcard._id)
		list.reverse()
		for cardatt in table:
			for listcard in table:
				if cardatt.controller == me and cardatt.name == listcard.name and  listcard._id in (list) and cardatt.filter == WaitColor:
					list3.append(cardatt)
		i = 12			
		if len(list) > 0:
			for cardindex in list:
				for carda in table:
					if carda._id == cardindex and carda.controller == me:
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
		if card.unique == "Yes" and card.controller == me and card.filter != WaitColor:
			if len(list2) > 0:
				for cardindex in list2:
					for carda in table:
						if carda._id == cardindex and carda.controller == me:
							debug(carda._id)
							x1,y1 = card.position
							if me.isInverted:carda.moveToTable(x1+i,y1+i)
							else:carda.moveToTable(x1-i,y1-i)
							carda.sendToBack()
							i+=12
	for cards in table:
		if cards.controller == me and cards.filter != WaitColor:
			if cards.model == "fdf1989a-ee7d-4972-9d12-b299bfe3ba6d":
				for cardadd in table:
					if cardadd.controller == me and "Knight." in cardadd.traits and cardadd.filter != WaitColor and cardadd._id != cards._id:
						cardmarkers(cards,"str",1)
						cardmarkers(cards,"powicon",1)
						break
			if cards.model == "597acd7c-3424-4e8c-82e6-d6682d662c8c":
				for cardadd in table:
					if cardadd.controller == me and cardadd.model == "a5512893-cf5c-4e54-a8a7-87114492a50b" and cardadd.filter != WaitColor:
						cardmarkers(cards,"str",1)
						cardmarkers(cards,"powicon",1)
			if cards.model == "a5512893-cf5c-4e54-a8a7-87114492a50b":
				for cardadd in table:
					if cardadd.controller == me and cardadd.model == "597acd7c-3424-4e8c-82e6-d6682d662c8c" and cardadd.filter != WaitColor:
						cardmarkers(cards,"str",1)
						cardmarkers(cards,"inticon",1)

			if cards.model == "91b7190f-d0ba-4c3b-b9e2-5e7d2c872acb":
				for cardadd in table:
					if cardadd.controller == me and "Drowned God." in cardadd.traits:cardmarkers(cards,"str",1)
			if "The Reach" in cards.traits:
				for cardadd in table:
					if cardadd.controller == me and cardadd.model == "3e1a5952-f5d1-4bca-9226-2b94531cfa54":cardadd.markers[STR_Up] += 1
			if "Warship" in cards.traits:
				for cardadd in table:
					if cardadd.controller == me and cardadd.model == "cbeb3a37-d4c1-4697-b8d2-e366b4569002":cardadd.markers[STR_Up] += 1
			if cards.model == "5d20e021-5d12-4338-8bdd-42d008bff919":
				for cardadd in table:
					if cardadd.controller == me and cardadd.Faction == "Night's Watch." and cardadd.type == "Character" and cardadd.filter != WaitColor:cardadd.markers[STR_Up] += 1
			if "Direwolf" in cards.traits and cards.model != "c41d4a72-6919-4e32-97ef-a4b0f1acb281":
				for cardadd in table:
					if cardadd.controller == me and cardadd.model == "c41d4a72-6919-4e32-97ef-a4b0f1acb281":cardadd.markers[STR_Up] += 1
			if cards.model == "c41d4a72-6919-4e32-97ef-a4b0f1acb281":
				for cardadd in table:
					if cardadd.controller == me and cardadd.model == "c41d4a72-6919-4e32-97ef-a4b0f1acb281" and cards._id != cardadd._id:cardadd.markers[STR_Up] += 1
	notify("{} finished setup phase".format(me))
	me.setGlobalVariable("setupOk","5")

	# targetTuple = (["setupOk"], me._id)
	# me.setGlobalVariable("tableTargets", str(targetTuple))
	# setGlobalVariable("selectmode", "1")
	if fplay(1) == me:
		if me.isInverted:table.create("62bad042-fbb0-4121-85d2-92149576308b",-375,-250)
		else:table.create("62bad042-fbb0-4121-85d2-92149576308b",-375,200)
	# notify("**{} into selectmode**".format(me))

def setupnext(group, x = 0, y = 0):
	mute()
	for cardn in table:
		if cardn.name == "setupnextbutton" and cardn.controller == me:
			cardn.delete()#delete setupnextbutton
	me.setGlobalVariable("setupOk","6")
	if len(players) == 1:
		notify("just play for two players")
		return
	if me.getGlobalVariable("setupOk") == players[1].getGlobalVariable("setupOk") == "6":
		setGlobalVariable("selectmode", "0")
		notify("Plot phase start")
		remoteCall(me, "revealplot", [table])
		remoteCall(players[1], "revealplot", [table])
	else:
		c = 0
		for cardn in table:
			if cardn.name == "setupnextbutton" and cardn.controller != me:
				c = 1
		if c == 0:remoteCall(players[1], "plotphasestart", [3])

def drawphasestart(count):
	mute()
	if me.isInverted:table.create("634c8980-9e07-40ba-a259-df1fe8fd184a",-375,-250)
	else:table.create("634c8980-9e07-40ba-a259-df1fe8fd184a",-375,200)
	#if count == 1:remoteCall(players[1], "drawphasestart", [2])

def plotnext(group, x = 0, y = 0):
	mute()
	for cardn in table:
		if cardn.name == "plotnextbutton" and cardn.controller == me:
			cardn.delete()#delete plotnextbutton
	me.setGlobalVariable("plotOk","finished")
	if me.getGlobalVariable("plotOk") == players[1].getGlobalVariable("plotOk") == "finished":
		notify("plot phase over")
		setGlobalVariable("selectmode", "0")
		setGlobalVariable("reavelplot","0")
		setGlobalVariable("generalaction","0")
		setGlobalVariable("drawphase","1")
		notify("draw phase start")
		drawphase(table)
	else:
		c = 0
		for cardn in table:
			if cardn.name == "plotnextbutton" and cardn.controller != me:
				c = 1
		if c == 0:remoteCall(players[1], "drawphasestart", [3])

def marshalphasestart(count):
	mute()
	if me.isInverted:table.create("76d32ba3-bb1b-4c88-8e99-4381e45595e9",-375,-250)
	else:table.create("76d32ba3-bb1b-4c88-8e99-4381e45595e9",-375,200)
	#if count == 1:remoteCall(players[1], "marshalphasestart", [2])


def drawnext(group, x = 0, y = 0):
	mute()
	for cardn in table:
		if cardn.name == "drawnextbutton" and cardn.controller == me:
			cardn.delete()#delete drawnextbutton
	me.setGlobalVariable("drawOk","finished")
	if me.getGlobalVariable("drawOk") == players[1].getGlobalVariable("drawOk") == "finished":
		setGlobalVariable("selectmode", "0")
		notify("draw phase over")
		setGlobalVariable("drawphase","0")
		notify("marshal phase start")
		marshalcountincome()
	else:
		c = 0
		for cardn in table:
			if cardn.name == "drawnextbutton" and cardn.controller != me:
				c = 1
		if c == 0:remoteCall(players[1], "marshalphasestart", [3])

def countincome(group, x=0, y=0):
	mute()
	debug(getGlobalVariable("Kingdomgold0"))
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
						if card.controller == me and card.type == "Plot" and card.filter == None]
		plotlist.reverse()
		for plotcard in plotlist:
			if getGlobalVariable("Kingdomgold0") == "1" and "Kingdom" in plotcard.Traits:me.counters['Gold'].value += 0
			elif getGlobalVariable("Edictgold0") == "1" and "Edict" in plotcard.Traits:me.counters['Gold'].value += 0
			else:
				me.counters['Gold'].value += int(plotcard.plotgoldincome)
			plotcard.markers[Gold] = me.counters['Gold'].value
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
		if person.counters['Initiative'].value > 0:
 			person.counters['Initiative'].value = person.counters['Initiative'].value
 		else:
 			person.counters['Initiative'].value = 0
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
		#notify("{} has a total of {} power.".format(person.name,person.counters['Power'].value))

def delendbutton(count):
	mute()
	me.setGlobalVariable("finished","0")
	for cardn in table:
		if cardn.name == "endbutton" and cardn.controller == me:
			cardn.delete()
	if count == 1:remoteCall(players[1], "delendbutton", [2])

def checkcardmodel(model,controller = me):
	mute()
	for card in table:
		if controller == "" and card.model == model:return True
		if controller != "" and card.controller == controller and card.model == model:return True


def endphase(group, x=0, y=0):
	mute()
	me.setGlobalVariable("finished","1")
	for cardn in table:
		if cardn.name == "endbutton" and cardn.controller == me:
			cardn.delete()
	if getGlobalVariable("reavelplot") == "2":
		if fplay(1) != me:
			resetperturn()
			remoteCall(players[1], "resetperturn", [])
			setGlobalVariable("reavelplot","0")
			notify("plotend")
			delendbutton(1)
			#drawphasestart(1)
			remoteCall(fplay(1), "drawphasestart", [1])
		else:
			c = 0
			for cardn in table:
				if cardn.name == "endbutton" and cardn.controller != me:
					c = 1
			if c == 0:remoteCall(players[1], "dominancephaseend", [table])
		return
	if getGlobalVariable("drawphase") == "2":
		if fplay(1) != me:
			resetperturn()
			remoteCall(players[1], "resetperturn", [])
			setGlobalVariable("reavelplot","0")
			notify("drawend")
			delendbutton(1)
			#marshalphasestart(1)
			remoteCall(fplay(1), "marshalphasestart", [1])
		else:
			c = 0
			for cardn in table:
				if cardn.name == "endbutton" and cardn.controller != me:
					c = 1
			if c == 0:remoteCall(players[1], "dominancephaseend", [table])
		return
	if getGlobalVariable("dominancephase") == "1":
		# debug(getGlobalVariable("dominancephase"))
		# setGlobalVariable("dominancephase","2")
		if fplay(1) != me:
			resetperturn()
			remoteCall(players[1], "resetperturn", [])
			setGlobalVariable("dominancephase","0")
			notify("dominanceend")
			delendbutton(1)
			#standingphasestart(1)
			remoteCall(fplay(1), "standingphasestart", [1])
		else:
			c = 0
			for cardn in table:
				if cardn.name == "endbutton" and cardn.controller != me:
					c = 1
			if c == 0:remoteCall(players[1], "dominancephaseend", [table])
		return
	# if getGlobalVariable("dominancephase") == "2":
	# 	debug(getGlobalVariable("dominancephase"))
	# 	resetperturn()
	# 	setGlobalVariable("dominancephase","0")
	# 	notify("dominanceend")
	# 	#standingphasestart(1)
	# 	test(table)
	# 	return
	if getGlobalVariable("standingphase") == "1":
		if fplay(1) != me:
			resetperturn()
			remoteCall(players[1], "resetperturn", [])
			setGlobalVariable("standingphase","0")
			notify("standingend")
			delendbutton(1)
			#taxationphasestart(1)
			remoteCall(fplay(1), "taxationphasestart", [1])
		else:
			c = 0
			for cardn in table:
				if cardn.name == "endbutton" and cardn.controller != me:
					c = 1
			if c == 0:remoteCall(players[1], "dominancephaseend", [table])
		return
	# if getGlobalVariable("standingphase") == "2":
	# 	resetperturn()
	# 	setGlobalVariable("standingphase","0")
	# 	notify("standingend")
	# 	taxationphasestart(1)
	# 	return
	if getGlobalVariable("marshalphase") == "1":
		if fplay(1) != me:
			resetperturn()
			remoteCall(players[1], "resetperturn", [])
			setGlobalVariable("marshalphase","0")
			for card in table:
				if card.highlight == showColor:card.highlight = None
				if card.highlight == activcolor:card.highlight = None
			notify("marshalend")
			delendbutton(1)
			#challengephasestart(1)
			remoteCall(fplay(1), "challengephasestart", [1])
		else:
			c = 0
			for cardn in table:
				if cardn.name == "endbutton" and cardn.controller != me:
					c = 1
			if c == 0:remoteCall(players[1], "dominancephaseend", [table])
		return
	# if getGlobalVariable("marshalphase") == "2":
	# 	resetperturn()
	# 	setGlobalVariable("marshalphase","0")
	# 	for card in table:
	# 		if card.highlight == PowerColor:card.highlight = None
	# 	notify("marshalend")
	# 	challengephasestart(1)
	# 	return
	if getGlobalVariable("taxationphase") == "1":
		if fplay(1) != me:
			resetperturn()
			remoteCall(players[1], "resetperturn", [])
			setGlobalVariable("taxationphase","0")
			notify("taxationend")
			delendbutton(1)
			#startnextphase(1)
			remoteCall(fplay(1), "startnextphase", [1])
		else:
			c = 0
			for cardn in table:
				if cardn.name == "endbutton" and cardn.controller != me:
					c = 1
			if c == 0:remoteCall(players[1], "dominancephaseend", [table])
		return
	# if getGlobalVariable("taxationphase") == "2":
	# 	resetperturn()
	# 	setGlobalVariable("taxationphase","0")
	# 	notify("taxationend")
	# 	startnextphase(1)
	# 	return
	if getGlobalVariable("challengephase") == "2":
		if fplay(1) != me:
			resetperturn()
			remoteCall(players[1], "resetperturn", [])
			setGlobalVariable("challengephase","0")
			setGlobalVariable("activeplayer","")
			setGlobalVariable("ambush", "0")
			for card in table:
				if card.highlight in (MilitaryColor,IntrigueColor,PowerColor):card.highlight = None
				if card.highlight == activcolor:card.highlight = None
			notify("challengephaseend")
			delendbutton(1)
			#dominancephasestart(1)
			remoteCall(fplay(1), "dominancephasestart", [1])
		else:
			c = 0
			for cardn in table:
				if cardn.name == "endbutton" and cardn.controller != me:
					c = 1
			if c == 0:remoteCall(players[1], "dominancephaseend", [table])
		return
	# if getGlobalVariable("challengephase") == "3":
	# 	resetperturn()
	# 	setGlobalVariable("challengephase","0")
	# 	setGlobalVariable("activeplayer","")
	# 	for card in table:
	# 		if card.highlight == PowerColor:card.highlight = None
	# 	notify("challengephaseend")
	# 	dominancephasestart(1)
	# 	return


def challenge(group, x=0, y=0):
	mute()
	global winplayer
	global attacker
	global defender
	global unopposed
	if getGlobalVariable("automode") == "1":
		if attacker == []:
			notify("Please announce a attacker.")
			return
		if defender == []:
			notify("Please announce a defender.")
			return
		choice = challengetype
	else:
		choiceList = ['Military', 'Intrigue', 'Power']
		choice = askChoice("To which challenge do you want to calculate? ", choiceList)
	for person in players:
		person.counters['Str'].value = 0
		ignorestr = eval(getGlobalVariable("ignorestr"))
		personCards = (card for card in table
						if card.controller == person and card._id not in ignorestr)
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
	winplayer = []
	#challengetype = choice
	if getGlobalVariable("automode") == "1":
		if getGlobalVariable("numplayer") == "2":
		#if otherplayer != []
			if players[0].counters['Str'].value == players[1].counters['Str'].value:
				if players[0] == attacker:
					notify("attacker {} wins this challenge.".format(players[0]))
					winplayer = attacker
					if players[1].counters['Str'].value == 0:unopposed = 1
				else:
					notify("attacker {} wins this challenge.".format(players[1]))
					winplayer = players[1]
					if players[0].counters['Str'].value == 0:unopposed = 1
			elif players[0].counters['Str'].value > players[1].counters['Str'].value:
				if players[0] == attacker:
					notify("attacker {} wins this challenge.".format(players[0]))
					winplayer = players[0]
					if players[1].counters['Str'].value == 0:unopposed = 1
				else:
					notify("defender {} wins this challenge.".format(players[0]))
					winplayer = players[0]
			else:
				if players[0] == attacker:
					notify("defender {} wins this challenge.".format(players[1]))
					winplayer = players[1]
				else:
					notify("attacker {} wins this challenge.".format(players[1]))
					winplayer = players[1]
					if players[0].counters['Str'].value == 0:unopposed = 1
			remoteCall(otherplayer, "getwinner", [winplayer,unopposed,challengetype])
			if challengetype == 2 and getGlobalVariable("winint") == "1":winplayer.setGlobalVariable("intwin", "1")
			setGlobalVariable("mainstep", "5")
			aftercalculatestand = eval(getGlobalVariable("aftercalculatestand"))
			aftercalculatedraw = eval(getGlobalVariable("aftercalculatedraw"))
			debug(aftercalculatedraw)
			for kcard in table:
				if kcard.controller == winplayer and kcard._id in aftercalculatestand and kcard.orientation == 0:
					remoteCall(winplayer, "kneel", [kcard])
					notify("{} stand {} by [Ours is the Fury].".format(winplayer,kcard))
				if kcard.controller == winplayer and kcard._id in aftercalculatedraw and len(winplayer.deck) > 0:
					remoteCall(winplayer, "draw", [winplayer.deck])
					notify("{} draw 1 card by [For the North].".format(winplayer))
			if fplay(1) == me:checkaftercalculatereacioncardforce(1)
			else:remoteCall(otherplayer, "checkaftercalculatereacioncardforce", [1])
		else:
			notify("Only supported for Joust format.")
	# global Heartsbaneused
	# for card in table:
	# 	if card.model == "4c8a114e-106c-4460-846b-28f73914fc11" and Heartsbaneused == 1:#just for Heartsbane
	# 		attach = card.name+str(card.position)
	# 		for cards in table:
	# 			f = cards.name+str(cards.position)
	# 			if f == attachmodify[attach]:
	# 				cards.markers[STR_Up] -=3
	# 				Heartsbaneused = 0

def balancechallenge(challenge,winplayer,checkcount):
	mute()
	if checkcount == 1:
		f = (card for card in table  
			if card.name == "1st Player Token")
		for card in f:
			if card.controller == me:
				notify("waiting for fp balance the challenge")  
				if confirm("Continue to balance the challenge?"): remoteCall(otherplayer, "balancechallenge", [challenge,winplayer,2])
				else:
					notify("fp want to action") 
					return
			else:
				remoteCall(otherplayer, "balancechallenge", [challenge,winplayer,1])
	if checkcount == 2:
		notify("waiting for 2ndplayer balance the challenge")
		if confirm("Continue to balance the challenge?"):
			notify("all players checkok")
			debug(winplayer)
			balancechallengefinish(challenge,winplayer)
		else:
			notify("2ndplayer want to action") 
			return

def getotherplayer(player):
	global otherplayer
	otherplayer = player

def getwinner(winner,uo,ct):
	global winplayer
	global unopposed
	global challengetype
	winplayer = winner
	unopposed = uo
	challengetype = ct

def getattacker(attackerother,ct):
	global attacker
	global challengetype
	attacker = attackerother
	challengetype = ct

def getdefender(defenderother):
	global defender
	defender = defenderother

def challengecheck(group, x=0, y=0):
	mute()
	if getGlobalVariable("automode") == "1": 
		if winplayer != []:
			balancechallenge(challengetype,winplayer,1)
		else:
			notify("No challenge happened.")
	else:
		notify("Just for automode.")

def challengeclaim(group):
	claimcount = 0
	if attacker != []:
		plotlist = [card for card in table
			if card.controller == attacker and card.type == "Plot"]
	plotlist.reverse()
	for card in plotlist:
		claimcount = int(card.PlotClaim)
		break
	plotlist.reverse()
	return claimcount

def balancechallengefinish(challenge,winplay):
	mute()
	claim = challengeclaim(table)
	notify("claim is {}.".format(claim))
	if winplayer != defender:
		setGlobalVariable("mainstep", "6")
		if unopposed != 0:
			notify("{} add 1 pow from unopposed.".format(winplay))
			if winplay == me:
				addhousepow(1)
			else:
				remoteCall(otherplayer, "addhousepow", 1)
		if claim != 0:
			setGlobalVariable("mainstep", "7")
			if challenge == 1:
				if winplay != me:
					if getGlobalVariable("automode") != "1":
						Militarychallenge(claim)
					else:
						intomil(table)
				else:
					if getGlobalVariable("automode") != "1":
						remoteCall(otherplayer, "Militarychallenge", claim)
					else:
						remoteCall(otherplayer, "intomil", [table])
			if challenge == 2:
				for count in range(0,claim):
					if winplay != me:
						randomDiscard(me.hand)
					else:
						remoteCall(otherplayer, "randomDiscard", [otherplayer.hand])
				remoteCall(winplayer, "keyword", [1])
			if challenge == 3:
				if winplay == me:
					if checkhousepow(otherplayer) >= claim:
						remoteCall(otherplayer, "subhousepow", claim)
						addhousepow(claim)
					else:
						remoteCall(otherplayer, "subhousepow", otherplayer.counters['Power'].value)
						addhousepow(otherplayer.counters['Power'].value)
				else:
					if me.counters['Power'].value >= claim:
						subhousepow(claim)
						remoteCall(otherplayer, "addhousepow", claim)
					else:
						subhousepow(me.counters['Power'].value)
						remoteCall(otherplayer, "addhousepow", me.counters['Power'].value)
				remoteCall(winplayer, "keyword", [1])
		else:remoteCall(winplayer, "keyword", [1])
	else:
		remoteCall(winplayer, "keyword", [1])

def intomil(group):
	mute()
	global sessionpass
	list = []
	claim = challengeclaim(table)
	for card in table:
		if card.type == "Character" and card.controller == me and card.filter != WaitColor:
			list.append(card)
		c = len(list)
		if c < claim:
			b = c
		else:
			b = claim
	targetTuple = ([card._id for card in table if card.type == "Character" and card.controller == me and card.filter != WaitColor], me._id) 
	setGlobalVariable("tableTargets", str(targetTuple))
	setGlobalVariable("selectmode", "1")
	if me.isInverted:table.create("584a37d7-5a30-4018-ae21-0ad325203fa0",-375,-250)
	else:table.create("584a37d7-5a30-4018-ae21-0ad325203fa0",-375,200)
	sessionpass = "milkillplayerselect"
	whisper("Please select {} players to be killed".format(b))
	whisper("**selectmode**")

def challengebalanceover(count):
	mute()
	global winplayer
	global attacker
	global defender
	global unopposed
	global challengetype
	global savetarget
	global inserttarget
	global interruptcancelcard
	global interruptcancelplayer
	global interruptcanceledcard
	global interruptcancellastcard
	global interruptlib
	global interruptcancelok
	global saveactionplayer
	global interruptpass
	global cardkilllist
	global abilityattach
	global leavecardtype
	global leavetablecard
	global reactionattach
	global reactioncardlimit
	global keywordattach

	savetarget = []
	inserttarget = []
	interruptpass = 0
	interruptcancelplayer = []
	saveactionplayer = []
	interruptcancelcard = []
	interruptcancellastcard = []
	interruptcanceledcard = []
	interruptcancelok = 1
	interruptlib = {}
	cardkilllist = []
	abilityattach = {}
	leavecardtype = []
	leavetablecard = []
	if getGlobalVariable("mainstep") == "78":
		for card in table:
			card.highlight = None
			card.target(False)
		winplayer = []
		attacker = []
		defender = []
		unopposed = 0
		challengetype = 0
		reactionattach = {}
		reactioncardlimit = {}
		keywordattach = []
	if count == 1:
		remoteCall(otherplayer, "challengebalanceover", [2])
		return
	if getGlobalVariable("aftcuevent") != "-1":
		aftcuevent = getGlobalVariable("aftcuevent")
		debug(getGlobalVariable("aftcuevent"))
		setGlobalVariable("aftcuevent", "-1")
		notify("balance over")
		if int(aftcuevent) == me._id:
			remoteCall(otherplayer, "reaction", ["aftercalculate",1])
		else:reaction("aftercalculate",1)
		return
	if getGlobalVariable("chaevent") != "-1":
		chaevent = getGlobalVariable("chaevent")
		debug(getGlobalVariable("chaevent"))
		setGlobalVariable("chaevent", "-1")
		notify("balance over")
		if int(chaevent) == me._id:
			remoteCall(otherplayer, "action", ["challenge",1])
		else:action("challenge",1)
		return
	setGlobalVariable("mainstep", "0")
	notify("challenge balance over")
	challengeaction(1)

def challengephasestart(count):
	mute()
	setGlobalVariable("ambush", "1")
	me.setGlobalVariable("finished","0")
	me.setGlobalVariable("active","0")
	if me.isInverted:table.create("2d4834e4-bd76-4e8d-9e5a-638cd25e6107",-375,-250)
	else:table.create("2d4834e4-bd76-4e8d-9e5a-638cd25e6107",-375,200)
	#if count == 1:remoteCall(players[1], "challengephasestart", [2])

def challengenext():
	mute()
	me.setGlobalVariable("finished","1")
	for cardn in table:
		if cardn.name == "challengenextbutton" and cardn.controller == me:
			cardn.delete()
	if getGlobalVariable("challengephase") == "0":
		if me.getGlobalVariable("finished") == players[1].getGlobalVariable("finished") == "1":
			setGlobalVariable("challengephase", "1")
			setGlobalVariable("activeplayer",str(fplay(1)._id))
			fplay(1).setGlobalVariable("active","1")
			if fplay(1) == me:challengeAnnounce(table)
			else:remoteCall(players[1], "challengeAnnounce", [table])
		else:
			c = 0
			for cardn in table:
				if cardn.name == "challengenextbutton" and cardn.controller != me:
					c = 1
			if c == 0:remoteCall(players[1], "challengephasestart", [3])
		return


def challengeAnnounce(group, x=0, y=0):
	mute()
	me.setGlobalVariable("active","1")
	activefaction()
	if me.isInverted:table.create("bb79eb8b-2593-4b1f-a62d-c0e86b6aaf14",-240,-175)
	else:table.create("bb79eb8b-2593-4b1f-a62d-c0e86b6aaf14",-240,125)
	if me.isInverted:table.create("ce281a89-276d-4a1c-b542-91680776b1d4",-240,-215)
	else:table.create("ce281a89-276d-4a1c-b542-91680776b1d4",-240,85)
	if me.isInverted:table.create("db7fc2af-6201-4112-9512-e78f10f5cd14",-280,-195)
	else:table.create("db7fc2af-6201-4112-9512-e78f10f5cd14",-280,105)
	if me.isInverted:table.create("6d6562bf-3f80-4964-b342-9c3f48e3be06",-320,-215)
	else:table.create("6d6562bf-3f80-4964-b342-9c3f48e3be06",-320,125)

def challengedeficon(ctype):
	mute()
	if ctype == "mil":
		if me.isInverted:table.create("a576df8f-7ff2-4b79-bb7d-8fa54d47ccf8",-280,-195)
		else:table.create("a576df8f-7ff2-4b79-bb7d-8fa54d47ccf8",-280,105)
	if ctype == "int":
		if me.isInverted:table.create("6ebd872e-b372-4973-b793-cd4d84d31476",-280,-195)
		else:table.create("6ebd872e-b372-4973-b793-cd4d84d31476",-280,105)
	if ctype == "pow":
		if me.isInverted:table.create("9944aa40-0680-4f77-a668-80b5585af2df",-280,-195)
		else:table.create("9944aa40-0680-4f77-a668-80b5585af2df",-280,105)
	if me.isInverted:table.create("0952de65-f260-49d1-a8aa-184a6ff7251b",-320,-215)
	else:table.create("0952de65-f260-49d1-a8aa-184a6ff7251b",-320,125)


def challengeAnnounceold(group, x=0, y=0):
	mute()
	cc = 0
	ccc = 1
	cccc = 0
	global sessionpass
	if attacker ==[]:
		if getGlobalVariable("automode") != "1":
			choiceList = ['Military', 'Intrigue', 'Power', 'No challenge and Pass']
			colorList = ['#ae0603' ,'#006b34','#1a4d8f','#D8D8D8']
			choice = askChoice("Which challenge do you want to initiate?", choiceList,colorList)
		else:
			choiceList = []
			colorList = []
			if getGlobalVariable("winint") == "1" and me.getGlobalVariable("intwin") != "1":
				ccc = 0
				whisper("you cannot initiate a [MIL] or [POW] challenge unless won an [INT] challenge this phase.")#AGameofThrones
			if me.getGlobalVariable("limitchallenge") != "0":
				if int(me.getGlobalVariable("milcount")) == int(me.getGlobalVariable("limitchallenge")) or int(me.getGlobalVariable("intcount")) == int(me.getGlobalVariable("limitchallenge")) or int(me.getGlobalVariable("powcount")) == int(me.getGlobalVariable("limitchallenge")):
					ccc = 0
					whisper("you cannot challenge this phase.")#SneakAttack
			for card in table:
				if card.model == "09903f79-6155-4a63-9b52-e10fb2e69898" and card.controller == me:
					cccc = 1
					break
			if int(me.getGlobalVariable("milcount")) < (int(me.getGlobalVariable("milcountmax")) + cccc) and ccc == 1:
				for card in table: 
					if card.type == "Character" and card.controller == me and card.isFaceUp and checkchallengeicon(card,"milicon") and card.orientation == 0:
						choiceList.append('Military')
						colorList.append('#ae0603')
						cc = 1
						break
			if int(me.getGlobalVariable("intcount")) < int(me.getGlobalVariable("intcountmax")):
				for card in table: 
					if card.type == "Character" and card.controller == me and card.isFaceUp and checkchallengeicon(card,"inticon") and card.orientation == 0:
						choiceList.append('Intrigue')
						colorList.append('#006b34')
						cc = 1
						break
			if int(me.getGlobalVariable("powcount")) < int(me.getGlobalVariable("powcountmax")) and ccc == 1:
				for card in table: 
					if card.type == "Character" and card.controller == me and card.isFaceUp and checkchallengeicon(card,"powicon") and card.orientation == 0:
						choiceList.append('Power')
						colorList.append('#1a4d8f')
						cc = 1
						break
			if cc == 1:
				choiceList.append('No challenge and Pass')
				colorList.append('#D8D8D8')
				choice = askChoice("Which challenge do you want to initiate?", choiceList,colorList)
			else:
				return
				# if getGlobalVariable("challengephase") == "1":
				# 	setGlobalVariable("challengephase","2")
				# 	notify("{} has been active player".format(players[1]))
				# 	remoteCall(players[1], "challengeAnnounce", table)
				# 	return
				# if getGlobalVariable("challengephase") == "2":
				# 	setGlobalVariable("challengephase","0")
				# 	remoteCall(players[1], "dominance", table)
				# 	return
		if getGlobalVariable("automode") != "1":
			if choice == 1:announceMil(table)
			if choice == 2:announceInt(table)
			if choice == 3:announcePow(table)
			if choice == 4:notify("{} has no challenge to initiate.".format(me))
			if choice == 0:return
		else:
			if choiceList[choice-1] == 'Military':
				targetTuple = ([card._id for card in table if card.type == "Character" and card.controller == me and card.isFaceUp and checkchallengeicon(card,"milicon") and card.orientation == 0], me._id) 
				setGlobalVariable("tableTargets", str(targetTuple))
				setGlobalVariable("selectmode", "2")
				if me.isInverted:table.create("584a37d7-5a30-4018-ae21-0ad325203fa0",-375,-250)
				else:table.create("584a37d7-5a30-4018-ae21-0ad325203fa0",-375,200)
				sessionpass = "milselect"
				notify("**{} into selectmode**".format(me))
			elif choiceList[choice-1] == 'Intrigue':
				targetTuple = ([card._id for card in table if card.type == "Character" and card.controller == me and card.isFaceUp and checkchallengeicon(card,"inticon") and card.orientation == 0], me._id) 
				setGlobalVariable("tableTargets", str(targetTuple))
				setGlobalVariable("selectmode", "1")
				if me.isInverted:table.create("584a37d7-5a30-4018-ae21-0ad325203fa0",-375,-250)
				else:table.create("584a37d7-5a30-4018-ae21-0ad325203fa0",-375,200)
				sessionpass = "intselect"
				notify("**{} into selectmode**".format(me))
			elif choiceList[choice-1] == 'Power':
				targetTuple = ([card._id for card in table if card.type == "Character" and card.controller == me and card.isFaceUp and checkchallengeicon(card,"powicon") and card.orientation == 0], me._id) 
				setGlobalVariable("tableTargets", str(targetTuple))
				setGlobalVariable("selectmode", "1")
				if me.isInverted:table.create("584a37d7-5a30-4018-ae21-0ad325203fa0",-375,-250)
				else:table.create("584a37d7-5a30-4018-ae21-0ad325203fa0",-375,200)
				sessionpass = "powselect"
				notify("**{} into selectmode**".format(me))
			elif choiceList[choice-1] == 'No challenge and Pass':
				notify("{} has no challenge to initiate.".format(me))
				# if getGlobalVariable("challengephase") == "1":
				# 	setGlobalVariable("challengephase","2")
				# 	setGlobalVariable("activeplayer",str(players[1]._id))
				# 	players[1].setGlobalVariable("active","1")
				# 	notify("{} has been active player".format(players[1]))
				# 	remoteCall(players[1], "challengeAnnounce", table)
				# 	return
				# if getGlobalVariable("challengephase") == "2":
				# 	setGlobalVariable("challengephase","0")
				# 	remoteCall(players[1], "dominance", table)
				# 	return
			else:
				notify("{} has no challenge to initiate.".format(me))
				# if getGlobalVariable("challengephase") == "1":
				# 	setGlobalVariable("challengephase","2")
				# 	setGlobalVariable("activeplayer",str(players[1]._id))
				# 	players[1].setGlobalVariable("active","1")
				# 	notify("{} has been active player".format(players[1]))
				# 	remoteCall(players[1], "challengeAnnounce", table)
				# 	return
				# if me.getGlobalVariable("active") == players[1].getGlobalVariable("active") == "1":
				# 	setGlobalVariable("challengephase","0")
				# 	remoteCall(players[1], "dominance", table)
				# 	return
	else:
		notify("challenge already happened.")

def selectchallenge(ctype):
	mute()
	if ctype in("mil","int","pow"):
		for card in table:
			if card.highlight != Stealthcolor:card.highlight = None
			card.target(False)
	if ctype == "mil":
		remoteCall(players[1], "deletecicon", [])
		targetTuple = [card._id for card in table if card.type == "Character" and card.controller == me and card.isFaceUp and card.orientation == 0]
		selectcardnext(targetTuple,"milselect",table,[],me,1,99)
	if ctype == "int":
		remoteCall(players[1], "deletecicon", [])
		targetTuple = [card._id for card in table if card.type == "Character" and card.controller == me and card.isFaceUp and card.orientation == 0]
		selectcardnext(targetTuple,"intselect",table,[],me,1,99)
	if ctype == "pow":
		remoteCall(players[1], "deletecicon", [])
		targetTuple = [card._id for card in table if card.type == "Character" and card.controller == me and card.isFaceUp and card.orientation == 0]
		selectcardnext(targetTuple,"powselect",table,[],me,1,99)
	if ctype == "defmil":
		targetTuple = [card._id for card in table if card.type == "Character" and card.controller == me and card.isFaceUp and card.highlight != Stealthcolor and card.orientation == 0]
		selectcardnext(targetTuple,"mildefselect",table,[],me,1,99)
	if ctype == "defint":
		targetTuple = [card._id for card in table if card.type == "Character" and card.controller == me and card.isFaceUp and card.highlight != Stealthcolor and card.orientation == 0]
		selectcardnext(targetTuple,"intdefselect",table,[],me,1,99)
	if ctype == "defpow":
		targetTuple = [card._id for card in table if card.type == "Character" and card.controller == me and card.isFaceUp and card.highlight != Stealthcolor and card.orientation == 0]
		selectcardnext(targetTuple,"powdefselect",table,[],me,1,99)
	if ctype == "end":
		for cardn in table:
			if cardn.name in ("AttackMil","AttackInt","AttackPow","AttackNon") and cardn.controller == me:
				cardn.delete()
		remoteCall(players[1], "deletecicon", [])
		if getGlobalVariable("challengephase") == "1":
			setGlobalVariable("challengephase","2")
			setGlobalVariable("activeplayer",str(players[1]._id))
			notify("{} has been active player".format(players[1]))
			remoteCall(players[1], "challengeAnnounce", [table])
			return
		if me.getGlobalVariable("active") == players[1].getGlobalVariable("active") == "1":
			for card in table:
				card.highlight = None
				card.target(False)
			if fplay(1) == me:challengephaseend(table)
			else:remoteCall(players[1], "challengephaseend", [table])
			return
	if ctype == "nodef":
		notify("{} declares no defenders.".format(me))

def deletecicon():
	mute()
	for cardn in table:
		if cardn.name in ("DefendMil","DefendInt","DefendPow","DefendNon"):
			cardn.delete()


def challengephaseend(group, x=0, y=0):
	mute()
	me.setGlobalVariable("finished","0")
	if me.isInverted:table.create("cb48782b-3bdd-4024-af85-fb0eb65a8f51",-320,-215)
	else:table.create("cb48782b-3bdd-4024-af85-fb0eb65a8f51",-320,125)

def Militarychallenge(claim = 0):
	mute()
	c = 0
	list = []
	list2 = []
	discard = 0
	cards = []
	global selectedcard
	global sessionpass
	if sessionpass != "milkillplayerselectok":
		if claim == 0:return
		#cardlist = [card for card in table
			#if card.type == "Character" and card.controller == me and card.unique == "Yes"]
		#cardlist.reverse()
		for card in table:
			if card.type == "Character" and card.controller == me and card.filter != WaitColor:
				list.append(card)
		if len(list) > 0:
			dlg = cardDlg(list)
			dlg.title = "These cards are in your table:"
			dlg.text = "Declares at least 1 character to be killed.(total is {})".format(claim)
			if len(list) < claim:
				dlg.min = len(list)
				dlg.max = len(list)
			else:
				dlg.max = claim
				dlg.min = claim
			cards = dlg.show()
		if cards == []:return
	else:
		if claim == 0:
			remoteCall(winplayer, "keyword", [1])
			sessionpass = ""
			selectedcard = []
			return
		else:
			cards = selectedcard
	if cards != None and cards != []:
		for card in cards:
			card.highlight = miljudgecolor
			list2.append(card)
		if len(list2) > 0:
			miljudgementfinish(list2,claim)
			remoteCall(otherplayer, "miljudgementfinish", [list2,claim])
			sessionpass = ""
			selectedcard = []
			f = (card for card in table  
				if card.name == "1st Player Token")
			for card1 in f:
				if card1.controller == me:
					interruptevent("miljudgementfp",1)
					#setTimer(me,"miljudgementfp",table)
					#miljudgement(table,card,1,claim)
				else:
					debug("2")
					#remoteCall(otherplayer, "miljudgement", ["table",card,1,claim])
					#remoteCall(otherplayer, "setTimer", [otherplayer,"miljudgementfp",table])
					remoteCall(otherplayer, "interruptevent", ["miljudgementfp",1])
			notify("waiting for fp action")
			return
	else:
		Militarychallenge(claim)
		return
	if discard != claim and c == 0:
		Militarychallenge(claim-discard)
	if discard == claim:
		remoteCall(winplayer, "keyword", [1])
	#cardlist.reverse()

def intointerruptevent(count):
	mute()
	global sessionpass
	global smcount
	sessionpass = ""
	targetTuple = ([card._id for card in mjfinishcard if card.highlight == miljudgecolor], me._id) 
	setGlobalVariable("tableTargets", str(targetTuple))
	setGlobalVariable("selectmode", "1")
	if me.isInverted:table.create("584a37d7-5a30-4018-ae21-0ad325203fa0",-375,-250)
	else:table.create("584a37d7-5a30-4018-ae21-0ad325203fa0",-375,200)
	sessionpass = "miljudgementselect"
	notify("**{} into selectmode**".format(me))
	smcount = count

def miljudgementfinish(mfcard,claim):
	mute()
	global mjfinish
	global mjfinishcard
	global claimtmp
	mjfinish = 1
	mjfinishcard = mfcard
	claimtmp = claim

def miljudgementfinished(mfcard,claim,count):
	mute()
	global cardkilllist
	for card in mfcard:
		if card.controller == me:
			if card.highlight == miljudgecolor:
				cardkilllist.append(card)
				#card.moveTo(me.piles['Dead pile'])
				#notify("{} killed {}.".format(me,card))
			else:
				notify("{} saved {}.".format(me,card))
	if len(cardkilllist) > 0:remoteCall(otherplayer, "getcardkilllist", [cardkilllist])
	if count == 1:
		remoteCall(otherplayer, "miljudgementfinished", [mfcard,claim,2])
	else:
		if len(cardkilllist) > 0:
			remoteCall(otherplayer, "characterkilled", [cardkilllist,1])
		else:
			remoteCall(winplayer, "keyword", [1])

def getcardkilllist(listkill):
	global cardkilllist
	cardkilllist = listkill


def revealplot(group, x = 0, y = 0):
	mute()
	global usedplot
	plot = 0
	me.piles['Plot Deck'].addViewer(me)
	if len(me.piles['Plot Deck']) == 0:return
	dlg=cardDlg([c for c in me.piles['Plot Deck']])
	dlg.title = "These cards are in your unused-plot pile:"
	dlg.text = "Select a plot card to reveal."
	cards = dlg.show()
	if cards != None:
		#reset
		setGlobalVariable("challengeplayer","0")
		me.setGlobalVariable("cantuseevent", "0")
		me.setGlobalVariable("cantuselocation", "0")
		me.setGlobalVariable("cantuseattach", "0")
		setGlobalVariable("Kingdomgold0","0")
		setGlobalVariable("Edictgold0","0")
		setGlobalVariable("winint","0")
		me.setGlobalVariable("intwin", "0")
		me.setGlobalVariable("submilclaim", "0")
		me.setGlobalVariable("subintclaim", "0")
		me.setGlobalVariable("subpowclaim", "0")
		me.setGlobalVariable("limitchallenge", "0")
		setGlobalVariable("plotdisc","0")
		setGlobalVariable("plotkill","0")
		setGlobalVariable("firstreveal", "")
		if getGlobalVariable("noprint") == "1":
			for ncard in table:
				if ncard.type == "Character" and ncard.controller ==me:
					restoreprintcard(ncard)
				if ncard.type == "Character" and ncard.controller !=me:
					remoteCall(players[1], "restoreprintcard", [ncard])

			setGlobalVariable("noprint","0")
		
		countxy = 5
		usedplot = []
		for c in table: 
			if c.Type == "Plot" and c.controller == me and c not in cards:
				c.markers[standIcon] = 0
				c.filter = "#0099ffff"
				x, y = c.position
				plot = 1
				usedplot.append(c)
				#if me.isInverted:c.moveToTable(x, y-30)
				#else:c.moveToTable(x, y+30)
		for card in cards:
			if plot == 0:
				if me.isInverted:card.moveToTable(-430,-75,True)
				else:card.moveToTable(-430,10,True)
			else:
				if me.isInverted:card.moveToTable(x-5, y-20,True)
				else:card.moveToTable(x-5, y+20,True)
			me.setGlobalVariable("turn","1")
			if getGlobalVariable("automode") == "0":
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
					remoteCall(me, "fp", table)
			if len(players) == 1:
				flipplotcard(card)
			else:
				card.peek()
	else:
		if getGlobalVariable("automode") == "1":revealplot(table)
		else:return
		
def decidefirstplayer(group, x = 0, y = 0):
	mute()
	if getGlobalVariable("firstplay") == "{}".format(me._id):  
		askfirstplayer(table)
	else: 
		remoteCall(players[1], "askfirstplayer", table)     


def askfirstplayer(group, x = 0, y = 0):
	mute()
	colorList = ['#1a4d8f','#ae0603']
	choiceList = ['{}'.format(me.name),'{}'.format(players[1].name)]
	choice = askChoice("Decide who is First player.", choiceList,colorList)
	if choice == 1:
		notify("**{} is firstplayer.**".format(me))
		setGlobalVariable("firstplay",str(me._id))
		f = (card for card in table  
			if card.name == "1st Player Token")
		for card in f:
			if card.controller == me:    
				moveFP(card,1)
			else:                        
				remoteCall(players[1], "moveFP", [card,1])
	elif choice == 2:
		notify("**{} is firstplayer.**".format(players[1]))
		setGlobalVariable("firstplay",str(players[1]._id))
		f = (card for card in table  
			if card.name == "1st Player Token")
		for card in f:
			if card.controller == me:   
				moveFP(card,1)
			else:                       
				remoteCall(players[1], "moveFP", [card,1])
	else:
		askfirstplayer(table)
		return
	#if getGlobalVariable("automode") == "1":askfirstreveal(table)

def askfirstreveal(group, x = 0, y = 0):
	mute()
	meplotcard = []
	otherplotcard = []
	colorList = []
	if fplay(1) == me:
		for card in table:
			if card.type == "Plot" and card.controller == me and card.filter == None and "When Revealed" in card.text:
				colorList.append("#1a4d8f")
				meplotcard = card
			if card.type == "Plot" and card.controller == players[1] and card.filter == None and "When Revealed" in card.text:
				colorList.append('#ae0603')
				otherplotcard = card
		if len(colorList) > 1:
			choiceList = ["{}'s {}".format(me,meplotcard.name),"{}'s {}".format(players[1],otherplotcard.name)]
			choice = askChoice("Decide who will First reveal.", choiceList,colorList)
			if choice == 1:
				notify("{} First reveal.".format(me))
				setGlobalVariable("reavelplot","1")
				setGlobalVariable("firstreveal", str(me._id))
				reavelplot(table)
			if choice == 2:
				notify("{} First reveal.".format(players[1]))
				setGlobalVariable("reavelplot","1")
				setGlobalVariable("firstreveal", str(players[1]._id))
				remoteCall(players[1], "reavelplot", table)
			if choice == 0:askfirstreveal(table)
		else:
			setGlobalVariable("reavelplot","1")
			if meplotcard != []:
				setGlobalVariable("firstreveal", str(me._id))
				remoteCall(me, "reavelplot", table)
			elif otherplotcard != []:
				setGlobalVariable("firstreveal", str(players[1]._id))
				remoteCall(players[1], "reavelplot", table)
			else:
				setGlobalVariable("firstreveal", str(me._id))
				setGlobalVariable("reavelplot","1")
				remoteCall(me, "reavelplot", table)
	else:remoteCall(players[1], "askfirstreveal", table)

def reavelplot(group, x = 0, y = 0):
	mute()
	getreserve(table)
	for card in table:
		if card.type == "Plot" and card.controller == me and card.filter == None:
			notify("use {}'s ability".format(card))
			plotability(card)
			return


def plotability(card):
	mute()
	global sessionpass
	global nextcardtmp
	global plotcard
	list10 = []
	listcount = 0
	searchok = 0
	drawcount = 0
	cards = None
	for d in plotdict:
		if card.model == plotdict[d][1] and card.controller == me:
			if plotdict[d][2] == "manual":
				manualprocess(card,"plotability")
				return
			if plotdict[d][2] == "winint":
				setGlobalVariable("winint","1")
				notify("{} reaveled {}, A player cannot initiate a [MIL] or [POW] challenge unless he or she has won an [INT] challenge that phase.".format(me,card))#AGameofThrones
			if plotdict[d][2] == "firstll":
				me.setGlobalVariable("firstll", "1")
				notify("{} reaveled {}, Reduce the cost of the first Lord or Lady character {} marshal this round by 2.".format(me,card,me))#ANobleCause
			if plotdict[d][2] == "addmilcount":
				me.setGlobalVariable("milcountmax",str(int(me.getGlobalVariable("milcountmax"))+1))
				notify("{} reaveled {}, may initiate an additional [MIL] challenge during the challenges phase.".format(me,card,me))#AStormofSwords
			if plotdict[d][2] == "10searchatloc":
				if len(me.deck) < 10:listcount = len(me.deck)
				else:listcount = 10
				for c in me.deck.top(listcount):
					if c.Type in ("Attachment","Location"):
						searchok = 1
				dlg = cardDlg(me.deck.top(listcount))
				dlg.title = "These cards are in your deck:"
				dlg.text = "select 1 Location or Attachment card add it to your hand."
				dlg.min = 0
				dlg.max = 1
				cards = dlg.show()
				if cards != [] and cards != None:
					if cards[0].Type in ("Attachment","Location"):
						cardintable(cards[0],"Location")
						plotcard = cards[0]
						cards[0].highlight = showColor
						#cards[0].moveTo(me.hand)
						me.deck.shuffle()
						notify("{} reaveled {}, add {} to {} hand.".format(me,card,cards[0],me))#BuildingOrders
						remoteCall(me, "setTimer", [me,"plotshow",table])
						return
					else:
						if searchok == 1:
							if confirm("There is a Attachment or Location in these cards, select again？"):
								plotability(card)
								return
						else:notify("search failed")
				else:
					if searchok == 1:
						if confirm("There is a Attachment or Location in these cards, select again？"):
							plotability(card)
							return
					else:notify("search failed")
			if plotdict[d][2] == "1c1g":
				c = 0
				for e in table:
					if e.controller != me and e.type == "Character" and e.filter != WaitColor:c += 1
				plotlist = [pcard for pcard in table
						if pcard.controller == me and pcard.type == "Plot"]
				plotlist.reverse()
				for plotcard in plotlist:
					me.counters['Gold'].value += c
					plotcard.markers[Gold] += c
					break
				notify("{} reaveled {},  Gain {} gold.".format(me,card,c))#CallingtheBanners
			if plotdict[d][2] == "subclaim":
				choiceList = ['Military', 'Intrigue', 'Power']
				colorList = ['#ae0603' ,'#006b34','#1a4d8f']
				choice = askChoice("Which challenge do you want to name?", choiceList,colorList)
				if choice == 1:
					cardmarkers(card,"milicon",1)
					players[1].setGlobalVariable("submilclaim", str(int(players[1].getGlobalVariable("submilclaim"))+1))
				if choice == 2:
					cardmarkers(card,"inticon",1)
					players[1].setGlobalVariable("subintclaim", str(int(players[1].getGlobalVariable("subintclaim"))+1))
				if choice == 3:
					addPower(card)
					players[1].setGlobalVariable("subpowclaim", str(int(players[1].getGlobalVariable("subpowclaim"))+1))
				if choice == 0:
					plotability(card)
					return
				notify("{} reaveled {}, reduce the claim value on the attacker's revealed plot card by 1 during {} challenges.".format(me,card,choiceList[choice-1]))#CalmOverWesteros
			if plotdict[d][2] == "discattachment":
				if checkattachment(1) > 0:
					plotcard = card
					nextcardtmp = card
					selectlist = checkcardid(deck = table,cardtype = "Attachment")
					selectcardnext(selectlist,"Confiscationselect",table,card,"",1)
					return
				else:notify("There is no attachment card in table can't use {} 's ability".format(card))
			if plotdict[d][2] == "draw3":
				for count in range(0,3):
					if len(me.deck) > 0:
						draw(me.deck)
						drawcount += 1
				notify("{} reaveled {}, Draw {} cards.".format(me,card,drawcount))#CountingCoppers
			if plotdict[d][2] == "kneel":
				if checkstandplayer(table):
					plotcard = card
					nextcardtmp = card
					selectlist = checkcardid(deck = table,cardtype = "Character",stand = 0)
					selectcardnext(selectlist,"FilthyAccusationsselect",table,card,"",1)
					return
			if plotdict[d][2] == "discplayer":
				cards = players[1].hand.random()
				remoteCall(players[1], "HeadsonSpikes", [card,cards])
				return
			if plotdict[d][2] == "challenge1player":
				setGlobalVariable("challengeplayer","1")
				notify("{} reaveled {}, Each player cannot declare more than 1 character as an attacker or a defender in each challenge.".format(me,card))#JoustingContest
			if plotdict[d][2] == "cantuselia":
				me.setGlobalVariable("cantuseevent", "1")
				me.setGlobalVariable("cantuselocation", "1")
				me.setGlobalVariable("cantuseattach", "1")
				notify("{} reaveled {}, {} cannot marshal locations or attachments, or play events.".format(me,card,me))#MarchingOrders
			if plotdict[d][2] == "gold0":
				setGlobalVariable("Kingdomgold0","1")
				setGlobalVariable("Edictgold0","1")
				notify("{} reaveled {}, Treat the base gold value on each revealed Kingdom and each revealed Edict plot card as if it were 0.".format(me,card))#NavalSuperiority
			if plotdict[d][2] == "adddisc3":
				if len(me.piles['Discard pile']) > 0:
					for c in me.piles['Discard pile']:
						list10.append(c)
					dlg = cardDlg(list10)
					dlg.title = "These cards are in your deck:"
					dlg.text = "select Choose up to 3 cards shuffle them into your deck."
					dlg.min = 0
					dlg.max = 3
					cards = dlg.show()
					if cards != None:
						for dc in cards:
							dc.moveTo(me.deck)
						me.deck.shuffle()
						drawcount = len(cards)
				else:drawcount = 0
				notify("{} reaveled {}, choose {} cards shuffle them into {} deck..".format(me,card,drawcount,me))#Rebuilding
			if plotdict[d][2] == "1challenge":
				me.setGlobalVariable("limitchallenge", "1")
				notify("{} reaveled {}, {} cannot initiate more than 1 challenge in the challenges phase.".format(me,card,me))#SneakAttack
			if plotdict[d][2] == "10searchcha":
				if len(me.deck) < 10:listcount = len(me.deck)
				else:listcount = 10
				for c in me.deck.top(listcount):
					if c.Type in ("Character"):
						searchok = 1
				dlg = cardDlg(me.deck.top(listcount))
				dlg.title = "These cards are in your deck:"
				dlg.text = "select 1 Character card add it to your hand."
				dlg.min = 0
				dlg.max = 1
				cards = dlg.show()
				if cards != [] and cards != None:
					if cards[0].Type in ("Character"):
						cardintable(cards[0],"Character")
						plotcard = cards[0]
						cards[0].highlight = showColor
						#cards[0].moveTo(me.hand)
						me.deck.shuffle()
						notify("{} reaveled {}, add {} to {} hand.".format(me,card,cards[0],me))#Summons
						remoteCall(me, "setTimer", [me,"plotshow",table])
						return
					else:
						debug("1111")
						if searchok == 1:
							if confirm("There is a Character in these cards, select again？"):
								debug("3333")
								plotability(card)
								return
						else:notify("search failed")
				else:
					debug("222")
					if searchok == 1:
						if confirm("There is a Character in these cards, select again？"):
							plotability(card)
							return
					else:notify("search failed")
			if plotdict[d][2] == "search5c":
				choiceList = ['Hand','Discard pile']
				colorList = ['#ae0603' ,'#1a4d8f']
				choice = askChoice("Which deck do you want to select?", choiceList,colorList)
				if choice == 0:
					plotability(card)
					return
				if choice == 1:
					for c in me.hand:
						if c.type == "Character" and int(c.cost) <= 5:
							list10.append(c)
				if choice == 2:
					for c in me.piles['Discard pile']:
						if c.type == "Character" and int(c.cost) <= 5:
							list10.append(c)
				dlg = cardDlg(list10)
				dlg.title = "These cards are in your deck:"
				dlg.text = "select 1 Character card put it into play.do not select card to reselect."
				dlg.min = 0
				dlg.max = 1
				cards = dlg.show()
				if cards != [] and cards != None:
					if me.isInverted:cards[0].moveToTable(20,-100)			
					else:cards[0].moveToTable(-20,0)
					notify("{} reaveled {}, put {} to into play.".format(me,card,cards[0]))#Reinforcements
				elif cards == []:plotability(card)
			if plotdict[d][2] == "disc1player":
				notify("{} reaveled {}, Each player chooses a character he or she controls (if able), and discards it from play (cannot be saved).".format(me,card))#MarchedtotheWall
				if fplay(1) == me:plotdisccharacter("disc1",card)
				else:remoteCall(players[1], "plotdisccharacter", ["disc1",card])
				return
			if plotdict[d][2] == "kill3player":
				if fplay(1) == me:plotdisccharacter("kill1",card)
				else:remoteCall(players[1], "plotdisccharacter", ["kill1",card])
				return
			if plotdict[d][2] == "addstandicon":
				card.markers[standIcon] = 1
				notify("{} reaveled {}, Place a stand token on {}.".format(me,card,card))#PowerBehindtheThrone
			if plotdict[d][2] == "gain3gold":
				remoteCall(players[1], "addplotgold", table)
				remoteCall(players[1], "addplotgold", table)
				remoteCall(players[1], "addplotgold", table)
				notify("{} reaveled {}, {} gains 3 gold.".format(me,card,players[1]))#TradingwiththePentoshi
			if plotdict[d][2] == "search3maester":
				for c in me.deck:
					if "Maester" in c.traits:
						searchok = 1
				dlg = cardDlg(me.deck)
				dlg.title = "These cards are in your deck:"
				dlg.text = "select 1 Maester Character card add it to your hand."
				dlg.min = 0
				dlg.max = 1
				cards = dlg.show()
				if cards != [] and cards != None:
					if "Maester" in cards[0].traits:
						cardintable(cards[0],"Character")
						#cards[0].moveTo(me.hand)
						me.deck.shuffle()
						notify("{} reaveled {}, add {} to table.".format(me,card,cards[0]))#HeretoServe
					else:
						debug("1111")
						if searchok == 1:
							if confirm("There is a Maester Character in these cards, select again？"):
								debug("3333")
								plotability(card)
								return
						else:notify("search failed")
				else:
					debug("222")
					if searchok == 1:
						if confirm("There is a Character in these cards, select again？"):
							plotability(card)
							return
					else:notify("search failed")
			if plotdict[d][2] == "select2location":
				if fplay(1) == me:plotdisccharacter("disclocation1",card)
				else:remoteCall(players[1], "plotdisccharacter", ["disclocation1",card])
				return
			if plotdict[d][2] == "allnoprint":
				for ncard in table:
					if ncard.type == "Character" and ncard.controller ==me:
						noprintcard(ncard,3)
					if ncard.type == "Character" and ncard.controller !=me:
						remoteCall(players[1], "noprintcard", [ncard,3])
				setGlobalVariable("noprint","1")
				notify("{} reaveled {}, Treat each character's printed text box as if it were blank (except for Traits)".format(me,card))#FortifiedPosition
	if getGlobalVariable("reavelplot") == "1":
		setGlobalVariable("reavelplot","2")
		if str(me._id) == getGlobalVariable("firstreveal"):remoteCall(players[1], "reavelplot", table)
		else:reavelplot(table)
		return
	if getGlobalVariable("reavelplot") == "2":
		resetplot()
		remoteCall(players[1], "resetplot", [])
		if fplay(1) == me:actiongeneral(1)
		else:remoteCall(players[1], "actiongeneral", 1)
		return

def resetplot():
	mute()
	global usedplot
	if len(me.piles['Plot Deck']) == 0:
		for card in table:
			if card in usedplot:
				card.moveTo(me.piles['Plot Deck'])
		usedplot = []
		for card in table:
			if card.Type == "Plot" and card.controller == me:
				if me.isInverted:card.moveToTable(-430,-75,True)
				else:card.moveToTable(-430,10,True)

def addplotgold(group, x = 0, y = 0):
	mute()
	for card in table:
		if card.type == "Plot" and card.controller == me and card.filter == None:addGold(card)


def plotdisccharacter(typep,card):
	mute()
	global sessionpass
	global plotcard
	if typep == "disc1":
		plotcard = card
		if checkcharacter(me):
			selectlist = checkcardid(deck = table,cardtype = "Character",player = me)
			selectcardnext(selectlist,"plotdisccharacter1",table,card,"",1)
			setGlobalVariable("plotdisc","1")
		else:remoteCall(players[1], "plotdisccharacter", ["disc2",card])
	if typep == "disc2":
		plotcard = card
		if checkcharacter(me):
			selectlist = checkcardid(deck = table,cardtype = "Character",player = me)
			selectcardnext(selectlist,"plotdisccharacter2",table,card,"",1)
			setGlobalVariable("plotdisc","1")
		else:remoteCall(fplay(1), "callplotleave", [1])
	if typep == "kill1":
		setGlobalVariable("plotkill","1")
		plotcard = card
		if checkcharacter(me):
			selectlist = checkcardid(deck = table,cardtype = "Character",player = me)
			selectcardnext(selectlist,"plotkillcharacter1",table,card,"",1,mode = 3)
		else:remoteCall(players[1], "plotdisccharacter", ["kill2",card])
	if typep == "kill2":
		setGlobalVariable("plotkill","1")
		plotcard = card
		if checkcharacter(me):
			selectlist = checkcardid(deck = table,cardtype = "Character",player = me)
			selectcardnext(selectlist,"plotkillcharacter2",table,card,"",1,mode = 3)
		else:
			cardbekill = []
			for card in table:
				if card.highlight == miljudgecolor:cardbekill.append(card)
			remoteCall(fplay(1), "characterkilled", [cardbekill,1])
	if typep == "disclocation1":
		plotcard = card
		if checkcardstatus(cardtype = "Location",player = me):
			selectlist = checkcardid(deck = table,cardtype = "Location",player = me)
			selectcardnext(selectlist,"plotdisclocation1",table,[],"",1,2)
		else:remoteCall(players[1], "plotdisccharacter", ["disc2",card])
	if typep == "disclocation2":
		plotcard = card
		if checkcardstatus(cardtype = "Location",player = me):
			selectlist = checkcardid(deck = table,cardtype = "Location",player = me)
			selectcardnext(selectlist,"plotdisclocation2",table,[],"",1,2)
			
def disclocation(count):#PoliticalDisaster
	mute()
	for card in table:
		if card.filter == discfilter and card.type == "Location" and card.controller == me:
			disc(card)
	if count == 1:
		remoteCall(players[1], "disclocation", [2])
		return
	if getGlobalVariable("reavelplot") == "1":
		setGlobalVariable("reavelplot","2")
		if str(me._id) == getGlobalVariable("firstreveal"):remoteCall(players[1], "reavelplot", table)
		else:reavelplot(table)
		return
	if getGlobalVariable("reavelplot") == "2":
		resetplot()
		remoteCall(players[1], "resetplot", [])
		if fplay(1) == me:actiongeneral(1)
		else:remoteCall(players[1], "actiongeneral", 1)
		return

def plotleave(cardbekill,count):
	mute()
	global abilityattach
	debug(cardbekill)
	c = 0
	list = []
	for cardt in table:
		if cardt.type == "Attachment":
			list.append(cardt)
	debug(list)
	for card in cardbekill:
		whisper("{}".format(card))
		for d in cardkill:
			if card.model == cardkill[d][1] and card.controller == me and cardkill[d][2] != "link":
				if cardkill[d][4] == "Attachment":
					if len(list) > 0:
						if not abilityattach.has_key(card._id):
							abilityattach[card._id] = 1
						else:abilityattach[card._id] += 1
	debug(abilityattach)
	if count == 1:remoteCall(players[1], "callplotleave", [2])
	if count == 2:remoteCall(fplay(1), "interruptevent", ["characterkill",1])


def plotdisccard(count):
	mute()
	global selectedcard
	global sessionpass
	global nextcardtmp
	global plotcard
	if nextcardtmp != []:disc(nextcardtmp)
	notify("{} disc {} for {}.".format(me,nextcardtmp,plotcard))#MarchedtotheWall
	nextcardtmp = []
	selectedcard = []
	plotcard = []
	if count == 1:
		remoteCall(otherplayer, "plotdisccard", [2])
	else:
		setGlobalVariable("plotdisc","0")
		if getGlobalVariable("reavelplot") == "1":
			setGlobalVariable("reavelplot","2")
			if str(me._id) == getGlobalVariable("firstreveal"):remoteCall(players[1], "reavelplot", table)
			else:reavelplot(table)
			return
		if getGlobalVariable("reavelplot") == "2":
			resetplot()
			remoteCall(players[1], "resetplot", [])
			if fplay(1) == me:actiongeneral(1)
			else:remoteCall(players[1], "actiongeneral", 1)


def HeadsonSpikes(card,cards):
	mute()
	if cards.type == "Character":
		cards.moveTo(me.piles['Dead pile'])
		remoteCall(players[1], "addhousepow", [2])
		notify("{} reaveled {}, {} disc {} and gain 2 power for {} faction.".format(players[1],card,me,cards,players[1]))#HeadsonSpikes
	else:
		cards.moveTo(me.piles['Discard pile'])
		notify("{} reaveled {}, {} disc {}.".format(players[1],card,me,cards))#HeadsonSpikes
	if getGlobalVariable("reavelplot") == "1":
		setGlobalVariable("reavelplot","2")
		if str(me._id) == getGlobalVariable("firstreveal"):remoteCall(players[1], "reavelplot", table)
		else:reavelplot(table)
		return
	if getGlobalVariable("reavelplot") == "2":
		resetplot()
		remoteCall(players[1], "resetplot", [])
		if fplay(1) == me:actiongeneral(1)
		else:remoteCall(players[1], "actiongeneral", 1)

def plotphaseend():
	mute()
	me.setGlobalVariable("finished","0")
	if me.isInverted:table.create("cb48782b-3bdd-4024-af85-fb0eb65a8f51",-320,-215)
	else:table.create("cb48782b-3bdd-4024-af85-fb0eb65a8f51",-320,125)		

def drawphase(group, x = 0, y = 0):
	mute()
	if len(me.deck) > 0:
		draw(me.deck)
	if len(me.deck) > 0:
		draw(me.deck)
	if getGlobalVariable("drawphase") == "1":
		setGlobalVariable("drawphase","2")
		remoteCall(players[1], "drawphase", table)
		return
	if getGlobalVariable("drawphase") == "2":
		if fplay(1) == me:actiongeneral(1)
		else:remoteCall(players[1], "actiongeneral", 1)
		# notify("draw phase over")
		# setGlobalVariable("drawphase","0")
		# notify("marshal phase start")
		# setGlobalVariable("marshalphase","1")
		# me.setGlobalVariable("inmarshal","1")
		# if fplay(1) == me:marshalphase(table)
		# else:remoteCall(players[1], "marshalphase", table)

def drawphaseend():
	mute()
	me.setGlobalVariable("finished","0")
	if me.isInverted:table.create("cb48782b-3bdd-4024-af85-fb0eb65a8f51",-320,-215)
	else:table.create("cb48782b-3bdd-4024-af85-fb0eb65a8f51",-320,125)

def marshalphase(group, x = 0, y = 0):
	mute()
	if me.getGlobalVariable("turn") == "0":countincome(table)
	choiceList = ['Marshal', 'Action', 'No action and Pass']
	colorList = ['#ae0603' ,'#006b34','#D8D8D8']
	choice = askChoice("Which pass do you want to action?", choiceList,colorList)
	if choice == 1:marshalcard(table)
	if choice == 2:marshalphase(table)
	if choice == 3:
		if getGlobalVariable("marshalphase") =="1":
			setGlobalVariable("marshalphase","2")
			players[1].setGlobalVariable("inmarshal","1")
			remoteCall(players[1], "marshalphase", table)
			return
		elif getGlobalVariable("marshalphase") =="2":
			setGlobalVariable("marshalphase","0")
			notify("marshal phase over")
			notify("challenge phase start")
			if fplay(1) == me:
				setGlobalVariable("activeplayer",str(me._id))
				me.setGlobalVariable("active","1")
			else:
				setGlobalVariable("activeplayer",str(players[1]._id))
				players[1].setGlobalVariable("active","1")
			challengeaction(1)

def marshalcountincome():
	mute()
	setGlobalVariable("marshalphase","1")
	if fplay(1) == me:
		setGlobalVariable("activeplayer",str(me._id))	
		marshalactions()
	else:
		setGlobalVariable("activeplayer",str(players[1]._id))
		remoteCall(players[1], "marshalactions", [])

def marshalend():
	mute()
	global sessionpass
	if str(me._id) == getGlobalVariable("activeplayer") and fplay(1) == me:
		if not confirm("End Marshal?"):return
	if str(me._id) == getGlobalVariable("activeplayer") and fplay(1) != me:
		actioncancelcount = int(getGlobalVariable("actioncancel"))+1
		debug(actioncancelcount)
		if actioncancelcount == 2:
			if not confirm("End Marshal?"):return
		setGlobalVariable("actioncancel", str(actioncancelcount))
	clearfilter("")
	
	for cardn in table:
		if cardn.name == "marshalendbutton" and cardn.controller == me:
			cardn.delete()
		if cardn.name == "nextbutton" and cardn.controller == me:
			cardn.delete()
		if cardn.name == "passnextbutton" and cardn.controller == me:
			cardn.delete()#delete marshalendbutton
	setGlobalVariable("selectmode", "0")
	sessionpass = ""
	if fplay(1) == me:
		setGlobalVariable("actioncancel", "0")
		if str(me._id) == getGlobalVariable("activeplayer"):
			setGlobalVariable("activeplayer",str(players[1]._id))
			remoteCall(players[1], "marshalactions", [])
		else:marshalactions()
	else:
		if actioncancelcount == 2:
			setGlobalVariable("actioncancel", "0")
			notify("action over")
			if fplay(1) == me:marshalphaseend()
			else:remoteCall(players[1], "marshalphaseend", [])
		else:remoteCall(players[1], "marshalactions", [])
	# if fplay(1) == me:remoteCall(players[1], "marshalactions", [])
	# else:
	# 	if fplay(1) == me:marshalphaseend()
	# 	else:remoteCall(players[1], "marshalphaseend", [])

def activefaction():
	mute()
	for card in table:
		if card.type == "Faction" and card.controller == me:
			card.highlight = activcolor
		if card.type == "Faction" and card.controller != me:
			card.highlight = None

def marshalactions():
	mute()
	countincome(table)
	activefaction()
	me.setGlobalVariable("active","1")
	remoteCall(fplay(1), "actionmarshal", [1])
	#actionmarshal(1)
	# if me.isInverted:table.create("f5fb1824-1d0e-4a4a-a431-46e0a06f1a42",-375,-250)
	# else:table.create("f5fb1824-1d0e-4a4a-a431-46e0a06f1a42",-375,200)

def marshalphaseend():
	mute()
	me.setGlobalVariable("finished","0")
	if me.isInverted:table.create("cb48782b-3bdd-4024-af85-fb0eb65a8f51",-320,-215)
	else:table.create("cb48782b-3bdd-4024-af85-fb0eb65a8f51",-320,125)

def marshalcard(group, x = 0, y = 0):
	mute()
	global sessionpass
	targetTuple = ([card._id for card in me.hand if card.type in ("Character","Location","Attachment")], me._id) 
	setGlobalVariable("tableTargets", str(targetTuple))
	setGlobalVariable("selectmode", "1")
	if me.isInverted:table.create("584a37d7-5a30-4018-ae21-0ad325203fa0",-375,-250)
	else:table.create("584a37d7-5a30-4018-ae21-0ad325203fa0",-375,200)
	sessionpass = "marshalcardselect"
	whisper("**selectmode**")			
#---------------------------------------------------------------------------
# New Table card actions
#---------------------------------------------------------------------------
def displayCardText(card, x = 0, y = 0):
	mute()
	
	notify('{} - Card Text:'.format(card))
	notify('{}'.format(card.Text))


def displayErrata(card, x = 0, y = 0):
	mute()
	
	notify('{} - ErrataText:'.format(card._id))
	notify('{} - ErrataText:'.format(card.filter))
	notify('{} - ErrataText:'.format(card.highlight))
	notify('{} - ErrataText:'.format(card.position))
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
		for cardc in table:
			if attach.has_key(card._id):
				if attach[card._id] == cardc._id:
					del attach[card._id]
					setGlobalVariable("attachmodify",str(attach))
					debug(getGlobalVariable("attachmodify"))
					#rollback
					# if card.model == "9e6bf142-159b-4a3b-9d4c-d8bf233a6f0c":
					# 	cardc.markers[STR_Up] -= len(me.piles['Used Plot Pile'])
					if card.model == "4dd074aa-af6c-4897-b7b2-bff3493bcf9e" and cardc.model == "df79718d-b01d-4338-8907-7b6abff58303":cardmarkers(cardc,"milicon",-1)#096
					if card.model == "8dea9db3-58a4-4f47-9671-9109f2be46c0" and cardc.model == "fd60e197-476c-4d8d-811f-e0a403a12b48":cardmarkers(cardc,"inticon",1)
					if cardc.model == "f176a119-9fa1-465f-91d4-53ebe6cb65ac":cardmarkers(cardc,"milicon",-1)#MerchantPrince
					if cardc.model == "f176a119-9fa1-465f-91d4-53ebe6cb65ac":cardmarkers(cardc,"str",-1)#MerchantPrince
					if card.model == "a8bebc54-d01c-424d-8839-460ec09b733f":restoreprintcard(cardc)
					if re.search('\+\d\sSTR', card.Text) and card.model != "9e6bf142-159b-4a3b-9d4c-d8bf233a6f0c" and card.model != "4c8a114e-106c-4460-846b-28f73914fc11":
						stradd = re.search('\+\d\sSTR', card.Text).group()
						#choose.markers[STR_Up] += int(stradd[1])
						cardmarkers(cardc,"str",-int(stradd[1]))
					if re.search('\-\d\sSTR', card.Text) and card.model != "9e6bf142-159b-4a3b-9d4c-d8bf233a6f0c" and card.model != "4c8a114e-106c-4460-846b-28f73914fc11":
						stradd = re.search('\-\d\sSTR', card.Text).group()
						#choose.markers[STR_Sub] += int(stradd[1])
						cardmarkers(cardc,"str",int(stradd[1]))

					if re.search('gains an \[INT]\sicon', card.Text):cardmarkers(cardc,"inticon",-1)
					if re.search('gains a \[POW]\sicon', card.Text):cardmarkers(cardc,"powicon",-1)
					if re.search('gains a \[MIL]\sicon', card.Text) and cardc.model != "4dd074aa-af6c-4897-b7b2-bff3493bcf9e":cardmarkers(cardc,"milicon",-1)
					if re.search('loses an \[INT]\sicon', card.Text):cardmarkers(cardc,"inticon",1)
					if re.search('loses a \[POW]\sicon', card.Text):cardmarkers(cardc,"powicon",1)
					if re.search('loses a [MIL]\sicon', card.Text):cardmarkers(cardc,"milicon",1)
					if card.Text.find('Terminal.') == -1 and card.Keywords.find('Terminal.') == -1:remoteCall(card.owner, "returncard", card)
					else:remoteCall(card.owner, "disccard", card)
					return
		remoteCall(card.owner, "disccard", card)
		if card.highlight == sacrificecolor:
			card.highlight = None
			notify("{} sacrifice {}.".format(me, card))
		else:
			notify("{} discard {}.".format(me, card))
		# if card.Text.find('Terminal.') == -1 and card.Keywords.find('Terminal.') == -1:remoteCall(card.owner, "returncard", card)
		# else:remoteCall(card.owner, "disccard", card)
		card.resetProperties()
	elif card.type == "Character":
		for d in attach:
			if attach[d] == card._id:
				for cardd in table:
					if cardd._id == d:
						if cardd.Text.find('Terminal.') == -1 and cardd.Keywords.find('Terminal.') == -1:remoteCall(cardd.owner, "returncard", cardd)
						else:remoteCall(cardd.owner, "disccard", cardd)
						del attach[d]
						setGlobalVariable("attachmodify",str(attach))
						debug(getGlobalVariable("attachmodify"))
		if card.highlight == sacrificecolor:
			card.highlight = None
			card.moveTo(me.piles['Dead pile'])
			notify("{} sacrifice {}.".format(me, card))
		else:
			card.moveTo(me.piles['Discard pile'])
			notify("{} discard {}.".format(me, card))
	elif card.type == "Event":
		card.moveTo(me.piles['Discard pile'])
		notify("{} discard {}.".format(me, card))
	elif card.type == "Location":
		for dcard in table:
			if dcard.name == card.name and dcard.filter == WaitColor and dcard.controller == me:
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
		if card.highlight == sacrificecolor:
			card.highlight = None
			notify("{} sacrifice {}.".format(me, card))
		else:
			notify("{} discard {}.".format(me, card))
		card.moveTo(me.piles['Discard pile'])

def defaultAction(card, x = 0, y = 0):
	mute()
	# Default for Done button is playerDone
	if card.Type == "Internal": 
		if card.name == "Done Token":
			DoneButton(card)
		if card.name == "1st Player Token":
			moveFP(card)
	

def moveFP(card,plot = 0):
	mute()
	global reactionattach
	if getGlobalVariable("firstplay") == str(me._id):
		if me.isInverted: 
			card.moveToTable(-160,-100)
			card.controller = me
		else:
			card.moveToTable(-160,8)
			card.controller = me
	elif getGlobalVariable("firstplay") == str(players[1]._id):
		if me.isInverted: 
			card.moveToTable(-160,8)
			card.controller = players[1]
		else:
			card.moveToTable(-160,-100)
			card.controller = players[1]
	else:
		return
	if plot == 1:remoteCall(fplay(1), "fpreaction", [])

def fpreaction():
	mute()
	for cardfp in table:
		# if checknoprint(cardfp):continue
		if cardfp.model == "53d1c773-0f71-429c-a94e-6473d2e5a100"  and cardfp.filter != WaitColor:
			if getGlobalVariable("firstplay") == str(cardfp.controller._id):
				reactionattach[cardfp._id] = 1#Cersei’s Wheelhouse
	debug(reactionattach)
	if len(reactionattach) > 0:
		if getGlobalVariable("firstplay") == str(me._id):reaction("reactionplot",1)
		else:remoteCall(players[1], "reaction", ["reactionplot",1])
	else:askfirstreveal(table)

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

def cardintable(card,cardtype,controller = me,changediscpile = 0):
	mute()
	clist = [p for p in table
				if p.controller == controller and p.type == cardtype and p.isFaceUp and card != p]
	if len(clist) > 0:
		clist.reverse()
		for character in clist:
			x, y = character.position
			break
		clist.reverse()
		if controller == me:
			if me.isInverted:card.moveToTable(x-80,y)
			else:card.moveToTable(x+80,y)
		else:
			if me.isInverted:card.moveToTable(x+80,y)
			else:card.moveToTable(x-80,y)
	else:
		if cardtype == "Character":
			if controller == me:
				debug("1111")
				if me.isInverted:card.moveToTable(-60,-100)			
				else:card.moveToTable(-60,10)
			else:
				if me.isInverted:card.moveToTable(-60,10)			
				else:card.moveToTable(-60,-100)
		else:
			if me.isInverted:card.moveToTable(-60,-220)			
			else:card.moveToTable(-60,120)
	if changediscpile == 1:players[1].piles['Discard pile'].controller = players[1]

def play(card):
	mute()
	global nextcardtmp
	global selectedcard
	global sessionpass
	#me.setGlobalVariable("setupOk","")
	ambush = 0
	fll = 0
	reduce_character_turn = 0
	reduce_Stark_character_turn = 0
	reduce_Lannister_character_turn = 0
	reduce_Greyjoy_character_turn = 0
	reduce_Martell_character_turn = 0
	reduce_Baratheon_character_turn = 0
	reduce_Targaryen_character_turn = 0
	reduce_NW_character_turn = 0
	reduce_Tyrell_character_turn = 0

	reduce_Stark_card_turn = 0
	reduce_Lannister_card_turn = 0
	reduce_Greyjoy_card_turn = 0
	reduce_Martell_card_turn = 0
	reduce_Baratheon_card_turn = 0
	reduce_Targaryen_card_turn = 0
	reduce_Tyrell_card_turn = 0
	reduce_NW_card_turn = 0

	reduceloyal_turn = 0

	if getGlobalVariable("selectmode") != "0":return#and sessionpass == "savecardselect":return
	if card.type == "Event" and me.getGlobalVariable("cantuseevent") == "1":
		whisper("You cannot play events.")
		return
	if card.type == "Location" and me.getGlobalVariable("cantuselocation") == "1":
		whisper("You cannot marshal locations .")
		return
	if card.type == "Attachment" and me.getGlobalVariable("cantuseattach") == "1":
		whisper("You cannot marshal attachments ")
		return
	c = 0
	if card.cost == "" : 
		whisper("You can't play this card")
		return
	if card.Cost == "X": cost=askInteger("How much do you want to pay to play {} ? ".format(card.name),0)
	else :
		if getGlobalVariable("ambush") == "1" and "Ambush" in card.keywords:
			cost=int(re.search('Ambush\s\(\d\).', card.keywords).group()[8])
			ambush = 1
		else:cost=int(card.Cost)
		if me.getGlobalVariable("firstlimit") != "0" and "Limited" in card.keywords:
			whisper("You can only play one limited card")
			return
		if me.getGlobalVariable("firstevent") == "0":
			if checkpr(me) and card.type == "Event":
				cost -= 1
				if cost < 0:cost = 0
				notify("You control Paxter Redwyne the first event you play Reduce the gold cost by 1.")
		if card.loyal == "Yes":
			cost -= int(me.getGlobalVariable("reduceloyal_turn"))
			if cost < 0:cost = 0
			if me.getGlobalVariable("reduceloyal_turn") != "0":notify("Reduce the cost of the next loyal card you marshal or play this phase by 1 from Fealty")
			# me.setGlobalVariable("reduceloyal_turn", "0")
			reduceloyal_turn = 1


		if getGlobalVariable("marshalphase") != "0" and me.getGlobalVariable("firstll") == "1" and me.getGlobalVariable("firstcharacter") == "0":
			if card.type == "Character" and card.Traits.find('Lord') != -1 or card.Traits.find('Lady') != -1:
				cost -= 2
				if cost < 0:cost = 0
				fll = 1
				notify(" the first Lord or Lady character you marshal this round by 2")
		if getGlobalVariable("marshalphase") != "0":
			if checkcardmodel("a28ec48c-ee57-4c6a-a940-b59c1aeff251") and me.getGlobalVariable("firstlocation") == "0":
				if card.type == "Location":
					cost -= 1
			if me.getGlobalVariable("firstnobaratheonplayer") == "0":
				if checkrl(me) and card.type == "Character" and card.faction != "Baratheon.":
					cost -= 1
					if cost < 0:cost = 0
			if card.type == "Character":
				if card.model == "b785b7fc-2a11-4ba5-87e7-7c06c79d6210":
					for ccard in table:
						if ccard.controller == me and ccard.type == "Character" and ccard.filter != WaitColor and "Dothraki" in ccard.traits:
							cost -= 1
				if me.getGlobalVariable("reduce_character_turn") != "0":
					cost -= int(me.getGlobalVariable("reduce_character_turn"))
					reduce_character_turn = 1
				if card.faction == "Stark.":
					if me.getGlobalVariable("reduce_Stark_character_turn") != "0":
						cost -= int(me.getGlobalVariable("reduce_Stark_character_turn"))
						reduce_Stark_character_turn = 1
				if card.faction == "Lannister.":
					if me.getGlobalVariable("reduce_Lannister_character_turn") != "0":
						cost -= int(me.getGlobalVariable("reduce_Lannister_character_turn"))
						reduce_Lannister_character_turn = 1
				if card.faction == "Greyjoy.":
					if me.getGlobalVariable("reduce_Greyjoy_character_turn") != "0":
						cost -= int(me.getGlobalVariable("reduce_Greyjoy_character_turn"))
						reduce_Greyjoy_character_turn = 1
				if card.faction == "Martell.":
					if me.getGlobalVariable("reduce_Martell_character_turn") != "0":
						cost -= int(me.getGlobalVariable("reduce_Martell_character_turn"))
						reduce_Martell_character_turn = 1
				if card.faction == "Baratheon.":
					if me.getGlobalVariable("reduce_Baratheon_character_turn") != "0":
						cost -= int(me.getGlobalVariable("reduce_Baratheon_character_turn"))
						reduce_Baratheon_character_turn = 1
				if card.faction == "Targaryen.":
					if me.getGlobalVariable("reduce_Targaryen_character_turn") != "0":
						cost -= int(me.getGlobalVariable("reduce_Targaryen_character_turn"))
						reduce_Targaryen_character_turn = 1
				if card.faction == "Night's Watch.":
					if me.getGlobalVariable("reduce_NW_character_turn") != "0":
						cost -= int(me.getGlobalVariable("reduce_NW_character_turn"))
						reduce_NW_character_turn = 1
				if card.faction == "Tyrell.":
					if me.getGlobalVariable("reduce_Tyrell_character_turn") != "0":
						cost -= int(me.getGlobalVariable("reduce_Tyrell_character_turn"))
						reduce_Tyrell_character_turn = 1
			if cost < 0:cost = 0
			if card.faction == "Stark.":
				if me.getGlobalVariable("reduce_Stark_card_turn") != "0":
					cost -= int(me.getGlobalVariable("reduce_Stark_card_turn"))
					reduce_Stark_card_turn = 1
			if card.faction == "Lannister.":
				if me.getGlobalVariable("reduce_Lannister_card_turn") != "0":
					cost -= int(me.getGlobalVariable("reduce_Lannister_card_turn"))
					reduce_Lannister_card_turn = 1
			if card.faction == "Greyjoy.":
				if me.getGlobalVariable("reduce_Greyjoy_card_turn") != "0":
					cost -= int(me.getGlobalVariable("reduce_Greyjoy_card_turn"))
					reduce_Greyjoy_card_turn = 1
			if card.faction == "Martell.":
				if me.getGlobalVariable("reduce_Martell_card_turn") != "0":
					cost -= int(me.getGlobalVariable("reduce_Martell_card_turn"))
					reduce_Martell_card_turn = 1
			if card.faction == "Baratheon.":
				if me.getGlobalVariable("reduce_Baratheon_card_turn") != "0":
					cost -= int(me.getGlobalVariable("reduce_Baratheon_card_turn"))
					reduce_Baratheon_card_turn = 1
			if card.faction == "Targaryen.":
				if me.getGlobalVariable("reduce_Targaryen_card_turn") != "0":
					cost -= int(me.getGlobalVariable("reduce_Targaryen_card_turn"))
					reduce_Targaryen_card_turn = 1
			if card.faction == "Tyrell.":
				if me.getGlobalVariable("reduce_Tyrell_card_turn") != "0":
					cost -= int(me.getGlobalVariable("reduce_Tyrell_card_turn"))
					reduce_Tyrell_card_turn = 1
			if card.faction == "Night's Watch.":
				if me.getGlobalVariable("reduce_NW_card_turn") != "0":
					cost -= int(me.getGlobalVariable("reduce_NW_card_turn"))
					reduce_NW_card_turn = 1
			if cost < 0:cost = 0

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
			global countusedplot
			countusedplot = len(me.piles['Used Plot Pile'])
			list = []
			if me.getGlobalVariable("playattach") == "1":
				me.setGlobalVariable("playattach","")
				list.append(selectedcard[0])
				nextcardtmp = []
				selectedcard = []
				sessionpass = ""
			else:
				for targetcard in table:
					if targetcard.filter == targetcardcolor:
						if 'No attachments.' in targetcard.Keywords:
							whisper("{} cannot be attached.".format(targetcard))
							targetcard.filter = None
						elif 'No attachments except Weapon.' in targetcard.Keywords:
							if "Weapon." in card.traits:
								list.append(targetcard)
								targetcard.filter = None
								if cardtmp != []:cardtmp.arrow(cardtmp,False)
							else:
								whisper("{} cannot be attached.".format(targetcard))
								targetcard.filter = None
								continue
						elif re.search(r'(.*) or (.*) character only.', card.Text,re.I):
							if targetcard.Traits.find('Lord') != -1 or targetcard.Traits.find('Lady') != -1:
								list.append(targetcard)
								targetcard.filter = None
								if cardtmp != []:cardtmp.arrow(cardtmp,False)
							else:
								whisper("{} can only be attached to [Lord or Lady] characters.".format(card))
								targetcard.filter = None
								if cardtmp != []:cardtmp.arrow(cardtmp,False)
						elif re.search(r'\[(.*)] character only.', card.Text,re.I):
							chaonly = re.search(r'\[(.*)] character only.', card.Text,re.I).group(1)
							if targetcard.Faction.find(chaonly) != -1 or targetcard.Traits.find(chaonly) != -1:
								list.append(targetcard)
								targetcard.filter = None
								if cardtmp != []:cardtmp.arrow(cardtmp,False)
							else:
								whisper("{} can only be attached to [{}] characters.".format(card,chaonly))
								targetcard.filter = None
								if cardtmp != []:cardtmp.arrow(cardtmp,False)
						elif card.model == "2b3f8c07-5602-4dc0-9929-5c1f8ca9cfd6":
							if not "Limited" in targetcard.keywords and targetcard.type == "Location" and int(targetcard.cost) <= 3:
								list.append(targetcard)
								targetcard.filter = None
							else:
								whisper("{} cannot be attached.".format(targetcard))
								targetcard.filter = None
						else:
							if me.getGlobalVariable("setupOk") in ("4","5"):
								if targetcard.controller == me:list.append(targetcard)
							else:list.append(targetcard)
							targetcard.filter = None
							if cardtmp != []:cardtmp.arrow(cardtmp,False)
					elif len(me.piles['Plot Deck']) != 7 and targetcard.filter != WaitColor:
						debug(targetcard)
						debug(card.type)
						debug(targetcard.Keywords)
						if not "Weapon." in card.traits and 'No attachments except Weapon.' in targetcard.Keywords:continue
						elif re.search(r'(.*) or (.*) character only.', card.Text,re.I):
							if targetcard.Traits.find('Lord') != -1 or targetcard.Traits.find('Lady') != -1:
								list.append(targetcard)
						elif re.search(r'\[(.*)] character only.', card.Text,re.I):
							chaonly = re.search(r'\[(.*)] character only.', card.Text,re.I).group(1)
							if targetcard.Faction.find(chaonly) != -1 or targetcard.Traits.find(chaonly) != -1:
								list.append(targetcard)
						elif card.model == "2b3f8c07-5602-4dc0-9929-5c1f8ca9cfd6":
							if not "Limited" in targetcard.keywords and targetcard.type == "Location" and int(targetcard.cost) <= 3:
								list.append(targetcard)
						elif card.model == "9e378524-0d9b-47c7-847b-7d7b2a690556":
							if targetcard.type == "Character" and int(targetcard.cost) <= 4:
								list.append(targetcard)
						else:
							if "Opponent’s character only" in card.text:
								if targetcard.type == "Character" and 'No attachments.' not in targetcard.Keywords and targetcard.controller != me:list.append(targetcard)
							else:
								if targetcard.type == "Character" and 'No attachments.' not in targetcard.Keywords:list.append(targetcard)
				if len(me.piles['Plot Deck']) != 7:
					nextcardtmp = card
					targetTuple = [cardatt._id for cardatt in list]
					debug(nextcardtmp)
					selectcardnext(targetTuple,"playattach",table,[],"",1,1)
					return
			if len(list) == 1:cards=list
			if list == []:
				whisper("You must targeted(use Shift+mouse left button) a card which you want to attach to.")
				return
			if len(list) > 0:
				if len(list) > 1:
					dlg = cardDlg(list)
					dlg.title = "These cards can be attached:"
					dlg.text = "Choose a card to attach."
					dlg.min = 1
					dlg.max = 1
					cards = dlg.show()
				if cards != None:
					for choose in cards:
						if len(me.piles['Plot Deck']) != 7:
							# reduc=askInteger("Reduce Cost by ?",0)
							# if reduc == None or cost == None: return False
							# if reduc>cost: reduc=cost
							# cost-=reduc
							reduc = int(card.Cost) - cost
							if me.counters['Gold'].value < cost :
								whisper("You don't have enough Gold to pay for {}.".format(card))
								return False
							me.counters['Gold'].value -= cost
							# for incomecard in table:
							# 	if incomecard.controller == me and incomecard.markers[Gold] > 0:
							# 		incomecard.markers[Gold] -= cost
						cx,cy = choose.position
						if me.isInverted:x,y = attachat(cx-15,cy-15,table)
						else:x,y = attachat(cx+15,cy+15,table)
						card.moveToTable(x,y)
						attach = eval(getGlobalVariable("attachmodify"))
						if not attach.has_key(card._id):
							attach[card._id] = choose._id
						else:attach[card._id].append(choose._id)
						setGlobalVariable("attachmodify",str(attach))
						debug(card.text)
						if card.model == "4dd074aa-af6c-4897-b7b2-bff3493bcf9e" and choose.model == "df79718d-b01d-4338-8907-7b6abff58303":cardmarkers(choose,"milicon",1)#096
						if card.model == "8dea9db3-58a4-4f47-9671-9109f2be46c0" and choose.model == "fd60e197-476c-4d8d-811f-e0a403a12b48":cardmarkers(choose,"inticon",1)
						if choose.model == "f176a119-9fa1-465f-91d4-53ebe6cb65ac":cardmarkers(choose,"milicon",1)#MerchantPrince
						if choose.model == "f176a119-9fa1-465f-91d4-53ebe6cb65ac":cardmarkers(choose,"str",1)#MerchantPrince
						# if card.model == "9e6bf142-159b-4a3b-9d4c-d8bf233a6f0c":choose.markers[STR_Up] += countusedplot
						if card.model == "a8bebc54-d01c-424d-8839-460ec09b733f":noprintcard(choose)
						if re.search('\+\d\sSTR', card.Text) and card.model != "9e6bf142-159b-4a3b-9d4c-d8bf233a6f0c" and card.model != "4c8a114e-106c-4460-846b-28f73914fc11":
							stradd = re.search('\+\d\sSTR', card.Text).group()
							#choose.markers[STR_Up] += int(stradd[1])
							cardmarkers(choose,"str",int(stradd[1]))
						if re.search('\-\d\sSTR', card.Text) and card.model != "9e6bf142-159b-4a3b-9d4c-d8bf233a6f0c" and card.model != "4c8a114e-106c-4460-846b-28f73914fc11":
							stradd = re.search('\-\d\sSTR', card.Text).group()
							#choose.markers[STR_Sub] += int(stradd[1])
							cardmarkers(choose,"str",-int(stradd[1]))
						if re.search('gains an \[INT]\sicon', card.Text):cardmarkers(choose,"inticon",1)
						if re.search('gains a \[POW]\sicon', card.Text):cardmarkers(choose,"powicon",1)
						if re.search('gains a \[MIL]\sicon', card.Text) and card.model != "4dd074aa-af6c-4897-b7b2-bff3493bcf9e":cardmarkers(choose,"milicon",1)
						if re.search('loses an \[INT]\sicon', card.Text):cardmarkers(choose,"inticon",-1)
						if re.search('loses a \[POW]\sicon', card.Text):cardmarkers(choose,"powicon",-1)
						if re.search('loses a [MIL]\sicon', card.Text):cardmarkers(choose,"milicon",-1)
						card.sendToBack()
						if len(me.piles['Plot Deck']) == 7:
							notify("{} plays {} and attachs to {}.".format(me,card,choose))
						else:
							card.highlight = PlayColor
							notify("{} plays {} and attachs to {} for {} Gold (Cost reduced by {}).".format(me,card,choose,cost,reduc))
					if me.getGlobalVariable("firstlimit") == "0":
						if "Limited" in card.keywords:me.setGlobalVariable("firstlimit","1")
					if reduce_Stark_card_turn != 0:me.setGlobalVariable("reduce_Stark_card_turn", "0")
					if reduce_Lannister_card_turn != 0:me.setGlobalVariable("reduce_Lannister_card_turn", "0")
					if reduce_Greyjoy_card_turn != 0:me.setGlobalVariable("reduce_Greyjoy_card_turn", "0")
					if reduce_Martell_card_turn != 0:me.setGlobalVariable("reduce_Martell_card_turn", "0")
					if reduce_Baratheon_card_turn != 0:me.setGlobalVariable("reduce_Baratheon_card_turn", "0")
					if reduce_Targaryen_card_turn != 0:me.setGlobalVariable("reduce_Targaryen_card_turn", "0")
					if reduce_Tyrell_card_turn != 0:me.setGlobalVariable("reduce_Tyrell_card_turn", "0")
					if reduce_NW_card_turn != 0:me.setGlobalVariable("reduce_NW_card_turn", "0")

					if reduceloyal_turn == 1:me.setGlobalVariable("reduceloyal_turn", "0")
					if getGlobalVariable("marshalphase") != "0":
						reactionmarshal(card)
						# remoteCall(players[1], "action", ["marshal",1])
					return True
				else:
					whisper("Attachment cards must be attached to another card or game element.")
					if getGlobalVariable("marshalphase") != "0":remoteCall(players[1], "action", ["marshal",1])
					return
		else:
			# reduc=askInteger("Reduce Cost by ?",0)
			# if reduc == None or cost == None: return False
			# if reduc>cost: reduc=cost
			# cost-=reduc
			reduc = int(card.Cost) - cost
			if me.counters['Gold'].value < cost :
				whisper("You don't have enough Gold to pay for {}.".format(card))
				if getGlobalVariable("marshalphase") != "0":remoteCall(players[1], "action", ["marshal",1])
				return		
			if card.type == "Character":
				if getGlobalVariable("marshalphase") != "0":
					if card.type == "Character" and card.Traits.find('Lord') != -1 or card.Traits.find('Lady') != -1:
						me.setGlobalVariable("firstcharacter","1")
				clist = [p for p in table
							if p.controller == me and p.type == "Character" and p.isFaceUp]
				if len(clist) > 0:
					clist.reverse()
					for character in clist:
						x, y = character.position
						break
					clist.reverse()
					if me.isInverted: card.moveToTable(x+80,y)
					else:card.moveToTable(x+80,y)
				else:
					if me.isInverted:card.moveToTable(-60,-100)			
					else:card.moveToTable(-60,10)
				if getGlobalVariable("marshalphase") != "0":
					if me.getGlobalVariable("firstnobaratheonplayer") == "0":
						if checkrl(me) and card.type == "Character" and card.faction != "Baratheon.":me.setGlobalVariable("firstnobaratheonplayer", "1")
			elif card.Type == "Location":
				if getGlobalVariable("marshalphase") != "0":
					me.setGlobalVariable("firstlocation","1")
				clist = [p for p in table
							if p.controller == me and p.type == "Location" and p.isFaceUp]
				if len(clist) > 0:
					clist.reverse()
					for location in clist:
						x, y = location.position
						break
					clist.reverse()
					if me.isInverted: card.moveToTable(x+80,y)
					else:card.moveToTable(x+80,y)
				else:
					if me.isInverted:card.moveToTable(-60,-220)			
					else:card.moveToTable(-60,120)
			elif card.type == "Event":
				if me.isInverted: card.moveToTable(-130,-230)
				else: card.moveToTable(-130,130)
				if me.getGlobalVariable("firstevent") == "0":me.setGlobalVariable("firstevent", "1")
				#whisper("Select a target.")
				#checksaveevent(card)
			else:
				if me.isInverted: card.moveToTable(-130,-230)
				else: card.moveToTable(-130,130)
			if card.type != "Event":
				card.highlight = PlayColor
			if ambush != 1:notify("{} plays {} for {} Gold (Cost reduced by {}).".format(me,card,cost,reduc))
			else:notify("{} ambush {} for {} Gold).".format(me,card,cost))
			me.counters['Gold'].value -= cost
			# for incomecard in table:
			# 	if incomecard.controller == me and incomecard.markers[Gold] > 0:
			# 		incomecard.markers[Gold] -= cost
			if me.getGlobalVariable("firstlimit") == "0":
				if "Limited" in card.keywords:me.setGlobalVariable("firstlimit","1")
			if reduce_character_turn != 0:me.setGlobalVariable("reduce_character_turn", "0")
			if reduce_Stark_character_turn != 0:me.setGlobalVariable("reduce_Stark_character_turn", "0")
			if reduce_Lannister_character_turn != 0:me.setGlobalVariable("reduce_Lannister_character_turn", "0")
			if reduce_Greyjoy_character_turn != 0:me.setGlobalVariable("reduce_Greyjoy_character_turn", "0")
			if reduce_Martell_character_turn != 0:me.setGlobalVariable("reduce_Martell_character_turn", "0")
			if reduce_Baratheon_character_turn != 0:me.setGlobalVariable("reduce_Baratheon_character_turn", "0")
			if reduce_Targaryen_character_turn != 0:me.setGlobalVariable("reduce_Targaryen_character_turn", "0")
			if reduce_NW_character_turn != 0:me.setGlobalVariable("reduce_NW_character_turn", "0")
			if reduce_Tyrell_character_turn != 0:me.setGlobalVariable("reduce_Tyrell_character_turn", "0")

			if reduce_Stark_card_turn != 0:me.setGlobalVariable("reduce_Stark_card_turn", "0")
			if reduce_Lannister_card_turn != 0:me.setGlobalVariable("reduce_Lannister_card_turn", "0")
			if reduce_Greyjoy_card_turn != 0:me.setGlobalVariable("reduce_Greyjoy_card_turn", "0")
			if reduce_Martell_card_turn != 0:me.setGlobalVariable("reduce_Martell_card_turn", "0")
			if reduce_Baratheon_card_turn != 0:me.setGlobalVariable("reduce_Baratheon_card_turn", "0")
			if reduce_Targaryen_card_turn != 0:me.setGlobalVariable("reduce_Targaryen_card_turn", "0")
			if reduce_Tyrell_card_turn != 0:me.setGlobalVariable("reduce_Tyrell_card_turn", "0")
			if reduce_NW_card_turn != 0:me.setGlobalVariable("reduce_NW_card_turn", "0")

			if reduceloyal_turn == 1:me.setGlobalVariable("reduceloyal_turn", "0")
			if getGlobalVariable("marshalphase") != "0" and card.type != "Event":
				reactionmarshal(card)
			return True
		
	else:
		if me.isInverted: 
			card.moveToTable(x-12,y-12)
		else:
			card.moveToTable(x+12,y+12)
		card.filter = "#005c3521"
		card.highlight = PlayColor
		notify("{} plays {}'s duplicate.".format(me,card))
		card.sendToBack()
		if getGlobalVariable("marshalphase") != "0":remoteCall(players[1], "action", ["marshal",1])

			
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
		setup(table)
	else:
		notify("Deck of {} is NOT OK".format(me))
		#setup(table)
	
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
def on_table_load():
	mute()
	#webRead('http://qxu2309320040.my3w.com/action.php?winner={}&loser=xing'.format(me.name), 5000)
	me.setGlobalVariable("finished","0")
	if getSetting("welcome", "1") == "1":
		if not confirm("Welcome to AGOT OCTGN Automation Version\n\nYou can enter the menu [Game Documents],and selet [Manual book] to see how to use automation.\n\nYou can also visit the offical site to create issues.\n\nChoss [No] Never show this window"):
			setSetting("welcome","0")
	# setGlobalVariable("Invertedloaddeck","0")
	# setGlobalVariable("selectgamemode","0")
	# # ver = "1.4.2.0"
	# # log = changelogcn["1.4.2.0"]
	# # log = '\n\n>>> '.join(log)
	# # choice = confirm("Changes in {}:\n>>> {}\n\nSee more info?".format(ver, log))
	# # if choice == True:openUrl('https://github.com/TassLehoff/AGoTv2-OCTGN')
	
	# if not me.isInverted:
	# 	notify("waiting for HOST select game mode.")
	# 	selectgamemode()



def selectgamemode():
	mute()
	choiceList = ['Automation', 'Manually']
	colorList = ['#ae0603' ,'#006b34']
	choice = askChoice("select game mode", choiceList,colorList)
	if choice == 1:setGlobalVariable("automode","1")
	elif choice == 2:setGlobalVariable("automode","0")
	else:
		selectgamemode()
		return
	setGlobalVariable("selectgamemode","1")
	if getGlobalVariable("Invertedloaddeck") =="1":remoteCall(players[1], "afterload", [players[1]])


def onloaddeck(args):
	mute()
	setGlobalVariable("automode","1")
	# if args.player == me:
	# 	if getGlobalVariable("selectgamemode") =="1":afterload(me)
	# 	else:
	# 		setGlobalVariable("Invertedloaddeck","1")
	# 		notify("waiting for host select game mode")
	if args.player == me:afterload(me)

def afterload(player):
	mute()
	c = len(players)
	setGlobalVariable("numplayer","{}".format(c))
	if not me.isInverted:
		setGlobalVariable("AID","{}".format(me))
		setGlobalVariable("aside","{}".format(me._id))
	else:
		setGlobalVariable("BID","{}".format(me))
		setGlobalVariable("bside","{}".format(me._id))


	setGlobalVariable("gameover","0")
	me.setGlobalVariable("isselect", "0")
	me.setGlobalVariable("actionstyle", "0")
	setGlobalVariable("actionplay", "")

	setGlobalVariable("actioncancel", "0")
	setGlobalVariable("tableTargets", "")
	setGlobalVariable("selectmode", "0")
	setGlobalVariable("insertre", "")
	setGlobalVariable("cantchallenge", "0")
	setGlobalVariable("bedefend", "")
	setGlobalVariable("aftcr", "")
	setGlobalVariable("aftcu", "")
	setGlobalVariable("dominancestart", "")
	setGlobalVariable("dominancewin", "")
	setGlobalVariable("dominancewinplayer","")
	setGlobalVariable("dominanceend", "")
	setGlobalVariable("standingstart", "")
	setGlobalVariable("standingover", "")
	setGlobalVariable("standingend", "")
	setGlobalVariable("taxationstart", "")
	setGlobalVariable("taxationreturn", "")
	setGlobalVariable("taxationrcheckhand", "")
	setGlobalVariable("taxationend", "")
	setGlobalVariable("aftcuevent", "-1")
	setGlobalVariable("chaevent", "-1")
	setGlobalVariable("attachmodify", "{}")
	setGlobalVariable("mainstep", "0")
	setGlobalVariable("ambush", "0")
	setGlobalVariable("aftercalculatestand", "[]")
	setGlobalVariable("aftercalculatedraw", "[]")
	setGlobalVariable("ignorestr", "[]")
	setGlobalVariable("addclaim","0")
	setGlobalVariable("addclaimall","0")
	setGlobalVariable("reavelplot","1")
	setGlobalVariable("drawphase","0")
	setGlobalVariable("marshalphase","0")
	me.setGlobalVariable("inmarshal","1")
	me.setGlobalVariable("firstevent", "0")
	me.setGlobalVariable("firstnobaratheonplayer","0")
	me.setGlobalVariable("firstcharacter", "0")
	me.setGlobalVariable("firstll", "0")#A Noble Cause
	me.setGlobalVariable("firstdraw","0")
	me.setGlobalVariable("firstlocation","0")

	setGlobalVariable("firstreveal", "")
	setGlobalVariable("challengephase","0")
	setGlobalVariable("dominancephase","0")
	setGlobalVariable("standingphase","0")
	setGlobalVariable("taxationphase","0")
	me.setGlobalVariable("milcount","0")
	me.setGlobalVariable("milcountmax","1")
	me.setGlobalVariable("intcount","0")
	me.setGlobalVariable("intcountmax","1")
	me.setGlobalVariable("powcount","0")
	me.setGlobalVariable("powcountmax","1")
	setGlobalVariable("action","0")
	setGlobalVariable("activeplayer","")
	me.setGlobalVariable("active","0")
	setGlobalVariable("winint","0")
	me.setGlobalVariable("intwin", "0")
	me.setGlobalVariable("submilclaim", "0")
	me.setGlobalVariable("subintclaim", "0")
	me.setGlobalVariable("subpowclaim", "0")
	setGlobalVariable("challengeplayer","0")

	me.setGlobalVariable("cantuseevent", "0")
	me.setGlobalVariable("cantuselocation", "0")
	me.setGlobalVariable("cantuseattach", "0")

	setGlobalVariable("Kingdomgold0","0")
	setGlobalVariable("Edictgold0","0")
	me.setGlobalVariable("firstlimit","0")
	setGlobalVariable("noprint","0")

	me.setGlobalVariable("limitchallenge", "0")

	setGlobalVariable("plotdisc","0")
	setGlobalVariable("plotkill","0")
	me.setGlobalVariable("plotOk","")
	me.setGlobalVariable("drawOk","")

	setGlobalVariable("generalaction", "0")
	setGlobalVariable("dominanceaction", "0")
	setGlobalVariable("standingaction", "0")
	setGlobalVariable("actiontaxation", "0")
	
	me.setGlobalVariable("playattach","")

	me.setGlobalVariable("reduceloyal_turn", "0")
	me.setGlobalVariable("reduce_character_turn", "0")
	me.setGlobalVariable("reduce_Baratheon_character_turn", "0")
	me.setGlobalVariable("reduce_Baratheon_card_turn", "0")
	me.setGlobalVariable("reduce_Greyjoy_character_turn", "0")
	me.setGlobalVariable("reduce_Greyjoy_card_turn", "0")
	me.setGlobalVariable("reduce_Lannister_character_turn", "0")
	me.setGlobalVariable("reduce_Lannister_card_turn", "0")
	me.setGlobalVariable("reduce_Martell_character_turn", "0")
	me.setGlobalVariable("reduce_Martell_card_turn", "0")
	me.setGlobalVariable("reduce_NW_character_turn", "0")
	me.setGlobalVariable("reduce_NW_card_turn", "0")
	me.setGlobalVariable("reduce_Stark_character_turn", "0")
	me.setGlobalVariable("reduce_Stark_card_turn", "0")
	me.setGlobalVariable("reduce_Targaryen_character_turn", "0")
	me.setGlobalVariable("reduce_Targaryen_card_turn", "0")
	me.setGlobalVariable("reduce_Tyrell_character_turn", "0")
	me.setGlobalVariable("reduce_Tyrell_card_turn", "0")
	if player == me:
		checkdeck()
		#setup(table)
		
def onmoved(args):
	mute()
	index = 0
	global aryaduplicate
	for card in args.cards:
		attach = eval(getGlobalVariable("attachmodify"))
		if args.cards[index].type in ("Character","Location") and args.toGroups[index].name == "Table" and args.fromGroups[index].name == "Table" and card.controller == me and card.filter != WaitColor:
			list = []
			list2 = []
			list3 = []
			for d in attach:
				if attach[d] == args.cards[index]._id:
					list.append(d)
			for dcard in table:
				if dcard.name == args.cards[index].name and dcard.filter == WaitColor and dcard.controller == me:
					list2.append(dcard._id)
				if dcard in aryaduplicate:
					list2.append(dcard._id)
			list.reverse()
			for cardatt in table:
				for listcard in table:
					if cardatt.controller == listcard.controller and cardatt.name == listcard.name and  listcard._id in (list) and cardatt.filter == WaitColor:
						list3.append(cardatt)
			i = 12			
			if len(list) > 0:
				for cardindex in list:
					for carda in table:
						if carda._id == cardindex:
							x1,y1 = card.position
							if me.isInverted:
								#carda.moveToTable(x1-i,y1-i)movecardp
								remoteCall(carda.owner, "movecardp", [carda,x1-i,y1-i,1])
							else:
								#carda.moveToTable(x1+i,y1+i)
								remoteCall(carda.owner, "movecardp", [carda,x1+i,y1+i,1])
							#carda.sendToBack()
							x2,y2 = carda.position
							i+=12
							k = 12
							for cardattd in list3:
								if cardattd.name == carda.name:
									if me.isInverted:
										#cardattd.moveToTable(x2-k,y2+k)
										remoteCall(cardattd.owner, "movecardp", [cardattd,x2-k,y2+k,1])
									else:
										#cardattd.moveToTable(x2+k,y2-k)
										remoteCall(cardattd.owner, "movecardp", [cardattd,x2+k,y2-k,1])
									#cardattd.sendToBack()
									k+=12
								
			i = 12
			if args.cards[index].unique == "Yes":
				if len(list2) > 0:
					for cardindex in list2:
						for carda in table:
							if carda._id == cardindex:
								x1,y1 = card.position
								if me.isInverted:carda.moveToTable(x1+i,y1+i)
								else:carda.moveToTable(x1-i,y1-i)
								carda.sendToBack()
								i+=12
		if card in aryaduplicate and args.toGroups[index].name != "Table" and args.fromGroups[index].name == "Table" and card.controller == me:
			aryaduplicate.remove(card)
			if len(aryaduplicate) == 0:
				for card in table:
					if card.model == "abf9c701-f480-4576-a5c0-44b4e9b04e6c" and card.controller == me and card not in noprint_turn:cardmarkers(card,"milicon",-1)
		if card.type == "Attachment" and args.toGroups[index].name != "Table" and args.fromGroups[index].name == "Table" and card.controller == me:
			for card in table:
				if attach.has_key(args.cards[index]._id):
					if attach[args.cards[index]._id] == card._id:
						del attach[args.cards[index]._id]
						setGlobalVariable("attachmodify",str(attach))
						debug(getGlobalVariable("attachmodify"))
					#rollback
						# if args.cards[index].model == "9e6bf142-159b-4a3b-9d4c-d8bf233a6f0c":
						# 	card.markers[STR_Up] -= len(me.piles['Used Plot Pile'])
						if args.cards[index].model == "4dd074aa-af6c-4897-b7b2-bff3493bcf9e" and card.model == "df79718d-b01d-4338-8907-7b6abff58303":cardmarkers(card,"milicon",-1)#096
						if args.cards[index].model == "8dea9db3-58a4-4f47-9671-9109f2be46c0" and card.model == "fd60e197-476c-4d8d-811f-e0a403a12b48":cardmarkers(card,"inticon",1)
						if card.model == "f176a119-9fa1-465f-91d4-53ebe6cb65ac":cardmarkers(card,"milicon",-1)#MerchantPrince
						if card.model == "f176a119-9fa1-465f-91d4-53ebe6cb65ac":cardmarkers(card,"str",-1)#MerchantPrince
						if re.search('\+\d\sSTR', args.cards[index].Text) and args.cards[index].model != "9e6bf142-159b-4a3b-9d4c-d8bf233a6f0c" and args.cards[index].model != "4c8a114e-106c-4460-846b-28f73914fc11":
							stradd = re.search('\+\d\sSTR', args.cards[index].Text).group()
							cardmarkers(card,"str",-int(stradd[1]))
						if re.search('\-\d\sSTR', args.cards[index].Text) and args.cards[index].model != "9e6bf142-159b-4a3b-9d4c-d8bf233a6f0c" and args.cards[index].model != "4c8a114e-106c-4460-846b-28f73914fc11":
							stradd = re.search('\-\d\sSTR', args.cards[index].Text).group()
							cardmarkers(card,"str",int(stradd[1]))
						if re.search('gains an \[INT]\sicon', args.cards[index].Text):cardmarkers(card,"inticon",-1)
						if re.search('gains a \[POW]\sicon', args.cards[index].Text):cardmarkers(card,"powicon",-1)
						if re.search('gains a \[MIL]\sicon', args.cards[index].Text) and card.model != "4dd074aa-af6c-4897-b7b2-bff3493bcf9e":cardmarkers(card,"milicon",-1)
						if re.search('loses an \[INT]\sicon', args.cards[index].Text):cardmarkers(card,"inticon",1)
						if re.search('loses a \[POW]\sicon', args.cards[index].Text):cardmarkers(card,"powicon",1)
						if re.search('loses a [MIL]\sicon', args.cards[index].Text):cardmarkers(card,"milicon",1)
						if args.cards[index].model == "a8bebc54-d01c-424d-8839-460ec09b733f":restoreprintcard(card)
						# if re.search('\[INT]\sicon', args.cards[index].Text):cardmarkers(card,"inticon",-1)
						# if re.search('\[POW]\sicon', args.cards[index].Text):cardmarkers(card,"powicon",-1)
						# if re.search('\[MIL]\sicon', args.cards[index].Text) and args.cards[index].model != "4dd074aa-af6c-4897-b7b2-bff3493bcf9e":cardmarkers(card,"milicon",-1)
			args.cards[index].resetProperties()
		if args.cards[index].type == "Character" and args.toGroups[index].name != "Table" and args.fromGroups[index].name == "Table" and card.controller == me:
			for d in attach:
				if attach[d] == args.cards[index]._id:
					for cardd in table:
						if cardd._id == d:
							remoteCall(cardd.owner, "disc", [cardd])
							del attach[d]
							setGlobalVariable("attachmodify",str(attach))
							debug(getGlobalVariable("attachmodify"))

		if args.cards[index].model == "5d20e021-5d12-4338-8bdd-42d008bff919" and args.toGroups[index].name == "Table" and args.fromGroups[index].name != "Table" and args.cards[index].controller == me and args.cards[index].filter != WaitColor and args.cards[index] not in noprint_turn:
				for cardadd in table:
					if cardadd.controller == me and cardadd.Faction == "Night's Watch." and cardadd.type == "Character" and cardadd.filter != WaitColor:cardmarkers(cardadd,"str",1)
		if args.cards[index].model == "5d20e021-5d12-4338-8bdd-42d008bff919" and args.toGroups[index].name != "Table" and args.fromGroups[index].name == "Table" and args.cards[index].controller == me and args.cards[index].filter != WaitColor and args.cards[index] not in noprint_turn:
				for cardadd in table:
					if cardadd.controller == me and cardadd.Faction == "Night's Watch."and cardadd.type == "Character" and cardadd.filter != WaitColor:cardmarkers(cardadd,"str",-1)
		#Warship and Drowned Men
		if getGlobalVariable("noprint") == "0":
			if args.cards[index].model == "fdf1989a-ee7d-4972-9d12-b299bfe3ba6d" and args.toGroups[index].name == "Table" and args.fromGroups[index].name != "Table" and args.cards[index].controller == me and args.cards[index].filter != WaitColor:
				for cardadd in table:
					if cardadd.controller == me and "Knight." in cardadd.traits and cardadd.filter != WaitColor and cardadd._id != args.cards[index]._id:
						cardmarkers(args.cards[index],"str",1)
						cardmarkers(args.cards[index],"powicon",1)
						break
			if "Knight." in args.cards[index].traits and args.toGroups[index].name == "Table" and args.fromGroups[index].name != "Table" and args.cards[index].controller == me and args.cards[index].filter != WaitColor:
				i = 0
				for cardadd in table:
					if cardadd.controller == me and "Knight." in cardadd.traits and cardadd.filter != WaitColor and cardadd._id != args.cards[index]._id:
						i += 1
				if i == 1:
					for cardaddd in table:
						if cardaddd.controller == me and cardaddd.model == "fdf1989a-ee7d-4972-9d12-b299bfe3ba6d" and cardaddd._id != args.cards[index]._id and cardaddd not in noprint_turn:
							cardmarkers(cardaddd,"str",1)
							cardmarkers(cardaddd,"powicon",1)
			if "Knight." in args.cards[index].traits and args.toGroups[index].name != "Table" and args.fromGroups[index].name == "Table" and args.cards[index].controller == me and args.cards[index].filter != WaitColor:
				i = 0
				for cardadd in table:
					if cardadd.controller == me and "Knight." in cardadd.traits and cardadd.filter != WaitColor and cardadd._id != args.cards[index]._id:
						i += 1
				if i == 1:
					for cardaddd in table:
						if cardaddd.controller == me and cardaddd.model == "fdf1989a-ee7d-4972-9d12-b299bfe3ba6d" and cardaddd not in noprint_turn:
							cardmarkers(cardaddd,"str",-1)
							cardmarkers(cardaddd,"powicon",-1)
			if args.cards[index].model == "91b7190f-d0ba-4c3b-b9e2-5e7d2c872acb" and args.toGroups[index].name == "Table" and args.fromGroups[index].name != "Table" and args.cards[index].controller == me and args.cards[index].filter != WaitColor:
				for cardadd in table:
					if cardadd.controller == me and "Drowned God." in cardadd.traits and cardadd.filter != WaitColor and cardadd._id != args.cards[index]._id:
						cardmarkers(cardadd,"str",1)
					elif cardadd._id == args.cards[index]._id:
						for cardaddd in table:
							if cardaddd.model == "91b7190f-d0ba-4c3b-b9e2-5e7d2c872acb" and cardaddd.controller == me:
								cardmarkers(cardadd,"str",1)
			if args.cards[index].model != "91b7190f-d0ba-4c3b-b9e2-5e7d2c872acb" and args.toGroups[index].name == "Table" and args.fromGroups[index].name != "Table" and args.cards[index].controller == me and args.cards[index].filter != WaitColor:
				if "Drowned God." in args.cards[index].traits:
					for cardadd in table:
						if cardadd.model == "91b7190f-d0ba-4c3b-b9e2-5e7d2c872acb" and cardadd.controller == me:
							cardmarkers(args.cards[index],"str",1)
			if args.cards[index].model == "91b7190f-d0ba-4c3b-b9e2-5e7d2c872acb" and args.toGroups[index].name != "Table" and args.fromGroups[index].name == "Table" and args.cards[index].controller == me and args.cards[index].filter != WaitColor and args.cards[index] not in noprint_turn:
					for cardaddd in table:
						if "Drowned God." in cardaddd.traits and cardaddd.controller == me:
							cardmarkers(cardaddd,"str",-1)
			if args.cards[index].model == "a5512893-cf5c-4e54-a8a7-87114492a50b" and args.toGroups[index].name == "Table" and args.fromGroups[index].name != "Table" and args.cards[index].controller == me and args.cards[index].filter != WaitColor:
				for cardaddd in table:
					if cardaddd.model == "597acd7c-3424-4e8c-82e6-d6682d662c8c" and cardaddd.controller == me and cardaddd.filter != WaitColor:
						for cardadd in table:
							if cardadd.controller == me and cardadd.model == "a5512893-cf5c-4e54-a8a7-87114492a50b" and cardadd.filter != WaitColor and cardadd not in noprint_turn:
								cardmarkers(cardadd,"str",1)
								cardmarkers(cardadd,"inticon",1)
							if cardadd.controller == me and cardadd.model == "597acd7c-3424-4e8c-82e6-d6682d662c8c" and cardadd.filter != WaitColor and cardadd not in noprint_turn:
								cardmarkers(cardadd,"str",1)
								cardmarkers(cardadd,"powicon",1)

			if args.cards[index].model == "597acd7c-3424-4e8c-82e6-d6682d662c8c" and args.toGroups[index].name == "Table" and args.fromGroups[index].name != "Table" and args.cards[index].controller == me and args.cards[index].filter != WaitColor:
				for cardaddd in table:
					if cardaddd.model == "a5512893-cf5c-4e54-a8a7-87114492a50b" and cardaddd.controller == me and cardaddd.filter != WaitColor:
						for cardadd in table:
							if cardadd.controller == me and cardadd.model == "a5512893-cf5c-4e54-a8a7-87114492a50b" and cardadd.filter != WaitColor and cardadd not in noprint_turn:
								cardmarkers(cardadd,"inticon",1)
							if cardadd.controller == me and cardadd.model == "597acd7c-3424-4e8c-82e6-d6682d662c8c" and cardadd.filter != WaitColor and cardadd not in noprint_turn:
								cardmarkers(cardadd,"str",1)
								cardmarkers(cardadd,"powicon",1)

			if args.cards[index].model in ("597acd7c-3424-4e8c-82e6-d6682d662c8c","a5512893-cf5c-4e54-a8a7-87114492a50b") and args.toGroups[index].name != "Table" and args.fromGroups[index].name == "Table" and args.cards[index].controller == me and args.cards[index].filter != WaitColor:
					for cardadd in table:
						if cardadd.controller == me and cardadd.model == "a5512893-cf5c-4e54-a8a7-87114492a50b" and cardadd.filter != WaitColor and cardadd not in noprint_turn:
							cardmarkers(cardadd,"str",-1)
							cardmarkers(cardadd,"inticon",-1)
						if cardadd.controller == me and cardadd.model == "597acd7c-3424-4e8c-82e6-d6682d662c8c" and cardadd.filter != WaitColor and cardadd not in noprint_turn:
							cardmarkers(cardadd,"str",-1)
							cardmarkers(cardadd,"powicon",-1)

			if args.cards[index].model == "cbeb3a37-d4c1-4697-b8d2-e366b4569002" and args.toGroups[index].name == "Table" and args.fromGroups[index].name != "Table" and args.cards[index].controller == me and args.cards[index].filter != WaitColor and args.cards[index] not in noprint_turn:
				for cardadd in table:
					if cardadd.controller == me and "Warship" in cardadd.traits:cardmarkers(args.cards[index],"str",1)
			if args.cards[index].model == "3e1a5952-f5d1-4bca-9226-2b94531cfa54" and args.toGroups[index].name == "Table" and args.fromGroups[index].name != "Table" and args.cards[index].controller == me and args.cards[index].filter != WaitColor and args.cards[index] not in noprint_turn:
				for cardadd in table:
					if cardadd.controller == me and "The Reach" in cardadd.traits:cardmarkers(args.cards[index],"str",1)
			if args.cards[index].Faction == "Night's Watch." and args.cards[index].type == "Character" and args.toGroups[index].name == "Table" and args.fromGroups[index].name != "Table" and args.cards[index].controller == me and args.cards[index].filter != WaitColor:
				for cardadd in table:
					if cardadd.controller == me and cardadd.model == "5d20e021-5d12-4338-8bdd-42d008bff919" and cardadd.filter != WaitColor and cardadd not in noprint_turn:cardmarkers(args.cards[index],"str",1)
			if args.cards[index].model == "390a8cf7-8bc4-45c1-bea5-e6a694e9f2d5" and args.toGroups[index].name == "Table" and args.fromGroups[index].name != "Table" and args.cards[index].controller == me and args.cards[index].filter != WaitColor:args.cards[index].markers[STR_Up] += me.counters['Gold'].value
			if args.cards[index].model == "c41d4a72-6919-4e32-97ef-a4b0f1acb281" and args.toGroups[index].name == "Table" and args.fromGroups[index].name != "Table" and args.cards[index].controller == me and args.cards[index].filter != WaitColor and args.cards[index] not in noprint_turn:
				for cardadd in table:
					if cardadd.controller == me and cardadd.model != "c41d4a72-6919-4e32-97ef-a4b0f1acb281" and "Direwolf" in cardadd.traits:cardmarkers(args.cards[index],"str",1)
					if cardadd.controller == me and cardadd.model == "c41d4a72-6919-4e32-97ef-a4b0f1acb281" and args.cards[index]._id != cardadd._id:
						for cardadd2 in table:
							if cardadd2.model == "c41d4a72-6919-4e32-97ef-a4b0f1acb281" and cardadd2._id != cardadd._id and cardadd2._id != args.cards[index]._id and cardadd2 not in noprint_turn:cardmarkers(cardadd2,"str",-1)
					if cardadd.controller == me and cardadd.model == "c41d4a72-6919-4e32-97ef-a4b0f1acb281":
						for cardadd2 in table:
							if cardadd2.model == "c41d4a72-6919-4e32-97ef-a4b0f1acb281" and cardadd2._id != cardadd._id and cardadd2 not in noprint_turn:cardmarkers(cardadd2,"str",1)
			if args.cards[index].model == "c41d4a72-6919-4e32-97ef-a4b0f1acb281" and args.toGroups[index].name != "Table" and args.fromGroups[index].name == "Table" and args.cards[index].controller == me and args.cards[index].filter != WaitColor:
				for cardadd in table:
					if cardadd.controller == me and cardadd.model == "c41d4a72-6919-4e32-97ef-a4b0f1acb281" and args.cards[index]._id != cardadd._id:cardmarkers(cardadd,"str",-1)
			if args.cards[index].model != "c41d4a72-6919-4e32-97ef-a4b0f1acb281" and args.toGroups[index].name == "Table" and args.fromGroups[index].name != "Table" and args.cards[index].controller == me and args.cards[index].filter != WaitColor:
				if "Direwolf" in args.cards[index].traits:
					for cardadd in table:
						if cardadd.controller == me and cardadd.model == "c41d4a72-6919-4e32-97ef-a4b0f1acb281" and cardadd not in noprint_turn:cardadd.markers[STR_Up] += 1
			if args.cards[index].model == "c41d4a72-6919-4e32-97ef-a4b0f1acb281" and args.toGroups[index].name == "Table" and args.fromGroups[index].name != "Table" and args.cards[index].controller == me and args.cards[index].filter != WaitColor and args.cards[index] in noprint_turn:
				if "Direwolf" in args.cards[index].traits:
					for cardadd in table:
						if cardadd.controller == me and cardadd.model == "c41d4a72-6919-4e32-97ef-a4b0f1acb281" and cardadd not in noprint_turn:cardadd.markers[STR_Up] += 1
			if args.cards[index].model != "c41d4a72-6919-4e32-97ef-a4b0f1acb281" and args.toGroups[index].name != "Table" and args.fromGroups[index].name == "Table" and args.cards[index].controller == me and args.cards[index].filter != WaitColor:
				if "Direwolf" in args.cards[index].traits:
					for cardadd in table:
						if cardadd.controller == me and cardadd.model == "c41d4a72-6919-4e32-97ef-a4b0f1acb281" and cardadd not in noprint_turn:cardmarkers(cardadd,"str",-1)
			if args.cards[index].type == "Location" and args.toGroups[index].name == "Table" and args.fromGroups[index].name != "Table" and args.cards[index].controller == me and args.cards[index].filter != WaitColor:
				if "Warship" in args.cards[index].traits:
					for cardadd in table:
						if cardadd.controller == me and cardadd.model == "cbeb3a37-d4c1-4697-b8d2-e366b4569002" and cardadd not in noprint_turn:cardmarkers(cardadd,"str",1)
				if "The Reach" in args.cards[index].traits:
					for cardadd in table:
						if cardadd.controller == me and cardadd.model == "3e1a5952-f5d1-4bca-9226-2b94531cfa54" and cardadd not in noprint_turn:cardmarkers(cardadd,"str",1)
			if args.cards[index].type == "Location" and args.toGroups[index].name != "Table" and args.fromGroups[index].name == "Table" and args.cards[index].controller == me and args.cards[index].filter != WaitColor:
				if "Warship" in args.cards[index].traits:
					for cardadd in table:
						if cardadd.controller == me and cardadd.model == "cbeb3a37-d4c1-4697-b8d2-e366b4569002" and cardadd not in noprint_turn:cardmarkers(cardadd,"str",-1)
				if "The Reach" in args.cards[index].traits:
					for cardadd in table:
						if cardadd.controller == me and cardadd.model == "3e1a5952-f5d1-4bca-9226-2b94531cfa54" and cardadd not in noprint_turn:cardmarkers(cardadd,"str",-1)

		index += 1

def setTimer(player,actioninsert,group,x = 0,y = 0):
    global timerIsRunning
    if player != me:return
    debug(actioninsert)
    if timerIsRunning:
        whisper("You cannot start a new timer until the current one finishes!")
        return
    timerIsRunning = True
    if actioninsert in ("plotshow","actionshow","actionshowall"):seconds = 4
    else:seconds = 2
    #whisper("please action in {} seconds.".format(seconds%60))
    notifications = range(11) + [30] + [x*60 for x in range(seconds/60+1)][1:]
    endTime = time.time() + seconds
    notifications = [endTime - t for t in notifications if t < seconds]
    updateTimer(endTime,notifications,actioninsert)

#This function checks the timer, and then remotecalls itself if the timer has not finished
def updateTimer(endTime,notifications,actioninsert):
    mute()
    global timerIsRunning
    global interruptreactioncard
    global isinsertreaction
    global cardtoaction
    global plotcard
    global sessionpass
    list = []
    currentTime = time.time()
    if currentTime>notifications[-1]:
            timeLeft = int(endTime - notifications[-1])
            #if timeLeft > 60: whisper("{} minutes left!".format(timeLeft/60))
            #else: whisper("{} seconds left!".format(timeLeft))
            notifications.remove(notifications[-1])
    if notifications: remoteCall(me,"updateTimer",[endTime,notifications,actioninsert])
    else:
		timerIsRunning = False
		if actioninsert == "interruptcancel":
			debug(inserttarget)
			debug(savetarget)
			debug(sessionpass)
			if sessionpass in ("3playeraddstr2selectok","kneel4cadd1powercselectok"):
				for arrowcard in cardtoaction:
					inserttarget.arrow(arrowcard)
			else:inserttarget.arrow(savetarget)
			remoteCall(players[1],"savetargetinserttarget",[savetarget,inserttarget,interruptcancelcard,interruptcancelplayer,interruptcancellastcard,interruptcanceledcard,interruptcancelok,saveactionplayer,mainpass])
			remoteCall(players[1], "interruptevent", ["interruptcancel",2])
		if actioninsert == "interruptcanceled":
			if interruptcancellastcard == []:
				interruptcanceledcard.arrow(inserttarget)
			else:interruptcanceledcard.arrow(interruptcancellastcard)
			remoteCall(otherplayer,"savetargetinserttarget",[savetarget,inserttarget,interruptcancelcard,interruptcancelplayer,interruptcancellastcard,interruptcanceledcard,interruptcancelok,saveactionplayer,mainpass])
			remoteCall(otherplayer,"interruptlibadd",[interruptpass])
			remoteCall(otherplayer, "interruptevent", ["interruptcancel",2])
		if actioninsert == "reactionaftuok":
			selectedcard[0].arrow(cardtoaction)
			reaction("aftercalculate",1)
		if actioninsert == "keywords":
			keywordforability(2)
		if actioninsert == "Confiscationselect":
			remoteCall(cardtoaction.controller,"disc",[cardtoaction])
			notify("{} reaveled {}, discard {} from play.".format(me,plotcard,cardtoaction))#Confiscation
			plotcard.target(False)
			cardtoaction = []
			plotcard = []
		if actioninsert == "FilthyAccusationsselect":
			remoteCall(cardtoaction.controller, "kneel", [cardtoaction])
			notify("{} reaveled {}, kneel {}.".format(me,plotcard,cardtoaction))#FilthyAccusations
			plotcard.target(False)
			cardtoaction = []
			plotcard = []
		if actioninsert == "plotshow":
			plotcard.moveTo(me.hand)
			cardtoaction = []
			plotcard = []
		if actioninsert == "actionshow":
			for c in plotcard:
				c.moveTo(me.hand)
			cardtoaction = []
			plotcard = []
		if actioninsert == "actionshowall":
			plotcard.moveTo(me.hand)
			cardtoaction = []
			plotcard = []

		if actioninsert in ("FilthyAccusationsselect","Confiscationselect","plotshow"):
			sessionpass = ""
			if getGlobalVariable("reavelplot") == "1":
				setGlobalVariable("reavelplot","2")
				if str(me._id) == getGlobalVariable("firstreveal"):remoteCall(players[1], "reavelplot", table)
				else:reavelplot(table)
				return
			if getGlobalVariable("reavelplot") == "2":
				if fplay(1) == me:actiongeneral(1)
				else:remoteCall(players[1], "actiongeneral", 1)
		if actioninsert in ("actionshow","actionshowall"):
			if sessionpass == "marshalaction":remoteCall(players[1], "action", ["marshal",1])
			if sessionpass == "generalaction":remoteCall(players[1], "action", ["general",1])
			if sessionpass == "dominanceaction":remoteCall(players[1], "action", ["dominance",1])
			sessionpass = ""


def interruptevent(actioninsert,interruptpasscount):
	mute()
	global interruptpass
	global savetarget
	global inserttarget
	global interruptcancelplayer
	global interruptcancelcard
	global interruptcancelok
	global interruptlib
	global interruptcanceledcard
	global interruptcancellastcard
	global saveactionplayer
	global sessionpass
	global leavecardtype
	global abilityattach
	global reactionattach
	global isinsertreaction
	global interruptreactioncard
	global interruptpasscounttmp
	global interruptsessionpass
	savetargets = []
	inserttargets = []
	interruptcards = []
	list = []
	list2 = []
	list3 = []
	list4= []
	listcancel = []
	Faction = ""
	duplicate = 0
	sourcecard = []
	duplicatecard = []
	cardtype = ""
	tmp = []
	debug(mainpass)
	if actioninsert == "miljudgementfp":
		debug(interruptpasscount)
		for card in mjfinishcard:
			if card.highlight == miljudgecolor:
				list2.append(card)
		if len(list2) > 0:
			if sessionpass == "":
				choiceList = ['save player', 'cancel and do not save']
				colorList = ['#006b34' ,'#ae0603']
				choice = askChoice("Which Pass do you want to action?", choiceList,colorList)
				if choice == 1:
					intointerruptevent(interruptpasscount)
					return
				else:
					if interruptpasscount == 2:
						f = (card for card in table  
							if card.name == "1st Player Token")
						for card1 in f:
							if card1.controller == me:miljudgementfinished(mjfinishcard,claimtmp,1)
							else:remoteCall(otherplayer, "miljudgementfinished", [mjfinishcard,claimtmp,1])
					else:
						interruptpasscount += 1
						remoteCall(otherplayer, "interruptevent", ["miljudgementfp",interruptpasscount])
					return
			if sessionpass == "miljudgementselectok":
				savetargets = selectedcard
				if savetargets == []:
					if interruptpasscount == 2:
						f = (card for card in table  
							if card.name == "1st Player Token")
						for card1 in f:
							if card1.controller == me:miljudgementfinished(mjfinishcard,claimtmp,1)
							else:remoteCall(otherplayer, "miljudgementfinished", [mjfinishcard,claimtmp,1])
					else:
						interruptpasscount += 1
						remoteCall(otherplayer, "interruptevent", ["miljudgementfp",interruptpasscount])
					sessionpass = ""
					return
			if sessionpass == "savecardselectok":	
				inserttargets = selectedcard
				if inserttargets == []:
					if interruptpasscount == 2:
						f = (card for card in table  
						if card.name == "1st Player Token")
						for card1 in f:
							if card1.controller == me:miljudgementfinished(mjfinishcard,claimtmp,1)
							else:remoteCall(otherplayer, "miljudgementfinished", [mjfinishcard,claimtmp,1])
					else:
						interruptpasscount += 1
						sessionpass = ""
						remoteCall(otherplayer, "interruptevent", ["miljudgementfp",interruptpasscount])
					return
				else:
					#inserttarget = inserttargets
					sessionpass = ""
					for card in inserttargets:
						if card.filter == WaitColor:
							savetarget.highlight = None
							disc(card)
							remoteCall(otherplayer, "interruptevent", ["miljudgementfp",interruptpasscount])
							return
						else:
							if card.type == "Event":
								if play(card):cardeffect(card,"saveaction")
								else:
									remoteCall(me, "interruptevent", ["miljudgementfp",interruptpasscount])
									return
							else:cardeffect(card,"saveaction")
							interruptcancelcard = card
						interruptcancelplayer = me
						saveactionplayer = me
						inserttarget = interruptcancelcard
						#interruptlib.append(interruptcancelcard)
						remoteCall(me, "setTimer", [me,"interruptcancel",table])
			else:
				if interruptpasscount < 2:
					interruptpasscount += 1
					remoteCall(otherplayer, "interruptevent", ["miljudgementfp",interruptpasscount])
					return
				if interruptpasscount == 2 and actioninsert == "miljudgementfp":
					f = (card for card in table  
						if card.name == "1st Player Token")
					for card1 in f:
						if card1.controller == me:miljudgementfinished(mjfinishcard,claimtmp,1)
						else:remoteCall(otherplayer, "miljudgementfinished", [mjfinishcard,claimtmp,1])
		else:
			f = (card for card in table  
				if card.name == "1st Player Token")
			for card1 in f:
				if card1.controller == me:miljudgementfinished(mjfinishcard,claimtmp,1)
				else:remoteCall(otherplayer, "miljudgementfinished", [mjfinishcard,claimtmp,1])
	if actioninsert == "interruptcancel":
		choice = 0
		debug(interruptcancelcard)
		debug(interruptlib)
		if checkcountercharater(interruptcancelcard) and interruptsessionpass == "":
			if interruptpasscount < 2:
				choiceList = ['interrupt', 'cancel']
				colorList = ['#ae0603' ,'#006b34']
				choice = askChoice("Do you want to interrupt {}'s {} ?".format(interruptcancelplayer,interruptcancelcard.name), choiceList,colorList)
			if interruptpasscount == 2:
				choiceList = ['interrupt', 'cancel']
				colorList = ['#ae0603' ,'#006b34']
				choice = askChoice("Do you want to interrupt {}'s {} ?".format(interruptcancelplayer,interruptcancelcard.name), choiceList,colorList)
		else:
			if interruptsessionpass == "":choice = 2
		if choice == 1 or interruptsessionpass != "":
			if interruptsessionpass == "":
				for c in me.hand:
					ee = 0
					for d in counterevent:
						if counterevent[d][3] == "Hand" and c.model == counterevent[d][1] and counterevent[d][4].find(interruptcancelcard.Type) != -1:
							if counterevent[d][5] == "all":
								if counterevent[d][7] == "opponent" and interruptcancelcard.controller != me:ee = 1
								elif counterevent[d][7] == "all":ee = 1
							elif counterevent[d][5] != "all":
								for cardunique in table:
									if cardunique.Faction == counterevent[d][5] and cardunique.Unique == counterevent[d][6]:
										if counterevent[d][7] == "opponent" and interruptcancelcard.controller != me:ee = 1
										elif counterevent[d][7] == "all":ee = 1
					if ee == 1:listcancel.append(c)
				for c in table:
					ee = 0
					for d in counterevent:
						if counterevent[d][3] == "table" and c.model == counterevent[d][1] and c.controller == me and counterevent[d][4].find(interruptcancelcard.Type) != -1 and c.highlight == None:
							if counterevent[d][5] == "all":
								if counterevent[d][7] == "opponent" and interruptcancelcard.controller != me:ee = 1
								elif counterevent[d][7] == "all":ee = 1
							elif counterevent[d][5] != "all":
								for cardunique in table:
									if cardunique.Faction == counterevent[d][5] and cardunique.Unique == counterevent[d][6]:
										if counterevent[d][7] == "opponent" and interruptcancelcard.controller != me:ee = 1
										elif counterevent[d][7] == "all":ee = 1
					if ee == 1:listcancel.append(c)
				interruptpasscounttmp = interruptpasscount
				targetTuple = [card._id for card in listcancel]
				selectcardnext(targetTuple,"selectinterruptcard",table,[],"",1,interrupt = 1,actionstyle = 1)
				return
				# dlg = cardDlg(listcancel)
				# dlg.title = "These cards are you can used:"
				# dlg.text = "Declares 1 card to used.  click close button if none or cancel"
				# dlg.min = 1
				# dlg.max = 1
				# interruptcards = dlg.show()
			interruptcards = interruptcardselect
			interruptsessionpass = ""
			if interruptcards == None:
				if interruptpasscount == 2:
					if len(interruptlib) > 0 and interruptcancellastcard != []:
						e = 0
						if interruptlib["pass"+str(interruptpass)][0].highlight == sacrificecolor:
							playertmp = []
							cardtmp = []
							if isinsertreaction == 0 and orientationintable(interruptlib["pass"+str(interruptpass)][0]):
								if checkinsertreaction(interruptlib["pass"+str(interruptpass)][0]):
									isinsertreaction = 1
									playertmp = interruptlib["pass"+str(interruptpass)][0].controller
									cardtmp = insertreactioncard
									e = 1
						if interruptlib["pass"+str(interruptpass)][0].controller == me:disc(interruptlib["pass"+str(interruptpass)][0])
						else:remoteCall(otherplayer, "disc", [interruptlib["pass"+str(interruptpass)][0]])
						del interruptlib["pass"+str(interruptpass)]
						remoteCall(otherplayer,"interruptlibdel",[interruptpass])
						interruptpass -= 1
						if e == 1:
							setGlobalVariable("insertre", "1")
							backupinterruptlib(1)
							remoteCall(otherplayer, "backupinterruptlib", [1])
							remoteCall(playertmp, "interruptreaction", [cardtmp,1])
							return
						if interruptpass > 0:
							e = 0
							if interruptlib["pass"+str(interruptpass)][0].highlight == sacrificecolor:
								playertmp = []
								cardtmp = []
								if isinsertreaction == 0 and orientationintable(interruptlib["pass"+str(interruptpass)][0]):
									if checkinsertreaction(interruptlib["pass"+str(interruptpass)][0]):
										isinsertreaction = 1
										playertmp = interruptlib["pass"+str(interruptpass)][0].controller
										cardtmp = insertreactioncard
										e = 1
							if interruptlib["pass"+str(interruptpass)][0].controller == me:disc(interruptlib["pass"+str(interruptpass)][0])
							else:remoteCall(otherplayer, "disc", [interruptlib["pass"+str(interruptpass)][0]])
							del interruptlib["pass"+str(interruptpass)]
							remoteCall(otherplayer,"interruptlibdel",[interruptpass])
							interruptpass -= 1
							if e == 1:
								setGlobalVariable("insertre", "2")
								backupinterruptlib(1)
								remoteCall(otherplayer, "backupinterruptlib", [1])
								remoteCall(playertmp, "interruptreaction", [cardtmp,1])
								return
						if interruptpass == 0:
							notify("over,disc card")
							debug(inserttarget)
							debug(interruptcancelok)
							if mainpass == "leave":
								if interruptcancelok == 1:
									leavecardtype.append(inserttarget._id)
									remoteCall(inserttarget.controller,"leaveforability",[inserttarget])
								else:
									remoteCall(inserttarget.controller,"abilityattachsub",[inserttarget])
									if inserttarget.controller == me:remoteCall(otherplayer, "interruptevent", ["characterkill",1])
									else:interruptevent("characterkill",1)
							elif mainpass == "leavereaction":
								if interruptcancelok == 1:
									remoteCall(inserttarget.controller,"reactionforability",[inserttarget,mainpass])
								else:
									remoteCall(inserttarget.controller,"reactionattachsub",[inserttarget])
									if inserttarget.controller == me:remoteCall(otherplayer, "reaction", ["leavetable",1])
									else:reaction("leavetable",1)
							elif mainpass == "afterchallenge":
								if interruptcancelok == 1:
									remoteCall(inserttarget.controller,"reactionforability",[inserttarget,mainpass])
								else:
									remoteCall(inserttarget.controller,"reactionattachsub",[inserttarget])
									if inserttarget.controller == me:remoteCall(otherplayer, "reaction", ["afterchallenge",1])
									else:reaction("afterchallenge",1)
							elif mainpass == "aftercalculate":
								if inserttarget.type == "Event":
									if inserttarget.controller == me:disc(inserttarget)
									else:remoteCall(otherplayer, "disc", [inserttarget])
								if interruptcancelok == 1:
									remoteCall(inserttarget.controller,"reactionforability",[inserttarget,mainpass])
								else:
									for card in table:
										card.target(False)
									remoteCall(inserttarget.controller,"reactionattachsub",[inserttarget])
									if inserttarget.controller == me:remoteCall(otherplayer, "reaction", ["aftercalculate",1])
									else:reaction("aftercalculate",1)
							elif mainpass in("dominancestart","dominancewin","dominanceend"):
								if inserttarget.type == "Event":
									if inserttarget.controller == me:disc(inserttarget)
									else:remoteCall(otherplayer, "disc", [inserttarget])
								if interruptcancelok == 1:
									remoteCall(inserttarget.controller,"reactionforability",[inserttarget,mainpass])
								else:
									for card in table:
										card.target(False)
									remoteCall(inserttarget.controller,"reactionattachsub",[inserttarget])
									if inserttarget.controller == me:remoteCall(otherplayer, "reaction", [mainpass,1])
									else:reaction(mainpass,1)
							elif mainpass == "challengeaction":
								if inserttarget.type == "Event":
									if inserttarget.controller == me:disc(inserttarget)
									else:remoteCall(otherplayer, "disc", [inserttarget])
								if interruptcancelok == 1:
									remoteCall(inserttarget.controller,"actionforability",[inserttarget,mainpass])
								else:
									for card in table:
										card.target(False)
									remoteCall(inserttarget.controller,"actionattachsub",[inserttarget])
									if inserttarget.controller == me:remoteCall(otherplayer, "action", ["challenge",1])
									else:action("challenge",1)
							elif mainpass == "generalaction":
								if inserttarget.type == "Event":
									if inserttarget.controller == me:disc(inserttarget)
									else:remoteCall(otherplayer, "disc", [inserttarget])
								if interruptcancelok == 1:
									remoteCall(inserttarget.controller,"actionforability",[inserttarget,mainpass])
								else:
									for card in table:
										card.target(False)
										if card.filter == showtablecolor:
											remoteCall(card.controller,"returncard",[card])
									remoteCall(inserttarget.controller,"actionattachsub",[inserttarget])
									if inserttarget.controller == me:remoteCall(otherplayer, "action", ["general",1])
									else:action("general",1)
							elif mainpass == "dominanceaction":
								if inserttarget.type == "Event":
									if inserttarget.controller == me:disc(inserttarget)
									else:remoteCall(otherplayer, "disc", [inserttarget])
								if interruptcancelok == 1:
									remoteCall(inserttarget.controller,"actionforability",[inserttarget,mainpass])
								else:
									for card in table:
										card.target(False)
										if card.filter == showtablecolor:
											remoteCall(card.controller,"returncard",[card])
									remoteCall(inserttarget.controller,"actionattachsub",[inserttarget])
									if inserttarget.controller == me:remoteCall(otherplayer, "action", ["dominance",1])
									else:action("dominance",1)
							elif mainpass == "marshalaction":
								if inserttarget.type == "Event":
									if inserttarget.controller == me:disc(inserttarget)
									else:remoteCall(otherplayer, "disc", [inserttarget])
								if interruptcancelok == 1:
									remoteCall(inserttarget.controller,"actionforability",[inserttarget,mainpass])
								else:
									for card in table:
										card.target(False)
										if card.filter == showtablecolor:
											remoteCall(card.controller,"returncard",[card])
									remoteCall(inserttarget.controller,"actionattachsub",[inserttarget])
									if inserttarget.controller == me:remoteCall(otherplayer, "action", ["marshal",1])
									else:action("marshal",1)
							elif mainpass in("reactionmarshal"):
								if inserttarget.type == "Event":
									if inserttarget.controller == me:disc(inserttarget)
									else:remoteCall(otherplayer, "disc", [inserttarget])
								if interruptcancelok == 1:
									remoteCall(inserttarget.controller,"reactionforability",[inserttarget,mainpass])
								else:
									for card in table:
										card.target(False)
									remoteCall(inserttarget.controller,"reactionattachsub",[inserttarget])
									if inserttarget.controller == me:remoteCall(otherplayer, "action", ["marshal",1])
									else:action("marshal",1)
							elif mainpass in("reactionplot"):
								if inserttarget.type == "Event":
									if inserttarget.controller == me:disc(inserttarget)
									else:remoteCall(otherplayer, "disc", [inserttarget])
								if interruptcancelok == 1:
									remoteCall(inserttarget.controller,"reactionforability",[inserttarget,mainpass])
								else:
									for card in table:
										card.target(False)
									remoteCall(inserttarget.controller,"reactionattachsub",[inserttarget])
									askfirstreveal(table)
							else:
								if interruptcancelok == 1:
									savetarget.highlight = milsavecolor
									savepassfinish(1)
								else:
									if inserttarget.controller == me:disc(inserttarget)
									else:remoteCall(otherplayer, "disc", [inserttarget])
								notify("ballanceover")
								if saveactionplayer == me:remoteCall(otherplayer, "interruptevent", ["miljudgementfp",1])
								else :remoteCall(me, "interruptevent", ["miljudgementfp",1])
						else:
							interruptcancellastcard = interruptlib["pass"+str(interruptpass)][1]
							interruptcanceledcard = interruptlib["pass"+str(interruptpass)][0]
							interruptcancelcard = interruptcanceledcard
							remoteCall(otherplayer,"savetargetinserttarget",[savetarget,inserttarget,interruptcancelcard,interruptcancelplayer,interruptcancellastcard,interruptcanceledcard,interruptcancelok,saveactionplayer,mainpass])
							if interruptlib["pass"+str(interruptpass)][2] == me:remoteCall(otherplayer, "interruptevent", ["interruptcancel",1])
							else:remoteCall(me, "interruptevent", ["interruptcancel",1])
					else:
						if interruptpass > 0:
							e = 0
							if interruptlib["pass"+str(interruptpass)][0].highlight == sacrificecolor:
								playertmp = []
								cardtmp = []
								if isinsertreaction == 0 and orientationintable(interruptlib["pass"+str(interruptpass)][0]):
									if checkinsertreaction(interruptlib["pass"+str(interruptpass)][0]):
										isinsertreaction = 1
										playertmp = interruptlib["pass"+str(interruptpass)][0].controller
										cardtmp = insertreactioncard
										e = 1
							if interruptlib["pass"+str(interruptpass)][0].controller == me:disc(interruptlib["pass"+str(interruptpass)][0])
							else:remoteCall(otherplayer, "disc", [interruptlib["pass"+str(interruptpass)][0]])
							del interruptlib["pass"+str(interruptpass)]
							remoteCall(otherplayer,"interruptlibdel",[interruptpass])
							interruptpass -= 1
							if e == 1:
								setGlobalVariable("insertre", "3")
								backupinterruptlib(1)
								remoteCall(otherplayer, "backupinterruptlib", [1])
								remoteCall(playertmp, "interruptreaction", [cardtmp,1])
								return
						notify("over,disc card")
						debug(interruptcancelok)
						debug(inserttarget)
						if mainpass == "leave":
							if interruptcancelok == 1:
								leavecardtype.append(inserttarget._id)
								remoteCall(inserttarget.controller,"leaveforability",[inserttarget])
							else:
								remoteCall(inserttarget.controller,"abilityattachsub",[inserttarget])
								if inserttarget.controller == me:remoteCall(otherplayer, "interruptevent", ["characterkill",1])
								else:interruptevent("characterkill",1)
						elif mainpass == "leavereaction":
							if interruptcancelok == 1:
								remoteCall(inserttarget.controller,"reactionforability",[inserttarget,mainpass])
							else:
								remoteCall(inserttarget.controller,"reactionattachsub",[inserttarget])
								if inserttarget.controller == me:remoteCall(otherplayer, "reaction", ["leavetable",1])
								else:reaction("leavetable",1)
						elif mainpass == "afterchallenge":
							if interruptcancelok == 1:
								remoteCall(inserttarget.controller,"reactionforability",[inserttarget,mainpass])
							else:
								remoteCall(inserttarget.controller,"reactionattachsub",[inserttarget])
								if inserttarget.controller == me:remoteCall(otherplayer, "reaction", ["afterchallenge",1])
								else:reaction("afterchallenge",1)
						elif mainpass == "aftercalculate":
							if inserttarget.type == "Event":
								if inserttarget.controller == me:disc(inserttarget)
								else:remoteCall(otherplayer, "disc", [inserttarget])
							if interruptcancelok == 1:
								remoteCall(inserttarget.controller,"reactionforability",[inserttarget,mainpass])
							else:
								for card in table:
										card.target(False)
								remoteCall(inserttarget.controller,"reactionattachsub",[inserttarget])
								if inserttarget.controller == me:remoteCall(otherplayer, "reaction", ["aftercalculate",1])
								else:reaction("aftercalculate",1)
						elif mainpass in("dominancestart","dominancewin","dominanceend"):
							if inserttarget.type == "Event":
								if inserttarget.controller == me:disc(inserttarget)
								else:remoteCall(otherplayer, "disc", [inserttarget])
							if interruptcancelok == 1:
								remoteCall(inserttarget.controller,"reactionforability",[inserttarget,mainpass])
							else:
								for card in table:
									card.target(False)
								remoteCall(inserttarget.controller,"reactionattachsub",[inserttarget])
								if inserttarget.controller == me:remoteCall(otherplayer, "reaction", [mainpass,1])
								else:reaction(mainpass,1)
						elif mainpass == "challengeaction":
							if inserttarget.type == "Event":
								if inserttarget.controller == me:disc(inserttarget)
								else:remoteCall(otherplayer, "disc", [inserttarget])
							if interruptcancelok == 1:
								remoteCall(inserttarget.controller,"actionforability",[inserttarget,mainpass])
							else:
								for card in table:
									card.target(False)
								remoteCall(inserttarget.controller,"actionattachsub",[inserttarget])
								if inserttarget.controller == me:remoteCall(otherplayer, "action", ["challenge",1])
								else:action("challenge",1)
						elif mainpass == "generalaction":
							if inserttarget.type == "Event":
								if inserttarget.controller == me:disc(inserttarget)
								else:remoteCall(otherplayer, "disc", [inserttarget])
							if interruptcancelok == 1:
								remoteCall(inserttarget.controller,"actionforability",[inserttarget,mainpass])
							else:
								for card in table:
									card.target(False)
									if card.filter == showtablecolor:
										remoteCall(card.controller,"returncard",[card])
								remoteCall(inserttarget.controller,"actionattachsub",[inserttarget])
								if inserttarget.controller == me:remoteCall(otherplayer, "action", ["general",1])
								else:action("general",1)
						elif mainpass == "dominanceaction":
							if inserttarget.type == "Event":
								if inserttarget.controller == me:disc(inserttarget)
								else:remoteCall(otherplayer, "disc", [inserttarget])
							if interruptcancelok == 1:
								remoteCall(inserttarget.controller,"actionforability",[inserttarget,mainpass])
							else:
								for card in table:
									card.target(False)
									if card.filter == showtablecolor:
										remoteCall(card.controller,"returncard",[card])
								remoteCall(inserttarget.controller,"actionattachsub",[inserttarget])
								if inserttarget.controller == me:remoteCall(otherplayer, "action", ["dominance",1])
								else:action("dominance",1)
						elif mainpass == "marshalaction":
							if inserttarget.type == "Event":
								if inserttarget.controller == me:disc(inserttarget)
								else:remoteCall(otherplayer, "disc", [inserttarget])
							if interruptcancelok == 1:
								remoteCall(inserttarget.controller,"actionforability",[inserttarget,mainpass])
							else:
								for card in table:
									card.target(False)
									if card.filter == showtablecolor:
										remoteCall(card.controller,"returncard",[card])
								remoteCall(inserttarget.controller,"actionattachsub",[inserttarget])
								if inserttarget.controller == me:remoteCall(otherplayer, "action", ["marshal",1])
								else:action("marshal",1)
						elif mainpass in("reactionmarshal"):
							if inserttarget.type == "Event":
								if inserttarget.controller == me:disc(inserttarget)
								else:remoteCall(otherplayer, "disc", [inserttarget])
							if interruptcancelok == 1:
								remoteCall(inserttarget.controller,"reactionforability",[inserttarget,mainpass])
							else:
								for card in table:
									card.target(False)
								remoteCall(inserttarget.controller,"reactionattachsub",[inserttarget])
								if inserttarget.controller == me:remoteCall(otherplayer, "action", ["marshal",1])
								else:action("marshal",1)
						elif mainpass in("reactionplot"):
							if inserttarget.type == "Event":
								if inserttarget.controller == me:disc(inserttarget)
								else:remoteCall(otherplayer, "disc", [inserttarget])
							if interruptcancelok == 1:
								remoteCall(inserttarget.controller,"reactionforability",[inserttarget,mainpass])
							else:
								for card in table:
									card.target(False)
								remoteCall(inserttarget.controller,"reactionattachsub",[inserttarget])
								askfirstreveal(table)
						else:		
							if interruptcancelok == 1:
								savetarget.highlight = milsavecolor
								savepassfinish(1)
							else:
								if inserttarget.type != "Character":
									if inserttarget.controller == me:disc(inserttarget)
									else:remoteCall(otherplayer, "disc", [inserttarget])
							notify("ballanceover")
							if saveactionplayer == me:remoteCall(otherplayer, "interruptevent", ["miljudgementfp",1])
							else :remoteCall(me, "interruptevent", ["miljudgementfp",1])
				else:
					interruptpasscount += 1
					remoteCall(otherplayer, "interruptevent", ["interruptcancel",interruptpasscount])
				return
			else:
				for card in interruptcards:
					if card.type == "Event":
						if play(card):cardeffect(card,"interrupt")
						else:
							remoteCall(me, "interruptevent", ["interruptcancel",interruptpasscount])
							return
					else:cardeffect(card,"interrupt")
					interruptcancelplayer = me
					interruptcancellastcard = interruptcanceledcard
					debug(interruptcancellastcard)
					interruptcanceledcard = card
					interruptcancelcard = card
					interruptpass += 1
					interruptlib["pass"+str(interruptpass)] = (interruptcanceledcard,interruptcancellastcard,me)
					debug(interruptlib)
				if interruptcancelok == 1:interruptcancelok = 0
				else:interruptcancelok = 1
				remoteCall(me, "setTimer", [me,"interruptcanceled",table])
		if choice == 2:
			if interruptpasscount < 2:
				interruptpasscount += 1
				remoteCall(otherplayer, "interruptevent", ["interruptcancel",interruptpasscount])
				return
			if interruptpasscount == 2 and actioninsert == "interruptcancel":
				if len(interruptlib) > 0 and interruptcancellastcard != []:
					e = 0
					if interruptlib["pass"+str(interruptpass)][0].highlight == sacrificecolor:
						playertmp = []
						cardtmp = []
						if isinsertreaction == 0 and orientationintable(interruptlib["pass"+str(interruptpass)][0]):
							if checkinsertreaction(interruptlib["pass"+str(interruptpass)][0]):
								isinsertreaction = 1
								playertmp = interruptlib["pass"+str(interruptpass)][0].controller
								cardtmp = insertreactioncard
								e = 1
					if interruptlib["pass"+str(interruptpass)][0].controller == me:disc(interruptlib["pass"+str(interruptpass)][0])
					else:remoteCall(otherplayer, "disc", [interruptlib["pass"+str(interruptpass)][0]])
					del interruptlib["pass"+str(interruptpass)]
					remoteCall(otherplayer,"interruptlibdel",[interruptpass])
					interruptpass -= 1
					if e == 1:
						setGlobalVariable("insertre", "1")
						backupinterruptlib(1)
						remoteCall(otherplayer, "backupinterruptlib", [1])
						remoteCall(playertmp, "interruptreaction", [cardtmp,1])
						return
					if interruptpass > 0:
						e = 0
						if interruptlib["pass"+str(interruptpass)][0].highlight == sacrificecolor:
							playertmp = []
							cardtmp = []
							if isinsertreaction == 0 and orientationintable(interruptlib["pass"+str(interruptpass)][0]):
								if checkinsertreaction(interruptlib["pass"+str(interruptpass)][0]):
									isinsertreaction = 1
									playertmp = interruptlib["pass"+str(interruptpass)][0].controller
									cardtmp = insertreactioncard
									e = 1
						if interruptlib["pass"+str(interruptpass)][0].controller == me:disc(interruptlib["pass"+str(interruptpass)][0])
						else:remoteCall(otherplayer, "disc", [interruptlib["pass"+str(interruptpass)][0]])
						del interruptlib["pass"+str(interruptpass)]
						remoteCall(otherplayer,"interruptlibdel",[interruptpass])
						interruptpass -= 1
						if e == 1:
							setGlobalVariable("insertre", "2")
							backupinterruptlib(1)
							remoteCall(otherplayer, "backupinterruptlib", [1])
							remoteCall(playertmp, "interruptreaction", [cardtmp,1])
							return
					if interruptpass == 0:
						notify("over,disc card")
						debug(inserttarget)
						debug(interruptcancelok)
						if mainpass == "leave":
							if interruptcancelok == 1:
								leavecardtype.append(inserttarget._id)
								remoteCall(inserttarget.controller,"leaveforability",[inserttarget])
							else:
								remoteCall(inserttarget.controller,"abilityattachsub",[inserttarget])
								if inserttarget.controller == me:remoteCall(otherplayer, "interruptevent", ["characterkill",1])
								else:interruptevent("characterkill",1)
						elif mainpass == "leavereaction":
							if interruptcancelok == 1:
								remoteCall(inserttarget.controller,"reactionforability",[inserttarget,mainpass])
							else:
								remoteCall(inserttarget.controller,"reactionattachsub",[inserttarget])
								if inserttarget.controller == me:remoteCall(otherplayer, "reaction", ["leavetable",1])
								else:reaction("leavetable",1)
						elif mainpass == "afterchallenge":
							if interruptcancelok == 1:
								remoteCall(inserttarget.controller,"reactionforability",[inserttarget,mainpass])
							else:
								remoteCall(inserttarget.controller,"reactionattachsub",[inserttarget])
								if inserttarget.controller == me:remoteCall(otherplayer, "reaction", ["afterchallenge",1])
								else:reaction("afterchallenge",1)
						elif mainpass == "aftercalculate":
							if inserttarget.type == "Event":
								if inserttarget.controller == me:disc(inserttarget)
								else:remoteCall(otherplayer, "disc", [inserttarget])
							if interruptcancelok == 1:
								remoteCall(inserttarget.controller,"reactionforability",[inserttarget,mainpass])
							else:
								for card in table:
									card.target(False)
								remoteCall(inserttarget.controller,"reactionattachsub",[inserttarget])
								if inserttarget.controller == me:remoteCall(otherplayer, "reaction", ["aftercalculate",1])
								else:reaction("aftercalculate",1)
						elif mainpass in("dominancestart","dominancewin","dominanceend"):
							if inserttarget.type == "Event":
								if inserttarget.controller == me:disc(inserttarget)
								else:remoteCall(otherplayer, "disc", [inserttarget])
							if interruptcancelok == 1:
								remoteCall(inserttarget.controller,"reactionforability",[inserttarget,mainpass])
							else:
								for card in table:
									card.target(False)
								remoteCall(inserttarget.controller,"reactionattachsub",[inserttarget])
								if inserttarget.controller == me:remoteCall(otherplayer, "reaction", [mainpass,1])
								else:reaction(mainpass,1)
						elif mainpass == "challengeaction":
							if inserttarget.type == "Event":
								if inserttarget.controller == me:disc(inserttarget)
								else:remoteCall(otherplayer, "disc", [inserttarget])
							if interruptcancelok == 1:
								remoteCall(inserttarget.controller,"actionforability",[inserttarget,mainpass])
							else:
								for card in table:
									card.target(False)
								remoteCall(inserttarget.controller,"actionattachsub",[inserttarget])
								if inserttarget.controller == me:remoteCall(otherplayer, "action", ["challenge",1])
								else:action("challenge",1)
						elif mainpass == "generalaction":
							if inserttarget.type == "Event":
								if inserttarget.controller == me:disc(inserttarget)
								else:remoteCall(otherplayer, "disc", [inserttarget])
							if interruptcancelok == 1:
								remoteCall(inserttarget.controller,"actionforability",[inserttarget,mainpass])
							else:
								for card in table:
									card.target(False)
									if card.filter == showtablecolor:
										remoteCall(card.controller,"returncard",[card])
								remoteCall(inserttarget.controller,"actionattachsub",[inserttarget])
								if inserttarget.controller == me:remoteCall(otherplayer, "action", ["general",1])
								else:action("general",1)
						elif mainpass == "dominanceaction":
							if inserttarget.type == "Event":
								if inserttarget.controller == me:disc(inserttarget)
								else:remoteCall(otherplayer, "disc", [inserttarget])
							if interruptcancelok == 1:
								remoteCall(inserttarget.controller,"actionforability",[inserttarget,mainpass])
							else:
								for card in table:
									card.target(False)
									if card.filter == showtablecolor:
										remoteCall(card.controller,"returncard",[card])
								remoteCall(inserttarget.controller,"actionattachsub",[inserttarget])
								if inserttarget.controller == me:remoteCall(otherplayer, "action", ["dominance",1])
								else:action("dominance",1)
						elif mainpass == "marshalaction":
							if inserttarget.type == "Event":
								if inserttarget.controller == me:disc(inserttarget)
								else:remoteCall(otherplayer, "disc", [inserttarget])
							if interruptcancelok == 1:
								remoteCall(inserttarget.controller,"actionforability",[inserttarget,mainpass])
							else:
								for card in table:
									card.target(False)
									if card.filter == showtablecolor:
										remoteCall(card.controller,"returncard",[card])
								remoteCall(inserttarget.controller,"actionattachsub",[inserttarget])
								if inserttarget.controller == me:remoteCall(otherplayer, "action", ["marshal",1])
								else:action("marshal",1)
						elif mainpass in("reactionmarshal"):
							if inserttarget.type == "Event":
								if inserttarget.controller == me:disc(inserttarget)
								else:remoteCall(otherplayer, "disc", [inserttarget])
							if interruptcancelok == 1:
								remoteCall(inserttarget.controller,"reactionforability",[inserttarget,mainpass])
							else:
								for card in table:
									card.target(False)
								remoteCall(inserttarget.controller,"reactionattachsub",[inserttarget])
								if inserttarget.controller == me:remoteCall(otherplayer, "action", ["marshal",1])
								else:action("marshal",1)
						elif mainpass in("reactionplot"):
							if inserttarget.type == "Event":
								if inserttarget.controller == me:disc(inserttarget)
								else:remoteCall(otherplayer, "disc", [inserttarget])
							if interruptcancelok == 1:
								remoteCall(inserttarget.controller,"reactionforability",[inserttarget,mainpass])
							else:
								for card in table:
									card.target(False)
								remoteCall(inserttarget.controller,"reactionattachsub",[inserttarget])
								askfirstreveal(table)
						else:
							if interruptcancelok == 1:
								savetarget.highlight = milsavecolor
								savepassfinish(1)
							else:
								if inserttarget.controller == me:disc(inserttarget)
								else:remoteCall(otherplayer, "disc", [inserttarget])
							notify("ballanceover")
							if saveactionplayer == me:remoteCall(otherplayer, "interruptevent", ["miljudgementfp",1])
							else :remoteCall(me, "interruptevent", ["miljudgementfp",1])
					else:
						interruptcancellastcard = interruptlib["pass"+str(interruptpass)][1]
						interruptcanceledcard = interruptlib["pass"+str(interruptpass)][0]
						interruptcancelcard = interruptcanceledcard
						remoteCall(otherplayer,"savetargetinserttarget",[savetarget,inserttarget,interruptcancelcard,interruptcancelplayer,interruptcancellastcard,interruptcanceledcard,interruptcancelok,saveactionplayer,mainpass])
						if interruptlib["pass"+str(interruptpass)][2] == me:remoteCall(otherplayer, "interruptevent", ["interruptcancel",1])
						else:remoteCall(me, "interruptevent", ["interruptcancel",1])
				else:
					if interruptpass > 0:
						e = 0
						if interruptlib["pass"+str(interruptpass)][0].highlight == sacrificecolor:
							playertmp = []
							cardtmp = []
							if isinsertreaction == 0 and orientationintable(interruptlib["pass"+str(interruptpass)][0]):
								if checkinsertreaction(interruptlib["pass"+str(interruptpass)][0]):
									isinsertreaction = 1
									playertmp = interruptlib["pass"+str(interruptpass)][0].controller
									cardtmp = insertreactioncard
									e = 1
						if interruptlib["pass"+str(interruptpass)][0].controller == me:disc(interruptlib["pass"+str(interruptpass)][0])
						else:remoteCall(otherplayer, "disc", [interruptlib["pass"+str(interruptpass)][0]])
						del interruptlib["pass"+str(interruptpass)]
						remoteCall(otherplayer,"interruptlibdel",[interruptpass])
						interruptpass -= 1
						if e == 1:
							setGlobalVariable("insertre", "3")
							backupinterruptlib(1)
							remoteCall(otherplayer, "backupinterruptlib", [1])
							remoteCall(playertmp, "interruptreaction", [cardtmp,1])
							return
					notify("over,disc card")
					debug(interruptcancelok)
					debug(inserttarget)
					if mainpass == "leave":
						if interruptcancelok == 1:
							leavecardtype.append(inserttarget._id)
							remoteCall(inserttarget.controller,"leaveforability",[inserttarget])
						else:
							remoteCall(inserttarget.controller,"abilityattachsub",[inserttarget])
							if inserttarget.controller == me:remoteCall(otherplayer, "interruptevent", ["characterkill",1])
							else:interruptevent("characterkill",1)
					elif mainpass == "leavereaction":
						if interruptcancelok == 1:
							remoteCall(inserttarget.controller,"reactionforability",[inserttarget,mainpass])
						else:
							remoteCall(inserttarget.controller,"reactionattachsub",[inserttarget])
							if inserttarget.controller == me:remoteCall(otherplayer, "reaction", ["leavetable",1])
							else:reaction("leavetable",1)
					elif mainpass == "afterchallenge":
						if interruptcancelok == 1:
							remoteCall(inserttarget.controller,"reactionforability",[inserttarget,mainpass])
						else:
							remoteCall(inserttarget.controller,"reactionattachsub",[inserttarget])
							if inserttarget.controller == me:remoteCall(otherplayer, "reaction", ["afterchallenge",1])
							else:reaction("afterchallenge",1)
					elif mainpass == "aftercalculate":
						if inserttarget.type == "Event":
							if inserttarget.controller == me:disc(inserttarget)
							else:remoteCall(otherplayer, "disc", [inserttarget])
						if interruptcancelok == 1:
							remoteCall(inserttarget.controller,"reactionforability",[inserttarget,mainpass])
						else:
							for card in table:
								card.target(False)
							remoteCall(inserttarget.controller,"reactionattachsub",[inserttarget])
							if inserttarget.controller == me:remoteCall(otherplayer, "reaction", ["aftercalculate",1])
							else:reaction("aftercalculate",1)
					elif mainpass in("dominancestart","dominancewin","dominanceend"):
						if inserttarget.type == "Event":
							if inserttarget.controller == me:disc(inserttarget)
							else:remoteCall(otherplayer, "disc", [inserttarget])
						if interruptcancelok == 1:
							remoteCall(inserttarget.controller,"reactionforability",[inserttarget,mainpass])
						else:
							for card in table:
								card.target(False)
							remoteCall(inserttarget.controller,"reactionattachsub",[inserttarget])
							if inserttarget.controller == me:remoteCall(otherplayer, "reaction", [mainpass,1])
							else:reaction(mainpass,1)
					elif mainpass == "challengeaction":
						if inserttarget.type == "Event":
							if inserttarget.controller == me:disc(inserttarget)
							else:remoteCall(otherplayer, "disc", [inserttarget])
						if interruptcancelok == 1:
							remoteCall(inserttarget.controller,"actionforability",[inserttarget,mainpass])
						else:
							for card in table:
								card.target(False)
							remoteCall(inserttarget.controller,"actionattachsub",[inserttarget])
							if inserttarget.controller == me:remoteCall(otherplayer, "action", ["challenge",1])
							else:action("challenge",1)
					elif mainpass == "generalaction":
						if inserttarget.type == "Event":
							if inserttarget.controller == me:disc(inserttarget)
							else:remoteCall(otherplayer, "disc", [inserttarget])
						if interruptcancelok == 1:
							remoteCall(inserttarget.controller,"actionforability",[inserttarget,mainpass])
						else:
							for card in table:
								card.target(False)
								if card.filter == showtablecolor:
									remoteCall(card.controller,"returncard",[card])
							remoteCall(inserttarget.controller,"actionattachsub",[inserttarget])
							if inserttarget.controller == me:remoteCall(otherplayer, "action", ["general",1])
							else:action("general",1)
					elif mainpass == "dominanceaction":
						if inserttarget.type == "Event":
							if inserttarget.controller == me:disc(inserttarget)
							else:remoteCall(otherplayer, "disc", [inserttarget])
						if interruptcancelok == 1:
							remoteCall(inserttarget.controller,"actionforability",[inserttarget,mainpass])
						else:
							for card in table:
								card.target(False)
								if card.filter == showtablecolor:
									remoteCall(card.controller,"returncard",[card])
							remoteCall(inserttarget.controller,"actionattachsub",[inserttarget])
							if inserttarget.controller == me:remoteCall(otherplayer, "action", ["dominance",1])
							else:action("dominance",1)
					elif mainpass == "marshalaction":
						if inserttarget.type == "Event":
							if inserttarget.controller == me:disc(inserttarget)
							else:remoteCall(otherplayer, "disc", [inserttarget])
						if interruptcancelok == 1:
							remoteCall(inserttarget.controller,"actionforability",[inserttarget,mainpass])
						else:
							for card in table:
								card.target(False)
								if card.filter == showtablecolor:
									remoteCall(card.controller,"returncard",[card])
							remoteCall(inserttarget.controller,"actionattachsub",[inserttarget])
							if inserttarget.controller == me:remoteCall(otherplayer, "action", ["marshal",1])
							else:remoteCall(me, "action", ["marshal",1])
					elif mainpass in("reactionmarshal"):
						if inserttarget.type == "Event":
							if inserttarget.controller == me:disc(inserttarget)
							else:remoteCall(otherplayer, "disc", [inserttarget])
						if interruptcancelok == 1:
							remoteCall(inserttarget.controller,"reactionforability",[inserttarget,mainpass])
						else:
							for card in table:
								card.target(False)
							remoteCall(inserttarget.controller,"reactionattachsub",[inserttarget])
							if inserttarget.controller == me:remoteCall(otherplayer, "action", ["marshal",1])
							else:action("marshal",1)
					elif mainpass in("reactionplot"):
						if inserttarget.type == "Event":
							if inserttarget.controller == me:disc(inserttarget)
							else:remoteCall(otherplayer, "disc", [inserttarget])
						if interruptcancelok == 1:
							remoteCall(inserttarget.controller,"reactionforability",[inserttarget,mainpass])
						else:
							for card in table:
								card.target(False)
							remoteCall(inserttarget.controller,"reactionattachsub",[inserttarget])
							askfirstreveal(table)
					else:		
						if interruptcancelok == 1:
							savetarget.highlight = milsavecolor
							savepassfinish(1)
						else:
							if inserttarget.type != "Character":
								if inserttarget.controller == me:disc(inserttarget)
								else:remoteCall(otherplayer, "disc", [inserttarget])
						notify("ballanceover")
						if saveactionplayer == me:remoteCall(otherplayer, "interruptevent", ["miljudgementfp",1])
						else :remoteCall(me, "interruptevent", ["miljudgementfp",1])
	if actioninsert == "characterkill":
		debug("aaaaaa")
		debug(abilityattach)
		if len(abilityattach) > 0:
			if sessionpass == "":
				intocharacterkill(abilityattach,interruptpasscount)
				return
			if sessionpass == "killabilityok":
				killcards = selectedcard
				if killcards == []:
					if interruptpasscount == 2:
						if getGlobalVariable("plotdisc") == "1":plotdisccard(1)
						else:cardleavetable(1)
					else:
						interruptpasscount += 1
						sessionpass = ""
						remoteCall(otherplayer, "interruptevent", ["characterkill",interruptpasscount])
					return
				else:
					setGlobalVariable("actioncancel", "0")
					debug(killcards[0])
					killcard = killcards[0]
					sessionpass = ""
					remoteCall(otherplayer, "checkinterruptkill", [killcard])
		else:
			if interruptpasscount == 2:
				if getGlobalVariable("plotdisc") == "1":plotdisccard(1)
				else:cardleavetable(1)
			else:
				interruptpasscount += 1
				remoteCall(otherplayer, "interruptevent", ["characterkill",interruptpasscount])
			return

def intocharacterkill(cards,count):
	mute()
	global sessionpass
	global kbcount
	sessionpass = ""
	targetTuple = [card._id for card in table if card.controller == me and cards.has_key(card._id)]
	selectcardnext(targetTuple,"killability",table,[],"",1,actionstyle = 1)
	kbcount = count



def checkinterruptkill(killcard):
	mute()
	global interruptcancelcard
	global interruptcancelplayer
	global inserttarget
	global interruptcancelok
	global mainpass

	if checkcountercharater(killcard):
		interruptcancelcard = killcard
		interruptcancelplayer = otherplayer
		inserttarget = interruptcancelcard
		mainpass = "leave"
		interruptcancelok = 1
		remoteCall(otherplayer,"savetargetinserttarget",[savetarget,inserttarget,interruptcancelcard,interruptcancelplayer,interruptcancellastcard,interruptcanceledcard,interruptcancelok,saveactionplayer,mainpass])
		interruptevent("interruptcancel",2)
	else:
		remoteCall(otherplayer,"leaveforability",[killcard])
		#interruptevent("characterkill",1)


def checkcountercharater(charatercard):
	mute()
	ee = 0
	subcost = 0
	debug(charatercard)
	# for cardhand in me.hand:
	# 	for d in counterevent:
	# 		if cardhand.model == counterevent[d][1] and counterevent[d][4].find(charatercard.Type) != -1:
	# 			if counterevent[d][5] == "all":
	# 				if counterevent[d][7] == "opponent" and charatercard.controller != me:ee = 1
	# 				elif counterevent[d][7] == "all":ee = 1
	# 			elif counterevent[d][5] != "all":
	# 				for cardunique in table:
	# 					if cardunique.Faction == counterevent[d][5] and cardunique.Unique == counterevent[d][6]:
	# 						if counterevent[d][7] == "opponent" and charatercard.controller != me:ee = 1
	# 						elif counterevent[d][7] == "all":ee = 1
	# if ee == 1:return True
	if charatercard.type in("Location","Character","Attachment"):
		if checkcardstatus(deck = table,player = me,cardtype = "Faction",faction = "Lannister."):
			if checkcardstatus(deck = table,player = me,cardtype = "Character",faction = "Lannister.",unique = "Yes"):
				if me.counters['Gold'].value >= 1:
					ee = 1
	elif charatercard.type == "Event":
		if charatercard.cost == "X":ee = 1
		else:
			if me.getGlobalVariable("firstevent") == "0" and checkpr(me):subcost = 1
			if me.counters['Gold'].value >= int(charatercard.cost)-subcost:ee = 1
			if checkcardstatus(deck = table,player = me,model = "9e56783a-c133-4f81-9914-4e81b92ba5d1"):ee = 1
	if charatercard.model == "d8f39831-ef30-4f90-a8cb-8bbc4c659c7d":return False
	if ee == 1:return True
	



def savepassfinish(ok):
	for d in cardability:
		if inserttarget.model == cardability[d][1]:
			cardtype = cardability[d][2]
			break
	if inserttarget.controller == me:usecardability(inserttarget,cardtype,savetarget)
	else:remoteCall(otherplayer, "usecardability", [inserttarget,cardtype,savetarget])

def usecardability(card,cardtype,target):
	attach = eval(getGlobalVariable("attachmodify"))
	if cardtype == "Attachment" and card.type != "Attachment":
		if target.Keywords.find('No attachments.') == -1:
			cx,cy = target.position
			if me.isInverted:x,y = attachat(cx-15,cy-15,table)
			else:x,y = attachat(cx+15,cy+15,table)
			card.moveToTable(x,y)
			debug(attach)
			if not attach.has_key(card._id):
				attach[card._id] = target._id
			else:attach[card._id].append(target._id)
			setGlobalVariable("attachmodify",str(attach))
			if re.search('\+\d\sSTR', card.Text):
				stradd = re.search('\+\d\sSTR', card.Text).group()
				target.markers[STR_Up] += int(stradd[1])
			card.sendToBack()
			card.type = "Attachment"
		else:
			disc(card)
	else:
		if attach.has_key(card._id):
			if attach[card._id] == target._id:
				del attach[card._id]
				setGlobalVariable("attachmodify",str(attach))
		debug(getGlobalVariable("attachmodify"))
		disc(card)

def getinterruptpass(interruptpassn):
	global interruptpass
	interruptpass = interruptpassn

def interruptlibadd(interruptpassn):
	global interruptpass
	interruptpass = interruptpassn
	interruptlib["pass"+str(interruptpass)] = (interruptcanceledcard,interruptcancellastcard,otherplayer)

def interruptlibdel(interruptpassn):
	global interruptpass
	interruptpass = interruptpassn
	debug(interruptlib)
	del interruptlib["pass"+str(interruptpass)]
	interruptpass -= 1

def cardeffect(card,actioninsert):
	mute()
	if actioninsert == "saveaction":
		for d in saveaction:
			if card.model == saveaction[d][1]:
				if  saveaction[d][2] == "Event":card.highlight = None
				if  saveaction[d][2] == "sacrifice":card.highlight = sacrificecolor
				if  saveaction[d][2] == "kneel":kneel(card)
	if actioninsert == "interrupt":
		for d in counterevent:
			if card.model == counterevent[d][1]:
				if  counterevent[d][2] == "sacrifice":card.highlight = sacrificecolor
				else:card.highlight = interruptcolor

def savetargetinserttarget(savetargetn,inserttargetn,interruptcancelcardn,interruptcancelplayern,interruptcancellastcardn,interruptcanceledcardn,interruptcancelokn,saveactionplayern,mainpassn):
	mute()
	global savetarget
	global inserttarget
	global interruptcancelcard
	global interruptcancelplayer
	global interruptcanceledcard
	global interruptcancellastcard
	global interruptlib
	global interruptcancelok
	global saveactionplayer
	global mainpass

	interruptcancelok = interruptcancelokn
	savetarget = savetargetn
	inserttarget = inserttargetn
	interruptcancelcard = interruptcancelcardn
	interruptcancelplayer = interruptcancelplayern
	interruptcancellastcard = interruptcancellastcardn
	interruptcanceledcard = interruptcanceledcardn
	saveactionplayer =  saveactionplayern
	mainpass = mainpassn

def characterkilled(cardbekill,count):
	mute()
	global abilityattach
	c = 0
	list = []
	for card in table:
		if card.type == "Attachment":
			list.append(card)
	for card in cardbekill:
		for d in cardkill:
			if card.model == cardkill[d][1] and card.controller == me and cardkill[d][2] != "link":
				if cardkill[d][4] == "Attachment":
					if len(list) > 0:
						if not abilityattach.has_key(card._id):
							abilityattach[card._id] = 1
						else:abilityattach[card._id] += 1
				elif cardkill[d][4] != "Attachment":
					if not abilityattach.has_key(card._id):
						abilityattach[card._id] = 1
					else:abilityattach[card._id] += 1
	debug(abilityattach)
	for card in cardbekill:
		for d in cardkill:
			if card.model == cardkill[d][1] and cardkill[d][2] == "link" :
				for cards in table:
					if cards.controller == me and cards.name == cardkill[d][6]:
						if not abilityattach.has_key(cards._id):
							abilityattach[cards._id] = 1
						else:abilityattach[cards._id] += 1
	debug(abilityattach)
	if count == 1:remoteCall(otherplayer, "characterkilled", [cardbekill,2])
	else:remoteCall(otherplayer, "interruptevent", ["characterkill",1])
				#if re.search('\d\spower', cardkill[d][3]):
					#powadd = re.search('\d\spower', cardkill[d][3]).group()
					#for c in table: 
						#if c.Type == "Faction" and c.controller == me:
							#c.markers[Power] += int(powadd[0])
def leaveforability(card):
	mute()
	debug(card)
	global abilityattach
	global sessionpass
	global cardtmp
	sessionpass = ""
	c = ""
	leavecardtype.append(card._id)
	for d in cardkill:
		if card.model == cardkill[d][1] and card.controller == me:
			if re.search('\d\spower', cardkill[d][3]):
				powadd = re.search('\d\spower', cardkill[d][3]).group()
				addhousepow(int(powadd[0]))
			if cardkill[d][2] == "other":
				if cardkill[d][4] == "card" and cardkill[d][3] == "discard":
					if len(players[1].hand) > 0:remoteCall(otherplayer, "randomDiscard", [otherplayer.hand])
				if cardkill[d][4] == "other" and cardkill[d][3] == "discard":
					if len(players[1].hand) > 0:remoteCall(otherplayer, "randomDiscard", [otherplayer.hand])
			if cardkill[d][2] == "all":
				if cardkill[d][4] == "Attachment" and cardkill[d][3] == "discard":
					c = "discattch"
					#discattch(table)
				if cardkill[d][4] == "Character" and cardkill[d][3] == "kneel":
					c = "kneelplayer"
					#kneelplayer(table)
	abilityattach[card._id] -= 1
	if abilityattach[card._id] == 0:del abilityattach[card._id]
	if c == "discattch":
		cardtmp = card
		discattch(table)
		return
	if c == "kneelplayer":
		cardtmp = card
		kneelplayer(table)
		return
	remoteCall(otherplayer,"interruptevent",["characterkill",1])

def discattch(group, x=0, y=0):
	mute()
	selectlist = checkcardid(deck = table,cardtype = "Attachment")
	selectcardnext(selectlist,"discattch",table,cardtmp,"",1)


def kneelplayer(group, x=0, y=0):
	mute()
	global sessionpass
	selectlist = checkcardid(deck = table,cardtype = "Character",stand = 0)
	selectcardnext(selectlist,"kneel",table,cardtmp,"",1)


def cardleavetable(count):
	mute()
	global leavecardtype
	global abilityattach
	global leavetablecard
	debug(leavecardtype)
	for card in table:
		if card.highlight == miljudgecolor and card.controller == me:
			leavetablecard.append(card)
			if card._id in leavecardtype:
				notify("{} killed {}.".format(me,card))
				for d in leavedeck:
					if card.model == leavedeck[d][1]:
						if leavedeck[d][2] == "deck":
							card.moveToBottom(me.deck)
							me.deck.shuffle()
					else:
						card.moveTo(me.piles['Dead pile'])
			else:
				if getGlobalVariable("aftcuevent") != "-1" or getGlobalVariable("chaevent") != "-1":
					notify("{} killed {}.".format(otherplayer,card))
				else:
					notify("{} killed {}.".format(me,card))
				card.moveTo(me.piles['Dead pile'])
	leavecardtype = []
	abilityattach = {}
	if count == 1:
		remoteCall(otherplayer, "getleavetablecard", [leavetablecard])
		remoteCall(otherplayer, "cardleavetable", [2])
	else:
		remoteCall(otherplayer, "getleavetablecard", [leavetablecard])
		f = (card for card in table  
				if card.name == "1st Player Token")
		for card1 in f:
			if card1.controller == me:
				checkreactioncard(1)
			else:
				remoteCall(otherplayer, "checkreactioncard", [1])

def getleavetablecard(leavetablecardn):
	global leavetablecard
	leavetablecard = leavetablecardn


def reaction(actioninsert,reactioncount):
	mute()
	global sessionpass
	global intertreaction
	if actioninsert == "leavetable":
		setGlobalVariable("mainstep", "77")
		if len(reactionattach) > 0:
			if sessionpass == "":
				intoreaction(reactionattach,reactioncount,"reaction")
				return
			if sessionpass == "reactionok":
				reactioncards = selectedcard
				if reactioncards == []:
					if reactioncount == 2:
						if getGlobalVariable("plotkill") == "1":
							if getGlobalVariable("reavelplot") == "1":
								setGlobalVariable("reavelplot","2")
								if str(me._id) == getGlobalVariable("firstreveal"):remoteCall(players[1], "reavelplot", table)
								else:reavelplot(table)
								return
							if getGlobalVariable("reavelplot") == "2":
								setGlobalVariable("plotkill","0")
								if fplay(1) == me:actiongeneral(1)
								else:remoteCall(players[1], "actiongeneral", 1)
								return
						if getGlobalVariable("aftcuevent") != "-1" or getGlobalVariable("chaevent") != "-1":challengebalanceover(1)
						else:remoteCall(winplayer, "keyword", [1])
					else:
						reactioncount += 1
						sessionpass = ""
						remoteCall(otherplayer, "reaction", ["leavetable",reactioncount])
					return
				else:
					debug(reactioncards[0])
					reactioncard = reactioncards[0]
					sessionpass = ""
					remoteCall(otherplayer, "checkreaction", [reactioncard,"leavetable"])
		else:
			if reactioncount == 2:
				if getGlobalVariable("insertre") != "":
					restoreinterruptlib(1)
					return
				if getGlobalVariable("plotkill") == "1":
					if getGlobalVariable("reavelplot") == "1":
						setGlobalVariable("reavelplot","2")
						if str(me._id) == getGlobalVariable("firstreveal"):remoteCall(players[1], "reavelplot", table)
						else:reavelplot(table)
						return
					if getGlobalVariable("reavelplot") == "2":
						setGlobalVariable("plotkill","0")
						if fplay(1) == me:actiongeneral(1)
						else:remoteCall(players[1], "actiongeneral", 1)
						return
				if getGlobalVariable("aftcuevent") != "-1" or getGlobalVariable("chaevent") != "-1":challengebalanceover(1)			
				else:remoteCall(winplayer, "keyword", [1])
			else:
				reactioncount += 1
				remoteCall(otherplayer, "reaction", ["leavetable",reactioncount])
			return
	if actioninsert == "afterchallenge":
		if len(reactionattach) > 0:
			if sessionpass == "":
				choiceList = ['reaction', 'cancel']
				colorList = ['#006b34' ,'#ae0603']
				choice = askChoice("Which Pass do you want to action?", choiceList,colorList)
				if choice == 1:
					intoreaction(reactionattach,reactioncount,"reactionaftc")
					return
				if choice == 2:
					if reactioncount == 2:
						notify("reaction over")
						clearreaction(1)
					else:
						reactioncount += 1
						remoteCall(otherplayer, "reaction", ["afterchallenge",reactioncount])
					return
			if sessionpass == "reactionaftcok":
				reactioncards = selectedcard
				if reactioncards == []:
					if reactioncount == 2:
						notify("reaction over")
						clearreaction(1)
					else:
						reactioncount += 1
						sessionpass = ""
						remoteCall(otherplayer, "reaction", ["afterchallenge",reactioncount])
					return
				else:
					debug(reactioncards[0])
					reactioncard = reactioncards[0]
					sessionpass = ""
					remoteCall(otherplayer, "checkreaction", [reactioncard,"afterchallenge"])
		else:
			if reactioncount == 2:
				notify("reaction over")
				clearreaction(1)
			else:
				reactioncount += 1
				remoteCall(otherplayer, "reaction", ["afterchallenge",reactioncount])
			return
	if actioninsert == "aftercalculate":
		if len(reactionattach) > 0:
			debug(sessionpass)
			if sessionpass == "":
				choiceList = ['reaction', 'cancel']
				colorList = ['#006b34' ,'#ae0603']
				choice = askChoice("Which Pass do you want to action?", choiceList,colorList)
				if choice == 1:
					intoreaction(reactionattach,reactioncount,"reactionaftu")
					return
				if choice == 2:
					if reactioncount == 2:
						notify("reaction over")
						clearreaction(5)
					else:
						reactioncount += 1
						remoteCall(otherplayer, "reaction", ["aftercalculate",reactioncount])
					return
			if sessionpass == "reactionaftuok":
				reactioncards = selectedcard
				if reactioncards == []:
					if reactioncount == 2:
						notify("reaction over")
						clearreaction(5)
					else:
						reactioncount += 1
						sessionpass = ""
						remoteCall(otherplayer, "reaction", ["aftercalculate",reactioncount])
					return
				else:
					debug(reactioncards[0])
					reactioncard = reactioncards[0]
					sessionpass = ""
					remoteCall(otherplayer, "checkreaction", [reactioncard,"aftercalculate"])
		else:
			if reactioncount == 2:
				notify("reaction over")
				clearreaction(5)
			else:
				reactioncount += 1
				remoteCall(otherplayer, "reaction", ["aftercalculate",reactioncount])
			return
	if actioninsert == "aftercalculatef":
		if len(reactionattach) > 0:
			for card in table:
				for d in reactionattach:
					if card._id == d:
						reactionforability(card,"aftercalculate")
						return
		else:
			if reactioncount == 2:
				notify("reaction over")
				clearreaction(3)
			else:
				reactioncount += 1
				remoteCall(otherplayer, "reaction", ["aftercalculatef",reactioncount])
			return
	if actioninsert == "keywords":
		choiceList = ['reaction', 'cancel']
		colorList = ['#006b34' ,'#ae0603']
		choice = askChoice("Which Pass do you want to action?", choiceList,colorList)
		if choice == 1:
			remoteCall(otherplayer, "checkreaction", [cardtoaction,"keywords"])
			return
		if choice == 2:
			keywordforability(1)
	if actioninsert in ("dominancestart","dominancewin","dominanceend"):
		if len(reactionattach) > 0:
			debug(sessionpass)
			if sessionpass == "":
				intoreaction(reactionattach,reactioncount,actioninsert)
				return
			if sessionpass in ("reactiondsuok","reactiondswinok"):
				reactioncards = selectedcard
				if reactioncards == []:
					if reactioncount == 2:
						notify("reaction over")
						clearreaction(1)
					else:
						reactioncount += 1
						sessionpass = ""
						remoteCall(players[1], "reaction", [actioninsert,reactioncount])
					return
				else:
					debug(reactioncards[0])
					reactioncard = reactioncards[0]
					sessionpass = ""
					remoteCall(players[1], "checkreaction", [reactioncard,actioninsert])
		else:
			if reactioncount == 2:
				notify("reaction over")
				clearreaction(1)
			else:
				reactioncount += 1
				remoteCall(otherplayer, "reaction", [actioninsert,reactioncount])
			return
	if actioninsert in ("standingstart","standingover","standingend"):
		if len(reactionattach) > 0:
			debug(sessionpass)
			if sessionpass == "":
				intoreaction(reactionattach,reactioncount,actioninsert)
				return
			if sessionpass in ("reactionstandingok"):
				reactioncards = selectedcard
				if reactioncards == []:
					if reactioncount == 2:
						notify("reaction over")
						clearreaction(1)
					else:
						reactioncount += 1
						sessionpass = ""
						remoteCall(players[1], "reaction", [actioninsert,reactioncount])
					return
				else:
					debug(reactioncards[0])
					reactioncard = reactioncards[0]
					sessionpass = ""
					remoteCall(players[1], "checkreaction", [reactioncard,actioninsert])
		else:
			if reactioncount == 2:
				notify("reaction over")
				clearreaction(1)
			else:
				reactioncount += 1
				remoteCall(otherplayer, "reaction", [actioninsert,reactioncount])
			return
	if actioninsert in ("taxationstart","taxationreturnover","taxationcheckhandover","taxationend"):
		if len(reactionattach) > 0:
			debug(sessionpass)
			if sessionpass == "":
				intoreaction(reactionattach,reactioncount,actioninsert)
				return
			if sessionpass in ("reactiontaxationok"):
				reactioncards = selectedcard
				if reactioncards == []:
					if reactioncount == 2:
						notify("reaction over")
						clearreaction(1)
					else:
						reactioncount += 1
						sessionpass = ""
						remoteCall(players[1], "reaction", [actioninsert,reactioncount])
					return
				else:
					debug(reactioncards[0])
					reactioncard = reactioncards[0]
					sessionpass = ""
					remoteCall(players[1], "checkreaction", [reactioncard,actioninsert])
		else:
			if reactioncount == 2:
				notify("reaction over")
				clearreaction(1)
			else:
				reactioncount += 1
				remoteCall(otherplayer, "reaction", [actioninsert,reactioncount])
			return
	if actioninsert == "reactionmarshal":
		if len(reactionattach) > 0:
			debug(sessionpass)
			if sessionpass == "":
				intoreaction(reactionattach,reactioncount,actioninsert)
				return
			if sessionpass in ("reactionmarshalok"):
				reactioncards = selectedcard
				debug(reactioncards[0])
				reactioncard = reactioncards[0]
				sessionpass = ""
				remoteCall(players[1], "checkreaction", [reactioncard,actioninsert])
	if actioninsert == "reactionplot":
		if len(reactionattach) > 0:
			debug(sessionpass)
			if sessionpass == "":
				intoreaction(reactionattach,reactioncount,actioninsert)
				return
			if sessionpass in ("reactionplotok"):
				reactioncards = selectedcard
				debug(reactioncards[0])
				reactioncard = reactioncards[0]
				sessionpass = ""
				remoteCall(players[1], "checkreaction", [reactioncard,actioninsert])

def checkreaction(reactioncard,repass):
	mute()
	global interruptcancelcard
	global interruptcancelplayer
	global inserttarget
	global interruptcancelok
	global interruptcanceledcard
	global mainpass
	global leavecardtype
	global sessionpass

	sessionpass = ""
	
	if checkcountercharater(reactioncard):
		if getGlobalVariable("insertre") == "1":
			interruptcanceledcard = []
		interruptcancelcard = reactioncard
		interruptcancelplayer = otherplayer
		inserttarget = interruptcancelcard
		mainpass = repass
		interruptcancelok = 1
		remoteCall(players[1],"savetargetinserttarget",[savetarget,inserttarget,interruptcancelcard,interruptcancelplayer,interruptcancellastcard,interruptcanceledcard,interruptcancelok,saveactionplayer,mainpass])
		remoteCall(me, "interruptevent", ["interruptcancel",2])
	else:
		remoteCall(players[1],"reactionforability",[reactioncard,repass])

def intoreaction(cards,count,sepass):
	mute()
	global sessionpass
	global recount
	sessionpass = ""
	targetTuple = [d for d in reactionattach]
	if sepass in("reactionmarshal","leavetable","afterchallenge","aftercalculate","aftercalculatef","keywords","dominancestart","dominancewin","dominanceend","standingstart","standingover","standingend","taxationstart","taxationreturnover","taxationcheckhandover","taxationend","reactionplot"):selectcardnext(targetTuple,sepass,table,[],me,1,actionstyle = 1)
	else:selectcardnext(targetTuple,sepass,table,[],me,1)
	#targetTuple = ([card._id for card in table if card.controller == me and cards.has_key(card._id)], me._id) 
	# setGlobalVariable("tableTargets", str(targetTuple))
	# setGlobalVariable("selectmode", "1")
	# if me.isInverted:table.create("584a37d7-5a30-4018-ae21-0ad325203fa0",-375,-250)
	# else:table.create("584a37d7-5a30-4018-ae21-0ad325203fa0",-375,200)
	# notify("**{} into selectmode**".format(me))
	# sessionpass = sepass
	recount = count

def reactionforability(card,repass):
	mute()
	debug(card)
	debug(repass)
	global reactionattach
	global sessionpass
	global reactioncardlimit
	global intertreaction
	global cardtoaction
	global savetarget
	sessionpass = ""
	c = 0
	f = 0
	card.arrow(card,False)
	debug(mainpass)
	if repass == "leavetable":
		for d in leavereacion:
			if card.model == leavereacion[d][1] and card.controller == me:
				if re.search('\d\spower', leavereacion[d][4]):
					powadd = re.search('\d\spower', leavereacion[d][4]).group()
					card.markers[Power] += (int(powadd[0]))
					notify("{}'s {} reaction add 1 pow to him".format(me,card))
					if not reactioncardlimit.has_key(card._id):
						reactioncardlimit[card._id] = 1
					else:reactioncardlimit[card._id] += 1
					if reactioncardlimit[card._id] == leavereacion[d][5]:
						del reactionattach[card._id]
						c = 1
				if leavereacion[d][2] == "Faction" and leavereacion[d][4] == "stand":
					for cards in table:
						if cards.type == "Character" and cards.controller == me:
							cards.orientation = 0
					notify("{}'s {} reaction stand each character".format(me,card))
					if not reactioncardlimit.has_key(card._id):
						reactioncardlimit[card._id] = 1
					else:reactioncardlimit[card._id] += 1
					if reactioncardlimit[card._id] == leavereacion[d][5]:
						del reactionattach[card._id]
						c = 1
		if getGlobalVariable("insertre") != "":
			restoreinterruptlib(1)
			return
		if c == 0:
			reactionattach[card._id] -= 1
			if reactionattach[card._id] == 0:del reactionattach[card._id]
		remoteCall(otherplayer, "reaction", ["leavetable",1])
	if repass == "afterchallenge":
		for d in afterchallengereacion:
			if card.model == afterchallengereacion[d][1] and card.controller == me:
				if re.search('\d\sgold', afterchallengereacion[d][4]):
					goldadd = re.search('\d\sgold', afterchallengereacion[d][4]).group()
					me.counters['Gold'].value += (int(goldadd[0]))
					notify("{}'s {} reaction get {} gold".format(me,card,int(goldadd[0])))#imp
					if not reactioncardlimit.has_key(card._id):
						reactioncardlimit[card._id] = 1
					else:reactioncardlimit[card._id] += 1
					if reactioncardlimit[card._id] == afterchallengereacion[d][5]:
						del reactionattach[card._id]
						c = 1
				if afterchallengereacion[d][4] == "stand":
					card.orientation = 0
					notify("{}'s {} reaction stand himself".format(me,card))#ned
					if not reactioncardlimit.has_key(card._id):
						reactioncardlimit[card._id] = 1
					else:reactioncardlimit[card._id] += 1
					if reactioncardlimit[card._id] == afterchallengereacion[d][5]:
						del reactionattach[card._id]
						c = 1
				if afterchallengereacion[d][4] == "stealth":
					for cardcant in table:
						if cardcant._id == int(getGlobalVariable("cantchallenge")):cardcant.highlight = cantchallengecolor
					notify("{}'s {} reaction its target cannot be declared as a defender for any challenges until the end of the phase.".format(me,card))#ghost
					setGlobalVariable("cantchallenge", "")
					if not reactioncardlimit.has_key(card._id):
						reactioncardlimit[card._id] = 1
					else:reactioncardlimit[card._id] += 1
					if reactioncardlimit[card._id] == afterchallengereacion[d][5]:
						del reactionattach[card._id]
						c = 1
				if afterchallengereacion[d][4] == "makedefender":
					for cardbdf in table:
						if str(cardbdf._id) in getGlobalVariable("bedefend"):cardbdf.highlight = usedplotcolor
					notify("{}'s {} reaction its target must be declared as a defender for the challenge".format(me,card))#Dornish Paramour
					if not reactioncardlimit.has_key(card._id):
						reactioncardlimit[card._id] = 1
					else:reactioncardlimit[card._id] += 1
					if reactioncardlimit[card._id] == afterchallengereacion[d][5]:
						del reactionattach[card._id]
						c = 1
		if c == 0:
			reactionattach[card._id] -= 1
			if reactionattach[card._id] == 0:del reactionattach[card._id]
		remoteCall(otherplayer, "reaction", ["afterchallenge",1])
	if repass == "aftercalculate":
		for d in aftercalculate:
			if card.model == aftercalculate[d][1] and card.controller == me:
				if aftercalculate[d][4] == "disotherattachment":
					remoteCall(otherplayer,"disc",[cardtoaction])
					cardtoaction = []
					notify("{}'s {} reaction disc a attachment".format(me,card))#RattleshirtsRaiders					
				if aftercalculate[d][4] == "kill":
					card.highlight = sacrificecolor
					disc(card)
					f = 1
					notify("{}'s {} reaction kill {}".format(me,card,cardtoaction))#ThrowingAxe,Ice
					savetarget = cardtoaction
					cardtoaction = []
				if aftercalculate[d][4] == "attkilldef":
					f = 1
					disc(card)
					notify("{}'s {} reaction kill a character".format(me,card))#PuttotheSword
				if aftercalculate[d][4] == "disotherloaction":
					remoteCall(otherplayer,"disc",[cardtoaction])
					cardtoaction = []
					notify("{}'s {} reaction disc a loaction".format(me,card))#PuttotheTorch
				if re.search('\d\spow', aftercalculate[d][4]):
					powadd = re.search('\d\spower', aftercalculate[d][4]).group()
					addhousepow(int(powadd[0]))
					notify("{}'s {} reaction get {} pow".format(me,card,powadd))#SuperiorClaim
				if aftercalculate[d][4] == "stand":
					card.orientation = 0
					notify("{}'s {} reaction stand her".format(me,card))#AshaGreyjoy
				if aftercalculate[d][4] == "addpowself":
					card.markers[Power] += 1
					notify("{}'s {} reaction he gains 1 power".format(me,card))#TheonGreyjoy
				if aftercalculate[d][4] == "5pwinpow":
					ppoint = (attacker.counters['Str'].value - defender.counters['Str'].value)//5
					card.markers[Power] += ppoint
					notify("{}'s {} reaction he gains {} power".format(me,card,ppoint))#TheRedViper
				if aftercalculate[d][4] == "drawcardorpower":
					choiceList = ['draw 1 card', 'gain 1 power']
					colorList = ['#006b34' ,'#ae0603']
					choice = askChoice("Which Pass do you want to action?", choiceList,colorList)
					if choice == 1:
						draw(me.deck)
						notify("{}'s {} reaction draw 1 card".format(me,card))#GreatKraken
					if choice == 2:
						addhousepow(1)
						notify("{}'s {} reaction gain 1 power".format(me,card))#GreatKraken
				if aftercalculate[d][4] == "drawcard":
					draw(me.deck)
					notify("{}'s {} reaction draw 1 card".format(me,card))#Lannisport
				if aftercalculate[d][4] == "losekill":
					f = 1
					notify("{}'s {} reaction kill a character".format(me,card))#LikeWarmRain
					cardtoaction = []
				if aftercalculate[d][4] == "returndefender":
					remoteCall(otherplayer,"returncard",[cardtoaction])
					notify("{}'s {} reaction return {} to its owner's hand".format(me,card,cardtoaction))#GhastonGrey
					cardtoaction = []
				if aftercalculate[d][4] == "addusedplotpow":
					powadd = 5#......
					addhousepow(int(powadd))
					notify("{}'s {} reaction get {} pow".format(me,card,powadd))#DoransGame
				if aftercalculate[d][4] == "draw2card":
					draw(me.deck)
					draw(me.deck)
					notify("{}'s {} reaction draw 2 card".format(me,card))#TheMander
				if aftercalculate[d][4] == "addmarker":
					cardtoaction.markers[TokenBlue] += 1		
					notify("{}'s {} reaction place a poison token on {}".format(me,card,cardtoaction))#TearsofLys
					cardtoaction = []
				if aftercalculate[d][4] == "subability2":
					cardtoaction.markers[TokenBlue] += 2
					notify("{}'s {} reaction {} gets -2 STR".format(me,card,cardtoaction))#PlazaofPunishment
					for cards in table:
						cards.target(False)
					if int(cardtoaction.strength) + cardtoaction.markers[STR_Up] - cardtoaction.markers[Burn] - 2 <= 0:
						f = 1
						savetarget = cardtoaction
					cardtoaction = []
				if aftercalculate[d][4] == "addclaim":
					kneel(card)
					debug(challengetype)
					notify("{}'s {} reaction raise the claim value by 1".format(me,card,cardtoaction))#Sunspear
				if aftercalculate[d][4] == "standstm":
					for cards in table:
						cards.target(False)
					kneel(cardtoaction)		
					notify("{}'s {} reaction stand {}".format(me,card,cardtoaction))#Rhaegal
					cardtoaction = []
				if aftercalculate[d][4] == "discard":
					remoteCall(otherplayer, "randomDiscard", [otherplayer.hand])
					notify("{}'s {} reaction {} discard 1 card".format(me,card,otherplayer))#MaesterLomys
				if aftercalculate[d][4] == "addplayer":
					card.highlight = sacrificecolor
					disc(card)
					clist = [p for p in table
							if p.controller == me and p.type == "Character" and p.isFaceUp]
					if len(clist) > 0:
						clist.reverse()
						for character in clist:
							x, y = character.position
							break
						clist.reverse()
						if me.isInverted:cardtoaction.moveToTable(x-80,y)
						else:cardtoaction.moveToTable(x+80,y)
					notify("{}'s {} reaction put {} into play".format(me,card,cardtoaction))#DothrakiSea
					cardtoaction = []
				if aftercalculate[d][4] == "cantchallenge":
					debug("cannot initiate challenges")
					notify("{}'s {} reaction {} cannot initiate challenges".format(me,card,otherplayer))#TheSwordintheDarkness
				if aftercalculate[d][4] == "cant1challenge":
					c1c = ''
					choiceList = ['Military', 'Intrigue', 'Power']
					colorList = ['#ae0603' ,'#006b34','#1a4d8f']
					choice = askChoice("Which challenge do you want to cannot initiate?", choiceList,colorList)
					if choice == 1:c1c = 'Military'
					if choice == 2:c1c = 'Intrigue'
					if choice == 3:c1c = 'Power'
					if choice != 0:notify("{}'s {} reaction cannot initiate {} challenges".format(me,card,c1c))#UnbowedUnbentUnbroken
				if aftercalculate[d][4] == "addplayer6":
					clist = [p for p in table
							if p.controller == me and p.type == "Character" and p.isFaceUp]
					if len(clist) > 0:
						clist.reverse()
						for character in clist:
							x, y = character.position
							break
						clist.reverse()
						if me.isInverted:cardtoaction.moveToTable(x-80,y)
						else:cardtoaction.moveToTable(x+80,y)
					notify("{}'s {} reaction put {} into play".format(me,card,cardtoaction))#TheQueenofThorns
					cardtoaction = []
				if aftercalculate[d][4] == "addhand":
					remoteCall(otherplayer, "choosetype", [card])#OlennasCunning
					return
				if aftercalculate[d][4] == "submarker":
					choiceList = []
					colorList = []
					if checkchallengeicon(cardtoaction,"milicon") > 0:
						choiceList.append("Military")
						colorList.append('#ae0603')
					if checkchallengeicon(cardtoaction,"inticon") > 0:
						choiceList.append("Intrigue")
						colorList.append('#006b34')
					if checkchallengeicon(cardtoaction,"powicon") > 0:
						choiceList.append("Power")
						colorList.append('#1a4d8f')
					if choiceList != []:
						choice = askChoice("Which challenge icon do you want to loses?", choiceList,colorList)
					if choice != 0:
						c1c = choiceList[choice-1]
						notify("{}'s {} reaction {} loses {} challenge icon".format(me,card,cardtoaction,c1c))#MaesterCaleotte
					for cards in table:
						cards.target(False)
					cardtoaction = []
				if aftercalculate[d][4] == "movepow":
					remoteCall(otherplayer, "subhousepow", 1)
					addhousepow(1)
					notify("{}'s {} reaction move 1 power icon from {}".format(me,card,otherplayer))#AClashofKings
				if aftercalculate[d][4] == "addred":
					card.markers[betrayalIcon] += 1
					notify("{}'s {} forced reaction add 1 betrayal token".format(me,card))#SerJorahMormont
					if card.markers[betrayalIcon] == 3:
						card.highlight = sacrificecolor
						notify("{}'s {} reaction already have 3 betrayal token,sacrifice him".format(me,card))#SerJorahMormont
						disc(card)
				if aftercalculate[d][4] == "kneel":
					kneel(card)
					notify("{}'s {} forced reaction kneel it".format(me,card))#CastleBlack
				if not reactioncardlimit.has_key(card._id):
					reactioncardlimit[card._id] = 1
				else:reactioncardlimit[card._id] += 1
				if reactioncardlimit[card._id] == aftercalculate[d][5]:
					del reactionattach[card._id]
					c = 1
		if c == 0:
			reactionattach[card._id] -= 1
			if reactionattach[card._id] == 0:del reactionattach[card._id]
		if f == 1:
			savetarget.highlight = miljudgecolor
			setGlobalVariable("aftcuevent", str(me._id))
			miljudgementfinish([savetarget],1)
			remoteCall(otherplayer, "miljudgementfinish", [[savetarget],1])
			remoteCall(otherplayer, "interruptevent", ["miljudgementfp",2])
		else:
			if "Forced Reaction" in card.Text:remoteCall(otherplayer, "reaction", ["aftercalculatef",1])
			else:remoteCall(otherplayer, "reaction", ["aftercalculate",1])
	if repass in "1234":
		if repass == "1":choosedtype = "Character"
		if repass == "2":choosedtype = "Location"
		if repass == "3":choosedtype = "Attachment"
		if repass == "4":choosedtype = "Event"
		listtype = []
		for cardt in me.deck:
			if cardt.type != choosedtype:
				listtype.append(cardt)
		if len(listtype) > 0:
			dlg = cardDlg(listtype)
			dlg.title = "These cards are in your deck:"
			dlg.text = "select 1 card add it to your hand."
			dlg.min = 1
			dlg.max = 1
			cards = dlg.show()
			c = 0
			if cards != None:
				cards[0].moveTo(me.hand)
				me.deck.shuffle()
				notify("{}'s {} reaction put {} into {}'s hand".format(me,card,cards[0],me))
		else:whisper("{} search failed".format(card))
		for d in aftercalculate:
			if card.model == aftercalculate[d][1] and card.controller == me:
				if not reactioncardlimit.has_key(card._id):
					reactioncardlimit[card._id] = 1
				else:reactioncardlimit[card._id] += 1
				if reactioncardlimit[card._id] == aftercalculate[d][5]:
					del reactionattach[card._id]
					c = 1
		if c == 0:
			reactionattach[card._id] -= 1
			if reactionattach[card._id] == 0:del reactionattach[card._id]
		remoteCall(otherplayer, "reaction", ["aftercalculate",1])
	if repass == "keywords":
		list = []
		for card in otherplayer.piles['Discard Pile']:
			if card.type == "Location":
				list.append(card)
				debug(card)
		dlg = cardDlg(list)
		dlg.title = "These cards are in your table:"
		dlg.text = "Declares at least 1 Location to move."
		dlg.min = 1
		dlg.max = 1
		cards = dlg.show()
		if cards != None:
			remoteCall(otherplayer, "movecard", [cards[0]])
			cards[0].controller = me
			notify("{}'s {} reaction put {} into play under {} control.".format(me,cardtoaction,cards[0],me))
		keywordattach.remove(cardtoaction)
		cardtoaction = []
		keywordforability(1)
	if repass == "dominancestart":
		for d in dominancestart:
			if card.model == dominancestart[d][1] and card.controller == me:
				if dominancestart[d][2] == "stand":
					card.orientation = 0
					notify("{}'s {} reaction stand himself".format(me,card))#FieryFollowers
				if not reactioncardlimit.has_key(card._id):
					reactioncardlimit[card._id] = 1
				else:reactioncardlimit[card._id] += 1
				if reactioncardlimit[card._id] == dominancestart[d][5]:
					del reactionattach[card._id]
					c = 1
		if c == 0:
			reactionattach[card._id] -= 1
			if reactionattach[card._id] == 0:del reactionattach[card._id]
		remoteCall(players[1], "reaction", ["dominancestart",1])
	if repass == "dominancewin":
		for d in dominancewin:
			if card.model == dominancewin[d][1] and card.controller == me:
				if dominancewin[d][2] == "2power":
					addhousepow(2)
					notify("{}'s {} reaction add 2 power".format(me,card))#AFeastforCrows
				if dominancewin[d][2] == "move1pow":
					remoteCall(otherplayer, "subhousepow", 1)
					addhousepow(1)
					notify("{}'s {} reaction move 1 power icon from {}".format(me,card,players[1]))#ChamberofthePaintedTable
				if dominancewin[d][2] == "returniron":
					for cardhand in me.piles['Discard Pile']:
						if "Ironborn" in cardhand.traits and cardhand.type == "Character":
							list.append(cardhand)
					dlg = cardDlg(list)
					dlg.title = "These cards are in your Discard Pile:"
					dlg.text = "Declares at least 1 Ironborn Character put it into play."
					dlg.min = 1
					dlg.max = 1
					cards = dlg.show()
					if cards != None:
						cardintable(cards[0],"Character")
						notify("{}'s {} reaction put {} into play".format(me,card,cards[0]))#AeronDamphair
				if not reactioncardlimit.has_key(card._id):
					reactioncardlimit[card._id] = 1
				else:reactioncardlimit[card._id] += 1
				if reactioncardlimit[card._id] == dominancewin[d][5]:
					del reactionattach[card._id]
					c = 1
		if c == 0:
			reactionattach[card._id] -= 1
			if reactionattach[card._id] == 0:del reactionattach[card._id]
		remoteCall(players[1], "reaction", ["dominancewin",1])
	if repass == "reactionmarshal":
		if card.model == "499ed82d-cc0e-43a5-89ba-a748b388f528" and card.controller == me:
			if len(me.deck) > 0:
				draw(me.deck)
			if len(me.deck) > 0:
				draw(me.deck)
			notify("{}'s {} reaction draw cards".format(me,card,))#Littlefinger
		if card.model == "6ab37ed8-df99-410d-a9ff-7afe98f7ee22" and card.controller == me:
			remoteCall(cardtoaction.controller, "kneel", [cardtoaction])
			notify("{}'s {} reaction kneel {}".format(me,card,cardtoaction))#Melisandre
		if card.model == "47f94d62-7d83-4e36-80c6-0062d56aa820" and card.controller == me:
			list = []
			for disccard in players[1].piles['Discard pile']:
				if disccard.type == "Character" and int(disccard.cost) <= 3:
					if disccard.unique == "Yes":
						c = 0
						for ucard in table:
							if ucard.controller == me and ucard.name == disccard.name:
								c = 1
						if c == 0:list.append(disccard)
					else:
						list.append(disccard)
			dlg = cardDlg(list)
			dlg.title = "These cards are in Discard pile:"
			dlg.text = "select 1 Character card put it to tab."
			dlg.min = 1
			dlg.max = 1
			cards = dlg.show()
			if cards != None:
				remoteCall(players[1], "discintotable", [cards[0]])
				notify("{}'s {} reaction put {} in to play under {} control".format(me,card,cards[0],me))#Yoren
		if card.model == "8f2b58df-649e-4793-bd4c-bbf701cd57c5" and card.controller == me:
			if len(me.deck) > 0:
				draw(me.deck)
			if len(me.deck) > 0:
				draw(me.deck)
			if len(me.deck) > 0:
				draw(me.deck)
			notify("{}'s {} reaction draw 3 cards".format(me,card))#Pleasure Barge
		if card.model == "5347c5c6-a2cf-48e3-b851-7d4c68ffafc5" and card.controller == me:
			reduceint = int(me.getGlobalVariable("reduce_NW_card_turn")) + 1
			me.setGlobalVariable("reduce_NW_card_turn", str(reduceint))
			notify("{}'s {} reaction reduce the cost of the next [Night's Watch] card you marshal this phase by 1".format(me,card))#Brandon's Gift
		if card.model == "f88dd3c7-cae8-4e52-b810-8fbd8f70fd23" and card.controller == me:
			if len(me.deck) > 0:
				draw(me.deck)
			notify("{}'s {} reaction draw 1 card".format(me,card))#Northern Rookery
		if not reactioncardlimit.has_key(card._id):
			reactioncardlimit[card._id] = 1
		else:reactioncardlimit[card._id] += 1
		cardtoaction = []
		reactionattach = {}
		remoteCall(players[1], "action", ["marshal",1])

	if repass == "reactionplot":
		if card.model == "53d1c773-0f71-429c-a94e-6473d2e5a100" and card.controller == me:
			choiceList = ['Draw 1 card', 'Gain 1']
			colorList = ['#ae0603' ,'#006b34']
			choice = askChoice("Which one do you want to select?", choiceList,colorList)
			if choice == 1:
				if len(me.deck) > 0:draw(me.deck)
			if choice == 2:
				me.counters['Gold'].value += 1
		cardtoaction = []
		reactionattach = {}
		askfirstreveal(table)

def discintotable(card):
	mute()
	#cardintable(card,"Character",players[1])
	me.piles['Discard pile'].controller = players[1]
	card.controller = players[1]
	remoteCall(players[1], "cardintable", [card,"Character",players[1],1])

def checkreactioncard(count):
	mute()
	global reactionattach
	for card in table:
		for d in leavereacion:
			if card.model == leavereacion[d][1] and card.controller == me:
				for cards in leavetablecard:
					if leavereacion[d][2] == "Traits":
					 	if leavereacion[d][3] == "Lord./Lady.":
					 		if cards.Traits.find("Lord.") !=-1 or cards.Traits.find("Lady.") !=-1:
								if not reactionattach.has_key(card._id):
									reactionattach[card._id] = 1
								else:reactionattach[card._id] += 1
					elif leavereacion[d][2] == "Faction":
						if cards.Faction.find(leavereacion[d][3]) != -1 and cards.controller == me and orientationintable(card):
							if not reactionattach.has_key(card._id):
								reactionattach[card._id] = 1
							else:reactionattach[card._id] += 1
	debug("reactionattach2")
	debug(reactionattach)
	if count == 1:remoteCall(otherplayer, "checkreactioncard", [2])
	else:remoteCall(otherplayer, "reaction", ["leavetable",1])

def checkafterchallengereacioncard(count):
	mute()
	global reactionattach
	for card in table:
		for d in afterchallengereacion:
			if card.model == afterchallengereacion[d][1] and card.controller == me:
				if afterchallengereacion[d][2] != "all":
				 	if afterchallengereacion[d][2] == str(challengetype):
				 		if afterchallengereacion[d][3] == "all":
							if not reactionattach.has_key(card._id):
								reactionattach[card._id] = 1
							else:reactionattach[card._id] += 1
				elif afterchallengereacion[d][2] == "all":
					if afterchallengereacion[d][4] == "stand" and card.orientation == 1 and card.controller != attacker:
						if not reactionattach.has_key(card._id):
							reactionattach[card._id] = 1
						else:reactionattach[card._id] += 1
					if afterchallengereacion[d][4] == "stealth" and int(getGlobalVariable("cantchallenge")) > 1 and card.highlight in(MilitaryColor,IntrigueColor,PowerColor):
						if checktablecount(0) > 0 and card.controller == attacker:
							if not reactionattach.has_key(card._id):
								reactionattach[card._id] = 1
							else:reactionattach[card._id] += 1
					if afterchallengereacion[d][4] == "makedefender" and card.highlight in(MilitaryColor,IntrigueColor,PowerColor):
						if checktablecount(0) > 0 and card.controller == attacker:
							setGlobalVariable("bedefend","[]")
							if not reactionattach.has_key(card._id):
								reactionattach[card._id] = 1
							else:reactionattach[card._id] += 1
	debug("reactionattach1")
	debug(reactionattach)
	if len(reactionattach) > 0:setGlobalVariable("aftcr", "1")
	if count == 1:remoteCall(otherplayer, "checkafterchallengereacioncard", [2])
	else:
		if getGlobalVariable("aftcr") == "1":
			setGlobalVariable("aftcr", "")
			if fplay(1) == me:reaction("afterchallenge",1)
			else: 
				remoteCall(otherplayer, "reaction", ["afterchallenge",1])
		else:
			challengeaction(1)

def selectstealth(group, x=0, y=0):
	mute()
	targetTuple = [card._id for card in table if card in liststeal]
	selectcardnext(targetTuple,"stealthselect",table,[],me,1,actionstyle = 1)
	# setGlobalVariable("tableTargets", str(targetTuple))
	# setGlobalVariable("selectmode", "1")
	# if me.isInverted:table.create("584a37d7-5a30-4018-ae21-0ad325203fa0",-375,-250)
	# else:table.create("584a37d7-5a30-4018-ae21-0ad325203fa0",-375,200)
	# notify("**{} into selectmode**".format(me))
	# sessionpass = "stealthselect"

def selectcard(group,dlgmax,dlgmin,dlgtitle,dlgtext):
	listname = []
	listsamename = []
	dictsame = {}
	disctlistcount = {}
	listcheckcard = []
	listunsamecard = []
	global selectplayer
	selectplayer = []
	for card in group:
		if card.name not in listname:
			listname.append(card.name) 
		else:
			listsamename.append(card.name)
	for cname in listsamename:
		dictsame[cname]= 0
	for cardname in group:
		if cardname.name in listsamename:dictsame[cardname.name] = dictsame[cardname.name]+1

	dlg = cardDlg(group)
	dlg.title = dlgtitle
	dlg.text = dlgtext
	dlg.max = dlgmax
	dlg.min = dlgmin
	select = dlg.show()
	if select == None:selectcard(group,dlgmax,dlgmin,dlgtitle,dlgtext)
	else:
		debug(listsamename)
		for countcard in select:
			if countcard.name in listsamename:
				disctlistcount[countcard.name] = 0
		for countcards in select:
			if countcards.name in listsamename:
				disctlistcount[countcards.name] = disctlistcount[countcards.name]+1
		debug(listsamename)
		debug(disctlistcount)
		debug(dictsame)
		for cardselect in select:
			if cardselect.name in listsamename:
				if disctlistcount[cardselect.name] != dictsame[cardselect.name]:
					listcheckcard.append(cardselect.name)
		for card in select:
			if card.name not in listcheckcard:
				selectplayer.append(card)
		debug(listcheckcard)
		if len(listcheckcard) > 0:
			samecardproscess(group,listcheckcard,disctlistcount)

def samecardproscess(group,listname,count):
	global selectplayer
	listcard = []
	listchoice = []
	listcolor = []
	#listname = [carda,cardb....]
	#count= {carda:1,cardb:2.....}
	processcardname = ""
	debug(listname)
	for c in listname:
		processcardname = c
		break
	debug(processcardname)
	for card in group:
		if card.name == processcardname and card not in selectplayer:
			listchoice.append(card.name+" ability: "+str(int(card.Strength)+card.markers[STR_Up]))
			listcolor.append('#8f8f8f')
			listcard.append(card)
	choice = askChoice("select one?", listchoice,listcolor)
	if choice == 0:samecardproscess(group,listname,count)
	else:choice -= 1

	selectplayer.append(listcard[choice])
	listcard[choice].highlight = leaveandabilitycolor

	count[processcardname] -= 1
	if count[processcardname] == 0:
		del count[processcardname]
		listname.remove(processcardname)
	debug(count)
	if len(count) > 0:
		samecardproscess(group,listname,count)
	else:
		notify("ok")
		debug(selectplayer)

def next(group, x=0, y=0):
	mute()
	global selectedcard
	global sessionpass
	global stealthcount
	global savetarget
	global abilityattach
	global nextcardtmp
	global cardtoaction
	global interruptcancelcard
	global interruptcancelplayer
	global saveactionplayer
	global inserttarget
	global savetarget
	global mainpass
	global dwtmpcard
	global listattach
	global cardtmp
	global liststeal
	global interruptcardselect
	debug(sessionpass)
	selectedcard = []
	list = []
	listsave = []

	for card in table:
		if card.filter == targetcardcolor:
			if me.getGlobalVariable("setupOk") in ("4","5"):
				if card.controller == me:selectedcard.append(card)
			else:selectedcard.append(card)
	for card in me.hand:
		if card.filter == targetcardcolor:
			selectedcard.append(card)
	if sessionpass == "stealthselect":
		if len(selectedcard) > 1:
			whisper("You must select {} character.".format(stealthcount))
			return
		if len(selectedcard) == 0:
			liststeal = []
		else:
			nextcardtmp = selectedcard[0]
			selectlist = [card._id for card in table if card.Type == "Character" and card.controller != me and card.keywords.find("Stealth") == -1 and card.highlight == None]
			selectcardnext(selectlist,"stealthselectok",table,nextcardtmp,me)
			return
			# sessionpass = "stealthselectok"
			# stealthcard(table)
	if sessionpass == "milkillplayerselect":
		claim = challengeclaim(table)
		for card in table:
			if card.type == "Character" and card.controller == me and card.filter != WaitColor:
				list.append(card)
		c = len(list)
		if c < claim:
			b = c
		else:
			b = claim
		if len(selectedcard) != b:
			whisper("You must select {} character.".format(b))
			return
	
	if sessionpass == "selectadd1power":
		if len(selectedcard) == 0:
			whisper("You must select only one character gain 1 power.")
			return
	if sessionpass == "playattach":
		if len(selectedcard) == 1:
			debug(nextcardtmp)
			me.setGlobalVariable("playattach","1")
			setGlobalVariable("selectmode", "0")
			clearfilter("")
			for cardn in table:
				if cardn.name == "nextbutton" and cardn.controller == me:
					cardn.delete()#delete nextbutton
				if cardn.name == "marshalendbutton" and cardn.controller == me:
					cardn.delete()
				if cardn.name == "passnextbutton" and cardn.controller == me:
					cardn.delete()
			play(nextcardtmp)
			return
		if len(selectedcard) == 0:
			nextcardtmp = []
			sessionpass = ""
			clearfilter("")
			if getGlobalVariable("dominanceaction") != "0":remoteCall(players[1], "action", ["dominance",1])
			elif getGlobalVariable("marshalphase") != "0":action("marshal",1)
			else:remoteCall(players[1], "action", ["general",1])
			return
	if sessionpass == "attatchcardselect":
		if len(selectedcard) > 1 or len(selectedcard) == 0:
			whisper("You must select only one character to attach.")
			return
		# if len(selectedcard) == 0:
		# 	disc(listattach[0])
		# 	del listattach[0]
		# 	selectedcard = []
		# 	if len(listattach) > 0:attatchcard(listattach)
		# 	else:
		# 		reordertable(table)
		# 	return
	if interruptsessionpass == "selectinterruptcard":
		if len(selectedcard) == 0:interruptcardselect = None
		else:interruptcardselect = selectedcard
		interruptevent("interruptcancel",interruptpasscounttmp)
		clearfilter("")
		for cardn in table:
			if cardn.name == "nextbutton" and cardn.controller == me:
				cardn.delete()#delete nextbutton
		setGlobalVariable("selectmode", "0")
		return
	if sessionpass == "discattch":
		if len(selectedcard) > 1:
			whisper("You must select only one attachment to discard.")
			return
		elif len(selectedcard) == 0:
			sessionpass = ""
			clearfilter("")
			remoteCall(otherplayer,"interruptevent",["characterkill",1])
			return
		elif len(selectedcard) == 1:
			for card in table:
				card.target(False)
			remoteCall(selectedcard[0].controller, "disc", [selectedcard[0]])
	if sessionpass == "kneel" or sessionpass == "initimidateselect" or sessionpass == "FilthyAccusationsselect":
		if len(selectedcard) > 1:
			whisper("You must select only one character to kneel.")
			return
		elif len(selectedcard) == 0 and sessionpass != "FilthyAccusationsselect":
			sessionpass = ""
			clearfilter("")
			remoteCall(otherplayer,"interruptevent",["characterkill",1])
		elif len(selectedcard) == 1 and sessionpass != "FilthyAccusationsselect":
			for card in table:
				card.target(False)
			remoteCall(selectedcard[0].controller, "kneel", [selectedcard[0]])
	if sessionpass == "miljudgementselect":
		if len(selectedcard) > 1:
			whisper("You must select only one character to save.")
			return
		if len(selectedcard) == 1:
			listsave = checksavecard(selectedcard)
			if listsave != []:
				debug(listsave)
				for card in table:
					card.target(False)
				savetarget = selectedcard[0]
				debug("savetarget")
				debug(savetarget)
				targetTuple = ([card._id for card in listsave], me._id) 
				setGlobalVariable("tableTargets", str(targetTuple))
				setGlobalVariable("selectmode", "1")
				sessionpass = "savecardselect"
				notify("**{} into selectmode**".format(me))
				return
			else:
				whisper("You cannot save the character")
				return
	if sessionpass == "reactionaftc":
		if len(selectedcard) > 1:
			whisper("You must select only one card to reaction.")
			return
		if len(selectedcard) == 1 and selectedcard[0].model == afterchallengereacion['DornishParamour'][1] and getGlobalVariable("bedefend") != "":
			nextcardtmp = selectedcard[0]
			for card in table:
				card.target(False)
			targetTuple = ([card._id for card in table if card.Type == "Character" and card.controller != me], me._id) 
			setGlobalVariable("tableTargets", str(targetTuple))
			setGlobalVariable("selectmode", "1")
			sessionpass = "bedefendselect"
			notify("**{} into selectmode**".format(me))
			return
	if sessionpass == "bedefendselect":
		if len(selectedcard) > 1:
			whisper("You must select only one card to reaction.")
			return
	if sessionpass in ("select1cardme","select1cardot"):
		if len(selectedcard) == 0:
			whisper("You must select one card.")
			return
	if sessionpass == "select1cardme":
		selectedcard[0].highlight = standcolor
		#remoteCall(me, "returncard", [selectedcard[0]])
		selectlist = checkcardid(deck = table,player = players[1],highlight = '#ffa6f8')
		selectcardnext(selectlist,"select1cardot",table,[])
		return
	if sessionpass == "select1cardot":
		selectedcard[0].controller = me
		selectedcard[0].highlight = standcolor
		#remoteCall(me, "returncard", [selectedcard[0]])
		if fplay(1) == me:remoteCall(players[1], "select1card", [])
		else:remoteCall(fplay(1), "select1cardover", [1])
		clearfilter("")
		for cardn in table:
			if cardn.name == "nextbutton" and cardn.controller == me:
				cardn.delete()#delete nextbutton
				stealthcount = 0
			if cardn.name == "passnextbutton" and cardn.controller == me:
				cardn.delete()#delete nextbutton
			if cardn.name == "marshalendbutton" and cardn.controller == me:
				cardn.delete()
		setGlobalVariable("selectmode", "0")
		return
	if sessionpass == "Direwolfselect":
		if len(selectedcard) > 1:
			whisper("You must select only one card to reaction.")
			return
		if len(selectedcard) == 1:
			dwtmpcard = selectedcard[0]
			#kneel(selectedcard[0])
			for card in me.hand:
				card.target(False)
			for card in table:
				card.target(False)
			targetTuple = ([card._id for card in table if card.Type == "Character" and card.controller != me and card.highlight == IntrigueColor], me._id)
			setGlobalVariable("tableTargets", str(targetTuple))
			setGlobalVariable("selectmode", "1")
			sessionpass = "killselect"
			notify("**{} into selectmode**".format(me))
			return			
	if sessionpass == "reactionaftu":
		if len(selectedcard) > 1:
			whisper("You must select only one card to reaction.")
			return
		if len(selectedcard) == 1 and selectedcard[0].model == aftercalculate['RattleshirtsRaiders'][1]:
			nextcardtmp = selectedcard[0]
			for card in table:
				card.target(False)
			targetTuple = ([card._id for card in table if card.Type == "Attachment" and card.controller != me], me._id) 
			setGlobalVariable("tableTargets", str(targetTuple))
			setGlobalVariable("selectmode", "1")
			sessionpass = "discattchselect"
			notify("**{} into selectmode**".format(me))
			return
		if len(selectedcard) == 1 and selectedcard[0].model == aftercalculate['ThrowingAxe'][1]:
			nextcardtmp = selectedcard[0]
			if challengetype == 1:color = MilitaryColor
			if challengetype == 2:color = IntrigueColor
			if challengetype == 3:color = PowerColor
			debug(color)
			for card in table:
				card.target(False)
			targetTuple = ([card._id for card in table if card.Type == "Character" and card.controller != me and card.highlight == color], me._id) 
			setGlobalVariable("tableTargets", str(targetTuple))
			setGlobalVariable("selectmode", "1")
			sessionpass = "attkilldefselect"
			notify("**{} into selectmode**".format(me))
			return
		if len(selectedcard) == 1 and selectedcard[0].model == aftercalculate['GhastonGrey'][1]:
			nextcardtmp = selectedcard[0]
			if challengetype == 1:color = MilitaryColor
			if challengetype == 2:color = IntrigueColor
			if challengetype == 3:color = PowerColor
			debug(color)
			for card in table:
				card.target(False)
			targetTuple = ([card._id for card in table if card.Type == "Character" and card.controller != me and card.highlight == color], me._id) 
			setGlobalVariable("tableTargets", str(targetTuple))
			setGlobalVariable("selectmode", "1")
			sessionpass = "returndefenderselect"
			notify("**{} into selectmode**".format(me))
			return
		if len(selectedcard) == 1 and selectedcard[0].model == aftercalculate['PuttotheSword'][1]:
			nextcardtmp = selectedcard[0]
			debug(nextcardtmp)
			for card in me.hand:
				card.target(False)
			targetTuple = ([card._id for card in table if card.Type == "Character" and card.controller != me], me._id) 
			setGlobalVariable("tableTargets", str(targetTuple))
			setGlobalVariable("selectmode", "1")
			sessionpass = "killselect"
			notify("**{} into selectmode**".format(me))
			return
		if len(selectedcard) == 1 and selectedcard[0].model == aftercalculate['LikeWarmRain'][1]:
			nextcardtmp = selectedcard[0]
			for card in me.hand:
				card.target(False)
			targetTuple = ([card._id for card in table if card.controller == me and card.Traits == "Direwolf." and card.orientation == 0], me._id)
			setGlobalVariable("tableTargets", str(targetTuple))
			setGlobalVariable("selectmode", "1")
			sessionpass = "Direwolfselect"
			notify("**{} into selectmode**".format(me))
			return
		if len(selectedcard) == 1 and selectedcard[0].model == aftercalculate['PuttotheTorch'][1]:
			nextcardtmp = selectedcard[0]
			debug(nextcardtmp)
			for card in me.hand:
				card.target(False)
			targetTuple = ([card._id for card in table if card.Type == "Location" and card.controller != me], me._id) 
			setGlobalVariable("tableTargets", str(targetTuple))
			setGlobalVariable("selectmode", "1")
			sessionpass = "Locationselect"
			notify("**{} into selectmode**".format(me))
			return
		if len(selectedcard) == 1 and selectedcard[0].model == aftercalculate['TearsofLys'][1]:
			nextcardtmp = selectedcard[0]
			for card in me.hand:
				card.target(False)
			targetTuple = ([card._id for card in table if card.Type == "Character" and card.controller != me and card.Intrigue != "Yes" and  card.markers[IntrigueIcon] == 0], me._id) 
			setGlobalVariable("tableTargets", str(targetTuple))
			setGlobalVariable("selectmode", "1")
			sessionpass = "lysselect"
			notify("**{} into selectmode**".format(me))
			return
		if len(selectedcard) == 1 and selectedcard[0].model == aftercalculate['PlazaofPunishment'][1]:
			nextcardtmp = selectedcard[0]
			for card in table:
				card.target(False)
			attach = eval(getGlobalVariable("attachmodify"))
			listpop = []
			for card in table:
				if card.controller != me:
					c = 0
					for d in attach:
						if card._id == d:
							c = 1
					if c == 0:
						listpop.append(card)
			targetTuple = ([card._id for card in table if card in listpop ], me._id) 
			setGlobalVariable("tableTargets", str(targetTuple))
			setGlobalVariable("selectmode", "1")
			sessionpass = "popselect"
			notify("**{} into selectmode**".format(me))
			return
		if len(selectedcard) == 1 and selectedcard[0].model == aftercalculate['TheMander'][1]:
			kneel(selectedcard[0])
		if len(selectedcard) == 1 and selectedcard[0].model == aftercalculate['Rhaegal'][1]:
			nextcardtmp = selectedcard[0]
			for card in table:
				card.target(False)
			targetTuple = ([card._id for card in table if card.controller == me and card.highlight in (MilitaryColor,IntrigueColor,PowerColor) and "Stormborn." in card.Traits and card.orientation == 1], me._id) 
			setGlobalVariable("tableTargets", str(targetTuple))
			setGlobalVariable("selectmode", "1")
			sessionpass = "stmselect"
			notify("**{} into selectmode**".format(me))
			return
		if len(selectedcard) == 1 and selectedcard[0].model == aftercalculate['DothrakiSea'][1]:
			nextcardtmp = selectedcard[0]
			for card in table:
				card.target(False)
			targetTuple = ([card._id for card in me.hand if card.Type == "Character" and "Dothraki." in card.Traits], me._id)
			setGlobalVariable("tableTargets", str(targetTuple))
			setGlobalVariable("selectmode", "1")
			sessionpass = "dothrakiselect"
			notify("**{} into selectmode**".format(me))
			return
		if len(selectedcard) == 1 and selectedcard[0].model == aftercalculate['TheQueenofThorns'][1]:
			nextcardtmp = selectedcard[0]
			for card in table:
				card.target(False)
			targetTuple = ([card._id for card in me.hand if "Tyrell." in card.Faction and int(card.cost) <= 6 and card.Type == "Character"], me._id)
			setGlobalVariable("tableTargets", str(targetTuple))
			setGlobalVariable("selectmode", "1")
			sessionpass = "tyrellselect"
			notify("**{} into selectmode**".format(me))
			return
		if len(selectedcard) == 1 and selectedcard[0].model == aftercalculate['MaesterCaleotte'][1]:
			nextcardtmp = selectedcard[0]
			for card in table:
				card.target(False)
			targetTuple = ([card._id for card in table if card.Type == "Character"], me._id)
			setGlobalVariable("tableTargets", str(targetTuple))
			setGlobalVariable("selectmode", "1")
			sessionpass = "submarkerselect"
			notify("**{} into selectmode**".format(me))
			return
		if len(selectedcard) == 1 and selectedcard[0].model == aftercalculate['Ice'][1]:
			nextcardtmp = selectedcard[0]
			for card in table:
				card.target(False)
			targetTuple = ([card._id for card in table if card.Type == "Character" and card.controller != me], me._id)
			setGlobalVariable("tableTargets", str(targetTuple))
			setGlobalVariable("selectmode", "1")
			sessionpass = "iceselect"
			notify("**{} into selectmode**".format(me))
			return
	if sessionpass == "challenge":
		if len(selectedcard) > 1:
			whisper("You must select only one card to action.")
			return
		if len(selectedcard) == 0:
			remoteCall(otherplayer, "action", ["challenge",1])
			return
		if len(selectedcard) == 1 and "Ambush" in selectedcard[0].keywords:
			sessionpass = "ambush"
			
		if len(selectedcard) == 1 and selectedcard[0].model == actionchallenge['WildlingHorde'][1]:
			nextcardtmp = selectedcard[0]
			for card in table:
				card.target(False)
			targetTuple = ([card._id for card in table if "Wildling" in card.Traits and card.highlight in (MilitaryColor,IntrigueColor,PowerColor) and card.controller == me], me._id)
			setGlobalVariable("tableTargets", str(targetTuple))
			setGlobalVariable("selectmode", "1")
			sessionpass = "kneelhouseok"
			notify("**{} into selectmode**".format(me))
			return
		if len(selectedcard) == 1 and selectedcard[0].model == actionchallenge['SelyseBaratheon'][1]:
			nextcardtmp = selectedcard[0]
			for card in table:
				card.target(False)
			targetTuple = ([card._id for card in table if card.Faction == "Baratheon."], me._id)
			setGlobalVariable("tableTargets", str(targetTuple))
			setGlobalVariable("selectmode", "1")
			sessionpass = "addintselectok"
			notify("**{} into selectmode**".format(me))
			return
		if len(selectedcard) == 1 and selectedcard[0].model == actionchallenge['OursistheFury'][1]:
			nextcardtmp = selectedcard[0]
			for card in me.hand:
				card.target(False)
			targetTuple = ([card._id for card in table if card.Faction == "Baratheon." and card.type == "Character" and card.orientation == 1], me._id)
			setGlobalVariable("tableTargets", str(targetTuple))
			setGlobalVariable("selectmode", "1")
			sessionpass = "adddefselectok"
			notify("**{} into selectmode**".format(me))
			return
		if len(selectedcard) == 1 and selectedcard[0].model == actionchallenge['SeenInFlames'][1]:
			nextcardtmp = selectedcard[0]
			sessionpass = "dischandselectok"
		if len(selectedcard) == 1 and selectedcard[0].model == actionchallenge['IronFleetScout'][1]:
			nextcardtmp = selectedcard[0]
			for card in table:
				card.target(False)
			targetTuple = ([card._id for card in table if card.Faction == "Greyjoy." and card.type == "Character" and card.highlight in (MilitaryColor,IntrigueColor,PowerColor)], me._id)
			setGlobalVariable("tableTargets", str(targetTuple))
			setGlobalVariable("selectmode", "1")
			sessionpass = "adddstrselectok"
			notify("**{} into selectmode**".format(me))
			return
		if len(selectedcard) == 1 and selectedcard[0].model == actionchallenge['TheKrakensGrasp'][1]:
			nextcardtmp = selectedcard[0]
			for card in me.hand:
				card.target(False)
			targetTuple = ([card._id for card in table if card.controller != me and card.type == "Character" and card.highlight in (MilitaryColor,IntrigueColor,PowerColor) and int(card.cost) <= 5], me._id)
			setGlobalVariable("tableTargets", str(targetTuple))
			setGlobalVariable("selectmode", "1")
			sessionpass = "ignorestrselectok"
			notify("**{} into selectmode**".format(me))
			return
		if len(selectedcard) == 1 and selectedcard[0].model == actionchallenge['TheThingsIDoForLove'][1]:
			nextcardtmp = selectedcard[0]
			for card in me.hand:
				card.target(False)
			cost=askInteger("How much do you want to pay to play {} ? ".format(selectedcard[0].name),0)
			if cost > 0:
				targetTuple = ([card._id for card in table if card.controller != me and card.type == "Character" and int(card.cost) <= cost], me._id)
				setGlobalVariable("tableTargets", str(targetTuple))
				setGlobalVariable("selectmode", "1")
				sessionpass = "addstrdrawselectok"
				notify("**{} into selectmode**".format(me))
				return
			else:
				delactioncard(nextcardtmp)
				nextcardtmp = []
				sessionpass = ""
				remoteCall(otherplayer, "action", ["challenge",1])
				return
		if len(selectedcard) == 1 and selectedcard[0].model == actionchallenge['FortheNorth'][1]:
			nextcardtmp = selectedcard[0]
			for card in me.hand:
				card.target(False)
			targetTuple = ([card._id for card in table if card.type == "Character" and card.highlight in (MilitaryColor,IntrigueColor,PowerColor) and card.faction == "Stark."], me._id)
			setGlobalVariable("tableTargets", str(targetTuple))
			setGlobalVariable("selectmode", "1")
			sessionpass = "addclaimselectok"
			notify("**{} into selectmode**".format(me))
			return
		if len(selectedcard) == 1 and selectedcard[0].model == actionchallenge['WinterIsComing'][1]:
			nextcardtmp = selectedcard[0]
			sessionpass = "drawstarkselectok"
		if len(selectedcard) == 1 and selectedcard[0].model == actionchallenge['GatesofWinterfell'][1]:
			nextcardtmp = selectedcard[0]
			sessionpass = "drawstarkselectok"
		if len(selectedcard) == 1 and selectedcard[0].model == actionchallenge['Dracarys'][1]:
			nextcardtmp = selectedcard[0]
			for card in me.hand:
				card.target(False)
			targetTuple = ([card._id for card in table if "Dragon." in card.traits or card.model == "a2f21413-0272-47dc-a197-e364aa942d4c" and card.controller == me and card.orientation == 0], me._id)
			setGlobalVariable("tableTargets", str(targetTuple))
			setGlobalVariable("selectmode", "1")
			sessionpass = "burnselect"
			notify("**{} into selectmode**".format(me))
			return
		if len(selectedcard) == 1 and selectedcard[0].model == actionchallenge['FireandBlood'][1]:
			nextcardtmp = selectedcard[0]
			for card in me.hand:
				card.target(False)
			list2 = []
			for carddead in me.piles['Dead Pile']:
				if carddead.Faction == "Targaryen." and carddead.Unique =="Yes" and carddead.Type == "Character":
					list.append(carddead)
			dlg = cardDlg(list)
			dlg.title = "These cards are in your Dead Pile:"
			dlg.text = "Declares at least 1 card to action."
			dlg.min = 1
			dlg.max = 1
			cards = dlg.show()
			cardtoaction = cards[0]
			sessionpass = "returndeadselectok"
		if len(selectedcard) == 1 and selectedcard[0].model == actionchallenge['MargaeryTyrell'][1]:
			nextcardtmp = selectedcard[0]
			for card in table:
				card.target(False)
			targetTuple = ([card._id for card in table if card.type == "Character"], me._id)
			setGlobalVariable("tableTargets", str(targetTuple))
			setGlobalVariable("selectmode", "1")
			sessionpass = "addstr3selectok"
			notify("**{} into selectmode**".format(me))
			return
		if len(selectedcard) == 1 and selectedcard[0].model == actionchallenge['Heartsbane'][1]:
			nextcardtmp = selectedcard[0]
			for card in table:
				card.target(False)
			attach = eval(getGlobalVariable("attachmodify"))
			for cardatt in table:
				if cardatt._id == attach[nextcardtmp._id]:
					cardtoaction = cardatt
			sessionpass = "attaddstr3selectok"
		if len(selectedcard) == 1 and selectedcard[0].model == actionchallenge['Highgarden'][1]:
			nextcardtmp = selectedcard[0]
			for card in table:
				card.target(False)
			targetTuple = ([card._id for card in table if card.type == "Character" and card.highlight in (MilitaryColor,IntrigueColor,PowerColor) and card.controller == attacker], me._id)
			setGlobalVariable("tableTargets", str(targetTuple))
			setGlobalVariable("selectmode", "1")
			sessionpass = "standremovechallengeselectok"
			notify("**{} into selectmode**".format(me))
			return
		if len(selectedcard) == 1 and selectedcard[0].model == actionchallenge['GrowingStrong'][1]:
			nextcardtmp = selectedcard[0]
			for card in me.hand:
				card.target(False)
			targetTuple = ([card._id for card in table if card.type == "Character" and card.Faction == "Tyrell."], me._id)
			setGlobalVariable("tableTargets", str(targetTuple))
			setGlobalVariable("selectmode", "1")
			sessionpass = "3playeraddstr2selectok"
			notify("**{} into selectmode**".format(me))
			return
	if sessionpass == "burnselect":
		dwtmpcard = selectedcard[0]
		for card in me.hand:
			card.target(False)
		for card in table:
			card.target(False)
		targetTuple = ([card._id for card in table if card.type == "Character" and card.highlight in (MilitaryColor,IntrigueColor,PowerColor) and int(card.cost)], me._id)
		setGlobalVariable("tableTargets", str(targetTuple))
		setGlobalVariable("selectmode", "1")
		sessionpass = "burnselectok"
		notify("**{} into selectmode**".format(me))
		return
	if sessionpass == "marshal":
		if len(selectedcard) == 1:
			c = 0
			uniquecards = []
			for u in table:
				if u.controller == me and u.unique == "Yes":
					uniquecards.append(u.name)
					if selectedcard[0].name in uniquecards: 
						cost=0
						c = 1   #Duplicates
						x,y = u.position
						break
			for card in me.hand:
				if card.type in("Character","Attachment","Location") and card._id == selectedcard[0]._id:
					if c == 1 or me.getGlobalVariable("isselect") == "1" or checkdbclickselectcard(selectedcard[0]):
						sessionpass = ""
						clearfilter("")
						for cardn in table:
							if cardn.name == "nextbutton" and cardn.controller == me:
								cardn.delete()#delete nextbutton
							if cardn.name == "marshalendbutton" and cardn.controller == me:
								cardn.delete()
							if cardn.name == "passnextbutton" and cardn.controller == me:
								cardn.delete()
						setGlobalVariable("selectmode", "0")
						me.setGlobalVariable("isselect", "0")
						play(selectedcard[0])
						return
	if sessionpass == "reactionmarshal":
		if len(selectedcard) == 0:
			clearfilter("")
			for cardn in table:
				if cardn.name == "nextbutton" and cardn.controller == me:
					cardn.delete()#delete nextbutton
			remoteCall(players[1], "action", ["marshal",1])
		if len(selectedcard) == 1 and selectedcard[0].model == "499ed82d-cc0e-43a5-89ba-a748b388f528":
			for card in table:card.target(False)
			nextcardtmp = selectedcard[0]
			sessionpass = "drwa2cardselectok"
		if len(selectedcard) == 1 and selectedcard[0].model == "6ab37ed8-df99-410d-a9ff-7afe98f7ee22":
			for card in table:card.target(False)
			nextcardtmp = selectedcard[0]
			selectlist = checkcardid(deck = table,cardtype = "Character",stand = 0)
			selectcardnext(selectlist,"lhlkneelselectok",table,nextcardtmp,me)
			return
		if len(selectedcard) == 1 and selectedcard[0].model == "47f94d62-7d83-4e36-80c6-0062d56aa820":
			for card in table:card.target(False)
			nextcardtmp = selectedcard[0]
			sessionpass = "discdiscselectok"
		if len(selectedcard) == 1 and selectedcard[0].model == "8f2b58df-649e-4793-bd4c-bbf701cd57c5":
			for card in table:card.target(False)
			nextcardtmp = selectedcard[0]
			sessionpass = "draw3selectok"
		if len(selectedcard) == 1 and selectedcard[0].model == "5347c5c6-a2cf-48e3-b851-7d4c68ffafc5":
			for card in table:card.target(False)
			nextcardtmp = selectedcard[0]
			sessionpass = "reducenwselectok"
		if len(selectedcard) == 1 and selectedcard[0].model == "f88dd3c7-cae8-4e52-b810-8fbd8f70fd23":
			for card in table:card.target(False)
			nextcardtmp = selectedcard[0]
			sessionpass = "mdraw1selectok"
	if sessionpass == "reactionplot":
		if len(selectedcard) == 0:
			clearfilter("")
			for cardn in table:
				if cardn.name == "nextbutton" and cardn.controller == me:
					cardn.delete()#delete nextbutton
			askfirstreveal(table)
		if len(selectedcard) == 1 and selectedcard[0].model == "53d1c773-0f71-429c-a94e-6473d2e5a100":
			for card in table:card.target(False)
			nextcardtmp = selectedcard[0]
			sessionpass = "plotdrawgoldselectok"

	if sessionpass in ("general","dominance","standing","taxation","marshal"):
		if len(selectedcard) > 1:
			whisper("You must select only one card to action.")
			return
		if len(selectedcard) == 0:
			actioncancelcount = int(getGlobalVariable("actioncancel"))+1
			debug(actioncancelcount)
			if actioncancelcount == 2 and sessionpass == "marshal":
				if not confirm("End Marshal?"):return
			setGlobalVariable("actioncancel", str(actioncancelcount))
			clearfilter("")
			for cardn in table:
				if cardn.name == "nextbutton" and cardn.controller == me:
					cardn.delete()#delete nextbutton
					stealthcount = 0
				if cardn.name == "marshalendbutton" and cardn.controller == me:
					cardn.delete()#delete marshalendbutton
				if cardn.name == "passnextbutton" and cardn.controller == me:
					cardn.delete()#delete marshalendbutton
			setGlobalVariable("selectmode", "0")
			if actioncancelcount == 2:
				setGlobalVariable("actioncancel", "0")
				notify("action over")
				if sessionpass != "marshal":clearaction(1)
				if sessionpass == "marshal":
					if str(me._id) == getGlobalVariable("activeplayer") and fplay(1) == me:
						setGlobalVariable("activeplayer",str(players[1]._id))
						remoteCall(players[1], "marshalactions", [])
					elif str(me._id) != getGlobalVariable("activeplayer") and fplay(1) != me:
						setGlobalVariable("activeplayer",str(me._id))
						remoteCall(me, "marshalactions", [])
					elif str(me._id) != getGlobalVariable("activeplayer") and fplay(1) == me:
						if fplay(1) == me:marshalphaseend()
						else:remoteCall(players[1], "marshalphaseend", [])
					elif str(me._id) == getGlobalVariable("activeplayer") and fplay(1) != me:
						if fplay(1) == me:marshalphaseend()
						else:remoteCall(players[1], "marshalphaseend", [])
			else:remoteCall(players[1], "action", [sessionpass,2])
			sessionpass = ""

			return
		if len(selectedcard) == 1 and selectedcard[0].model == generalaction['HearMeRoar'][1]:
			for card in me.hand:card.target(False)
			nextcardtmp = selectedcard[0]
			selectlist = checkcardid(deck = me.hand,cardtype = "Character",faction = "Lannister.")
			selectcardnext(selectlist,"addlanselectok",me.hand,nextcardtmp,me)
			return
		if len(selectedcard) == 1 and selectedcard[0].model == generalaction['ArianneMartell'][1]:
			for card in table:card.target(False)
			nextcardtmp = selectedcard[0]
			selectlist = checkcardid(deck = me.hand,cardtype = "Character",cost = 5)
			debug(selectlist)
			selectcardnext(selectlist,"add5returnmeselectok",me.hand,nextcardtmp,me)
			return
		if len(selectedcard) == 1 and selectedcard[0].model == generalaction['EdricDayne'][1]:
			for card in table:card.target(False)
			nextcardtmp = selectedcard[0]
			sessionpass = "1goldiconselectok"
		if len(selectedcard) == 1 and selectedcard[0].model == generalaction['Confinement'][1]:
			for card in me.hand:card.target(False)
			nextcardtmp = selectedcard[0]
			selectlist = checkcardid(deck = table,cardtype = "Character",cost = 4)
			selectcardnext(selectlist,"loseiconselectok",table,nextcardtmp,me)
			return
		if len(selectedcard) == 1 and selectedcard[0].model == generalaction['OldForestHunter'][1]:
			for card in table:card.target(False)
			nextcardtmp = selectedcard[0]
			selectlist = checkcardid(deck = me.hand)
			selectcardnext(selectlist,"d1cg1gselectok",me.hand,nextcardtmp,me)
			return
		if len(selectedcard) == 1 and selectedcard[0].model == generalaction['VeteranBuilder'][1]:
			for card in table:card.target(False)
			nextcardtmp = selectedcard[0]
			selectlist = checkcardid(deck = table,cardtype = "Location",stand = 1)
			selectcardnext(selectlist,"standlocationselectok",table,nextcardtmp,me)
			return
		if len(selectedcard) == 1 and selectedcard[0].model == generalaction['MagisterIllyrio'][1]:
			for card in table:card.target(False)
			nextcardtmp = selectedcard[0]
			selectlist = checkcardid(deck = table,cardtype = "Character",stand = 1)
			selectcardnext(selectlist,"2gstandcselectok",table,nextcardtmp,me)
			return
		if len(selectedcard) == 1 and selectedcard[0].model == generalaction['Handmaiden'][1]:
			for card in table:card.target(False)
			nextcardtmp = selectedcard[0]
			selectlist = checkcardid(deck = table,cardtype = "Character",traits = "Lady.",stand = 1)
			selectcardnext(selectlist,"standladyselectok",table,nextcardtmp,me)
			return
		if len(selectedcard) == 1 and selectedcard[0].model == generalaction['WakingtheDragon'][1]:
			for card in me.hand:card.target(False)
			nextcardtmp = selectedcard[0]
			selectlist = checkcardid(deck = table,cardtype = "Character",faction = "Targaryen.",unique = "Yes")
			selectcardnext(selectlist,"standtcselectok",table,nextcardtmp,me)
			return
		if len(selectedcard) == 1 and selectedcard[0].model == generalaction['TheBearandtheMaidenFair'][1]:
			for card in me.hand:card.target(False)
			nextcardtmp = selectedcard[0]
			sessionpass = "5t3bselectok"
		if len(selectedcard) == 1 and selectedcard[0].model == generalaction['Fealty'][1]:
			for card in table:card.target(False)
			nextcardtmp = selectedcard[0]
			sessionpass = "kneelfactionselectok"
		if len(selectedcard) == 1 and selectedcard[0].model == generalaction['PowerBehindtheThrone'][1]:
			for card in table:card.target(False)
			nextcardtmp = selectedcard[0]
			selectlist = checkcardid(deck = table,cardtype = "Character",stand = 1)
			selectcardnext(selectlist,"standiconselectok",table,nextcardtmp,me)
			return
		if len(selectedcard) == 1 and selectedcard[0].model == generalaction['Nightmares'][1]:
			for card in table:card.target(False)
			nextcardtmp = selectedcard[0]
			selectlist = checkcardid(deck = table,cardtype = ("Character","Location"))
			selectcardnext(selectlist,"noprintselectok",table,nextcardtmp,me)
			return
		if len(selectedcard) == 1 and selectedcard[0].model == generalaction['Lady'][1]:
			for card in table:card.target(False)
			nextcardtmp = selectedcard[0]
			debug(cardtmp)
			for checkcard in table:
				if checkcard.faction == "Stark." and checkcard.type == "Character" and checkcard.filter != WaitColor and  not 'No attachments' in checkcard.Keywords and checkcard != cardtoaction:
					list.append(checkcard._id)
			selectcardnext(list,"changecontrollselectok",table,nextcardtmp)
			return
		if len(selectedcard) == 1 and selectedcard[0].model == generalaction['AGiftofArborRed'][1]:
			for card in table:card.target(False)
			nextcardtmp = selectedcard[0]
			sessionpass = "4cardchoose2selectok"
		if len(selectedcard) == 1 and selectedcard[0].model == generalaction['Halder'][1] and generalaction['Halder'][2] == "manual":
			manualprocess(selectedcard[0],"generalaction")
		if len(selectedcard) == 1 and selectedcard[0].model == generalaction['TheWatchHasNeed'][1]:
			for card in me.hand:card.target(False)
			nextcardtmp = selectedcard[0]
			sessionpass = "searchbrsok"
		if len(selectedcard) == 1 and selectedcard[0].model == generalaction['InDoransName'][1]:
			for card in me.hand:card.target(False)
			nextcardtmp = selectedcard[0]
			sessionpass = "addusedplotgoldselectok"
		if len(selectedcard) == 1 and selectedcard[0].model == generalaction['WolfDreams'][1]:
			for card in me.hand:card.target(False)
			nextcardtmp = selectedcard[0]
			sessionpass = "searchwolfselectok"
		if len(selectedcard) == 1 and selectedcard[0].model == marshalaction['Bronn'][1]:
			for card in me.hand:card.target(False)
			nextcardtmp = selectedcard[0]
			sessionpass = "controllbselectok"
		if len(selectedcard) == 1 and selectedcard[0].model == dominanceaction['TaketheBlack'][1]:
			setGlobalVariable("selectmode", "0")
			play(selectedcard[0])
			manualprocess(selectedcard[0],"dominance")
		if len(selectedcard) == 1 and selectedcard[0].model == dominanceaction['MessengerRaven'][1]:
			for card in me.hand:card.target(False)
			nextcardtmp = selectedcard[0]
			sessionpass = "returndraw1selectok"
		if len(selectedcard) == 1 and selectedcard[0].model == dominanceaction['TheTickler'][1]:
			# setGlobalVariable("selectmode", "0")
			# manualprocess(selectedcard[0],"dominance")
			for card in table:card.target(False)
			nextcardtmp = selectedcard[0]
			sessionpass = "disctopselectok"
		if len(selectedcard) == 1 and selectedcard[0].model == marshalaction['TheKingsroad'][1]:
			for card in me.hand:card.target(False)
			nextcardtmp = selectedcard[0]
			sessionpass = "reduce3sselectok"
		if len(selectedcard) == 1 and selectedcard[0].model in (marshalaction['DragonstoneFaithful'][1],marshalaction['DragonstonePort'][1],marshalaction['IronIslandsFishmonger'][1],marshalaction['SeaTower'][1],marshalaction['LannisportMerchant'][1],marshalaction['WesternFiefdom'][1],marshalaction['DesertScavenger'][1],marshalaction['BloodOrangeGrove'][1],marshalaction['StewardattheWall'][1],marshalaction['Winterfellteward'][1],marshalaction['HeartTreeGrove'][1],marshalaction['TargaryenLoyalist'][1],marshalaction['IllyriosEstate'][1],marshalaction['GardenCaretake'][1],marshalaction['RoseGarden'][1]):
			for card in me.hand:card.target(False)
			nextcardtmp = selectedcard[0]
			sessionpass = "reducecardselectok"
		if len(selectedcard) == 1 and selectedcard[0].model == marshalaction['MaesterCressen'][1]:
			for card in table:card.target(False)
			nextcardtmp = selectedcard[0]
			selectlist = checkcardid(deck = table,cardtype = "Attachment",traits = "Condition.")
			selectcardnext(selectlist,"discattachmentcselectok",table,nextcardtmp,"")
			return
		if len(selectedcard) == 1 and selectedcard[0].model == marshalaction['ConsolidationofPower'][1]:
			for card in table:card.target(False)
			nextcardtmp = selectedcard[0]
			selectlist = checkcardid(deck = table,cardtype = "Character",stand = 0,cost = 4)
			selectcardnext(selectlist,"kneel4cadd1powercselectok",table,nextcardtmp,"",0,mode = 99)
			return
		if len(selectedcard) == 1 and selectedcard[0].model == marshalaction['LordsportShipwright'][1]:
			for card in table:card.target(False)
			nextcardtmp = selectedcard[0]
			if fplay(1) == me:selectlist = checkcardid(deck = table,cardtype = "Location",stand = 0,cost = 3)
			else:selectlist = checkcardid(deck = table,cardtype = "Location",stand = 0,cost = 3)
			selectcardnext(selectlist,"kneel2locationselectok",table,nextcardtmp,"",0,mode = 1)
			return

	if sessionpass == "dominancestart":
		if len(selectedcard) > 1:
			whisper("You must select only one card to action.")
			return
		if len(selectedcard) == 0:
			sessionpass = ""
			clearfilter("")
			for cardn in table:
				if cardn.name == "nextbutton" and cardn.controller == me:
					cardn.delete()#delete nextbutton
					stealthcount = 0
			setGlobalVariable("selectmode", "0")
			actioncancelcount = int(getGlobalVariable("actioncancel"))+1
			setGlobalVariable("actioncancel", str(actioncancelcount))
			if actioncancelcount == 2:
				setGlobalVariable("actioncancel", "0")
				notify("reaction over")
				clearaction(1)
			else:
				remoteCall(players[1], "reaction", ["dominancestart",2])
				return
		if len(selectedcard) == 1 and selectedcard[0].model == dominancestart['FieryFollowers'][1]:
			for card in table:card.target(False)
			nextcardtmp = selectedcard[0]
			sessionpass = "dominancestandok"
	if sessionpass == "dominancewin":
		if len(selectedcard) > 1:
			whisper("You must select only one card to action.")
			return
		if len(selectedcard) == 0:
			sessionpass = ""
			clearfilter("")
			for cardn in table:
				if cardn.name == "nextbutton" and cardn.controller == me:
					cardn.delete()#delete nextbutton
					stealthcount = 0
			setGlobalVariable("selectmode", "0")
			actioncancelcount = int(getGlobalVariable("actioncancel"))+1
			setGlobalVariable("actioncancel", str(actioncancelcount))
			if actioncancelcount == 2:
				setGlobalVariable("actioncancel", "0")
				notify("reaction over")
				clearaction(1)
			else:
				remoteCall(players[1], "reaction", ["dominancewin",2])
				return
		if len(selectedcard) == 1 and selectedcard[0].model == dominancewin['AFeastforCrows'][1]:
			for card in table:card.target(False)
			nextcardtmp = selectedcard[0]
			sessionpass = "dominance2powerok"
		if len(selectedcard) == 1 and selectedcard[0].model == dominancewin['ChamberofthePaintedTable'][1]:
			for card in table:card.target(False)
			nextcardtmp = selectedcard[0]
			sessionpass = "dominancemove1powok"
		if len(selectedcard) == 1 and selectedcard[0].model == dominancewin['AeronDamphair'][1]:
			for card in table:card.target(False)
			nextcardtmp = selectedcard[0]
			sessionpass = "dominancereturnironok"
	if sessionpass == "dominanceend":
		if len(selectedcard) > 1:
			whisper("You must select only one card to action.")
		if len(selectedcard) == 0:
			sessionpass = ""
			clearfilter("")
			for cardn in table:
				if cardn.name == "nextbutton" and cardn.controller == me:
					cardn.delete()#delete nextbutton
					stealthcount = 0
			setGlobalVariable("selectmode", "0")
			actioncancelcount = int(getGlobalVariable("actioncancel"))+1
			setGlobalVariable("actioncancel", str(actioncancelcount))
			if actioncancelcount == 2:
				setGlobalVariable("actioncancel", "0")
				notify("reaction over")
				clearaction(1)
			else:
				remoteCall(players[1], "reaction", ["dominanceend",2])
				return
		if len(selectedcard) == 1 and selectedcard[0].model == dominanceend['Varys'][1]:
			manualprocess(selectedcard[0],"dominanceend")

	if sessionpass in("addlanselectok","add5returnmeselectok","loseiconselectok","standlocationselectok","2gstandcselectok","standladyselectok","standtcselectok","5t3bselectok","standiconselectok","d1cg1gselectok"):
		if len(selectedcard) > 1:
			whisper("You must select only one card to action.")
			return

	if sessionpass == "kneel4cadd1powercselectok":
		if len(selectedcard) > 1:
			countplayer = []
			for countcard in selectedcard:
				debug(countplayer)
				if countplayer == []:countplayer = countcard.controller
				else:
					if countplayer != countcard.controller:
						whisper("Please select characters for only one player")
						return
			costcard = 0
			for cardcost in selectedcard:
				costcard += int(cardcost.cost)
			if 	costcard > 4:
				whisper("Please select  up to 4 STR worth of characters")
				return
	if sessionpass == "actionok":
		if len(selectedcard) > 1:
			whisper("You must select only one card to action.")
			return
	if sessionpass == "marshalcardselect":
		if len(selectedcard) > 1:
			whisper("You must select only one card to marshal.")
			return
		if len(selectedcard) == 0:
			marshalphase(table)
			return
	if sessionpass == "Confiscationselect":
		if len(selectedcard) > 1:
			whisper("You must select only one attachment.")
			return
	if sessionpass == "savecardselect":
		if len(selectedcard) > 1:
			whisper("You must select only one card to save.")
			return
	if sessionpass == "killability" or sessionpass == "attkilldefselect":
		if len(selectedcard) > 1:
			whisper("You must select only one Character.")
			return
		if len(selectedcard) == 0:
			clearfilter("")
			for cardn in table:
				if cardn.name == "nextbutton" and cardn.controller == me:
					cardn.delete()#delete nextbutton
					stealthcount = 0
			setGlobalVariable("selectmode", "0")
			actioncancelcount = int(getGlobalVariable("actioncancel"))+1
			setGlobalVariable("actioncancel", str(actioncancelcount))
			if actioncancelcount == 2:
				setGlobalVariable("actioncancel", "0")
				notify("action over")
				if getGlobalVariable("plotdisc") == "1":plotdisccard(1)
				else:cardleavetable(1)
			else:remoteCall(otherplayer, "action", [sessionpass,2])
			sessionpass = ""
			return
	if sessionpass == "plotdisccharacter1" or sessionpass == "plotdisccharacter2":
		if len(selectedcard) > 1 or len(selectedcard) == 0:
			whisper("You must select only one Character.")
			return
	if sessionpass == "plotkillcharacter1" or sessionpass == "plotkillcharacter2":
		if len(selectedcard) > 3:
			whisper("You must select up to 3 characters.")
			return
		if len(selectedcard) == 0:
			if not confirm ("This will kill all of your characters,continue?"):return
	if sessionpass == "killabilitychooseone":
		if len(selectedcard) > 1:
			whisper("You must select only one Character.")
			return
	if sessionpass == "reaction" or sessionpass == "reactionaftc":
		if len(selectedcard) > 1:
			whisper("You must select only one card to reaction.")
			return
		if len(selectedcard) == 0:
			clearfilter("")
			for cardn in table:
				if cardn.name == "nextbutton" and cardn.controller == me:
					cardn.delete()#delete nextbutton
					stealthcount = 0
			setGlobalVariable("selectmode", "0")
			actioncancelcount = int(getGlobalVariable("actioncancel"))+1
			setGlobalVariable("actioncancel", str(actioncancelcount))
			if actioncancelcount == 2:
				if sessionpass == "reactionaftc":
					setGlobalVariable("actioncancel", "0")
					notify("reaction over")
					clearaction(1)
					return
				if sessionpass == "reaction":
					if getGlobalVariable("insertre") != "":
						restoreinterruptlib(1)
						return
					if getGlobalVariable("plotkill") == "1":
						if getGlobalVariable("reavelplot") == "1":
							setGlobalVariable("reavelplot","2")
							if str(me._id) == getGlobalVariable("firstreveal"):remoteCall(players[1], "reavelplot", table)
							else:reavelplot(table)
							return
						if getGlobalVariable("reavelplot") == "2":
							setGlobalVariable("plotkill","0")
							if fplay(1) == me:actiongeneral(1)
							else:remoteCall(players[1], "actiongeneral", 1)
							return
					if getGlobalVariable("aftcuevent") != "-1" or getGlobalVariable("chaevent") != "-1":challengebalanceover(1)			
					else:remoteCall(winplayer, "keyword", [1])
			else:remoteCall(otherplayer, "reaction", [sessionpass,2])
			sessionpass = ""
			return
	if sessionpass  in ("milselect","intselect","powselect","mildefselect","intdefselect","powdefselect"):
		if getGlobalVariable("challengeplayer") != "0":
			cpc = int(getGlobalVariable("challengeplayer"))
			if len(selectedcard) > cpc:
				whisper("You must select only {} Character.".format(cpc))
				for card in table:
					card.target(False)
				return
	for cardn in table:
		if cardn.name == "nextbutton" and cardn.controller == me:
			cardn.delete()#delete nextbutton
			stealthcount = 0
		if cardn.name == "passnextbutton" and cardn.controller == me:
			cardn.delete()#delete nextbutton
		if cardn.name == "marshalendbutton" and cardn.controller == me:
			cardn.delete()
	setGlobalVariable("selectmode", "0")
	if intertreaction == 0 and sessionpass != "attatchcardselect":
		cardtmp = []
		clearfilter("")
		for card in table:
			card.target(False)
		for card in me.hand:
			card.target(False)
	if sessionpass == "milselect":
		sessionpass = "milselectok"
		announceMil(table)
		return
	if sessionpass == "intselect":
		sessionpass = "intselectok"
		announceInt(table)
		return
	if sessionpass == "powselect":
		sessionpass = "powselectok"
		announcePow(table)
		return
	if sessionpass == "mildefselect":
		sessionpass = "mildefselectok"
		defMil(table)
		return
	if sessionpass == "intdefselect":
		sessionpass = "intdefselectok"
		defInt(table)
		return
	if sessionpass == "powdefselect":
		sessionpass = "powdefselectok"
		defPow(table)
		return
	if sessionpass == "miljudgementselect":
		sessionpass = "miljudgementselectok"
		interruptevent("miljudgementfp",smcount)
	if sessionpass == "milkillplayerselect":
		sessionpass = "milkillplayerselectok"
		Militarychallenge(b)
	if sessionpass == "savecardselect":
		sessionpass = "savecardselectok"
		interruptevent("miljudgementfp",smcount)
	if sessionpass == "killability":
		sessionpass = "killabilityok"
		interruptevent("characterkill",1)
	if sessionpass == "discattch" or sessionpass == "kneel":
		remoteCall(otherplayer,"interruptevent",["characterkill",1])
	if sessionpass == "reaction":
		sessionpass = "reactionok"
		reaction("leavetable",1)
	if sessionpass == "reactionaftc":
		sessionpass = "reactionaftcok"
		reaction("afterchallenge",1)
	if sessionpass == "bedefendselect":
		tmp = eval(getGlobalVariable("bedefend"))
		tmp.append(selectedcard[0]._id)
		setGlobalVariable("bedefend",str(tmp))
		selectedcard[0] = nextcardtmp
		nextcardtmp = []
		sessionpass = "reactionaftcok"
		debug(getGlobalVariable("bedefend"))
		reaction("afterchallenge",1)
	if sessionpass == "attkilldefselect" or sessionpass == "iceselect":
		if len(selectedcard) == 1:
			savetarget = selectedcard[0]
			debug(savetarget)
			cardtoaction = selectedcard[0]
			selectedcard[0] = nextcardtmp
			remoteCall(otherplayer,"savetargetinserttarget",[savetarget,inserttarget,interruptcancelcard,interruptcancelplayer,interruptcancellastcard,interruptcanceledcard,interruptcancelok,saveactionplayer,mainpass])
		else:
			delreactioncard(nextcardtmp)
			#remoteCall(otherplayer,"disc",[selectedcard[0]])
		nextcardtmp = []
		sessionpass = "reactionaftuok"
		if cardtoaction != []:setTimer(me,"reactionaftuok",table)
		else:reaction("aftercalculate",1)
	if sessionpass == "discattchselect" or sessionpass == "popselect" or sessionpass == "stmselect" or sessionpass == "dothrakiselect" or sessionpass == "tyrellselect" or sessionpass == "submarkerselect":
		if len(selectedcard) > 1:
			whisper("You must select only one card to reaction.")
			return
		if len(selectedcard) == 1:
			cardtoaction = selectedcard[0]
			selectedcard[0] = nextcardtmp
			if sessionpass == "popselect":kneel(selectedcard[0])
			if sessionpass != "dothrakiselect" and sessionpass != "tyrellselect":
				selectedcard[0].arrow(cardtoaction)
		elif len(selectedcard) == 0:
			delreactioncard(nextcardtmp)
			nextcardtmp = []
			sessionpass = ""
			remoteCall(otherplayer, "reaction", ["aftercalculate",1])
			return
		nextcardtmp = []
		sessionpass = "reactionaftuok"
		reaction("aftercalculate",1)
	if sessionpass == "returndefenderselect":
		if len(selectedcard) == 1:
			cardtoaction = selectedcard[0]
			selectedcard[0] = nextcardtmp
		elif len(selectedcard) == 0:
			delreactioncard(nextcardtmp)
			nextcardtmp = []
			sessionpass = ""
			remoteCall(otherplayer, "reaction", ["aftercalculate",1])
			return
		elif len(selectedcard) > 1:
			whisper("You must select only one card.")
			return
		nextcardtmp = []
		sessionpass = "reactionaftuok"
		reaction("aftercalculate",1)
	if sessionpass in  ("killselect","Locationselect","lysselect") and nextcardtmp.type == "Event":
		if play(nextcardtmp):
			if dwtmpcard != []:
				kneel(dwtmpcard)
				dwtmpcard = []
			cardtoaction = selectedcard[0]
			savetarget = selectedcard[0]
			interruptcancelcard = nextcardtmp
			interruptcancelplayer = me
			saveactionplayer = me
			inserttarget = interruptcancelcard
			mainpass = "aftercalculate"
			remoteCall(otherplayer,"savetargetinserttarget",[savetarget,inserttarget,interruptcancelcard,interruptcancelplayer,interruptcancellastcard,interruptcanceledcard,interruptcancelok,saveactionplayer,mainpass])
			remoteCall(me, "setTimer", [me,"interruptcancel",table])
		else:
			delreactioncard(nextcardtmp)
			selectedcard = []
			reaction("aftercalculate",1)
	if selectedcard != []:
		if sessionpass == "reactionaftu" and selectedcard[0].type == "Event":
			if play(selectedcard[0]):
				interruptcancelcard = selectedcard[0]
				interruptcancelplayer = me
				inserttarget = interruptcancelcard
				mainpass = "aftercalculate"
				remoteCall(otherplayer,"savetargetinserttarget",[savetarget,inserttarget,interruptcancelcard,interruptcancelplayer,interruptcancellastcard,interruptcanceledcard,interruptcancelok,saveactionplayer,mainpass])
				remoteCall(otherplayer, "interruptevent", ["interruptcancel",2])
			else:
				delreactioncard(nextcardtmp)
				selectedcard = []
				reaction("aftercalculate",1)
		elif sessionpass == "reactionaftu" and selectedcard[0].type in ("Character","Location"):
			sessionpass = "reactionaftuok"
			reaction("aftercalculate",1)
		elif sessionpass == "reactionaftu" and selectedcard[0].type == "Plot":
			reactionforability(selectedcard[0],"aftercalculate")
	elif sessionpass == "reactionaftu":
		sessionpass = "reactionaftuok"
		remoteCall(otherplayer, "reaction", ["aftercalculate",1])
	if sessionpass == "Direwolfselect":
		if len(selectedcard) == 0:
			delreactioncard(nextcardtmp)
			selectedcard = []
			remoteCall(otherplayer, "reaction", ["aftercalculate",1])
	if sessionpass == "initimidateselect":
		if len(selectedcard) != 0:
			selectedcard[0].orientation = 1
			notify("{}'s {} kneel {} by Initimidate".format(me,cardtoaction,selectedcard[0]))
			cardtoaction = []
		keywordforability(1)
	if sessionpass in("kneelhouseok","addintselectok","adddefselectok","dischandselectok","adddstrselectok","ignorestrselectok","returnhandselectok","drawstarkselectok","burnselectok","returndeadselectok","addstrdrawselectok","addclaimselectok","addstr3selectok","attaddstr3selectok","standremovechallengeselectok","3playeraddstr2selectok","removechallengeok"):
		if len(selectedcard) > 1 and sessionpass != "3playeraddstr2selectok":
			whisper("You must select only one card to action.")
			return
		if len(selectedcard) > 3 and sessionpass == "3playeraddstr2selectok":
			whisper("You must select at most 3 character to action.")
			return
		if len(selectedcard) == 1 and sessionpass != "3playeraddstr2selectok":
			if sessionpass != "returndeadselectok" and sessionpass != "attaddstr3selectok":cardtoaction = selectedcard[0]
			if sessionpass == "kneelhouseok" or sessionpass == "returnhandselectok":
				if sessionpass == "kneelhouseok":selectedcard[0] = nextcardtmp
				for cardhouse in table:
					if cardhouse.type == "Faction" and cardhouse.controller == me:
						kneel(cardhouse)
			if sessionpass == "addintselectok" or sessionpass == "standremovechallengeselectok":
				selectedcard[0] = nextcardtmp
				me.counters['Gold'].value -= 1
				# for incomecard in table:
				# 	if incomecard.controller == me and incomecard.markers[Gold] > 0:
				# 		incomecard.markers[Gold] -= 1
			if sessionpass in ("adddefselectok","dischandselectok","ignorestrselectok","returnhandselectok","burnselectok","returndeadselectok","addstrdrawselectok","addclaimselectok","removechallengeok"):
				if sessionpass == "returndeadselectok":
					debug(cardtoaction)
					if cardtoaction == None:
						delactioncard(nextcardtmp)
						nextcardtmp = []
						sessionpass = ""
						remoteCall(otherplayer, "action", ["challenge",1])
						return
				if sessionpass == "removechallengeok":
					savetarget = selectedcard[0]
					debug(savetarget)
					interruptcancelcard = nextcardtmp
					interruptcancelplayer = me
					saveactionplayer = me
					inserttarget = interruptcancelcard
					mainpass = "challengeaction"
					remoteCall(otherplayer,"savetargetinserttarget",[savetarget,inserttarget,interruptcancelcard,interruptcancelplayer,interruptcancellastcard,interruptcanceledcard,interruptcancelok,saveactionplayer,mainpass])
					remoteCall(me, "setTimer", [me,"interruptcancel",table])
					nextcardtmp = []
					return
				if play(nextcardtmp):
					if dwtmpcard != []:
						kneel(dwtmpcard)
						dwtmpcard = []
					if sessionpass != "returndeadselectok":cardtoaction = selectedcard[0]
					savetarget = selectedcard[0]
					debug(savetarget)
					interruptcancelcard = nextcardtmp
					interruptcancelplayer = me
					saveactionplayer = me
					inserttarget = interruptcancelcard
					mainpass = "challengeaction"
					remoteCall(otherplayer,"savetargetinserttarget",[savetarget,inserttarget,interruptcancelcard,interruptcancelplayer,interruptcancellastcard,interruptcanceledcard,interruptcancelok,saveactionplayer,mainpass])
					remoteCall(me, "setTimer", [me,"interruptcancel",table])
					nextcardtmp = []
					return
				else:
					delactioncard(nextcardtmp)
					nextcardtmp = []
					sessionpass = ""
					remoteCall(otherplayer, "action", ["challenge",1])
					return
			if sessionpass == "adddstrselectok" or sessionpass == "addstr3selectok" or sessionpass == "attaddstr3selectok" or sessionpass == "standremovechallengeselectok":
				selectedcard[0] = nextcardtmp
				kneel(nextcardtmp)
			if sessionpass == "drawstarkselectok":
				cardtoaction = me.deck.top()
				kneel(nextcardtmp)
		elif sessionpass != "3playeraddstr2selectok":
			delactioncard(nextcardtmp)
			nextcardtmp = []
			sessionpass = ""
			remoteCall(otherplayer, "action", ["challenge",1])
			return
		if sessionpass == "3playeraddstr2selectok":
			if play(nextcardtmp):
				cardtoaction = selectedcard
				savetarget = selectedcard[0]
				debug(savetarget)
				interruptcancelcard = nextcardtmp
				interruptcancelplayer = me
				saveactionplayer = me
				inserttarget = interruptcancelcard
				mainpass = "challengeaction"
				remoteCall(otherplayer,"savetargetinserttarget",[savetarget,inserttarget,interruptcancelcard,interruptcancelplayer,interruptcancellastcard,interruptcanceledcard,interruptcancelok,saveactionplayer,mainpass])
				remoteCall(me, "setTimer", [me,"interruptcancel",table])
				nextcardtmp = []
				return
			else:
				delactioncard(nextcardtmp)
				nextcardtmp = []
				sessionpass = ""
				remoteCall(otherplayer, "action", ["challenge",1])
				return
		nextcardtmp = []
		sessionpass = "actionok"
		action("challenge",1)
	if sessionpass == "ambush":
		if play(selectedcard[0]):
			if selectedcard[0].model == actionchallenge['OlennasInformant'][1]:
				cardtoaction = selectedcard
				savetarget = selectedcard[0]
				debug(savetarget)
				interruptcancelcard = selectedcard[0]
				interruptcancelplayer = me
				saveactionplayer = me
				inserttarget = interruptcancelcard
				mainpass = "challengeaction"
				remoteCall(otherplayer,"savetargetinserttarget",[savetarget,inserttarget,interruptcancelcard,interruptcancelplayer,interruptcancellastcard,interruptcanceledcard,interruptcancelok,saveactionplayer,mainpass])
				remoteCall(otherplayer, "interruptevent", ["interruptcancel",2])			
			if selectedcard[0].model == actionchallenge['AreoHotah'][1]:
				if checkinchallengeplay("all",0):
					nextcardtmp = selectedcard[0]
					for card in me.hand:
						card.target(False)
					targetTuple = ([card._id for card in table if card.type == "Character" and card.highlight in (MilitaryColor,IntrigueColor,PowerColor)], me._id)
					setGlobalVariable("tableTargets", str(targetTuple))
					setGlobalVariable("selectmode", "1")
					if me.isInverted:table.create("584a37d7-5a30-4018-ae21-0ad325203fa0",-375,-250)
					else:table.create("584a37d7-5a30-4018-ae21-0ad325203fa0",-375,200)
					sessionpass = "removechallengeok"
					notify("**{} into selectmode**".format(me))
					return
				else:
					for card in me.hand:
						card.target(False)
					delactioncard(selectedcard[0])
					nextcardtmp = []
					sessionpass = ""
					remoteCall(otherplayer, "action", ["challenge",1])
					return

		else:
			for card in me.hand:
				card.target(False)
			delactioncard(selectedcard[0])
			nextcardtmp = []
			sessionpass = ""
			remoteCall(otherplayer, "action", ["challenge",1])
			return
	if sessionpass == "attatchcardselect":
		
		if play(listattach[0]):
			clearfilter(me)
			del listattach[0]
			selectedcard = []
			if len(listattach) > 0:attatchcard(listattach)
			else:
				reordertable(table)
		else:
			clearfilter(me)
			del listattach[0]
			selectedcard = []
			if len(listattach) > 0:attatchcard(listattach)
			else:
				reordertable(table)

	if sessionpass == "stealthselectok":
		sessionpass = ""
		if len(selectedcard) == 1:
			cardtoaction = selectedcard[0]
			selectedcard[0] = nextcardtmp
			cardtoaction.highlight = Stealthcolor
			if getGlobalVariable("cantchallenge") == "1":setGlobalVariable("cantchallenge", card._id)
			liststeal.remove(selectedcard[0])
			cardtoaction = []
			if len(liststeal) > 0:
				if checktablestealthcount(0):
					selectstealth(table)
			else:
				if challengetype == 1:remoteCall(otherplayer, "challengedeficon", ["mil"])
				if challengetype == 2:remoteCall(otherplayer, "challengedeficon", ["int"])
				if challengetype == 3:remoteCall(otherplayer, "challengedeficon", ["pow"])
		elif len(selectedcard) == 0:
			liststeal.remove(nextcardtmp)
			if len(liststeal) > 0:
				if checktablestealthcount(0):
					selectstealth(table)
			else:
				if challengetype == 1:remoteCall(otherplayer, "challengedeficon", ["mil"])
				if challengetype == 2:remoteCall(otherplayer, "challengedeficon", ["int"])
				if challengetype == 3:remoteCall(otherplayer, "challengedeficon", ["pow"])
	if sessionpass == "marshalcardselect":
		if play(selectedcard[0]):marshalphase(table)
		else:marshalphase(table)
	if sessionpass in ("Confiscationselect","FilthyAccusationsselect"):
		if len(selectedcard) == 1:
			cardtoaction = selectedcard[0]
			selectedcard[0] = nextcardtmp
			selectedcard[0].arrow(cardtoaction)
			remoteCall(me, "setTimer", [me,sessionpass,table])
		elif len(selectedcard) == 0:
			nextcardtmp = []
			sessionpass = ""
			if getGlobalVariable("reavelplot") == "1":
				setGlobalVariable("reavelplot","2")
				if str(me._id) == getGlobalVariable("firstreveal"):remoteCall(players[1], "reavelplot", table)
				else:reavelplot(table)
				return
			if getGlobalVariable("reavelplot") == "2":
				if fplay(1) == me:actiongeneral(1)
				else:remoteCall(players[1], "actiongeneral", 1)
			return
	if sessionpass == "plotdisccharacter1":
		sessionpass = ""
		nextcardtmp = selectedcard[0]
		remoteCall(players[1], "plotdisccharacter", ["disc2",plotcard])
	if sessionpass == "plotdisccharacter2":
		sessionpass = ""
		nextcardtmp = selectedcard[0]
		remoteCall(fplay(1), "callplotleave", [1])
	if sessionpass == "standcharacter1":
		sessionpass = ""
		if len(selectedcard) != 0:
			for standcard in selectedcard:
				standcard.filter = standfilter
		remoteCall(players[1], "standcharacter", ["stand2"])
	if sessionpass == "standcharacter2":
		sessionpass = ""
		if len(selectedcard) != 0:
			for standcard in selectedcard:
				standcard.filter = standfilter
		remoteCall(fplay(1), "standcharacterend", [1])
	if sessionpass == "plotdisclocation1":
		sessionpass = ""
		for disccard in table:
			if disccard.controller == me and disccard.type == "Location" and disccard.filter != WaitColor and disccard not in selectedcard:
				disccard.filter = discfilter
		remoteCall(players[1], "plotdisccharacter", ["plotdisclocation2"])
	if sessionpass == "plotdisclocation2":
		sessionpass = ""
		for disccard in table:
			if disccard.controller == me and disccard.type == "Location" and disccard.filter != WaitColor and disccard not in selectedcard:
				disccard.filter = discfilter
		
	if sessionpass == "plotkillcharacter1":
		sessionpass = ""
		for cards in table:
			if cards.Type == "Character" and cards.filter == None and cards.controller == me and cards not in selectedcard:cards.highlight = miljudgecolor
		remoteCall(players[1], "plotdisccharacter", ["kill2",plotcard])
	if sessionpass == "plotkillcharacter2":
		sessionpass = ""
		for cards in table:
			if cards.Type == "Character" and cards.filter == None and cards.controller == me and cards not in selectedcard:cards.highlight = miljudgecolor
		cardbekill = []
		for card in table:
			if card.highlight == miljudgecolor:cardbekill.append(card)
		remoteCall(fplay(1), "characterkilled", [cardbekill,1])
	if sessionpass in ("1goldiconselectok","kneelfactionselectok","d1cg1gselectok","reduce3sselectok","reducecardselectok","controllbselectok","changecontrollselectok"):
		if sessionpass in ("1goldiconselectok","controllbselectok"):
			me.counters['Gold'].value -= 1
			# for incomecard in table:
			# 	if incomecard.controller == me and incomecard.markers[Gold] > 0:
			# 		incomecard.markers[Gold] -= 1
		if sessionpass == "d1cg1gselectok":
			disc(selectedcard[0])
			selectedcard[0] = nextcardtmp
		
		if sessionpass in ("kneelfactionselectok","addusedplotgoldselectok","searchwolfselectok"):
			for cardf in table:
				if cardf.Type == "Faction" and cardf.orientation == 0 and cardf.controller == me:
					kneel(cardf)
		if sessionpass == "reduce3sselectok":
			kneel(selectedcard[0])
			disc(selectedcard[0])
		if sessionpass == "reducecardselectok":
			kneel(selectedcard[0])
		if sessionpass == "changecontrollselectok":
			cardtoaction = selectedcard[0]
			selectedcard[0] = nextcardtmp
		nextcardtmp = []
		sessionpass = "actionok"
		if getGlobalVariable("dominanceaction") != "0":action("dominance",1)
		elif getGlobalVariable("marshalphase") != "0":action("marshal",1)
		else:action("general",1)
		return
	if sessionpass in("addlanselectok","add5returnmeselectok","loseiconselectok","standlocationselectok","2gstandcselectok","standladyselectok","standtcselectok","5t3bselectok","standiconselectok","d1cg1gselectok","discattachmentcselectok","kneel4cadd1powercselectok","kneel2locationselectok","searchbrsok","addusedplotgoldselectok","searchwolfselectok","noprintselectok","4cardchoose2selectok"):
		if len(selectedcard) == 0:
			delactioncard(nextcardtmp)
			nextcardtmp = []
			sessionpass = ""
			if getGlobalVariable("dominanceaction") != "0":remoteCall(players[1], "action", ["dominance",1])
			elif getGlobalVariable("marshalphase") != "0":action("marshal",1)
			else:remoteCall(players[1], "action", ["general",1])
			return
		if sessionpass == "2gstandcselectok":
			me.counters['Gold'].value -= 2
			# for incomecard in table:
			# 	if incomecard.controller == me and incomecard.markers[Gold] > 0:
			# 		incomecard.markers[Gold] -= 2
		if sessionpass in ("2gstandcselectok","kneel2locationselectok"):
			kneel(nextcardtmp)
		if sessionpass in ("addusedplotgoldselectok","searchwolfselectok","4cardchoose2selectok"):
			for cardf in table:
				if cardf.Type == "Faction" and cardf.orientation == 0 and cardf.controller == me:
					kneel(cardf)
		if sessionpass in("add5returnmeselectok","standlocationselectok","2gstandcselectok","standladyselectok","standiconselectok","discattachmentcselectok","kneel2locationselectok"):
			cardtoaction = selectedcard[0]
			if sessionpass in ("add5returnmeselectok"):
				savetarget = selectedcard[0]
				cardtoaction.moveToTable(100,200)
				cardtoaction.filter = showtablefilter
				interruptcancelcard = nextcardtmp
				interruptcancelplayer = me
				saveactionplayer = me
				inserttarget = interruptcancelcard
				if getGlobalVariable("dominanceaction") != "0":mainpass = "dominanceaction"
				elif getGlobalVariable("marshalphase") != "0":mainpass = "marshalaction"
				else:mainpass = "generalaction"
				remoteCall(otherplayer,"savetargetinserttarget",[savetarget,inserttarget,interruptcancelcard,interruptcancelplayer,interruptcancellastcard,interruptcanceledcard,interruptcancelok,saveactionplayer,mainpass])
				remoteCall(me, "setTimer", [me,"interruptcancel",table])
				nextcardtmp = []
				return
			else:
				selectedcard[0] = nextcardtmp
				selectedcard[0].arrow(cardtoaction)
		if sessionpass in("addlanselectok","loseiconselectok","5t3bselectok","standtcselectok","searchbrsok","addusedplotgoldselectok","noprintselectok","searchwolfselectok","4cardchoose2selectok"):
			if play(nextcardtmp):
				cardtoaction = selectedcard[0]
				savetarget = selectedcard[0]
				debug(savetarget)
				if sessionpass in ("addlanselectok"):
					cardintable(cardtoaction,"Character")
					#cardtoaction.moveToTable(100,200)
					cardtoaction.filter = showtablefilter
				interruptcancelcard = nextcardtmp
				interruptcancelplayer = me
				saveactionplayer = me
				inserttarget = interruptcancelcard
				if getGlobalVariable("dominanceaction") != "0":mainpass = "dominanceaction"
				elif getGlobalVariable("marshalphase") != "0":mainpass = "marshalaction"
				else:mainpass = "generalaction"
				remoteCall(players[1],"savetargetinserttarget",[savetarget,inserttarget,interruptcancelcard,interruptcancelplayer,interruptcancellastcard,interruptcanceledcard,interruptcancelok,saveactionplayer,mainpass])
				remoteCall(me, "setTimer", [me,"interruptcancel",table])
				nextcardtmp = []
				return
			else:
				delactioncard(nextcardtmp)
				nextcardtmp = []
				sessionpass = ""
				if getGlobalVariable("dominanceaction") != "0":remoteCall(players[1], "action", ["dominance",1])
				elif getGlobalVariable("marshalphase") != "0":action("marshal",1)
				else:remoteCall(players[1], "action", ["general",1])
				return
		if sessionpass in("kneel4cadd1powercselectok"):
			if play(nextcardtmp):
				cardtoaction = selectedcard
				savetarget = selectedcard
				debug(savetarget)
				interruptcancelcard = nextcardtmp
				interruptcancelplayer = me
				saveactionplayer = me
				inserttarget = interruptcancelcard
				mainpass = "marshalaction"
				debug(sessionpass)
				remoteCall(players[1],"savetargetinserttarget",[savetarget,inserttarget,interruptcancelcard,interruptcancelplayer,interruptcancellastcard,interruptcanceledcard,interruptcancelok,saveactionplayer,mainpass])
				remoteCall(me, "setTimer", [me,"interruptcancel",table])
				nextcardtmp = []
				return
			else:
				delactioncard(nextcardtmp)
				nextcardtmp = []
				sessionpass = ""
				if getGlobalVariable("dominanceaction") != "0":remoteCall(players[1], "action", ["dominance",1])
				elif getGlobalVariable("marshalphase") != "0":action("marshal",1)
				else:remoteCall(players[1], "action", ["general",1])
				return
		nextcardtmp = []
		sessionpass = "actionok"
		if getGlobalVariable("dominanceaction") != "0":action("dominance",1)
		elif getGlobalVariable("marshalphase") != "0":action("marshal",1)
		else:action("general",1)
		return
	if sessionpass == "dominancestandok":
		nextcardtmp = []
		sessionpass = "reactiondsuok"
		reaction("dominancestart",1)
		return
	if sessionpass in ("dominance2powerok","dominancemove1powok","dominancereturnironok"):
		nextcardtmp = []
		sessionpass = "reactiondswinok"
		reaction("dominancewin",1)
		return
	if sessionpass in ("returndraw1selectok","disctopselectok"):
		nextcardtmp = []
		sessionpass = "actionok"
		action("dominance",1)
		return
	if sessionpass == "ticklerdisc":
		if len(selectedcard) == 1:
			remoteCall(selectedcard[0].owner, "disc", selectedcard[0])
		remoteCall(players[1], "action", ["dominance",1])

	if sessionpass == "selectadd1power":
		remoteCall(selectedcard[0].controller, "addPower", [selectedcard[0]])#ConsolidationofPower
		remoteCall(players[1], "action", ["marshal",1])
	if sessionpass in ("drwa2cardselectok","discdiscselectok","draw3selectok","reducenwselectok","mdraw1selectok"):
		nextcardtmp = []
		sessionpass = "reactionmarshalok"
		reaction("reactionmarshal",1)
		return
	if sessionpass == "lhlkneelselectok":
		if len(selectedcard) == 0:
			delreactioncard(nextcardtmp)
			nextcardtmp = []
			sessionpass = ""
			remoteCall(players[1], "action", ["general",1])
		else:
			cardtoaction = selectedcard[0]
			savetarget = selectedcard[0]
			debug(savetarget)
			interruptcancelcard = nextcardtmp
			interruptcancelplayer = me
			saveactionplayer = me
			inserttarget = interruptcancelcard
			mainpass = "reactionmarshal"
			remoteCall(players[1],"savetargetinserttarget",[savetarget,inserttarget,interruptcancelcard,interruptcancelplayer,interruptcancellastcard,interruptcanceledcard,interruptcancelok,saveactionplayer,mainpass])
			remoteCall(me, "setTimer", [me,"interruptcancel",table])
			nextcardtmp = []
			return
	if sessionpass in ("plotdrawgoldselectok"):
		nextcardtmp = []
		sessionpass = "reactionplotok"
		reaction("reactionplot",1)
		return
def stealthcard(group, x=0, y=0):
	mute()
	global sessionpass
	global selectedcard
	if sessionpass == "stealthselectok" and selectedcard != []:
		for card in selectedcard:
			card.highlight = Stealthcolor
			if getGlobalVariable("cantchallenge") == "1":setGlobalVariable("cantchallenge", card._id)
			debug(getGlobalVariable("cantchallenge"))
		sessionpass = ""
		selectedcard = []
	setGlobalVariable("selectmode", "0")
	if challengetype == 1:remoteCall(otherplayer, "challengedeficon", ["mil"])
	if challengetype == 2:remoteCall(otherplayer, "challengedeficon", ["int"])
	if challengetype == 3:remoteCall(otherplayer, "challengedeficon", ["pow"])
	#checkafterchallengereacioncard(1)

def onclick(args):
	mute()
	if getGlobalVariable("selectmode") != "0" and args.card.type not in ("Internal") and me.getGlobalVariable("actionstyle") != "1":
		list2 = []
		if me.getGlobalVariable("setupOk") in ("4","5") or me.getGlobalVariable("plotOk") == "ok" or me.getGlobalVariable("drawOk") == "ok":tuplecard = eval(me.getGlobalVariable("tableTargets"))
		else:tuplecard = eval(getGlobalVariable("tableTargets"))
		debug(tuplecard)
		if me._id == tuplecard[1]:
			if args.card.type not in ("Internal"):
				if tuplecard[0] == ["setupOk"]:
					whisper("card cant be selected")
					return
				if cardtmp != []:
					if args.card._id in tuplecard[0]:
						if args.card.filter == targetcardcolor:
							if getGlobalVariable("selectmode") == "1":
								cardtmp.arrow(cardtmp,False)
								args.card.filter = None
							else:
								args.card.filter = None
								cardtmp.arrow(cardtmp,False)
								for card in table:
									if card.filter == targetcardcolor:cardtmp.arrow(card)
													
						else:
							if getGlobalVariable("selectmode") == "1":
								cardtmp.arrow(cardtmp,False)
								for card in table:
									if card.filter == targetcardcolor:card.filter = None
								cardtmp.arrow(args.card)
								args.card.filter = targetcardfilter
							else:
								debug(targetlen())
								if targetlen() == int(getGlobalVariable("selectmode")):return
								cardtmp.arrow(args.card)
								args.card.filter = targetcardfilter
					else:
						whisper("card cant be selected")
				else:
					if args.card._id in tuplecard[0]:
						if getGlobalVariable("selectmode") == "1":
							if args.card.filter == targetcardcolor:
								args.card.filter = None
							else:
								for card in table:
									if card.filter == targetcardcolor:card.filter = None
								for card in me.hand:
									if card.filter == targetcardcolor:card.filter = None
								args.card.filter = targetcardfilter
						else:
							if args.card.filter == targetcardcolor:
								args.card.filter = None
							else:
								debug(targetlen())
								if targetlen() == int(getGlobalVariable("selectmode")):return
								args.card.filter = targetcardfilter
					else:
						whisper("card cant be selected")
		else:
			whisper("is not your turn")

def targetlen():
	mute()
	list = []
	for card in table:
		if card.filter == targetcardcolor:
			list.append(card)
	return len(list)


def ondbclick(args):
	mute()
	if args.card.name == "nextbutton" and args.card.controller == me:next(table)
	elif args.card.name == "passnextbutton" and args.card.controller == me:next(table)
	elif args.card.name == "setupnextbutton" and args.card.controller == me:setupnext(table)
	elif args.card.name == "plotnextbutton" and args.card.controller == me:plotnext(table)
	elif args.card.name == "drawnextbutton" and args.card.controller == me:drawnext(table)
	elif args.card.name == "manualbutton" and args.card.controller == me:resumeprocess()
	elif args.card.name == "endbutton" and args.card.controller == me:endphase(table)
	elif args.card.name == "marshalendbutton" and args.card.controller == me:marshalend()
	elif args.card.name == "challengenextbutton" and args.card.controller == me:challengenext()
	elif args.card.name == "dominancenextbutton" and args.card.controller == me:dominancenext()
	elif args.card.name == "standingnextbutton" and args.card.controller == me:standingnext()
	elif args.card.name == "taxationnextbutton" and args.card.controller == me:taxationnext()
	elif args.card.name == "AttackMil" and args.card.controller == me:selectchallenge("mil")
	elif args.card.name == "AttackInt" and args.card.controller == me:selectchallenge("int")
	elif args.card.name == "AttackPow" and args.card.controller == me:selectchallenge("pow")
	elif args.card.name == "AttackNon" and args.card.controller == me:selectchallenge("end")
	elif args.card.name == "DefendMil" and args.card.controller == me:selectchallenge("defmil")
	elif args.card.name == "DefendInt" and args.card.controller == me:selectchallenge("defint")
	elif args.card.name == "DefendPow" and args.card.controller == me:selectchallenge("defpow")
	elif args.card.name == "DefendNon" and args.card.controller == me:selectchallenge("nodef")
	if getGlobalVariable("selectmode") != "0":
		if me.getGlobalVariable("actionstyle") != "0":
			if getGlobalVariable("marshalphase") == "0":
				tuplecard = eval(getGlobalVariable("tableTargets"))
				if me._id == tuplecard[1]:
					if args.card._id in tuplecard[0]:
						if confirm("Do you want use [{}]'s ability?\n{}".format(args.card.name,args.card.text)):
							args.card.filter = targetcardfilter
							me.setGlobalVariable("actionstyle", "0")
							setGlobalVariable("actioncancel", "0")
							next(table)
							return
						else:
							whisper("action cancel")
							return
					else:("card cant be selected")
				else:whisper("is not your turn")
			if getGlobalVariable("marshalphase") != "0":
				c = 0
				uniquecards = []
				for u in table:
					if u.controller == me and u.unique == "Yes":
						uniquecards.append(u.name)
						if args.card.name in uniquecards: 
							cost=0
							c = 1   #Duplicates
							x,y = u.position
							break
				tuplecard = eval(getGlobalVariable("tableTargets"))
				if me._id == tuplecard[1]:
					for card in me.hand:
						if args.card._id == card._id and args.card._id in tuplecard[0]:
							if args.card.type in ("Character","Location","Attachment"):
								if c == 1:
									args.card.filter = targetcardfilter
									me.setGlobalVariable("isselect", "1")
									me.setGlobalVariable("actionstyle", "0")
									setGlobalVariable("actioncancel", "0")
									next(table)
									return
								if checkdbclickselectcard(args.card):
									args.card.filter = targetcardfilter
									me.setGlobalVariable("isselect", "1")
									me.setGlobalVariable("actionstyle", "0")
									setGlobalVariable("actioncancel", "0")
									next(table)
									return
								else:
									whisper("cancel")
									return
							else:
								if confirm("You will play [{}], it can be reduced cost by [{}],finally marshal for cost [{}], after marshal you have [{}] gold".format(args.card.name,int(args.card.cost)-checkreduce(args.card),checkreduce(args.card),me.counters['Gold'].value-checkreduce(args.card))):
									args.card.filter = targetcardfilter
									me.setGlobalVariable("isselect", "1")
									me.setGlobalVariable("actionstyle", "0")
									setGlobalVariable("actioncancel", "0")
									next(table)
									return
								return
					for card in table:
						if args.card._id == card._id and args.card._id in tuplecard[0]:
							if confirm("Do you want use [{}]'s ability?\n{}".format(args.card.name,args.card.text)):
								me.setGlobalVariable("actionstyle", "0")
								setGlobalVariable("actioncancel", "0")
								args.card.filter = targetcardfilter
								next(table)
								return
							else:
								whisper("action cancel")
								return
					whisper("card cant be selected")
				else:whisper("is not your turn")
	if getGlobalVariable("selectmode") == "0":
		if args.card.Type != "Internal":
			for card in table:
				if args.card._id == card._id:
					if card.Type == "Plot" and card.isFaceUp == True:
						countincome(table)
					elif not card.isFaceUp: #Face down card - flip
						flipcard(card)
					else:
						kneel(card)
		
def checkreduce(card):
	mute()
	cost = int(card.cost)
	if card.loyal == "Yes":
		cost -= int(me.getGlobalVariable("reduceloyal_turn"))

	if me.getGlobalVariable("firstll") == "1" and me.getGlobalVariable("firstcharacter") == "0":
		if card.type == "Character" and card.Traits.find('Lord') != -1 or card.Traits.find('Lady') != -1:
			cost -= 2
	if me.getGlobalVariable("firstnobaratheonplayer") == "0":
		if checkrl(me) and card.type == "Character" and card.faction != "Baratheon.":
			cost=int(card.Cost)-1
			if cost < 0:cost = 0
	if checkcardmodel("a28ec48c-ee57-4c6a-a940-b59c1aeff251") and me.getGlobalVariable("firstlocation") == "0":
		if card.type == "Location":
			cost -= 1


	if card.type == "Character":
		if me.getGlobalVariable("reduce_character_turn") != "0":
			cost -= int(me.getGlobalVariable("reduce_character_turn"))
			reduce_character_turn = 1
		if card.faction == "Stark.":
			if me.getGlobalVariable("reduce_Stark_character_turn") != "0":
				cost -= int(me.getGlobalVariable("reduce_Stark_character_turn"))
				reduce_Stark_character_turn = 1
		if card.faction == "Lannister.":
			if me.getGlobalVariable("reduce_Lannister_character_turn") != "0":
				cost -= int(me.getGlobalVariable("reduce_Lannister_character_turn"))
				reduce_Lannister_character_turn = 1
		if card.faction == "Greyjoy.":
			if me.getGlobalVariable("reduce_Greyjoy_character_turn") != "0":
				cost -= int(me.getGlobalVariable("reduce_Greyjoy_character_turn"))
				reduce_Greyjoy_character_turn = 1
		if card.faction == "Martell.":
			if me.getGlobalVariable("reduce_Martell_character_turn") != "0":
				cost -= int(me.getGlobalVariable("reduce_Martell_character_turn"))
				reduce_Martell_character_turn = 1
		if card.faction == "Baratheon.":
			if me.getGlobalVariable("reduce_Baratheon_character_turn") != "0":
				cost -= int(me.getGlobalVariable("reduce_Baratheon_character_turn"))
				reduce_Baratheon_character_turn = 1
		if card.faction == "Targaryen.":
			if me.getGlobalVariable("reduce_Targaryen_character_turn") != "0":
				cost -= int(me.getGlobalVariable("reduce_Targaryen_character_turn"))
				reduce_Targaryen_character_turn = 1
		if card.faction == "Night's Watch.":
			if me.getGlobalVariable("reduce_NW_character_turn") != "0":
				cost -= int(me.getGlobalVariable("reduce_NW_character_turn"))
				reduce_NW_character_turn = 1
		if card.faction == "Tyrell.":
			if me.getGlobalVariable("reduce_Tyrell_character_turn") != "0":
				cost -= int(me.getGlobalVariable("reduce_Tyrell_character_turn"))
				reduce_Tyrell_character_turn = 1
	if cost < 0:cost = 0
	if card.faction == "Stark.":
		if me.getGlobalVariable("reduce_Stark_card_turn") != "0":
			cost -= int(me.getGlobalVariable("reduce_Stark_card_turn"))
			reduce_Stark_card_turn = 1
	if card.faction == "Lannister.":
		if me.getGlobalVariable("reduce_Lannister_card_turn") != "0":
			cost -= int(me.getGlobalVariable("reduce_Lannister_card_turn"))
			reduce_Lannister_card_turn = 1
	if card.faction == "Greyjoy.":
		if me.getGlobalVariable("reduce_Greyjoy_card_turn") != "0":
			cost -= int(me.getGlobalVariable("reduce_Greyjoy_card_turn"))
			reduce_Greyjoy_card_turn = 1
	if card.faction == "Martell.":
		if me.getGlobalVariable("reduce_Martell_card_turn") != "0":
			cost -= int(me.getGlobalVariable("reduce_Martell_card_turn"))
			reduce_Martell_card_turn = 1
	if card.faction == "Baratheon.":
		if me.getGlobalVariable("reduce_Baratheon_card_turn") != "0":
			cost -= int(me.getGlobalVariable("reduce_Baratheon_card_turn"))
			reduce_Baratheon_card_turn = 1
	if card.faction == "Targaryen.":
		if me.getGlobalVariable("reduce_Targaryen_card_turn") != "0":
			cost -= int(me.getGlobalVariable("reduce_Targaryen_card_turn"))
			reduce_Targaryen_card_turn = 1
	if card.faction == "Tyrell.":
		if me.getGlobalVariable("reduce_Tyrell_card_turn") != "0":
			cost -= int(me.getGlobalVariable("reduce_Tyrell_card_turn"))
			reduce_Tyrell_card_turn = 1
	if card.faction == "Night's Watch.":
		if me.getGlobalVariable("reduce_NW_card_turn") != "0":
			cost -= int(me.getGlobalVariable("reduce_NW_card_turn"))
			reduce_NW_card_turn = 1
	if card.model == "b785b7fc-2a11-4ba5-87e7-7c06c79d6210":
		for ccard in table:
			if ccard.controller == me and ccard.type == "Character" and ccard.filter != WaitColor and "Dothraki" in ccard.traits:
				cost -= 1
	if cost < 0:cost = 0
	return cost

def test(group, x=0, y=0):
	mute()
	# if getGlobalVariable("noprint") == "1":
	# 	for ncard in table:
	# 		if ncard.type == "Character" and ncard.controller ==me:
	# 			restoreprintcard(ncard)
	# 		if ncard.type == "Character" and ncard.controller !=me:
	# 			remoteCall(players[1], "restoreprintcard", [ncard])

	# 	setGlobalVariable("noprint","0")
	# 	return
	# if getGlobalVariable("noprint") == "0":
	# 	for ncard in table:
	# 		if ncard.type == "Character" and ncard.controller ==me:
	# 			noprintcard(ncard)
	# 		if ncard.type == "Character" and ncard.controller !=me:
	# 			remoteCall(players[1], "noprintcard", [ncard])
	# 	setGlobalVariable("noprint","1")
	# 	return
	me.setGlobalVariable("setupOk","")
	# getreserve(table)
	# #taxationnext()
	# # me.setGlobalVariable("firstll","1")

	# # # actiondominance(2)
	# # # setGlobalVariable("activeplayer",str(me._id))
	# # me.setGlobalVariable("firstdraw","1")
	marshalcountincome()
	# setGlobalVariable("dominanceaction", "1")
	# actiondominance(2)
	#dominancestartreaction(2)
	#challengedeficon("pow")
	#actiongeneral(2)
	#resetperturn()
	#resetplot()
	#challengeAnnounce(table)
	#taxationphasestart(1)
	#setGlobalVariable("standingphase","1")
	#dominancewinplayer = me
	#setGlobalVariable("drawphase","2")
	#standcharacter("stand1")
	#actiongeneral(1)
	#reavelplot(table)
	#dominancewinreaction(1)
	#dominancestartreaction(1)
	#debug(checkstannis())
	#marshalcountincome()
	
def checksavecard(savecard):
	list = []
	attach = eval(getGlobalVariable("attachmodify"))
	for card in table:
		for cards in savecard:
			Faction = cards.Faction
			savetarget = cards
			if card.controller == me and cards.controller == me and card.name == cards.name and card.filter == WaitColor:
				list.append(card)
	for c in me.hand:
		for d in saveaction:
			if saveaction[d][3] == "Hand" and c.model == saveaction[d][1]:
				if saveaction[d][4] == "all":list.append(c)
				elif saveaction[d][4] == Faction:list.append(c)
	for c in table:
		for d in saveaction:
			if saveaction[d][3] == "table" and c.model == saveaction[d][1] and c.controller == me:
				if saveaction[d][5] == "Attachment":
					if attach.has_key(c._id):
						if attach[c._id] == savetarget._id:list.append(c)
				else:
					if saveaction[d][2] != "kneel":
						if saveaction[d][4] == "all":list.append(c)
						elif saveaction[d][4] == Faction:list.append(c)
					elif saveaction[d][2] == "kneel" and c.orientation == 0:
						if saveaction[d][4] == "all":list.append(c)
						elif saveaction[d][4] == Faction:list.append(c)
	return list

def reactionattachsub(card):
	mute()
	global reactionattach
	global sessionpass
	sessionpass = ""
	reactionattach[card._id] -= 1
	if reactionattach[card._id] == 0:del reactionattach[card._id]

def actionattachsub(card):
	mute()
	global actionattach
	global sessionpass
	sessionpass = ""
	actionattach[card._id] -= 1
	if actionattach[card._id] == 0:del actionattach[card._id]

def abilityattachsub(card):
	mute()
	global abilityattach
	global actioncardlimit
	if not actioncardlimit.has_key(card._id):
		actioncardlimit[card._id] = 1
	else:actioncardlimit[card._id] += 1

	actionattach[card._id] -= 1
	if actionattach[card._id] == 0:del actionattach[card._id]

def interruptreaction(card,count):
	mute()
	global intertreaction
	intertreaction = count
	reactionattach[card._id] = 1
	reaction("leavetable",1)

def backupinterruptlib(count):
	mute()
	global interruptlibtmp
	global interruptlib
	global interruptpass
	global interruptpasstmp
	interruptlibtmp = interruptlib
	interruptlib = {}
	interruptpasstmp = interruptpass
	interruptpass = 0
	savetargetinserttargettmp(savetarget,inserttarget,interruptcancelcard,interruptcancelplayer,interruptcancellastcard,interruptcanceledcard,interruptcancelok,saveactionplayer,mainpass)


def restoreinterruptlib(count):
	mute()
	global interruptlibtmp
	global interruptlib
	global interruptpass
	global interruptpasstmp
	global interruptcancellastcard
	global interruptcanceledcard
	global interruptcancelcard
	global isinsertreaction
	interruptlib = interruptlibtmp
	interruptlibtmp = {}
	interruptpass = interruptpasstmp
	interruptpasstmp = 0
	isinsertreaction = 0
	if count == 1:
		remoteCall(otherplayer,"restoreinterruptlib",[2])
	else:
		savetargetinserttarget(savetargettmp,inserttargettmp,interruptcancelcardtmp,interruptcancelplayertmp,interruptcancellastcardtmp,interruptcanceledcardtmp,interruptcanceloktmp,saveactionplayertmp,mainpasstmp)
		remoteCall(otherplayer,"savetargetinserttarget",[savetargettmp,inserttarget,interruptcancelcard,interruptcancelplayer,interruptcancellastcard,interruptcanceledcard,interruptcancelok,saveactionplayer,mainpass])
		debug("interruptlib")
		debug(interruptlib)
		debug(getGlobalVariable("insertre"))
		debug(interruptpass)
		if getGlobalVariable("insertre") == "1":
			if interruptlib["pass"+str(interruptpass)][0].controller == me:disc(interruptlib["pass"+str(interruptpass)][0])
			else:remoteCall(otherplayer, "disc", [interruptlib["pass"+str(interruptpass)][0]])
			del interruptlib["pass"+str(interruptpass)]
			remoteCall(otherplayer,"interruptlibdel",[interruptpass])
			interruptpass -= 1
		if getGlobalVariable("insertre") == "1" or getGlobalVariable("insertre") == "2":
			setGlobalVariable("insertre", "")
			if interruptpass == 0:
				notify("over,disc card")
				debug(inserttarget)
				debug(interruptcancelok)
				if mainpass == "leave":
					if interruptcancelok == 1:
						leavecardtype.append(inserttarget._id)
						remoteCall(inserttarget.controller,"leaveforability",[inserttarget])
					else:
						remoteCall(inserttarget.controller,"abilityattachsub",[inserttarget])
						if inserttarget.controller == me:remoteCall(otherplayer, "interruptevent", ["characterkill",1])
						else:interruptevent("characterkill",1)
				elif mainpass == "leavereaction":
					if interruptcancelok == 1:
						remoteCall(inserttarget.controller,"reactionforability",[inserttarget,mainpass])
					else:
						remoteCall(inserttarget.controller,"reactionattachsub",[inserttarget])
						if inserttarget.controller == me:remoteCall(otherplayer, "reaction", ["leavetable",1])
						else:reaction("leavetable",1)
				elif mainpass == "afterchallenge":
					if interruptcancelok == 1:
						remoteCall(inserttarget.controller,"reactionforability",[inserttarget,mainpass])
					else:
						remoteCall(inserttarget.controller,"reactionattachsub",[inserttarget])
						if inserttarget.controller == me:remoteCall(otherplayer, "reaction", ["afterchallenge",1])
						else:reaction("afterchallenge",1)
				else:
					if interruptcancelok == 1:
						savetarget.highlight = milsavecolor
						savepassfinish(1)
					else:
						if inserttarget.controller == me:disc(inserttarget)
						else:remoteCall(otherplayer, "disc", [inserttarget])
					notify("ballanceover")
					if saveactionplayer == me:remoteCall(otherplayer, "interruptevent", ["miljudgementfp",1])
					else :remoteCall(me, "interruptevent", ["miljudgementfp",1])
			else:
				interruptcancellastcard = interruptlib["pass"+str(interruptpass)][1]
				interruptcanceledcard = interruptlib["pass"+str(interruptpass)][0]
				interruptcancelcard = interruptcanceledcard
				remoteCall(otherplayer,"savetargetinserttarget",[savetarget,inserttarget,interruptcancelcard,interruptcancelplayer,interruptcancellastcard,interruptcanceledcard,interruptcancelok,saveactionplayer,mainpass])
				if interruptlib["pass"+str(interruptpass)][2] == me:remoteCall(otherplayer, "interruptevent", ["interruptcancel",1])
				else:
					debug(interruptlib)
					debug(interruptcancelcard)
					remoteCall(me, "interruptevent", ["interruptcancel",1])
					return
		if getGlobalVariable("insertre") == "3":
			setGlobalVariable("insertre", "")
			notify("over,disc card")
			debug(interruptcancelok)
			debug(inserttarget)
			if mainpass == "leave":
				if interruptcancelok == 1:
					leavecardtype.append(inserttarget._id)
					remoteCall(inserttarget.controller,"leaveforability",[inserttarget])
				else:
					remoteCall(inserttarget.controller,"abilityattachsub",[inserttarget])
					if inserttarget.controller == me:remoteCall(otherplayer, "interruptevent", ["characterkill",1])
					else:interruptevent("characterkill",1)
			elif mainpass == "leavereaction":
				if interruptcancelok == 1:
					remoteCall(inserttarget.controller,"reactionforability",[inserttarget,mainpass])
				else:
					remoteCall(inserttarget.controller,"reactionattachsub",[inserttarget])
					if inserttarget.controller == me:remoteCall(otherplayer, "reaction", ["leavetable",1])
					else:reaction("leavetable",1)
			elif mainpass == "afterchallenge":
				if interruptcancelok == 1:
					remoteCall(inserttarget.controller,"reactionforability",[inserttarget,mainpass])
				else:
					remoteCall(inserttarget.controller,"reactionattachsub",[inserttarget])
					if inserttarget.controller == me:remoteCall(otherplayer, "reaction", ["afterchallenge",1])
					else:reaction("afterchallenge",1)
			else:		
				if interruptcancelok == 1:
					savetarget.highlight = milsavecolor
					savepassfinish(1)
				else:
					if inserttarget.type != "Character":
						if inserttarget.controller == me:disc(inserttarget)
						else:remoteCall(otherplayer, "disc", [inserttarget])
				notify("ballanceover")
				if saveactionplayer == me:remoteCall(otherplayer, "interruptevent", ["miljudgementfp",1])
				else :remoteCall(me, "interruptevent", ["miljudgementfp",1])
				
def savetargetinserttargettmp(savetargetn,inserttargetn,interruptcancelcardn,interruptcancelplayern,interruptcancellastcardn,interruptcanceledcardn,interruptcancelokn,saveactionplayern,mainpassn):
	mute()
	global savetargettmp
	global inserttargettmp
	global interruptcancelcardtmp
	global interruptcancelplayertmp
	global interruptcanceledcardtmp
	global interruptcancellastcardtmp
	global interruptlibtmp
	global interruptcanceloktmp
	global saveactionplayertmp
	global mainpasstmp

	interruptcanceloktmp = interruptcancelokn
	savetargettmp = savetargetn
	inserttargettmp = inserttargetn
	interruptcancelcardtmp = interruptcancelcardn
	interruptcancelplayertmp = interruptcancelplayern
	interruptcancellastcardtmp = interruptcancellastcardn
	interruptcanceledcardtmp = interruptcanceledcardn
	saveactionplayertmp =  saveactionplayern
	mainpasstmp = mainpassn

def orientationintable(cards):
	mute()
	c = 0
	for card in table:
		if card.Type == "Character" and card.controller == cards.controller and card.orientation == 0:
			c = 1
	if c == 1:return True

def checkinsertreaction(cards):
	mute()
	global insertreactioncard
	c = 0
	for card in table:
		for d in leavereacion:
			if card.model == leavereacion[d][1] and card.controller == cards.controller:
				if leavereacion[d][2] == "Faction":
					if cards.Faction.find(leavereacion[d][3]) != -1:
						c = 1
						insertreactioncard = card
	if c == 1:return True


def checktablecount(count):
	mute()
	list = []
	for card in table:
		if card.Type == "Character" and card.controller != me:
			list.append(card)

	if len(list) > count:
		return len(list)
	else:return 0

def checktablestealthcount(count):
	mute()
	for card in table:
		if card.Type == "Character" and card.controller != me and card.keywords.find("Stealth") == -1 and card.highlight == None:
			return True

def stealthdict():
	mute()
	global liststeal
	for card in table:
		if card.Type == "Character" and card.controller == me and card.keywords.find("Stealth") != -1 and card.highlight in(MilitaryColor,IntrigueColor,PowerColor):
			liststeal.append(card)
	return liststeal

def fplay(n):
	for card in table:
		if card.name == "1st Player Token":return card.controller

def checkotherattachment(count):
	mute()
	list = []
	for card in table:
		if card.Type == "Attachment" and card.controller != me:
			list.append(card)
	return len(list)

def checkotherloaction(count):
	mute()
	list = []
	for card in table:
		if card.Type == "Location" and card.controller != me:
			list.append(card)
	return len(list)

def checkcharacter(player):
	mute()
	for card in table:
		if card.Type == "Character" and card.controller == player:
			return True

def checkothercharacter(count):
	mute()
	list = []
	for card in table:
		if card.Type == "Character" and card.controller != me:
			list.append(card)
	return len(list)

def checktearsofLys(count):
	mute()
	list = []
	for card in table:
		if card.Type == "Character" and card.controller != me and card.Intrigue != "Yes" and  card.markers[IntrigueIcon] == 0:
			list.append(card)
	return len(list)


def checkaftercalculatereacioncard(count):
	mute()
	global reactionattach
	attach = eval(getGlobalVariable("attachmodify"))
	for card in table:
		for d in aftercalculate:
			if card.model == aftercalculate[d][1] and card.controller == me and aftercalculate[d][6] == "table":
				if aftercalculate[d][2] == "all":
					if winplayer != me:
						if aftercalculate[d][4] == "returndefender" and card.orientation == 0 and aftercalculate[d][3] == "defender" and defender == me:
								if not reactionattach.has_key(card._id):
									reactionattach[card._id] = 1
								else:reactionattach[card._id] += 1
						if aftercalculate[d][4] == "addclaim" and card.orientation == 0 and aftercalculate[d][3] == "defender" and defender == me:
								if not reactionattach.has_key(card._id):
									reactionattach[card._id] = 1
								else:reactionattach[card._id] += 1
						if aftercalculate[d][4] == "submarker" and card.highlight in (MilitaryColor,IntrigueColor,PowerColor):
								if not reactionattach.has_key(card._id):
									reactionattach[card._id] = 1
								else:reactionattach[card._id] += 1
					if winplayer == me:
						if aftercalculate[d][4] == "draw2card" and card.orientation == 0 and aftercalculate[d][3] == "all":
								if not reactionattach.has_key(card._id):
									reactionattach[card._id] = 1
								else:reactionattach[card._id] += 1
						if aftercalculate[d][4] == "standstm" and aftercalculate[d][3] == "all" and checkstm(1):
								if not reactionattach.has_key(card._id):
									reactionattach[card._id] = 1
								else:reactionattach[card._id] += 1
				if aftercalculate[d][2] == "all" and card.highlight in (MilitaryColor,IntrigueColor,PowerColor):
				 	if aftercalculate[d][3] == "attacker" and attacker == me and winplayer == me:
				 		if aftercalculate[d][4] == "disotherattachment" and checkotherattachment(1) > 0:
							if not reactionattach.has_key(card._id):
								reactionattach[card._id] = 1
							else:reactionattach[card._id] += 1
						if aftercalculate[d][4] == "5pwinpow" and attacker.counters['Str'].value - defender.counters['Str'].value >= aftercalculate[d][7]:
							if not reactionattach.has_key(card._id):
								reactionattach[card._id] = 1
							else:reactionattach[card._id] += 1
						if aftercalculate[d][7] == "uo" and unopposed == 1:
							if aftercalculate[d][4] == "stand" and card.orientation == 1:
								if not reactionattach.has_key(card._id):
									reactionattach[card._id] = 1
								else:reactionattach[card._id] += 1
							if aftercalculate[d][4] == "addpowself":
								if not reactionattach.has_key(card._id):
									reactionattach[card._id] = 1
								else:reactionattach[card._id] += 1
					if aftercalculate[d][3] == "attacker" and attacker == me and winplayer == me:
						if aftercalculate[d][7] == "uo" and unopposed == 1:
							if aftercalculate[d][4] == "drawcardorpower":
								if not reactionattach.has_key(card._id):
									reactionattach[card._id] = 1
								else:reactionattach[card._id] += 1
						if aftercalculate[d][4] == "attkilldef":
							if attach.has_key(card._id):
								c = 0
								for attachcard in table:
									if attach[card._id] == attachcard._id and checkinchallengeplay(otherplayer,0) and attachcard.controller == me and attachcard.highlight in(MilitaryColor,IntrigueColor,PowerColor):
										c = 1
								if  c == 1:
									if not reactionattach.has_key(card._id):
										reactionattach[card._id] = 1
									else:reactionattach[card._id] += 1
				if aftercalculate[d][2] != "all":
					if aftercalculate[d][2] == str(challengetype) and winplayer == me:
						if aftercalculate[d][4] == "drawcard":
							if not reactionattach.has_key(card._id):
								reactionattach[card._id] = 1
							else:reactionattach[card._id] += 1
						if aftercalculate[d][4] == "subability2" and card.orientation == 0 and checkattachcard(1):
							if not reactionattach.has_key(card._id):
								reactionattach[card._id] = 1
							else:reactionattach[card._id] += 1
						if aftercalculate[d][4] == "discard" and aftercalculate[d][3] == "defender" and defender == me:
							if not reactionattach.has_key(card._id):
								reactionattach[card._id] = 1
							else:reactionattach[card._id] += 1
						if aftercalculate[d][4] == "addplayer" and checkdothrakhand(1):
							if not reactionattach.has_key(card._id):
								reactionattach[card._id] = 1
							else:reactionattach[card._id] += 1
						if card.highlight == IntrigueColor and aftercalculate[d][4] == "addplayer6" and checktyrellcharacter(6):
							if not reactionattach.has_key(card._id):
								reactionattach[card._id] = 1
							else:reactionattach[card._id] += 1
						if aftercalculate[d][4] == "kill" and checkice(card._id):
							if not reactionattach.has_key(card._id):
								reactionattach[card._id] = 1
							else:reactionattach[card._id] += 1
						debug(checkhousepow(otherplayer))
						if card.type == "Plot" and card.highlight == None and aftercalculate[d][4] == "movepow" and checkhousepow(otherplayer) > 0:
							if not reactionattach.has_key(card._id):
								reactionattach[card._id] = 1
							else:reactionattach[card._id] += 1
	for card in me.hand:
		for d in aftercalculate:
			if card.model == aftercalculate[d][1] and aftercalculate[d][6] == "Hand":
				if aftercalculate[d][2] != "all":
					if str(challengetype) in aftercalculate[d][2] and winplayer == me:
						if aftercalculate[d][4] == "addhand":
							if not reactionattach.has_key(card._id):
								reactionattach[card._id] = 1
							else:reactionattach[card._id] += 1
				 	if aftercalculate[d][2] == str(challengetype) and attacker == me and winplayer == me:
				 		if aftercalculate[d][7] != "" and attacker.counters['Str'].value - defender.counters['Str'].value >= aftercalculate[d][7]:
					 		if aftercalculate[d][4] == "disotherloaction" and checkotherloaction(1) > 0:
								if not reactionattach.has_key(card._id):
									reactionattach[card._id] = 1
								else:reactionattach[card._id] += 1
							if aftercalculate[d][4] == "kill" and checkothercharacter(1) > 0:
								if not reactionattach.has_key(card._id):
									reactionattach[card._id] = 1
								else:reactionattach[card._id] += 1
						if checktearsofLys(1) > 0 and aftercalculate[d][4] == "addmarker":
							if not reactionattach.has_key(card._id):
								reactionattach[card._id] = 1
							else:reactionattach[card._id] += 1
					if aftercalculate[d][2] == str(challengetype) and winplayer == me:
				 		if aftercalculate[d][7] != "" and attacker.counters['Str'].value - defender.counters['Str'].value >= aftercalculate[d][7]:
							if re.search('\d\spow', aftercalculate[d][4]):
								if not reactionattach.has_key(card._id):
									reactionattach[card._id] = 1
								else:reactionattach[card._id] += 1
							if aftercalculate[d][4] == "addusedplotpow":
								if not reactionattach.has_key(card._id):
									reactionattach[card._id] = 1
								else:reactionattach[card._id] += 1
					if winplayer != me:
						if aftercalculate[d][2] == str(challengetype):
							if aftercalculate[d][4] == "losekill" and checkinchallengeplay(otherplayer,0) and checkmytableTraits("Direwolf."):
								if not reactionattach.has_key(card._id):
									reactionattach[card._id] = 1
								else:reactionattach[card._id] += 1

				if aftercalculate[d][2] == "all":
					if winplayer == me:
						if aftercalculate[d][7] != "" and me.counters['Str'].value - otherplayer.counters['Str'].value >= aftercalculate[d][7]:
							if aftercalculate[d][4] == "cantchallenge" and aftercalculate[d][3] == "defender" and defender == me and checknwattacker(1):
								if not reactionattach.has_key(card._id):
									reactionattach[card._id] = 1
								else:reactionattach[card._id] += 1
					if winplayer != me:
						if aftercalculate[d][3] == "defender" and defender == me:
							if aftercalculate[d][4] == "cant1challenge":
								if not reactionattach.has_key(card._id):
									reactionattach[card._id] = 1
								else:reactionattach[card._id] += 1
				
	debug("reactionattach4")
	debug(reactionattach)
	if len(reactionattach) > 0:setGlobalVariable("aftcu", "1")
	if count == 1:remoteCall(otherplayer, "checkaftercalculatereacioncard", [2])
	else:
		if getGlobalVariable("aftcu") == "1":
			setGlobalVariable("aftcu", "")
			if fplay(1) == me:reaction("aftercalculate",1)
			else: 
				remoteCall(otherplayer, "reaction", ["aftercalculate",1])
		else:
			if fplay(1) == me:balancechallengefinish(challengetype,winplayer)
			else:remoteCall(otherplayer, "balancechallengefinish", [challengetype,winplayer])
			return

def checkaftercalculatereacioncardforce(count):
	mute()
	global reactionattach
	for card in table:
		for d in aftercalculate:
			if card.model == aftercalculate[d][1] and card.controller == me and aftercalculate[d][6] == "table" and "Forced Reaction" in card.Text:
				if aftercalculate[d][2] == "all":
					if winplayer == me:
						if aftercalculate[d][4] == "addred" and card.highlight in (MilitaryColor,IntrigueColor,PowerColor):
								if not reactionattach.has_key(card._id):
									reactionattach[card._id] = 1
								else:reactionattach[card._id] += 1
					if winplayer != me:
						if aftercalculate[d][4] == "kneel" and aftercalculate[d][7] == "uo" and unopposed == 1 and card.orientation == 0:
							if not reactionattach.has_key(card._id):
								reactionattach[card._id] = 1
							else:reactionattach[card._id] += 1
	debug("reactionattach3")
	debug(reactionattach)
	if len(reactionattach) > 0:setGlobalVariable("aftcu", "1")
	if count == 1:remoteCall(otherplayer, "checkaftercalculatereacioncardforce", [2])
	else:
		if getGlobalVariable("aftcu") == "1":
			setGlobalVariable("aftcu", "")
			if fplay(1) == me:reaction("aftercalculatef",1)
			else: 
				remoteCall(otherplayer, "reaction", ["aftercalculatef",1])
		else:
			if fplay(1) == me:checkaftercalculatereacioncard(1)
			else:remoteCall(otherplayer, "checkaftercalculatereacioncard", [1])
			return

def delreactioncard(card):
	mute()
	global reactioncardlimit
	global reactionattach
	c = 0
	if not reactioncardlimit.has_key(card._id):
		reactioncardlimit[card._id] = 1
	else:reactioncardlimit[card._id] += 1
	for d in afterchallengereacion:
		if card.model == aftercalculate[d][1]:
			if reactioncardlimit[card._id] == afterchallengereacion[d][5]:
				del reactionattach[card._id]
				c = 1
	for d in aftercalculate:
		if card.model == aftercalculate[d][1]:
			if reactioncardlimit[card._id] == aftercalculate[d][5]:
				del reactionattach[card._id]
				c = 1
	for d in leavereacion:
		if card.model == leavereacion[d][1]:
			if reactioncardlimit[card._id] == leavereacion[d][5]:
				del reactionattach[card._id]
				c = 1
	if c == 0:
		reactionattach[card._id] -= 1
		if reactionattach[card._id] == 0:del reactionattach[card._id]
	notify("reaction cancel.")

def checkinchallengeplay(person,cost):
	mute()
	c = 0
	for card in table:
		if person != "all":
			if card.controller == person:
				if challengetype == 1 and card.highlight == MilitaryColor:
					if cost != 0:
						if int(card.cost) <= cost:
							c = 1
					else:c = 1
				if challengetype == 2 and card.highlight == IntrigueColor:
					if cost != 0:
						if int(card.cost) <= cost:
							c = 1
					else:c = 1
				if challengetype == 2 and card.highlight == PowerColor:
					if cost != 0:
						if int(card.cost) <= cost:
							c = 1
					else:c = 1
		else:
			if challengetype == 1 and card.highlight == MilitaryColor:
					if cost != 0:
						if int(card.cost) <= cost:
							c = 1
					else:c = 1
			if challengetype == 2 and card.highlight == IntrigueColor:
				if cost != 0:
					if int(card.cost) <= cost:
						c = 1
				else:c = 1
			if challengetype == 2 and card.highlight == PowerColor:
				if cost != 0:
					if int(card.cost) <= cost:
						c = 1
				else:c = 1
	if c == 1:return True

def checkmytableTraits(cardTraits):
	mute()
	for card in table:
		if card.controller == me and card.Traits == cardTraits and card.orientation == 0:
			return True
			break
def returncard(card):
	mute()
	card.moveTo(me.hand)

def disccard(card):
	mute()
	card.moveTo(me.piles['Discard pile'])


def checkattachcard(card):
	mute()
	attach = eval(getGlobalVariable("attachmodify"))
	for card in table:
		if card.controller != me:
			c = 0
			for d in attach:
				if card._id == d:
					c = 1
			if c == 0:
				return True
				break

def checkattachment(count):
	mute()
	list = []
	for card in table:
		if card.Type == "Attachment":
			list.append(card)
	return len(list)

def checkstm(card):
	mute()
	for card in table:
		if card.controller == me and card.highlight in (MilitaryColor,IntrigueColor,PowerColor) and "Stormborn." in card.Traits and card.orientation == 1 and card.Type == "Character":
			return True
			break

def checkdothrakhand(card):
	mute()
	for card in me.hand:
		if "Dothraki." in card.Traits:
			return True
			break

def checknwattacker(card):
	mute()
	for card in table:
		if card.controller == me and card.highlight in (MilitaryColor,IntrigueColor,PowerColor) and "Night's Watch." in card.Faction and card.Type == "Character":
			return True
			break
def checktyrellcharacter(cardcost):
	mute()
	for card in me.hand:
		if "Tyrell." in card.Faction and int(card.cost) <= cardcost and card.Type == "Character":
			return True
			break

def clearreaction(count):
	mute()
	global reactionattach
	global sessionpass
	reactionattach = {}
	sessionpass = ""
	if count == 1:remoteCall(players[1], "clearreaction", [2])
	if count == 2:
		if getGlobalVariable("dominancestart") == "2":
			setGlobalVariable("dominancestart", "0")
			if fplay(1) == me:dominance(table)
			else: remoteCall(players[1], "dominance", [table])
			return
		if getGlobalVariable("dominancewin") == "2":
			setGlobalVariable("dominancewin", "0")
			if fplay(1) == me:actiondominance(1)
			else: remoteCall(players[1], "actiondominance", [1])
			return
		if getGlobalVariable("dominanceend") == "2":
			setGlobalVariable("dominanceend", "0")
			#dominancephaseend(table)
			remoteCall(fplay(1), "dominancephaseend", [table])
			return
		challengeaction(1)
	if count == 3:remoteCall(otherplayer, "clearreaction", [4])
	if count == 4:
		if fplay(1) == me:checkaftercalculatereacioncard(1)
		else:remoteCall(otherplayer, "checkaftercalculatereacioncard", [1])
	if count == 5:remoteCall(otherplayer, "clearreaction", [6])
	if count == 6:
		if fplay(1) == me:balancechallengefinish(challengetype,winplayer)
		else:remoteCall(otherplayer, "balancechallengefinish", [challengetype,winplayer])

def clearaction(count):
	mute()
	global actionattach
	global sessionpass
	actionattach = {}
	sessionpass = ""
	# if getGlobalVariable("reavelplot") == "2":
	# 	if me.isInverted:table.create("634c8980-9e07-40ba-a259-df1fe8fd184a",-375,-250)
	# 	else:table.create("634c8980-9e07-40ba-a259-df1fe8fd184a",-375,200)
	# if getGlobalVariable("drawphase") == "2":
	# 	if me.isInverted:table.create("76d32ba3-bb1b-4c88-8e99-4381e45595e9",-375,-250)
	# 	else:table.create("76d32ba3-bb1b-4c88-8e99-4381e45595e9",-375,200)
	if count == 1:

		remoteCall(players[1], "clearaction", [2])
	if count == 2:
		if getGlobalVariable("reavelplot") == "2":
			if fplay(1) == me:plotphaseend()
			else:remoteCall(players[1], "plotphaseend", [])
			return
		if getGlobalVariable("drawphase") == "2":
			if fplay(1) == me:drawphaseend()
			else:remoteCall(players[1], "drawphaseend", [])
			return
		if getGlobalVariable("dominanceaction") == "2":
			setGlobalVariable("dominanceaction","0")
			if fplay(1) == me:dominanceendreaction(1)
			else: remoteCall(players[1], "dominanceendreaction", [1])
			return
		if getGlobalVariable("standingaction") == "2":
			setGlobalVariable("standingaction","0")
			if fplay(1) == me:standingendreaction(1)
			else: remoteCall(players[1], "standingendreaction", [1])
			return
		if getGlobalVariable("actiontaxation") == "2":
			setGlobalVariable("actiontaxation","0")
			if fplay(1) == me:taxationendreaction(1)
			else: remoteCall(players[1], "taxationendreaction", [1])
			return
		if attacker == []:
			if getGlobalVariable("activeplayer") == str(me._id):challengeAnnounce(table)
			else:remoteCall(players[1], "challengeAnnounce", table)
		else:
			if defender == []:
				if attacker == me:remoteCall(otherplayer, "announceOpp", [table])
				else:announceOpp(table)
			else:
				challenge(table)

def choosetype(card):
	mute()
	choiceList = ['Character', 'Location', 'Attachment', 'Event']
	colorList = ['#ae0603' ,'#006b34','#1a4d8f','#a0522d']
	choice = askChoice("Which type do you want to select?", choiceList,colorList)
	if choice == 0:
		choosetype(card)
		return
	else:remoteCall(otherplayer, "reactionforability", [card,str(choice)])

def checkice(cardid):
	mute()
	attach = eval(getGlobalVariable("attachmodify"))
	for card in table:
		if attach[cardid] == card._id and card.controller == me and card.highlight == MilitaryColor:
			return True
			break

def checkheartsbane(cardid):
	mute()
	attach = eval(getGlobalVariable("attachmodify"))
	for card in table:
		if attach[cardid] == card._id and card.controller == me and card.highlight in (MilitaryColor,IntrigueColor,PowerColor):
			return True
			break

def checkstandplayer(group, x = 0, y = 0):
	mute()
	for card in table:
		if card.type == "Character" and card.orientation == 0:
			return True

def checkhousepow(player):
	mute()
	for card in table:
		if card.type == "Faction" and card.controller == player:
			return card.markers[Power]


def keyword(count):
	mute()
	global keywordattach
	for card in table:
		for d in keywordslib:
			if card.model == keywordslib[d][1] and card.controller == me and card.highlight in(MilitaryColor,IntrigueColor,PowerColor):
				if winplayer == me:
					keywordattach.append(card)
	debug(keywordattach)
	keywordforability(1)


def keywordforability(count):
	mute()
	global keywordattach
	global sessionpass
	global cardtoaction
	c = 0
	
	if len(keywordattach) > 0:
		for card in keywordattach:
			for d in keywordslib:
				if card.model == keywordslib[d][1] and card.controller == me:
					if count == 1:
						if "Renown" in keywordslib[d][2]:
							card.markers[Power] += 1
							notify("{}'s {} add 1 pow by Renown".format(me,card))
						if "Insight" in keywordslib[d][2] and len(me.deck) > 0:
							draw(me.deck)
							notify("{}'s {} draw 1 card by Insight".format(me,card))
						if "Pillage" in keywordslib[d][2] and len(otherplayer.deck) > 0:
							remoteCall(otherplayer, "disctop", [1])
							notify("{}'s {} discards 1 cards from the top of {} Deck by Pillage".format(me,card,otherplayer))
							setTimer(me,"keywords",table)
							return
					for f in keywordsreaction:
						if card.model == keywordsreaction[f][1] and len(otherplayer.piles['Discard Pile']) > 0:
							for cards in otherplayer.piles['Discard Pile']:
								if cards.type == "Location":
									cardtoaction = card
									reaction("keywords",1)
									return
					count = 1
					debug(card)
					debug(keywordslib[d][2])
					if "Initimidate" in keywordslib[d][2] and checkothercharacter(1) > 0:

						cardtoaction = card
						keywordattach.remove(card)
						sessionpass = ""
						targetTuple = ([cards._id for cards in table if cards.controller != me and cards.type == "Character" and int(cards.Cost) <= me.counters['Str'].value - otherplayer.counters['Str'].value and cards.orientation == 0], me._id) 
						setGlobalVariable("tableTargets", str(targetTuple))
						setGlobalVariable("selectmode", "1")
						if me.isInverted:table.create("584a37d7-5a30-4018-ae21-0ad325203fa0",-375,-250)
						else:table.create("584a37d7-5a30-4018-ae21-0ad325203fa0",-375,200)
						notify("**{} into selectmode**".format(me))
						sessionpass = "initimidateselect"				
						return
					keywordattach.remove(card)
		keywordforability(1)
	else:
		setGlobalVariable("mainstep", "78")
		notify("kw over")
		challengebalanceover(1)

def movecard(card):
	card.moveToTable(-200,200)

def disctop(player):
	mute()
	card = me.deck.top()
	card.moveTo(me.piles['Discard pile'])

def checktraits(traits,condition,player):
	mute()
	for card in table:
		if card.controller == player and traits in card.Traits:
			if condition == "challenge":
				if card.highlight in (MilitaryColor,IntrigueColor,PowerColor):
					return True
			else:return True

def checkhandfaction(faction,deck,player):
	mute()
	for card in deck:
		if card.controller == player and card.Faction == faction:
			return True

def checkcost(cost):
	mute()
	for card in table:
		if int(card.cost) <= cost:
			return True

def checkfaction(faction):
	mute()
	for card in table:
		if card.Faction == faction:
			return True

def checkchallengefaction(faction):
	mute()
	for card in table:
		if card.Faction == faction and card.highlight in (MilitaryColor,IntrigueColor,PowerColor):
			return True

def checkkneelfaction(faction):
	mute()
	for card in table:
		if card.Faction == faction and card.orientation == 1 and card.controller == me:
			return True

def checkcardstatus(deck = table,faction = "",cardtype = "",cardstr = -1,stand = -1,unique = "",cost = -1,player = "",traits = "",mil = "",intcard = "",powcard = "",highlight = "",model = ""):
	mute()
	for card in deck:
		if card.type not in ("Internal"):
			if checkcardunique(card,unique) and checkcardstand(card,stand) and checkcardstr(card,cardstr) and checkcardcost(card,cost) and checkcardtype(card,cardtype) and checkcardfaction(card,faction) and checkcardplayer(card,player) and checkcardtraits(card,traits) and checkcardmil(card,mil) and checkcardint(card,intcard) and checkcardpow(card,powcard) and checkcardhl(card,highlight) and checkcardmd(card,model):
				return True

def checkcardid(deck = table,faction = "",cardtype = "",cardstr = -1,stand = -1,unique = "",cost = -1,player = "",traits = "",mil = "",intcard = "",powcard = "",highlight = ""):
	mute()
	listid = []
	for card in deck:
		if card.type not in ("Internal"):
			if checkcardunique(card,unique) and checkcardstand(card,stand) and checkcardstr(card,cardstr) and checkcardcost(card,cost) and checkcardtype(card,cardtype) and checkcardfaction(card,faction) and checkcardplayer(card,player) and checkcardtraits(card,traits) and checkcardmil(card,mil) and checkcardint(card,intcard) and checkcardpow(card,powcard) and checkcardhl(card,highlight) and card.filter != WaitColor:
				listid.append(card._id)
	return listid

def checkcardunique(card,unique):
	mute()
	if unique != "" and card.unique == unique:return True
	if unique == "":return True

def checkcardstand(card,stand):
	mute()
	if stand != -1 and card.orientation == stand:return True
	if stand == -1:return True

def checkcardstr(card,cardstr):
	mute()
	if cardstr != -1 and card.type == "Character":
		if int(card.strength) <= cardstr:return True
	if cardstr == -1:return True

def checkcardcost(card,cost):
	mute()
	debug(card)
	if cost != -1 and card.type not in ("Internal","Faction","Agenda","Plot"):
		if int(card.cost) <= cost:return True
	if cost == -1:return True

def checkcardtype(card,cardtype):
	mute()
	if cardtype != "" and card.type in cardtype:return True
	if cardtype == "":return True

def checkcardfaction(card,faction):
	mute()
	if faction != "" and faction == card.faction:return True
	if faction == "":return True

def checkcardplayer(card,player):
	mute()
	if player != "" and card.controller == player:return True
	if player == "":return True

def checkcardtraits(card,traits):
	mute()
	if traits != "" and traits in card.traits:return True
	if traits == "":return True

def checkcardmil(card,mil):
	mute()
	if mil != "" and card.Military == mil:return True
	if mil == "":return True

def checkcardint(card,intcard):
	mute()
	if intcard != "" and card.Intrigue == intcard:return True
	if intcard == "":return True

def checkcardpow(card,powcard):
	mute()
	if powcard != "" and card.Power == powcard:return True
	if powcard == "":return True

def checkcardhl(card,highlight):
	mute()
	debug(highlight)
	if highlight != "" and card.highlight == highlight:return True
	if highlight == "":return True

def checkcardmd(card,model):
	mute()
	if model != "" and card.model == model:return True
	if model == "":return True


def checkburn(player):
	mute()
	for card in table:
		if "Dragon." in card.traits or card.model == "a2f21413-0272-47dc-a197-e364aa942d4c":
			if card.controller == player and card.orientation == 0:
				return True

def checkdeadtargaryen(ok):
	mute()
	for card in me.piles['Dead Pile']:
		if card.Faction == "Targaryen." and card.Unique =="Yes" and card.Type == "Character":
			return True

def checkpr(player):
	mute()
	for card in table:
		if card.model == "12bc6cd7-39f0-44b7-9492-101d8083c468" and card.controller == player:
			return True
def checkrl(player):
	mute()
	for card in table:
		if card.model == "b9e548d6-49df-4a34-b84d-22f92ec101c4" and card.controller == player:
			return True

def challengeaction(count):
	mute()
	global actionattach
	for card in table:
		for d in actionchallenge:
			if card.model == actionchallenge[d][1] and card.controller == me and actionchallenge[d][3] == "table":
				if actionchallenge[d][2] == "kneelhouse+2str" and checktraits("Wildling","challenge",me):
					for housecard in table:
						if housecard.type == "Faction" and housecard.controller == me and housecard.orientation == 0:
							if not actionattach.has_key(card._id):
								actionattach[card._id] = 1
							else:actionattach[card._id] += 1
				if actionchallenge[d][2] == "addinticon" and checkfaction("Baratheon."):
					if not actionattach.has_key(card._id):
						actionattach[card._id] = 1
					else:actionattach[card._id] += 1
				if actionchallenge[d][2] == "addstr" and checkchallengefaction("Greyjoy.") and card.orientation == 0:
					if not actionattach.has_key(card._id):
						actionattach[card._id] = 1
					else:actionattach[card._id] += 1
				if actionchallenge[d][2] == "drawstark" and card.orientation == 0 and len(me.hand) > 0:
					if not actionattach.has_key(card._id):
						actionattach[card._id] = 1
					else:actionattach[card._id] += 1
				if actionchallenge[d][2] == "addstr3" and card.orientation == 0:
					if not actionattach.has_key(card._id):
						actionattach[card._id] = 1
					else:actionattach[card._id] += 1
				if actionchallenge[d][2] == "attaddstr3" and checkheartsbane(card._id) and card.orientation == 0:
					if not actionattach.has_key(card._id):
						actionattach[card._id] = 1
					else:actionattach[card._id] += 1
				if actionchallenge[d][2] == "standremovechallenge" and checkinchallengeplay(attacker,0) and card.orientation == 0 and me.counters['Gold'].value > 0:
					if not actionattach.has_key(card._id):
						actionattach[card._id] = 1
					else:actionattach[card._id] += 1
	for card in me.hand:
		for d in actionchallenge:
			if card.model == actionchallenge[d][1] and actionchallenge[d][3] == "Hand":
				if actionchallenge[d][5] == "":
					if actionchallenge[d][2] == "dischand" and checktraits("R'hllor.","",me) and len(otherplayer.hand) > 0:
						if not actionattach.has_key(card._id):
							actionattach[card._id] = 1
						else:actionattach[card._id] += 1
					if actionchallenge[d][2] == "addstrdraw" and checkchallengefaction("Stark."):
						if not actionattach.has_key(card._id):
							actionattach[card._id] = 1
						else:actionattach[card._id] += 1
					if actionchallenge[d][2] == "addclaim":
						if not actionattach.has_key(card._id):
							actionattach[card._id] = 1
						else:actionattach[card._id] += 1
					if actionchallenge[d][2] == "burn" and checkburn(me) and checkinchallengeplay("all",0) :
						if not actionattach.has_key(card._id):
							actionattach[card._id] = 1
						else:actionattach[card._id] += 1
					if actionchallenge[d][2] == "returndead" and checkdeadtargaryen(1):
						if not actionattach.has_key(card._id):
							actionattach[card._id] = 1
						else:actionattach[card._id] += 1
					if actionchallenge[d][2] == "3playeraddstr2" and checkfaction("Tyrell."):
						if not actionattach.has_key(card._id):
							actionattach[card._id] = 1
						else:actionattach[card._id] += 1
				if actionchallenge[d][5] == "fplay" and fplay(1) == me:
					if actionchallenge[d][2] == "ignorestr":
						if not actionattach.has_key(card._id):
							actionattach[card._id] = 1
						else:actionattach[card._id] += 1
				if actionchallenge[d][5] == "defender" and defender == me:
					if actionchallenge[d][2] == "adddef" and  checkkneelfaction("Baratheon."):
						if not actionattach.has_key(card._id):
							actionattach[card._id] = 1
						else:actionattach[card._id] += 1
				if actionchallenge[d][5] == "Lord./Lady." and checktraits("Lord.","",me) or checktraits("Lady.","",me):
					if actionchallenge[d][2] == "kneelhousereturnhand" and checkothercharacter(1) > 0:
						for housecard in table:
							if housecard.type == "Faction" and housecard.controller == me and housecard.orientation == 0:
								if not actionattach.has_key(card._id):
									actionattach[card._id] = 1
								else:actionattach[card._id] += 1
				if actionchallenge[d][5] == "ambush":
					if actionchallenge[d][2] == "choosechallenge":
						if not actionattach.has_key(card._id):
							actionattach[card._id] = 1
						else:actionattach[card._id] += 1
					if actionchallenge[d][2] == "removechallenge":
						if not actionattach.has_key(card._id):
							actionattach[card._id] = 1
						else:actionattach[card._id] += 1


	debug(actionattach)
	if len(actionattach) > 0:setGlobalVariable("action", "1")
	if count == 1:remoteCall(otherplayer, "challengeaction", [2])
	if count == 2:
		if getGlobalVariable("action") == "1":
			setGlobalVariable("action", "0")
			if fplay(1) == me:action("challenge",1)
			else:remoteCall(otherplayer, "action", ["challenge",1])
		else:
			if attacker == []:
				if getGlobalVariable("activeplayer") == str(me._id):challengeAnnounce(table)
				else:remoteCall(players[1], "challengeAnnounce", table)
			else:
				if defender == []:
					if attacker == me:remoteCall(otherplayer, "announceOpp", [table])
					else:announceOpp(table)
				else:
					challenge(table)

def actiongeneral(count):
	mute()
	global actionattach
	global cardtoaction
	for card in me.hand:
		for d in generalaction:
			if card.model == generalaction[d][1] and card.controller == me and generalaction[d][3] == "Hand":
				if generalaction[d][2] == "addlan" and checkcardstatus(deck = me.hand,player = me,cardtype = "Character"):
					if not actionattach.has_key(card._id):
						actionattach[card._id] = 1
					else:actionattach[card._id] += 1
				if generalaction[d][2] == "loseicon" and checkcardstatus(cardtype = "Character",cardstr = 4):
					if not actionattach.has_key(card._id):
						actionattach[card._id] = 1
					else:actionattach[card._id] += 1
				if generalaction[d][2] == "standtc" and checkcardstatus(unique = "Yes",faction = "Targaryen.",player = me,stand = 1):
					if not actionattach.has_key(card._id):
						actionattach[card._id] = 1
					else:actionattach[card._id] += 1
				if generalaction[d][2] == "5t3b" and len(me.deck) > 0:
					if not actionattach.has_key(card._id):
						actionattach[card._id] = 1
					else:actionattach[card._id] += 1
				if generalaction[d][2] == "searchbrs" and len(me.deck) > 0 and me.counters['Reserve'].value > 0:
					if not actionattach.has_key(card._id):
						actionattach[card._id] = 1
					else:actionattach[card._id] += 1
				if generalaction[d][2] == "addusedplotgold" and checkcardstatus(cardtype = "Faction",stand = 0):
					if not actionattach.has_key(card._id):
						actionattach[card._id] = 1
					else:actionattach[card._id] += 1
				if generalaction[d][2] == "searchwolf" and checkcardstatus(cardtype = "Faction",stand = 0) and len(me.deck) > 0:
					if not actionattach.has_key(card._id):
						actionattach[card._id] = 1
					else:actionattach[card._id] += 1
				if generalaction[d][2] == "noprint" and checkcardstatus(cardtype = ("Character","Location")):
					if not actionattach.has_key(card._id):
						actionattach[card._id] = 1
					else:actionattach[card._id] += 1
				if generalaction[d][2] == "4cardchoose2" and checkcardstatus(cardtype = "Faction",stand = 0) and len(me.deck) > 0:
					if not actionattach.has_key(card._id):
						actionattach[card._id] = 1
					else:actionattach[card._id] += 1

	for card in table:
		for d in generalaction:
			if card.model == generalaction[d][1] and card.controller == me and generalaction[d][3] == "table":
				if card.type == "Character" and check511():continue
				if card.type in ("Character","Location") and checknoprint(card):continue
				if generalaction[d][2] == "add5returnme" and checkcardstatus(deck = me.hand,cost = 5):
					if not actionattach.has_key(card._id):
						actionattach[card._id] = 1
					else:actionattach[card._id] += 1
				if generalaction[d][2] == "1goldicon":
					if not actionattach.has_key(card._id):
						actionattach[card._id] = 1
					else:actionattach[card._id] += 1
				if generalaction[d][2] == "d1cg1g" and len(me.hand) > 1:
					if not actionattach.has_key(card._id):
						actionattach[card._id] = 1
					else:actionattach[card._id] += 1
				if generalaction[d][2] == "standlocation" and checkcardstatus(cardtype = "Location",stand = 1):
					if not actionattach.has_key(card._id):
						actionattach[card._id] = 1
					else:actionattach[card._id] += 1
				if generalaction[d][2] == "2gstandc" and checkcardstatus(cardtype = "Character",stand = 1):
					if not actionattach.has_key(card._id):
						actionattach[card._id] = 1
					else:actionattach[card._id] += 1
				if generalaction[d][2] == "standlady" and checkcardstatus(traits = "Lady.",stand = 1):
					if not actionattach.has_key(card._id):
						actionattach[card._id] = 1
					else:actionattach[card._id] += 1
				if generalaction[d][2] == "kneelfaction" and checkcardstatus(cardtype = "Faction",stand = 0):
					if not actionattach.has_key(card._id):
						actionattach[card._id] = 1
					else:actionattach[card._id] += 1
				if generalaction[d][2] == "standicon" and card.markers[standIcon] == 1:
					if not actionattach.has_key(card._id):
						actionattach[card._id] = 1
					else:actionattach[card._id] += 1
				if generalaction[d][2] == "changecontroll":
					eee = 0
					attach = eval(getGlobalVariable("attachmodify"))
					for cards in table:
						if attach[card._id] == cards._id:
							attachcard = cards
							cardtoaction = attachcard
					for checkcard in table:
						if checkcard.faction == "Stark." and checkcard.type == "Character" and checkcard.filter != WaitColor and  not 'No attachments.' in checkcard.Keywords and checkcard != attachcard:
							eee = 1
					if eee == 1:
						if not actionattach.has_key(card._id):
							actionattach[card._id] = 1
						else:actionattach[card._id] += 1	
				# if generalaction[d][2] == "manual":
				# 	if not actionattach.has_key(card._id):
				# 		actionattach[card._id] = 1
				# 	else:actionattach[card._id] += 1

	debug(cardtmp)
	debug(actionattach)
	if len(actionattach) > 0:setGlobalVariable("generalaction", "1")
	if count == 1:remoteCall(players[1], "actiongeneral", [2])
	if count == 2:
		debug(getGlobalVariable("generalaction"))
		if getGlobalVariable("generalaction") == "1":
			setGlobalVariable("generalaction", "2")
			if fplay(1) == me:action("general",1)
			else:remoteCall(otherplayer, "action", ["general",1])
		else:
			clearaction(1)


def action(actioninsert,actioncount):
	mute()
	debug(actioninsert)
	debug(sessionpass)
	global sessionpass
	global intertreaction
	if actioninsert == "challenge":
		#if getGlobalVariable("mainstep") == "7":setGlobalVariable("mainstep", "77")
		if len(actionattach) > 0:
			if sessionpass == "":
				choiceList = ['action', 'cancel']
				colorList = ['#006b34' ,'#ae0603']
				choice = askChoice("Which Pass do you want to action?", choiceList,colorList)
				if choice == 1:
					intoaction(actionattach,actioncount,"challenge")
					return
				if choice in (2,0):
					if actioncount == 2:
						notify("action over")
						clearaction(1)
					else:
						actioncount += 1
						remoteCall(otherplayer, "action", ["challenge",actioncount])
					return
			if sessionpass == "actionok":
				actioncards = selectedcard
				if actioncards == []:
					if actioncount == 2:
						notify("action over")
						clearaction(1)
					else:
						actioncount += 1
						sessionpass = ""
						remoteCall(otherplayer, "action", ["challenge",actioncount])
					return
				else:
					actioncard = actioncards[0]
					sessionpass = ""
					remoteCall(otherplayer, "checkaction", [actioncard,"challengeaction"])
		else:
			if actioncount == 2:
				notify("action over")
				clearaction(1)
			else:
				actioncount += 1
				remoteCall(otherplayer, "action", ["challenge",actioncount])
			return
	if actioninsert == "general":
		if sessionpass == "actionok" or len(checkactionattach("generalaction")) > 0:
			if sessionpass == "":
				intoaction(actionattach,actioncount,"general")
				return
			if sessionpass == "actionok":
				actioncards = selectedcard
				if actioncards == []:
					if actioncount == 2:
						notify("action over")
						clearaction(1)
					else:
						actioncount += 1
						sessionpass = ""
						remoteCall(players[1], "action", ["general",actioncount])
					return
				else:
					setGlobalVariable("actioncancel", "0")
					actioncard = actioncards[0]
					sessionpass = ""
					remoteCall(players[1], "checkaction", [actioncard,"generalaction"])
		else:
			if actioncount == 2:
				notify("action over")
				clearaction(1)
			else:
				actioncount += 1
				remoteCall(players[1], "action", ["general",actioncount])
			return
	if actioninsert == "dominance":
		debug(sessionpass)
		debug(checkactionattach("dominance"))
		if sessionpass == "actionok" or len(checkactionattach("dominance")) > 0:
			if sessionpass == "":
				intoaction(actionattach,actioncount,"dominance")
				return
			if sessionpass == "actionok":
				actioncards = selectedcard
				if actioncards == []:
					if actioncount == 2:
						notify("action over")
						clearaction(1)
					else:
						actioncount += 1
						sessionpass = ""
						remoteCall(players[1], "action", ["dominance",actioncount])
					return
				else:
					setGlobalVariable("actioncancel", "0")
					actioncard = actioncards[0]
					sessionpass = ""
					remoteCall(players[1], "checkaction", [actioncard,"dominanceaction"])
		else:
			if actioncount == 2:
				notify("action over")
				clearaction(1)
			else:
				actioncount += 1
				remoteCall(players[1], "action", ["dominance",actioncount])
			return
	if actioninsert == "standing":
		debug(sessionpass)
		if sessionpass == "actionok" or len(checkactionattach("standing")) > 0:
			if sessionpass == "":
				intoaction(actionattach,actioncount,"standing")
				return
			if sessionpass == "actionok":
				actioncards = selectedcard
				if actioncards == []:
					if actioncount == 2:
						notify("action over")
						clearaction(1)
					else:
						actioncount += 1
						sessionpass = ""
						remoteCall(players[1], "action", ["standing",actioncount])
					return
				else:
					setGlobalVariable("actioncancel", "0")
					actioncard = actioncards[0]
					sessionpass = ""
					remoteCall(players[1], "checkaction", [actioncard,"standingaction"])
		else:
			if actioncount == 2:
				notify("action over")
				clearaction(1)
			else:
				actioncount += 1
				remoteCall(players[1], "action", ["standing",actioncount])
			return
	if actioninsert == "taxation":
		debug(sessionpass)
		if sessionpass == "actionok" or len(checkactionattach("taxation")) > 0:
			if sessionpass == "":
				intoaction(actionattach,actioncount,"taxation")
				return
			if sessionpass == "actionok":
				actioncards = selectedcard
				if actioncards == []:
					if actioncount == 2:
						notify("action over")
						clearaction(1)
					else:
						actioncount += 1
						sessionpass = ""
						remoteCall(players[1], "action", ["taxation",actioncount])
					return
				else:
					setGlobalVariable("actioncancel", "0")
					actioncard = actioncards[0]
					sessionpass = ""
					remoteCall(players[1], "checkaction", [actioncard,"taxationaction"])
		else:
			if actioncount == 2:
				notify("action over")
				clearaction(1)
			else:
				actioncount += 1
				remoteCall(players[1], "action", ["taxation",actioncount])
			return
	if actioninsert == "marshal":
		if sessionpass == "actionok":
			actioncards = selectedcard
			if actioncards == []:
				# if actioncount == 2:
				# 	notify("action over")
				# 	clearaction(1)
				# else:
				# 	actioncount += 1
				# 	sessionpass = ""
				remoteCall(players[1], "action", ["marshal",1])
				return
			else:
				setGlobalVariable("actioncancel", "0")
				actioncard = actioncards[0]
				sessionpass = ""
				remoteCall(players[1], "checkaction", [actioncard,"marshalaction"])
		else:
			checkactionattach("marshal")
			if sessionpass == "":
				intoaction(actionattach,actioncount,"marshal")
				return

def checkaction(actioncard,repass):
	mute()
	global interruptcancelcard
	global interruptcancelplayer
	global inserttarget
	global interruptcancelok
	global interruptcanceledcard
	global mainpass
	global leavecardtype
	global sessionpass

	sessionpass = ""
	debug(checkcountercharater(actioncard))
	if checkcountercharater(actioncard):
		interruptcancelcard = actioncard
		interruptcancelplayer = otherplayer
		inserttarget = interruptcancelcard
		mainpass = repass
		interruptcancelok = 1
		remoteCall(otherplayer,"savetargetinserttarget",[savetarget,inserttarget,interruptcancelcard,interruptcancelplayer,interruptcancellastcard,interruptcanceledcard,interruptcancelok,saveactionplayer,mainpass])
		remoteCall(me, "interruptevent", ["interruptcancel",2])
	else:
		remoteCall(otherplayer,"actionforability",[actioncard,repass])

def intoaction(cards,count,sepass):
	mute()
	global recount
	sessionpass = ""
	targetTuple = [d for d in checkactionattach(sepass)]
	if getGlobalVariable("marshalphase") != "0" and str(me._id) == getGlobalVariable("activeplayer"):selectcardnext(targetTuple,sepass,table,[],me,2,actionstyle = 1)
	elif getGlobalVariable("marshalphase") != "0" and str(me._id) != getGlobalVariable("activeplayer"):selectcardnext(targetTuple,sepass,table,[],me,1,actionstyle = 1)
	elif sepass in("marshal","general","dominance","standing","taxation"):selectcardnext(targetTuple,sepass,table,[],me,1,actionstyle = 1)
	else:selectcardnext(targetTuple,sepass,table,[],me,1)
	recount = count

def delactioncard(card):
	mute()
	global actioncardlimit
	global actionattach
	c = 0
	if not actioncardlimit.has_key(card._id):
		actioncardlimit[card._id] = 1
	else:actioncardlimit[card._id] += 1
	
	for d in actionchallenge:
		if card.model == actionchallenge[d][1]:
			if actioncardlimit[card._id] == actionchallenge[d][5]:
				del actionattach[card._id]
				c = 1
	if c == 0:
		actionattach[card._id] -= 1
		if actionattach[card._id] == 0:del actionattach[card._id]
	notify("action cancel.")



def actionforability(card,repass):
	mute()
	debug(card)
	global actionattach
	global actioncardlimit
	global sessionpass
	global intertreaction
	global cardtoaction
	global savetarget
	global addiconmil_turn
	global addiconint_turn
	global addiconpow_turn
	global subiconmil_turn
	global subiconint_turn
	global subiconpow_turn
	global returntohand_turn
	global disc_turn
	global plotcard
	global noprint_turn
	global mainpass
	sessionpass = ""
	c = 0
	f = 0
	g = 0
	h = 0
	debug(actionattach)
	card.arrow(card,False)
	if repass == "challengeaction":
		for d in actionchallenge:
			if card.model == actionchallenge[d][1] and card.controller == me:
				if actionchallenge[d][2] == "kneelhouse+2str":
					cardtoaction.markers[STR_Up] += 2
					notify("{}'s {} action {} gets +2 STR".format(me,card,cardtoaction))#WildlingHorde
				if actionchallenge[d][2] == "addinticon":
					cardtoaction.markers[IntrigueIcon] += 1
					notify("{}'s {} action {} gets Intrigue Icon".format(me,card,cardtoaction))#SelyseBaratheon
				if actionchallenge[d][2] == "adddef":
					if challengetype == 1:cardtoaction.highlight = MilitaryColor
					if challengetype == 2:cardtoaction.highlight = IntrigueColor
					if challengetype == 3:cardtoaction.highlight = PowerColor
					aftercalculatestand = eval(getGlobalVariable("aftercalculatestand"))
					aftercalculatestand.append(cardtoaction._id)
					setGlobalVariable("aftercalculatestand", str(aftercalculatestand))
					notify("{}'s {} action {} participating as a defender".format(me,card,cardtoaction))#OursistheFury
				if actionchallenge[d][2] == "dischand":
					remoteCall(otherplayer, "handview", ['all'])
					list = []
					for cardhand in otherplayer.hand:
						list.append(cardhand)
					dlg = cardDlg(list)
					dlg.title = "These cards are in your table:"
					dlg.text = "Declares at least 1 card to disc."
					dlg.min = 1
					dlg.max = 1
					cards = dlg.show()
					if cards != None:
						remoteCall(otherplayer, "disc", [cards[0]])
						notify("{}'s {} action discard {} from {} hand".format(me,card,cards[0],otherplayer))#SeenInFlames
					remoteCall(otherplayer, "handview", ['me'])
				if actionchallenge[d][2] == "addstr":
					strup = 1
					if fplay(1) == me:strup = 2
					cardtoaction.markers[STR_Up] += strup
					notify("{}'s {} action {} gets +{} STR".format(me,card,cardtoaction,strup))#IronFleetScout
				if actionchallenge[d][2] == "ignorestr":
					ignorestr = eval(getGlobalVariable("ignorestr"))
					ignorestr.append(cardtoaction._id)
					setGlobalVariable("ignorestr", str(ignorestr))
					notify("{}'s {} action {} does not contribute its STR to the challenge".format(me,card,cardtoaction))#TheKrakensGrasp
				if actionchallenge[d][2] == "kneelhousereturnhand":
					remoteCall(otherplayer,"returncard",[cardtoaction])
					notify("{}'s {} action return {} into {}'s hand.".format(me,card,cardtoaction,otherplayer))#TheThingsIDoForLove
				if actionchallenge[d][2] == "drawstark":
					if me.isInverted: cardtoaction.moveToTable(150,-230)
					else: cardtoaction.moveToTable(-130,130)
					notify("{} reveal {}.".format(me,cardtoaction))
					if cardtoaction.Faction == "Stark.":
						cardtoaction.moveTo(me.hand)
						notify("{}'s {} action put {} into {}'s hand.".format(me,card,cardtoaction,me))#GatesofWinterfell
					else:
						cardtoaction.moveTo(me.deck)
						cardtoaction.index = 0
				if actionchallenge[d][2] == "addstrdraw":
					cardtoaction.markers[STR_Up] += 2
					aftercalculatedraw = eval(getGlobalVariable("aftercalculatedraw"))
					aftercalculatedraw.append(cardtoaction._id)
					setGlobalVariable("aftercalculatedraw", str(aftercalculatedraw))
					debug(getGlobalVariable("aftercalculatedraw"))
					notify("{}'s {} action {} gets +2 STR.".format(me,card,cardtoaction))#FortheNorth
				if actionchallenge[d][2] == "addclaim":
					notify("{}'s {} action raise the claim value by 1.".format(me,card))#WinterIsComing
				if actionchallenge[d][2] == "burn":
					cardtoaction.markers[Burn] += 1
					notify("{}'s {} action {} gets -4 STR".format(me,card,cardtoaction))#Dracarys
					for cards in table:
						cards.target(False)
					if int(cardtoaction.strength) + cardtoaction.markers[STR_Up] - cardtoaction.markers[Burn]*4 <= 0:
						f = 1
						savetarget = cardtoaction
				if actionchallenge[d][2] == "returndead":
					if "Hatchling." in cardtoaction.Traits:
						if me.isInverted: cardtoaction.moveToTable(150,-230)
						else: cardtoaction.moveToTable(-130,130)
						notify("{}'s {} action put {} into play".format(me,card,cardtoaction))#FireandBlood
					else:
						cardtoaction.moveTo(me.deck)
						me.deck.shuffle()
						notify("{}'s {} action shuffle {} back into {}'s' deck".format(me,card,cardtoaction,me))#FireandBlood
				if actionchallenge[d][2] == "addstr3":
					cardtoaction.markers[STR_Up] += 3
					notify("{}'s {} action {} gets +3 STR.".format(me,card,cardtoaction))#MargaeryTyrell
				if actionchallenge[d][2] == "attaddstr3":
					cardtoaction.markers[STR_Up] += 3
					notify("{}'s {} action {} gets +3 STR.".format(me,card,cardtoaction))#Heartsbane
				if actionchallenge[d][2] == "standremovechallenge":
					cardtoaction.orientation = 0
					cardtoaction.highlight = None
					notify("{}'s {} action Stand {} and remove it from the challenge.".format(me,card,cardtoaction))#Highgarden
				if actionchallenge[d][2] == "3playeraddstr2":
					for addcard in cardtoaction:
						addcard.markers[STR_Up] += 2
						notify("{}'s {} action {} gets +2 STR.".format(me,card,addcard))#GrowingStrong
				if actionchallenge[d][2] == "choosechallenge":
					choiceList = ['Military', 'Intrigue', 'Power']
					colorList = ['#ae0603' ,'#006b34','#1a4d8f']
					choice = askChoice("Which challenge do you want to cannot initiate?", choiceList,colorList)
					if choice == 0:
						actionforability(card,repass)
						return
					if choice == 1:notify("{}'s {} action name a Military challenge.".format(me,card))#OlennasInformant
					if choice == 2:notify("{}'s {} action name a Intrigue challenge.".format(me,card))#OlennasInformant
					if choice == 3:notify("{}'s {} action name a Power challenge.".format(me,card))#OlennasInformant
				if actionchallenge[d][2] == "removechallenge":
					card.target(False)
					cardtoaction.highlight = None
					notify("{}'s {} action remove {} from the challenge.".format(me,card,cardtoaction))#AreoHotah

				cardtoaction == []
				if not actioncardlimit.has_key(card._id):
					actioncardlimit[card._id] = 1
				else:actioncardlimit[card._id] += 1
				if actioncardlimit[card._id] == actionchallenge[d][4]:
					del actionattach[card._id]
					c = 1
		if c == 0:
			actionattach[card._id] -= 1
			if actionattach[card._id] == 0:del actionattach[card._id]
		if f == 1:
			savetarget.highlight = miljudgecolor
			setGlobalVariable("chaevent", str(me._id))
			miljudgementfinish([savetarget],1)
			remoteCall(otherplayer, "miljudgementfinish", [[savetarget],1])
			remoteCall(otherplayer, "interruptevent", ["miljudgementfp",2])
		else:
			remoteCall(otherplayer, "action", ["challenge",1])
	if repass in ("generalaction","dominanceaction","marshalaction"):
		for d in generalaction:
			if card.model == generalaction[d][1] and card.controller == me:
				if generalaction[d][2] == "addlan":
					cardintable(cardtoaction,"Character")
					notify("{}'s {} action put {} into play".format(me,card,cardtoaction))#HearMeRoar
					disc_turn.append(cardtoaction)
				if generalaction[d][2] == "add5returnme":
					uniquecards = []
					dc = 0
					for u in table:
						if u.controller == me and u.unique == "Yes" and u.filter != WaitColor and u._id != cardtoaction._id:
							uniquecards.append(u.name)
							if cardtoaction.name in uniquecards: 
								cost=0
								dc = 1   #Duplicates
								x,y = u.position
								break
					if dc == 1:
						if me.isInverted: 
							cardtoaction.moveToTable(x-8,y-8)
						else:
							cardtoaction.moveToTable(x+8,y+8)
						cardtoaction.filter = "#005c3521"
						cardtoaction.sendToBack()
						notify("{}'s {} action put {}'s duplicate into play".format(me,card,cardtoaction))#ArianneMartell
					else:
						cardintable(cardtoaction,"Character")
						card.moveTo(me.hand)
						notify("{}'s {} action put {} into play,{} return {}'s Hand".format(me,card,cardtoaction,card,me))#ArianneMartell
				if generalaction[d][2] == "1goldicon":
					choiceList = ['Military', 'Intrigue', 'Power']
					colorList = ['#ae0603' ,'#006b34','#1a4d8f']
					choice = askChoice("Which challenge do you want select?", choiceList,colorList)
					if choice == 0:
						actionforability(card,repass)
						return
					if choice == 1:
						cardmarkers(card,"milicon",1)
						addiconmil_turn.append(card)
						notify("{}'s {} action get a Military icon until the end of the phase.".format(me,card))#EdricDayne
					if choice == 2:
						cardmarkers(card,"inticon",1)
						addiconint_turn.append(card)
						notify("{}'s {} action get a Intrigue icon until the end of the phase.".format(me,card))#EdricDayne
					if choice == 3:
						cardmarkers(card,"powicon",1)
						addiconpow_turn.append(card)
						notify("{}'s {} action get a Power icon until the end of the phase.".format(me,card))#EdricDayne
				if generalaction[d][2] == "loseicon":
					cardmarkers(cardtoaction,"milicon",-1)
					cardmarkers(cardtoaction,"inticon",-1)
					cardmarkers(cardtoaction,"powicon",-1)
					subiconmil_turn.append(cardtoaction)
					subiconint_turn.append(cardtoaction)
					subiconpow_turn.append(cardtoaction)
					notify("{}'s {} action {} loses a [MIL], an [INT] and a [POW] icon.".format(me,card,cardtoaction))#Confinement
				if generalaction[d][2] == "d1cg1g":
					me.counters['Gold'].value += 1
					# for incomecard in table:
					# 	if incomecard.controller == me and incomecard.type == "Plot" and incomecard.filter == None:
					# 		incomecard.markers[Gold] += 1
					notify("{}'s {} action gain 1 gold.".format(me,card))#OldForestHunter
				if generalaction[d][2] == "standlocation":
					cardtoaction.orientation = 0
					card.moveTo(me.piles['Dead pile'])
					notify("{}'s {} action Sacrifice {} to stand {}.".format(me,card,card,cardtoaction))#VeteranBuilder
				if generalaction[d][2] == "2gstandc":
					card.arrow(cardtoaction,False)
					cardtoaction.orientation = 0
					notify("{}'s {} action pay 2 gold to stand {}.".format(me,card,cardtoaction))#MagisterIllyrio
				if generalaction[d][2] == "standlady":
					cardtoaction.orientation = 0
					card.moveTo(me.piles['Dead pile'])
					notify("{}'s {} action Sacrifice {} to stand {}.".format(me,card,card,cardtoaction))#Handmaiden
				if generalaction[d][2] == "standtc":
					cardtoaction.orientation = 0
					notify("{}'s {} action to stand {}.".format(me,card,cardtoaction))#WakingtheDragon
					returntohand_turn.append(cardtoaction)
				if generalaction[d][2] == "5t3b":
					colorList = ['#1a4d8f','#ae0603']
					choiceList = ['{}'.format(me),'{}'.format(players[1])]
					choice = askChoice("select {}'s target.".format(card.name), choiceList,colorList)
					if choice == 0:
						actionforability(card,repass)
						return
					if choice == 1:
						if len(me.deck) >= 5:top5list = me.deck.top(5)
						else:top5list = me.deck.top(len(me.deck))
					if choice == 2:
						if len(players[1].deck) >= 5:top5list = players[1].deck.top(5)
						else:top5list = players[1].deck.top(len(players[1].deck))
					dlg = cardDlg(top5list, [])
					dlg.title = "These cards are you can moved"
					dlg.text = "place up to 3 of those cards on the bottom of that deck, and the others on top, in any order. click close button if none or cancel."
					dlg.label = "Top of the deck"
					dlg.bottomLabel = "bottom of the deck"
					dlg.min = 2
					dlg.max = 5
					cardmove = dlg.show()
					if cardmove != None:
						dlg.list.reverse()
						if choice == 1:
							remoteCall(me, "movedeckbottom", [dlg.bottomList])
							remoteCall(me, "movedeckbottom", [dlg.list])
							notify("{}'s {} action reorder {}'deck.".format(me,card,me))#TheBearandtheMaidenFair
						if choice == 2:
							remoteCall(otherplayer, "movedeckbottom", [dlg.bottomList])
							remoteCall(otherplayer, "movedecktop", [dlg.list])
							notify("{}'s {} action reorder {}'deck.".format(me,card,players[1]))#TheBearandtheMaidenFair
					else:notify("{}'s {} action cancel.".format(me,card))#TheBearandtheMaidenFair
				if generalaction[d][2] == "kneelfaction":
					for cardk in table:
						if cardk.type == "Faction" and cardk.controller == me:
							cardtoaction = cardk
					me.setGlobalVariable("reduceloyal_turn", "1")
					notify("{}'s {} action kneel {} to reduce the cost of the next loyal card marshal or play this phase by 1.".format(me,card,cardtoaction))#Fealty
				if generalaction[d][2] == "standicon":
					cardtoaction.orientation = 0
					card.markers[standIcon] = 0
					notify("{}'s {} action to stand {}.".format(me,card,cardtoaction))#PowerBehindtheThrone
				if generalaction[d][2] == "searchbrs":
					cards = None
					choiceList = ['Builder', 'Ranger', 'Steward']
					colorList = ['#ae0603' ,'#006b34','#1a4d8f']
					choice = askChoice("Which type do you want to select?", choiceList,colorList)
					if choice == 1:searcht = 'Builder'
					if choice == 2:searcht = 'Ranger'
					if choice == 3:searcht = 'Steward'
					if choice == 0:
						actionforability(card,repass)
						return
					if len(me.deck) < me.counters['Reserve'].value:listcount = len(me.deck)
					else:listcount = me.counters['Reserve'].value
					for c in me.deck.top(listcount):
						if searcht in c.Traits:
							searchok = 1
					dlg = cardDlg(me.deck.top(listcount))
					dlg.title = "These cards are in your deck:"
					dlg.text = "select Builder or Ranger or Steward card add it to your hand."
					dlg.min = 0
					dlg.max = listcount
					cards = dlg.show()
					if cards != [] and cards != None:
						for a in cards:
							debug(a.Type)
							debug(a.Traits)
							if searcht in a.Traits:
								debug(a.Traits)
								cardintable(a,"Character")
								plotcard.append(a)
								a.highlight = showColor
								#cards[0].moveTo(me.hand)
								me.deck.shuffle()
								notify("{}'s {} action, add {} to {} hand.".format(me,card,a,me))#BuildingOrders
						sessionpass = repass
						remoteCall(me, "setTimer", [me,"actionshow",table])
						g = 1
					else:
						if searchok == 1:
							if confirm("There is a {} card in these cards, select again？".format(searcht)):
								actionforability(card,repass)
								return
						else:notify("search failed")
				if generalaction[d][2] == "addusedplotgold":
					for cardk in table:
						if cardk.type == "Faction" and cardk.controller == me:
							cardtoaction = cardk
					me.counters['Gold'].value += len(usedplot)
					notify("{}'s {} action kneel {} to gain {} gold.".format(me,card,cardtoaction,len(usedplot)))#InDoransName
				if generalaction[d][2] == "searchwolf":
					cards = None
					listcount = len(me.deck)
					for c in me.deck.top(listcount):
						if ("Direwolf.") in c.Traits:
							searchok = 1
					dlg = cardDlg(me.deck.top(listcount))
					dlg.title = "These cards are in your deck:"
					dlg.text = "select 1 Direwolf card add it to your hand."
					dlg.min = 0
					dlg.max = 1
					cards = dlg.show()
					if cards != [] and cards != None:
						if ("Direwolf.") in cards[0].Traits:
							cardintable(cards[0],"Character")
							plotcard = cards[0]
							cards[0].highlight = showColor
							#cards[0].moveTo(me.hand)
							me.deck.shuffle()
							notify("{}'s'{} action, add {} to {} hand.".format(me,card,cards[0],me))#WolfDreams
						sessionpass = repass
						remoteCall(me, "setTimer", [me,"actionshowall",table])
						g = 1
					else:
						if searchok == 1:
							if confirm("There is a Direwolf card in these cards, select again？"):
								actionforability(card,repass)
								return
						else:notify("search failed")
				if generalaction[d][2] == "noprint":
					cardtoaction.markers[TokenRed] += 1
					remoteCall(cardtoaction.controller, "noprintcard", [cardtoaction])
					notify("{}'s {} action treat {} printed text box as if it were blank (except for Traits).".format(me,card,cardtoaction))#Nightmares
				if generalaction[d][2] == "changecontroll":
					cardmarkers(cardtoaction,"str",2)
					cx,cy = cardtoaction.position
					if me.isInverted:x,y = attachat(cx-15,cy-15,table)
					else:x,y = attachat(cx+15,cy+15,table)
					card.moveToTable(x,y)
					card.sendToBack()
					attachcard = eval(getGlobalVariable("attachmodify"))
					if not attachcard.has_key(card._id):
						attachcard[card._id] = cardtoaction._id
					else:
						for subcard in table:
							if subcard._id == attachcard[card._id]:cardmarkers(subcard,"str",-2)
					attachcard[card._id] = cardtoaction._id
					setGlobalVariable("attachmodify",str(attachcard))
					if cardtoaction.name == "Sansa Stark":
						if cardtoaction.orientation == 0:
							remoteCall(cardtoaction.controller, "kneel", [cardtoaction])
					notify("{}'s {} action treat {} printed text box as if it were blank (except for Traits).".format(me,card,cardtoaction))#Nightmares
				if generalaction[d][2] == "4cardchoose2":
					setGlobalVariable("actionplay",str(me._id))
					mainpass = repass
					remoteCall(players[1], "move4card", [1])
					g = 1
				cardtoaction == []
				if not actioncardlimit.has_key(card._id):
					actioncardlimit[card._id] = 1
				else:actioncardlimit[card._id] += 1
				if actioncardlimit[card._id] == generalaction[d][4]:
					debug(actionattach)
					del actionattach[card._id]
					c = 1
		for d in dominanceaction:
			if card.model == dominanceaction[d][1] and card.controller == me:
				if dominanceaction[d][2] == "returndraw1":
					notify("{}'s {} action draw 1 card".format(me,card))#MessengerRaven
					card.moveTo(me.hand)
					draw(me.deck)
				if dominanceaction[d][2] == "disctop":
					kneel(card)
					remoteCall(players[1], "ticklerdisc", [card])#TheTickler
					g = 1
				cardtoaction == []
				if not actioncardlimit.has_key(card._id):
					actioncardlimit[card._id] = 1
				else:actioncardlimit[card._id] += 1
				if actioncardlimit[card._id] == dominanceaction[d][4]:
					debug(actionattach)
					del actionattach[card._id]
					c = 1
		for d in marshalaction:
			if card.model == marshalaction[d][1] and card.controller == me:
				if marshalaction[d][2] == "reduce3s":
					reduceint = int(me.getGlobalVariable("reduce_character_turn")) + 3
					me.setGlobalVariable("reduce_character_turn", str(reduceint))
					notify("{}'s {} action reduce the cost of the next character you marshal this phase by 3.".format(me,card))#TheKingsroad
				if marshalaction[d][2] == "reduce1Baratheoncharacter":
					reduceint = int(me.getGlobalVariable("reduce_Baratheon_character_turn")) + 1
					me.setGlobalVariable("reduce_Baratheon_character_turn", str(reduceint))
					notify("{}'s {} action reduce the cost of the next [Baratheon] character you marshal this phase by 1.".format(me,card))#DragonstoneFaithful
				if marshalaction[d][2] == "reduce1Baratheoncard":
					reduceint = int(me.getGlobalVariable("reduce_Baratheon_card_turn")) + 1
					me.setGlobalVariable("reduce_Baratheon_card_turn", str(reduceint))
					notify("{}'s {} action reduce the cost of the next [Baratheon] card you marshal this phase by 1.".format(me,card))#DragonstonePort
				if marshalaction[d][2] == "reduce1Greyjoycharacter":
					reduceint = int(me.getGlobalVariable("reduce_Greyjoy_character_turn")) + 1
					me.setGlobalVariable("reduce_Greyjoy_character_turn", str(reduceint))
					notify("{}'s {} action reduce the cost of the next [Greyjoy] character you marshal this phase by 1.".format(me,card))#IronIslandsFishmonger
				if marshalaction[d][2] == "reduce1Greyjoycard":
					reduceint = int(me.getGlobalVariable("reduce_Greyjoy_card_turn")) + 1
					me.setGlobalVariable("reduce_Greyjoy_card_turn", str(reduceint))
					notify("{}'s {} action reduce the cost of the next [Greyjoy] card you marshal this phase by 1.".format(me,card))#SeaTower
				if marshalaction[d][2] == "reduce1Lannistercharacter":
					reduceint = int(me.getGlobalVariable("reduce_Lannister_character_turn")) + 1
					me.setGlobalVariable("reduce_Lannister_character_turn", str(reduceint))
					notify("{}'s {} action reduce the cost of the next [Lannister] character you marshal this phase by 1.".format(me,card))#LannisportMerchant
				if marshalaction[d][2] == "reduce1Lannistercard":
					reduceint = int(me.getGlobalVariable("reduce_Lannister_card_turn")) + 1
					me.setGlobalVariable("reduce_Lannister_card_turn", str(reduceint))
					notify("{}'s {} action reduce the cost of the next [Lannister] card you marshal this phase by 1.".format(me,card))#WesternFiefdom
				if marshalaction[d][2] == "reduce1Martellcharacter":
					reduceint = int(me.getGlobalVariable("reduce_Martell_character_turn")) + 1
					me.setGlobalVariable("reduce_Martell_character_turn", str(reduceint))
					notify("{}'s {} action reduce the cost of the next [Martell] character you marshal this phase by 1.".format(me,card))#DesertScavenger
				if marshalaction[d][2] == "reduce1Martellcard":
					reduceint = int(me.getGlobalVariable("reduce_Martell_card_turn")) + 1
					me.setGlobalVariable("reduce_Martell_card_turn", str(reduceint))
					notify("{}'s {} action reduce the cost of the next [Martell] card you marshal this phase by 1.".format(me,card))#BloodOrangeGrove
				if marshalaction[d][2] == "reduce1NWcharacter":
					reduceint = int(me.getGlobalVariable("reduce_NW_character_turn")) + 1
					me.setGlobalVariable("reduce_NW_character_turn", str(reduceint))
					notify("{}'s {} action reduce the cost of the next [Night's Watch] character you marshal this phase by 1.".format(me,card))#StewardattheWall
				if marshalaction[d][2] == "reduce1Starkcharacter":
					reduceint = int(me.getGlobalVariable("reduce_Stark_character_turn")) + 1
					me.setGlobalVariable("reduce_Stark_character_turn", str(reduceint))
					notify("{}'s {} action reduce the cost of the next [Stark] character you marshal this phase by 1.".format(me,card))#Winterfellteward
				if marshalaction[d][2] == "reduce1Starkcard":
					reduceint = int(me.getGlobalVariable("reduce_Stark_card_turn")) + 1
					me.setGlobalVariable("reduce_Stark_card_turn", str(reduceint))
					notify("{}'s {} action reduce the cost of the next [Stark] card you marshal this phase by 1.".format(me,card))#HeartTreeGrove
				if marshalaction[d][2] == "reduce1Targaryencharacter":
					reduceint = int(me.getGlobalVariable("reduce_Targaryen_character_turn")) + 1
					me.setGlobalVariable("reduce_Targaryen_character_turn", str(reduceint))
					notify("{}'s {} action reduce the cost of the next [Targaryen] character you marshal this phase by 1.".format(me,card))#TargaryenLoyalist
				if marshalaction[d][2] == "reduce1Targaryencard":
					reduceint = int(me.getGlobalVariable("reduce_Targaryen_card_turn")) + 1
					me.setGlobalVariable("reduce_Targaryen_card_turn", str(reduceint))
					notify("{}'s {} action reduce the cost of the next [Targaryen] card you marshal this phase by 1.".format(me,card))#IllyriosEstate
				if marshalaction[d][2] == "reduce1Tyrellcharacter":
					reduceint = int(me.getGlobalVariable("reduce_Tyrell_character_turn")) + 1
					me.setGlobalVariable("reduce_Tyrell_character_turn", str(reduceint))
					notify("{}'s {} action reduce the cost of the next [Tyrell] character you marshal this phase by 1.".format(me,card))#GardenCaretake
				if marshalaction[d][2] == "reduce1Tyrellcard":
					reduceint = int(me.getGlobalVariable("reduce_Tyrell_card_turn")) + 1
					me.setGlobalVariable("reduce_Tyrell_card_turn", str(reduceint))
					notify("{}'s {} action reduce the cost of the next [Tyrell] card you marshal this phase by 1.".format(me,card))#RoseGarden


				if marshalaction[d][2] == "discattachmentc":
					remoteCall(cardtoaction.controller, "disc", [cardtoaction])
					notify("{}'s {} action disc {}.".format(me,card,cardtoaction))#MaesterCressen
				if marshalaction[d][2] == "kneel4cadd1power":
					for cardkneel in cardtoaction:
						remoteCall(cardkneel.controller, "kneel", [cardkneel])
						notify("{}'s {} action kneel {}.".format(me,card,cardkneel))#ConsolidationofPower
					for cardaddpow in table:
						if cardaddpow in cardtoaction:h = 1
				if marshalaction[d][2] == "kneel2location":
					remoteCall(cardtoaction.controller, "kneel", [cardtoaction])
					notify("{}'s {} action kneel {}.".format(me,card,cardtoaction))#LordsportShipwright
				if h == 0:cardtoaction == []
				if not actioncardlimit.has_key(card._id):
					actioncardlimit[card._id] = 1
				else:actioncardlimit[card._id] += 1
				if actioncardlimit[card._id] == marshalaction[d][4]:
					debug(actionattach)
					del actionattach[card._id]
					c = 1

			if card.model == marshalaction[d][1] and card.controller != me:
				if marshalaction[d][2] == "controllb":
					card.controller = me
					remoteCall(players[1], "cardintable", [card,"Character",me,1])
					notify("{} take control of {}.".format(me,card))#Bronn
				if not actioncardlimit.has_key(card._id):
					actioncardlimit[card._id] = 1
				else:actioncardlimit[card._id] += 1
				if actioncardlimit[card._id] == marshalaction[d][4]:
					debug(actionattach)
					del actionattach[card._id]
					c = 1
		if c == 0:
			actionattach[card._id] -= 1
			if actionattach[card._id] == 0:del actionattach[card._id]
		debug(repass)
		if h == 1:
			targetTuple = [card._id for card in table if card in cardtoaction]
			cardtoaction = []
			selectcardnext(targetTuple,"selectadd1power",table,[],"",1)
			return
		if g == 0:
			if repass == "marshalaction":remoteCall(players[1], "action", ["marshal",1])
			if repass == "generalaction":remoteCall(players[1], "action", ["general",1])
			if repass == "dominanceaction":remoteCall(players[1], "action", ["dominance",1])

def move4card(counter):
	mute()
	i = -800
	for count in range(0,4):
		if len(me.deck) > 0:
			movecard = me.deck.top()
			if me.isInverted:movecard.moveToTable(i,-100)
			else:movecard.moveToTable(i,10)
			movecard.highlight = showColor
			i += 80
	if counter == 1:
		debug(count)
		remoteCall(players[1], "move4card", [2])
	if counter == 2:
		remoteCall(fplay(1), "select1card", [])

def select1card():
	mute()
	me.setGlobalVariable("setupOk","")
	selectlist = checkcardid(deck = table,player = me,highlight = '#ffa6f8')
	selectcardnext(selectlist,"select1cardme",table,[])

def select1cardover(count):
	mute()
	global sessionpass
	sessionpass = ""
	for card in table:
		debug(card.highlight)
		if card.highlight == showColor and card.controller == me:
			card.moveTo(me.deck)
			card.highlight = None
		if card.highlight == standcolor and card.controller == me:
			card.moveTo(me.hand)
			card.highlight = None
	me.deck.shuffle()
	if count == 1:
		remoteCall(players[1], "select1cardover", [2])
	if count == 2:
		if getGlobalVariable("actionplay") == str(me._id):backtoaction()
		else:remoteCall(players[1], "backtoaction", [])


def backtoaction():
	mute()
	global mainpass
	if mainpass == "marshalaction":remoteCall(players[1], "action", ["marshal",1])
	if mainpass == "generalaction":remoteCall(players[1], "action", ["general",1])
	if mainpass == "dominanceaction":remoteCall(players[1], "action", ["dominance",1])
	setGlobalVariable("actionplay","")
	mainpass = ""

def getnoprint(card):
	mute()
	global noprint_turn
	noprint_turn.append(card)

def ticklerdisc(cardcation):
	mute()
	disccard = me.deck.top()
	disc(disccard)
	notify("{}'s {} action disc {}".format(players[1],cardcation,disccard))#TheTickler
	for cardd in table:
		if cardd.name == disccard.name:
			targetTuple = [card._id for card in table if card.name == disccard.name]
			remoteCall(players[1], "selectcardnext", [targetTuple,"ticklerdisc",table,[],"",1])
			# selectcardnext(targetTuple,"ticklerdisc",table,[],"",1)
			return
	remoteCall(players[1], "action", ["dominance",1])
		
def handview(vs):
	mute()
	me.hand.visibility = vs

def movedeckbottom(cardlist):
	mute()
	for card in cardlist:
		card.moveToBottom(me.Deck)

def movedecktop(cardlist):
	mute()
	for card in cardlist:
		card.moveTo(me.Deck)

def nextselectcard(selectlist,spass,deck = table,):
	mute()
	global sessionpass
	for card in deck:
		card.target(False)
	targetTuple = (selectlist, me._id)
	setGlobalVariable("tableTargets", str(targetTuple))
	setGlobalVariable("selectmode", "1")
	sessionpass = spass
	notify("**{} into selectmode**".format(me))
	return

def selectcardnext(selectlist,spass,deck = table,actioncard = [],player = "",button = 0,mode = 1,interrupt = 0,actionstyle = 0):
	mute()
	global sessionpass
	global interruptsessionpass
	global cardtmp
	attach = eval(getGlobalVariable("attachmodify"))
	for card in table:
		if player == "":
			if card.filter in (targetcardcolor,cantselectcardclor):card.filter = None
		else:
			if card.filter in (targetcardcolor,cantselectcardclor) and card.controller == player:card.filter = None
	for card in me.hand:
		if card.filter in (targetcardcolor,cantselectcardclor) and card.controller == player:card.filter = None

	if actioncard != []:
		cardtmp = actioncard
		cardtmp.filter = sourcecardcfilter
	else:cardtmp = []
	
	targetTuple = (selectlist, me._id)
	debug(selectlist)
	if me.getGlobalVariable("setupOk") in ("4","5") or me.getGlobalVariable("plotOk") == "ok" or me.getGlobalVariable("drawOk") == "ok":me.setGlobalVariable("tableTargets", str(targetTuple))
	else:setGlobalVariable("tableTargets", str(targetTuple))
	setGlobalVariable("selectmode", str(mode))
	if interrupt == 0:sessionpass = spass
	else:interruptsessionpass = spass
	for card in table:
		if card.type not in ("Internal"):
			if card._id not in targetTuple[0] and not attach.has_key(card._id):
				if player != "":
					if card.controller == player:
						if actioncard != []:
							if card._id != actioncard._id:card.filter = cantselectcardfilter
						else:card.filter = cantselectcardfilter
				else:
					if actioncard != []:
						if card._id != actioncard._id:card.filter = cantselectcardfilter
					else:card.filter = cantselectcardfilter
	for card in me.hand:
		if card._id not in targetTuple[0]:
			if actioncard != []:
				if card._id != actioncard._id:card.filter = cantselectcardfilter
			else:card.filter = cantselectcardfilter
	if button == 0:
		nn = 0
		for cardn in table:
			if cardn.name == "nextbutton" and cardn.controller == me:
				nn = 1
			if cardn.name == "passnextbutton" and cardn.controller == me:
				cardn.delete()#delete nextbutton
		if nn == 0:
			if me.isInverted:table.create("584a37d7-5a30-4018-ae21-0ad325203fa0",-375,-250)
			else:table.create("584a37d7-5a30-4018-ae21-0ad325203fa0",-375,200)
	if button == 1:
		if actionstyle == 1:
			if me.isInverted:table.create("cf4c922b-0316-43b1-9d2b-4926b78621af",-375,-250)
			else:table.create("cf4c922b-0316-43b1-9d2b-4926b78621af",-375,200)
		else:
			if me.isInverted:table.create("584a37d7-5a30-4018-ae21-0ad325203fa0",-375,-250)
			else:table.create("584a37d7-5a30-4018-ae21-0ad325203fa0",-375,200)
	if button == 2:
		if me.isInverted:table.create("f5fb1824-1d0e-4a4a-a431-46e0a06f1a42",-375,-250)
		else:table.create("f5fb1824-1d0e-4a4a-a431-46e0a06f1a42",-375,200)
		# if me.isInverted:table.create("f5fb1824-1d0e-4a4a-a431-46e0a06f1a42",-280,-250)
		# else:table.create("f5fb1824-1d0e-4a4a-a431-46e0a06f1a42",-280,200)
	me.setGlobalVariable("actionstyle", str(actionstyle))
	notify("**{} into selectmode**".format(me))
	return

def clearfilter(player = ""):
	mute()
	for card in table:
		if player == "":
			if card.filter in (targetcardcolor,cantselectcardclor,sourcecardcolor):card.filter = None
		else:
			if card.filter in (targetcardcolor,cantselectcardclor,sourcecardcolor) and card.controller == player:card.filter = None
	for card in me.hand:
		if card.filter in (targetcardcolor,cantselectcardclor,sourcecardcolor):card.filter = None

def cardmarkers(card,marker,add):
	mute()
	if marker == "str":
		addmodify = card.markers[STR_Up] - card.markers[STR_Sub] + add
		debug(addmodify)
		if addmodify > 0:
			card.markers[STR_Up] = addmodify
			card.markers[STR_Sub] = 0
		if addmodify < 0:
			card.markers[STR_Up] = 0
			card.markers[STR_Sub] = abs(addmodify)
		if addmodify == 0:
			card.markers[STR_Up] = 0
			card.markers[STR_Sub] = 0
	if marker == "milicon":
		addmodify = card.markers[MilitaryIcon] - card.markers[subMilitaryIcon] + add
		debug(addmodify)
		if addmodify > 0:card.markers[MilitaryIcon] = addmodify
		if addmodify < 0:card.markers[subMilitaryIcon] = abs(addmodify)
		if addmodify == 0:
			card.markers[MilitaryIcon] = 0
			card.markers[subMilitaryIcon] = 0
	if marker == "inticon":
		addmodify = card.markers[IntrigueIcon] - card.markers[subIntrigueIcon] + add
		debug(addmodify)
		if addmodify > 0:card.markers[IntrigueIcon] = addmodify
		if addmodify < 0:card.markers[subIntrigueIcon] = abs(addmodify)
		if addmodify == 0:
			card.markers[IntrigueIcon] = 0
			card.markers[subIntrigueIcon] = 0
	if marker == "powicon":
		addmodify = card.markers[PowerIcon] - card.markers[subPowerIcon] + add
		debug(addmodify)
		if addmodify > 0:card.markers[PowerIcon] = addmodify
		if addmodify < 0:card.markers[subPowerIcon] = abs(addmodify)
		if addmodify == 0:
			card.markers[PowerIcon] = 0
			card.markers[subPowerIcon] = 0

def checkchallengeicon(card,marker):
	mute()
	c = 0
	if marker == "milicon":
		if card.Military == "Yes":c = 1
		if card.markers[MilitaryIcon] - card.markers[subMilitaryIcon] + c > 0:return True
	if marker == "inticon":
		if card.Intrigue == "Yes":c = 1
		if card.markers[IntrigueIcon] - card.markers[subIntrigueIcon] + c > 0:return True
	if marker == "powicon":
		if card.Power == "Yes":c = 1
		if card.markers[PowerIcon] - card.markers[subPowerIcon] + c > 0:return True

def callplotleave(count):
	mute()
	plotleave(selectedcard,count)

def checkwinner(args):
	mute()
	if args.marker == "Power":
		i = 0 
		for card in table:
			if card.controller == me:
				i+=card.markers[Power]
		if i>=15:matchwin()
	# if args.marker == "Gold":
	# 	if args.card.model == "170f6c43-1cf5-460a-bd32-996d26dc0cd9":args.card.markers[STR_Up] += args.card.markers[Gold]-args.value
def matchwin(s = 0):
	mute()
	if getGlobalVariable("gameover") == "1":
		notify("game is already over")
		return
	#cn only
	# agendaa = ''
	# agendab = ''
	# if me.isInverted:
	# 	sidea = players[1].name
	# 	if s == 1:powera = 0
	# 	else:powera = players[1].counters['Power'].value
	# 	sideb = me.name
	# 	if s == 1:powerb = 15
	# 	else:powerb = me.counters['Power'].value
	# 	for card in table:
	# 		if card.type == "Faction":
	# 			if card.controller == me:factionb = card.name
	# 			else:factiona = card.name
	# 		if card.type == "Agenda":
	# 			if card.controller == me:agendab = card.name
	# 			else:agendaa = card.name
	# else:
	# 	sideb = players[1].name
	# 	if s == 1:powerb = 0
	# 	else:powerb = players[1].counters['Power'].value
	# 	sidea = me.name
	# 	if s == 1:powera = 15
	# 	else:powera = me.counters['Power'].value
	# 	for card in table:
	# 		if card.type == "Faction":
	# 			if card.controller == me:factiona = card.name
	# 			else:factionb = card.name
	# 		if card.type == "Agenda":
	# 			if card.controller == me:agendaa = card.name
	# 			else:agendab = card.name

	notify("{} is the winner".format(me))
	# webRead('http://agot.cceschool.com/action.php?winner={}&loser={}&sidea={}&factiona={}&agendaa={}&powera={}&sideb={}&factionb={}&agendab={}&powerb={}'.format(me.name,players[1].name,sidea,factiona,agendaa,powera,sideb,factionb,agendab,powerb), 5000)
	# notify("match result upload ok")
	setGlobalVariable("gameover","1")
	choiceList = ['You Win']
	colorList = ['#006b34']
	choice = askChoice("Game over", choiceList,colorList)

def defeat(group, x=0, y=0):
	mute()
	if getGlobalVariable("gameover") == "0":
		if confirm("want to surrender?"):remoteCall(players[1], "matchwin", [1])
	else:notify("game is already over")

def checkactionattach(checkpass):
	mute()
	global actionattach
	actionattach = {}
	actiongeneral(3)
	if checkpass == "dominance":
		actiondominance(3)
	if checkpass == "standing":
		actionstanding(3)
	if checkpass == "taxation":
		actiontaxation(3)
	if checkpass == "marshal":
		actionmarshal(3)
	actionattachtmp = actionattach.copy()
	debug("tmp")
	debug(actionattachtmp)
	for card in table:
		if card._id in actionattachtmp:
			for d in generalaction:
				if card.model == generalaction[d][1] and card.controller == me and generalaction[d][3] == "table":
					if "gold" in generalaction[d][5]:
						debug(generalaction[d][5][4])
						if me.counters['Gold'].value < int(generalaction[d][5][4]):
							actionattachtmp[card._id] -= 1
							if actionattachtmp[card._id] == 0:del actionattachtmp[card._id]
					if actioncardlimit.has_key(card._id) and actionattachtmp.has_key(card._id):
						if actioncardlimit[card._id] == generalaction[d][4]:
							del actionattachtmp[card._id]
	for card in table:
		if card._id in actionattachtmp:
			for d in marshalaction:
				if card.model == marshalaction[d][1] and card.controller == me and marshalaction[d][3] == "table":
					if "gold" in marshalaction[d][5]:
						debug(marshalaction[d][5][4])
						if me.counters['Gold'].value < int(marshalaction[d][5][4]):
							actionattachtmp[card._id] -= 1
							if actionattachtmp[card._id] == 0:del actionattachtmp[card._id]
					if actioncardlimit.has_key(card._id) and actionattachtmp.has_key(card._id):
						if actioncardlimit[card._id] == marshalaction[d][4]:
							del actionattachtmp[card._id]

	for card in table:
		if card._id in actionattachtmp:
			for d in dominanceaction:
				if card.model == dominanceaction[d][1] and card.controller == me and dominanceaction[d][3] == "table":
					if actioncardlimit.has_key(card._id) and actionattachtmp.has_key(card._id):
						if actioncardlimit[card._id] == dominanceaction[d][4]:
							del actionattachtmp[card._id]
	for card in me.hand:
		if card._id in actionattachtmp:
			for d in generalaction:
				if card.model == generalaction[d][1] and card.controller == me and generalaction[d][3] == "Hand":
					if card.type == "Event" and card.cost != "X":
						cost=int(card.Cost)
						if me.getGlobalVariable("firstevent") == "0":
							if checkpr(me) and card.type == "Event":
								cost=int(card.Cost)-1
						if card.loyal == "Yes":
							cost -= int(me.getGlobalVariable("reduceloyal_turn"))
						if me.counters['Gold'].value < cost:
							actionattachtmp[card._id] -= 1
							if actionattachtmp[card._id] == 0:del actionattachtmp[card._id]
					if actioncardlimit.has_key(card._id) and actionattachtmp.has_key(card._id):
						if actioncardlimit[card._id] == generalaction[d][4]:
							del actionattachtmp[card._id]
	for card in me.hand:
		if card._id in actionattachtmp:
			for d in dominanceaction:
				if card.model == dominanceaction[d][1] and card.controller == me and dominanceaction[d][3] == "Hand":
					if card.type == "Event" and card.cost != "X":
						cost=int(card.Cost)
						if me.getGlobalVariable("firstevent") == "0":
							if checkpr(me) and card.type == "Event":
								cost=int(card.Cost)-1
						if card.loyal == "Yes":
							cost -= int(me.getGlobalVariable("reduceloyal_turn"))
						if me.counters['Gold'].value < cost:
							actionattachtmp[card._id] -= 1
							if actionattachtmp[card._id] == 0:del actionattachtmp[card._id]
					if actioncardlimit.has_key(card._id) and actionattachtmp.has_key(card._id):
						if actioncardlimit[card._id] == dominanceaction[d][4]:
							del actionattachtmp[card._id]

	for card in me.hand:
		if card._id in actionattachtmp:
			for d in marshalaction:
				if card.model == marshalaction[d][1] and card.controller == me and marshalaction[d][3] == "Hand":
					if card.type == "Event" and card.cost != "X":
						cost=int(card.Cost)
						if me.getGlobalVariable("firstevent") == "0":
							if checkpr(me) and card.type == "Event":
								cost=int(card.Cost)-1
						if card.loyal == "Yes":
							cost -= int(me.getGlobalVariable("reduceloyal_turn"))
						if me.counters['Gold'].value < cost:
							actionattachtmp[card._id] -= 1
							if actionattachtmp[card._id] == 0:del actionattachtmp[card._id]
					if actioncardlimit.has_key(card._id) and actionattachtmp.has_key(card._id):
						if actioncardlimit[card._id] == marshalaction[d][4]:
							del actionattachtmp[card._id]
	if checkpass == "marshal":
		if str(me._id) == getGlobalVariable("activeplayer"):
			for card in me.hand:
				if card.type in("Character","Location","Attachment"):
					c = 0
					uniquecards = []
					for u in table:
						if u.controller == me and u.unique == "Yes":
							uniquecards.append(u.name)
							if card.name in uniquecards: 
								cost=0
								c = 1   #Duplicates
								x,y = u.position
								break
					if c == 1:
						if not actionattachtmp.has_key(card._id):
							actionattachtmp[card._id] = 1
						else:actionattachtmp[card._id] += 1
						continue
					if me.getGlobalVariable("firstlimit") != "0" and "Limited" in card.keywords:continue
					cost=int(card.Cost)
					if card.loyal == "Yes":
						cost -= int(me.getGlobalVariable("reduceloyal_turn"))
					if checkcardmodel("a28ec48c-ee57-4c6a-a940-b59c1aeff251") and me.getGlobalVariable("firstlocation") == "0":
						if card.type == "Location":
							cost -= 1
					if me.getGlobalVariable("firstll") == "1" and me.getGlobalVariable("firstcharacter") == "0":
						if card.type == "Character" and card.Traits.find('Lord') != -1 or card.Traits.find('Lady') != -1:
							debug(card)
							cost -= 2
					if me.getGlobalVariable("firstnobaratheonplayer") == "0":
						if checkrl(me) and card.type == "Character" and card.faction != "Baratheon.":
							cost -= 1
							if cost < 0:cost = 0
					if card.type == "Character":
						if me.getGlobalVariable("reduce_character_turn") != "0":
							cost -= int(me.getGlobalVariable("reduce_character_turn"))
							reduce_character_turn = 1
						if card.faction == "Stark.":
							if me.getGlobalVariable("reduce_Stark_character_turn") != "0":
								cost -= int(me.getGlobalVariable("reduce_Stark_character_turn"))
								reduce_Stark_character_turn = 1
						if card.faction == "Lannister.":
							if me.getGlobalVariable("reduce_Lannister_character_turn") != "0":
								cost -= int(me.getGlobalVariable("reduce_Lannister_character_turn"))
								reduce_Lannister_character_turn = 1
						if card.faction == "Greyjoy.":
							if me.getGlobalVariable("reduce_Greyjoy_character_turn") != "0":
								cost -= int(me.getGlobalVariable("reduce_Greyjoy_character_turn"))
								reduce_Greyjoy_character_turn = 1
						if card.faction == "Martell.":
							if me.getGlobalVariable("reduce_Martell_character_turn") != "0":
								cost -= int(me.getGlobalVariable("reduce_Martell_character_turn"))
								reduce_Martell_character_turn = 1
						if card.faction == "Baratheon.":
							if me.getGlobalVariable("reduce_Baratheon_character_turn") != "0":
								cost -= int(me.getGlobalVariable("reduce_Baratheon_character_turn"))
								reduce_Baratheon_character_turn = 1
						if card.faction == "Targaryen.":
							if me.getGlobalVariable("reduce_Targaryen_character_turn") != "0":
								cost -= int(me.getGlobalVariable("reduce_Targaryen_character_turn"))
								reduce_Targaryen_character_turn = 1
						if card.faction == "Night's Watch.":
							if me.getGlobalVariable("reduce_NW_character_turn") != "0":
								cost -= int(me.getGlobalVariable("reduce_NW_character_turn"))
								reduce_NW_character_turn = 1
						if card.faction == "Tyrell.":
							if me.getGlobalVariable("reduce_Tyrell_character_turn") != "0":
								cost -= int(me.getGlobalVariable("reduce_Tyrell_character_turn"))
								reduce_Tyrell_character_turn = 1
					if cost < 0:cost = 0
					if card.faction == "Stark.":
						if me.getGlobalVariable("reduce_Stark_card_turn") != "0":
							cost -= int(me.getGlobalVariable("reduce_Stark_card_turn"))
							reduce_Stark_card_turn = 1
					if card.faction == "Lannister.":
						if me.getGlobalVariable("reduce_Lannister_card_turn") != "0":
							cost -= int(me.getGlobalVariable("reduce_Lannister_card_turn"))
							reduce_Lannister_card_turn = 1
					if card.faction == "Greyjoy.":
						if me.getGlobalVariable("reduce_Greyjoy_card_turn") != "0":
							cost -= int(me.getGlobalVariable("reduce_Greyjoy_card_turn"))
							reduce_Greyjoy_card_turn = 1
					if card.faction == "Martell.":
						if me.getGlobalVariable("reduce_Martell_card_turn") != "0":
							cost -= int(me.getGlobalVariable("reduce_Martell_card_turn"))
							reduce_Martell_card_turn = 1
					if card.faction == "Baratheon.":
						if me.getGlobalVariable("reduce_Baratheon_card_turn") != "0":
							cost -= int(me.getGlobalVariable("reduce_Baratheon_card_turn"))
							reduce_Baratheon_card_turn = 1
					if card.faction == "Targaryen.":
						if me.getGlobalVariable("reduce_Targaryen_card_turn") != "0":
							cost -= int(me.getGlobalVariable("reduce_Targaryen_card_turn"))
							reduce_Targaryen_card_turn = 1
					if card.faction == "Tyrell.":
						if me.getGlobalVariable("reduce_Tyrell_card_turn") != "0":
							cost -= int(me.getGlobalVariable("reduce_Tyrell_card_turn"))
							reduce_Tyrell_card_turn = 1
					if card.faction == "Night's Watch.":
						if me.getGlobalVariable("reduce_NW_card_turn") != "0":
							cost -= int(me.getGlobalVariable("reduce_NW_card_turn"))
							reduce_NW_card_turn = 1
					if card.model == "b785b7fc-2a11-4ba5-87e7-7c06c79d6210":
						for ccard in table:
							if ccard.controller == me and ccard.type == "Character" and ccard.filter != WaitColor and "Dothraki" in ccard.traits:
								cost -= 1
					if cost < 0:cost = 0
					if me.counters['Gold'].value >= cost:
						if not actionattachtmp.has_key(card._id):
							actionattachtmp[card._id] = 1
						else:actionattachtmp[card._id] += 1
	debug(actionattachtmp)
	return actionattachtmp

def check511():
	mute()
	for card in table:
		if card.type == "Plot" and card.filter == None and card.model == "79877d2a-5b23-4c16-86df-9453c065835b":
			return True

def checknoprint(card):
	mute()
	debug(noprint_turn)
	for nocard in noprint_turn:
		if card == nocard:
			return True
	attach = eval(getGlobalVariable("attachmodify"))
	if checkcardattach(card):
		for d in attach:
			if attach[d] == card._id:
				debug(d)
				for cardatta in table:
					if cardatta._id == d:
						debug(cardatta.model)
						if cardatta.model == "a8bebc54-d01c-424d-8839-460ec09b733f":return True


def manualprocess(card,propass):
	mute()
	global manualpropass
	global manualcard
	
	manualcard = card
	manualpropass = propass
	if me.isInverted:table.create("90942683-91d6-414c-832d-5f6f0e495995",-375,-250)
	else:table.create("90942683-91d6-414c-832d-5f6f0e495995",-375,200)

def resumeprocess():
	mute()
	global manualpropass
	global manualcard
	global sessionpass
	sessionpass = ""
	c = 0
	for cardn in table:
		if cardn.name == "manualbutton" and cardn.controller == me:
			cardn.delete()
	if manualpropass == "plotability":
		manualpropass = ""
		manualcard = []
		if getGlobalVariable("reavelplot") == "1":
			setGlobalVariable("reavelplot","2")
			remoteCall(players[1], "reavelplot", table)
			return
		if getGlobalVariable("reavelplot") == "2":
			resetplot()
			remoteCall(players[1], "resetplot", [])
			if fplay(1) == me:actiongeneral(1)
			else:remoteCall(players[1], "actiongeneral", 1)
			return
	if manualpropass == "generalaction":
		for d in generalaction:
			if manualcard.model == generalaction[d][1] and manualcard.controller == me:
				if not actioncardlimit.has_key(manualcard._id):
					actioncardlimit[manualcard._id] = 1
				else:actioncardlimit[manualcard._id] += 1
				if actioncardlimit[manualcard._id] == generalaction[d][4]:
					debug(actionattach)
					del actionattach[manualcard._id]
					c = 1
		if c == 0:
			actionattach[manualcard._id] -= 1
			if actionattach[manualcard._id] == 0:del actionattach[manualcard._id]
		manualcard = []
		remoteCall(players[1], "action", ["general",1])
	if manualpropass == "dominanceend":
		for d in dominanceend:
			if manualcard.model == dominanceend[d][1] and manualcard.controller == me:
				if not reactioncardlimit.has_key(manualcard._id):
					reactioncardlimit[manualcard._id] = 1
				else:reactioncardlimit[manualcard._id] += 1
				if reactioncardlimit[manualcard._id] == dominanceend[d][4]:
					debug(reactionattach)
					del reactionattach[manualcard._id]
					c = 1
		if c == 0:
			reactionattach[manualcard._id] -= 1
			if reactionattach[manualcard._id] == 0:del reactionattach[manualcard._id]
		manualcard = []
		remoteCall(players[1], "reaction", ["dominanceend",1])
	if manualpropass == "dominance":
		for d in dominanceaction:
			if manualcard.model == dominanceaction[d][1] and manualcard.controller == me:
				if not actioncardlimit.has_key(manualcard._id):
					actioncardlimit[manualcard._id] = 1
				else:actioncardlimit[manualcard._id] += 1
				if actioncardlimit[manualcard._id] == dominanceaction[d][4]:
					debug(actionattach)
					del actionattach[manualcard._id]
					c = 1
		if c == 0:
			actionattach[manualcard._id] -= 1
			if actionattach[manualcard._id] == 0:del actionattach[manualcard._id]
		if manualcard.type == "Event":disc(manualcard)
		manualcard = []
		remoteCall(players[1], "action", ["dominance",1])

def dominancephasestart(count):
	mute()
	me.setGlobalVariable("finished","0")
	if me.isInverted:table.create("bd153c97-1108-4e65-bd46-88852ec7d5bc",-375,-250)
	else:table.create("bd153c97-1108-4e65-bd46-88852ec7d5bc",-375,200)
	#if count == 1:remoteCall(players[1], "dominancephasestart", [2])


def dominancenext():
	mute()
	me.setGlobalVariable("finished","1")
	for cardn in table:
		if cardn.name == "dominancenextbutton" and cardn.controller == me:
			cardn.delete()
	if getGlobalVariable("dominancephase") == "0":
		if me.getGlobalVariable("finished") == players[1].getGlobalVariable("finished") == "1":
			setGlobalVariable("dominancephase", "1")
			if fplay(1) == me:dominancestartreaction(1)
			else: remoteCall(players[1], "dominancestartreaction", [1])
		else:
			c = 0
			for cardn in table:
				if cardn.name == "dominancenextbutton" and cardn.controller != me:
					c = 1
			if c == 0:remoteCall(players[1], "dominancephasestart", [3])
		return


def dominancestartreaction(count):
	mute()
	global reactionattach
	for card in table:
		for d in dominancestart:
			if card.model == dominancestart[d][1] and card.controller == me and dominancestart[d][3] == "table":
				if dominancestart[d][2] == "stand" and card.orientation == 1:
					if not reactionattach.has_key(card._id):
						reactionattach[card._id] = 1
					else:reactionattach[card._id] += 1
					

	if len(reactionattach) > 0:setGlobalVariable("dominancestart", "1")
	if count == 1:remoteCall(players[1], "dominancestartreaction", [2])
	else:
		if getGlobalVariable("dominancestart") == "1":
			setGlobalVariable("dominancestart", "2")
			if fplay(1) == me:reaction("dominancestart",1)
			else: remoteCall(players[1], "reaction", ["dominancestart",1])
		else:
			if fplay(1) == me:dominance(table)
			else: remoteCall(players[1], "dominance", [table])

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
						if card.controller == person and card.model != "c8c63b0d-d3ea-4529-8022-1447655e740f")
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
					if card.markers[STR_Sub] > 0:
						str -= card.markers[STR_Sub]
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
	if winner == -1:
		notify("No one wins dominance.")
	else:
		notify("{} wins the dominance.".format(players[winner]))
		setGlobalVariable("dominancewinplayer",players[winner]._id)
		for housecard in table:
			if housecard.type == "Faction" and housecard.controller == players[winner]:
				remoteCall(housecard.controller, "addPower", [housecard])
	if fplay(1) == me:dominancewinreaction(1)
	else:remoteCall(players[1], "dominancewinreaction", [1])

def dominancewinreaction(count):
	mute()
	global reactionattach
	for card in table:
		for d in dominancewin:
			if card.model == dominancewin[d][1] and card.controller == me and dominancewin[d][3] == "table":
				if getGlobalVariable("dominancewinplayer") == str(me._id):
					if dominancewin[d][2] == "2power":
						if not reactionattach.has_key(card._id):
							reactionattach[card._id] = 1
						else:reactionattach[card._id] += 1
					if dominancewin[d][2] == "move1pow" and checkhousepow(players[1]) > 0:
						if not reactionattach.has_key(card._id):
							reactionattach[card._id] = 1
						else:reactionattach[card._id] += 1
					if dominancewin[d][2] == "returniron" and checkcardstatus(deck = me.piles['Dead pile'],traits = "Ironborn"):
						if not reactionattach.has_key(card._id):
							reactionattach[card._id] = 1
						else:reactionattach[card._id] += 1

	if len(reactionattach) > 0:setGlobalVariable("dominancewin", "1")
	if count == 1:remoteCall(players[1], "dominancewinreaction", [2])
	else:
		if getGlobalVariable("dominancewin") == "1":
			setGlobalVariable("dominancewin", "2")
			if fplay(1) == me:reaction("dominancewin",1)
			else: remoteCall(players[1], "reaction", ["dominancewin",1])
		else:
			if fplay(1) == me:actiondominance(1)
			else: remoteCall(players[1], "actiondominance", [1])

def dominanceendreaction(count):
	mute()
	global reactionattach
	for card in table:
		for d in dominanceend:
			if card.model == dominanceend[d][1] and card.controller == me and dominanceend[d][3] == "table":
				if dominanceend[d][2] == "cleartable":
					if not reactionattach.has_key(card._id):
						reactionattach[card._id] = 1
					else:reactionattach[card._id] += 1

	if len(reactionattach) > 0:setGlobalVariable("dominanceend", "1")
	if count == 1:remoteCall(players[1], "dominanceendreaction", [2])
	else:
		if getGlobalVariable("dominanceend") == "1":
			setGlobalVariable("dominanceend", "2")
			if fplay(1) == me:reaction("dominanceend",1)
			else: remoteCall(players[1], "reaction", ["dominanceend",1])
		else:
			if fplay(1) == me:dominancephaseend(table)
			else:remoteCall(players[1], "dominancephaseend", [table])

def dominancephaseend(group, x=0, y=0):
	mute()
	me.setGlobalVariable("finished","0")
	if me.isInverted:table.create("cb48782b-3bdd-4024-af85-fb0eb65a8f51",-320,-215)
	else:table.create("cb48782b-3bdd-4024-af85-fb0eb65a8f51",-320,125)

def actiondominance(count):
	mute()
	if count < 3:actiongeneral(3)
	global actionattach
	for card in me.hand:
		for d in dominanceaction:
			if card.model == dominanceaction[d][1] and card.controller == me and dominanceaction[d][3] == "Hand":
				if dominanceaction[d][2] == "controll6" and checkcardstatus(deck = table,player = players[1],cardtype = "Character",cost = 6,unique = "No"):
					if not actionattach.has_key(card._id):
						actionattach[card._id] = 1
					else:actionattach[card._id] += 1

	for card in table:
		for d in dominanceaction:
			if card.model == dominanceaction[d][1] and card.controller == me and dominanceaction[d][3] == "table":
				if card.type == "Character" and check511():continue
				if dominanceaction[d][2] == "returndraw1" and len(me.deck) > 0:
					if not actionattach.has_key(card._id):
						actionattach[card._id] = 1
					else:actionattach[card._id] += 1
				if dominanceaction[d][2] == "disctop" and len(players[1].deck) > 0 and card.orientation == 0:
					if not actionattach.has_key(card._id):
						actionattach[card._id] = 1
					else:actionattach[card._id] += 1



	debug(actionattach)
	if len(actionattach) > 0 and count < 3:setGlobalVariable("dominanceaction", "1")
	debug("dominanceaction1")
	debug(getGlobalVariable("dominanceaction"))
	if count == 1:remoteCall(players[1], "actiondominance", [2])
	if count == 2:

		if getGlobalVariable("dominanceaction") == "1":
			setGlobalVariable("dominanceaction", "2")
			debug("dominanceaction")
			debug(getGlobalVariable("dominanceaction"))
			if fplay(1) == me:action("dominance",1)
			else:remoteCall(otherplayer, "action", ["dominance",1])
		else:
			if fplay(1) == me:dominanceendreaction(1)
			else: remoteCall(players[1], "dominanceendreaction", [1])

def standingphasestart(count):
	mute()
	me.setGlobalVariable("finished","0")
	if me.isInverted:table.create("4d8aa7b0-f5ef-4584-be8c-601c45579dc6",-375,-250)
	else:table.create("4d8aa7b0-f5ef-4584-be8c-601c45579dc6",-375,200)
	#if count == 1:remoteCall(players[1], "standingphasestart", [2])

def standingnext():
	mute()
	me.setGlobalVariable("finished","1")
	for cardn in table:
		if cardn.name == "standingnextbutton" and cardn.controller == me:
			cardn.delete()
	if getGlobalVariable("standingphase") == "0":
		if me.getGlobalVariable("finished") == players[1].getGlobalVariable("finished") == "1":
			setGlobalVariable("standingphase", "1")
			if fplay(1) == me:standingstartreaction(1)
			else: remoteCall(players[1], "standingstartreaction", [1])
		else:
			c = 0
			for cardn in table:
				if cardn.name == "standingnextbutton" and cardn.controller != me:
					c = 1
			if c == 0:remoteCall(players[1], "standingphasestart", [3])
		return

def standingstartreaction(count):
	mute()
	global reactionattach

					

	if len(reactionattach) > 0:setGlobalVariable("standingstart", "1")
	if count == 1:remoteCall(players[1], "standingstartreaction", [2])
	else:
		if getGlobalVariable("standingstart") == "1":
			setGlobalVariable("standingstart", "2")
			if fplay(1) == me:reaction("standingstart",1)
			else: remoteCall(players[1], "reaction", ["standingstart",1])
		else:
			if fplay(1) == me:standingphase(table)
			else:remoteCall(players[1], "standingphase", [table])

def standingphase(group, x=0, y=0):
	mute()
	if checkstannis():
		if fplay(1) == me:standcharacter("stand1")
		else:remoteCall(players[1], "standcharacter", ["stand1"])
	else:standingcard(1)

def standingcard(count):
	mute()
	myCards = (card for card in table  #restore all cards
		if card.controller == me)
	for card in myCards:
		if card.isFaceUp:
			card.orientation &= ~Rot90
			card.highlight = None
			card.target(False)
	if count == 1:remoteCall(players[1], "standingcard", [2])
	if count == 2:
		if fplay(1) == me:standingoverreaction(1)
		else:remoteCall(players[1], "standingoverreaction", [1])

def standcharacter(typep):
	mute()
	if typep == "stand1":
		if checkcardstatus(cardtype = "Character",stand = 1,player = me):
			selectlist = checkcardid(deck = table,cardtype = "Character",player = me,stand = 1)
			selectcardnext(selectlist,"standcharacter1",table,[],me,1,2)
		else:remoteCall(players[1], "standcharacter", ["stand2"])
	if typep == "stand2":
		if checkcardstatus(cardtype = "Character",stand = 1,player = me):
			selectlist = checkcardid(deck = table,cardtype = "Character",player = me,stand = 1)
			selectcardnext(selectlist,"standcharacter2",table,[],me,1,2)

def standcharacterend(count):
	mute()
	for card in table:
		if card.filter == standcolor and card.controller == me:
			card.filter = None
			card.orientation = 0
	if count == 1:remoteCall(players[1], "standcharacterend", [2])
	if count == 2:
		if fplay(1) == me:standingoverreaction(1)
		else:remoteCall(players[1], "standingoverreaction", [1])

def checkstannis():
	mute()
	attach = eval(getGlobalVariable("attachmodify"))
	debug(attach)
	e = 0
	if not check511():
		for card in table:
			if card.model == "dfc85d0c-12a5-45b3-803a-98982c36d083":
				if checkcardattach(card):
					for d in attach:
						if attach[d] == card._id:
							debug(d)
							for cardatta in table:
								if cardatta._id == d:
									debug(cardatta.model)
									if cardatta.model != "a8bebc54-d01c-424d-8839-460ec09b733f":e = 1
				else:e = 1
	if e == 1:return True

def checkcardattach(card):
	mute()
	attach = eval(getGlobalVariable("attachmodify"))
	c = 0
	for card in table:
		for d in attach:
			if card._id == d:
				c = 1
				return True

def standingoverreaction(count):
	mute()
	global reactionattach

					

	if len(reactionattach) > 0:setGlobalVariable("standingover", "1")
	if count == 1:remoteCall(players[1], "standingoverreaction", [2])
	else:
		if getGlobalVariable("standingover") == "1":
			setGlobalVariable("standingover", "2")
			if fplay(1) == me:reaction("standingover",1)
			else: remoteCall(players[1], "reaction", ["standingover",1])
		else:
			if fplay(1) == me:actionstanding(1)
			else: remoteCall(players[1], "actionstanding", [1])

def actionstanding(count):
	mute()
	if count < 3:actiongeneral(3)

	debug(actionattach)
	if len(actionattach) > 0 and count < 3:setGlobalVariable("standingaction", "1")
	if count == 1:remoteCall(players[1], "actionstanding", [2])
	if count == 2:
		if getGlobalVariable("standingaction") == "1":
			setGlobalVariable("standingaction", "2")
			if fplay(1) == me:action("standing",1)
			else:remoteCall(otherplayer, "action", ["standing",1])
		else:
			if fplay(1) == me:standingendreaction(1)
			else: remoteCall(players[1], "standingendreaction", [1])


def standingendreaction(count):
	mute()
	global reactionattach
	
	if len(reactionattach) > 0:setGlobalVariable("standingend", "1")
	if count == 1:remoteCall(players[1], "standingendreaction", [2])
	else:
		if getGlobalVariable("standingend") == "1":
			setGlobalVariable("standingend", "2")
			if fplay(1) == me:reaction("standingend",1)
			else: remoteCall(players[1], "reaction", ["standingend",1])
		else:
			if fplay(1) == me:standingphaseend(table)
			else:remoteCall(players[1], "standingphaseend", [table])
			

def standingphaseend(group, x=0, y=0):
	mute()
	me.setGlobalVariable("finished","0")
	if me.isInverted:table.create("cb48782b-3bdd-4024-af85-fb0eb65a8f51",-320,-215)
	else:table.create("cb48782b-3bdd-4024-af85-fb0eb65a8f51",-320,125)

def taxationphasestart(count):
	mute()
	me.setGlobalVariable("finished","0")
	if me.isInverted:table.create("c38f6f47-54dc-4853-8000-ff2da81370ee",-375,-250)
	else:table.create("c38f6f47-54dc-4853-8000-ff2da81370ee",-375,200)
	#if count == 1:remoteCall(players[1], "taxationphasestart", [2])

def taxationnext():
	mute()
	me.setGlobalVariable("finished","1")
	for cardn in table:
		if cardn.name == "taxationnextbutton" and cardn.controller == me:
			cardn.delete()
	if getGlobalVariable("taxationphase") == "0":
		if me.getGlobalVariable("finished") == players[1].getGlobalVariable("finished") == "1":
			setGlobalVariable("taxationphase", "1")
			if fplay(1) == me:taxationstartreaction(1)
			else: remoteCall(players[1], "taxationstartreaction", [1])
		else:
			c = 0
			for cardn in table:
				if cardn.name == "taxationnextbutton" and cardn.controller != me:
					c = 1
			if c == 0:remoteCall(players[1], "taxationphasestart", [3])
		return

def taxationstartreaction(count):
	mute()
	global reactionattach

					
	if len(reactionattach) > 0:setGlobalVariable("taxationstart", "1")
	if count == 1:remoteCall(players[1], "taxationstartreaction", [2])
	else:
		if getGlobalVariable("taxationstart") == "1":
			setGlobalVariable("taxationstart", "2")
			if fplay(1) == me:reaction("taxationstart",1)
			else: remoteCall(players[1], "reaction", ["taxationstart",1])
		else:
			if fplay(1) == me:taxreturngold(1)
			else:remoteCall(players[1], "taxreturngold", [1])

def taxreturngold(count):
	mute()
	me.counters['Gold'].value = 0  #reset gold counters
	goldcard = (card for card in table
			if card.controller == me)
	for card in goldcard: 
		card.markers[Gold] = 0
	if count == 1:remoteCall(players[1], "taxreturngold", [2])
	if count == 2:
		if fplay(1) == me:taxationreturnoverreaction(1)
		else:remoteCall(players[1], "taxationreturnoverreaction", [1])

def taxationreturnoverreaction(count):
	mute()
	global reactionattach

					
	if len(reactionattach) > 0:setGlobalVariable("taxationreturn", "1")
	if count == 1:remoteCall(players[1], "taxationreturnoverreaction", [2])
	else:
		if getGlobalVariable("taxationreturn") == "1":
			setGlobalVariable("taxationreturn", "2")
			if fplay(1) == me:reaction("taxationreturnover",1)
			else: remoteCall(players[1], "reaction", ["taxationreturnover",1])
		else:
			if fplay(1) == me:taxationcheckhand(1)
			else:remoteCall(players[1], "taxationcheckhand", [1])

def taxationcheckhand(count):
	mute()
	getreserve(table)
	discAmount = None
	if len(me.hand) > me.counters['Reserve'].value:  #check reserve
		if discAmount == None: 
			whisper("The number of cards in {}'s hand is more than your reserve.You should discard {} cards.".format(me, len(me.hand)-me.counters['Reserve'].value))
			discAmount = len(me.hand)-me.counters['Reserve'].value
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
			if count == 1:remoteCall(players[1], "taxationcheckhand", [2])
			else:
				if fplay(1) == me:taxationrcheckhandreaction(1)
				else:remoteCall(players[1], "taxationrcheckhandreaction", [1])
		else:
			taxationcheckhand(count)
			return
	else:
		notify("Hand size is ok.")
		if count == 1:remoteCall(players[1], "taxationcheckhand", [2])
		else:
			if fplay(1) == me:taxationrcheckhandreaction(1)
			else:remoteCall(players[1], "taxationrcheckhandreaction", [1])

def taxationrcheckhandreaction(count):
	mute()
	global reactionattach

					
	if len(reactionattach) > 0:setGlobalVariable("taxationrcheckhand", "1")
	if count == 1:remoteCall(players[1], "taxationrcheckhandreaction", [2])
	else:
		if getGlobalVariable("taxationrcheckhand") == "1":
			setGlobalVariable("taxationrcheckhand", "2")
			if fplay(1) == me:reaction("taxationcheckhandover",1)
			else: remoteCall(players[1], "reaction", ["taxationcheckhandover",1])
		else:
			if fplay(1) == me:actiontaxation(1)
			else:remoteCall(players[1], "actiontaxation", [1])

def actiontaxation(count):
	mute()
	if count < 3:actiongeneral(3)

	debug(actionattach)
	if len(actionattach) > 0 and count < 3:setGlobalVariable("actiontaxation", "1")
	if count == 1:remoteCall(players[1], "actiontaxation", [2])
	if count == 2:
		if getGlobalVariable("actiontaxation") == "1":
			setGlobalVariable("actiontaxation", "2")
			if fplay(1) == me:action("taxation",1)
			else:remoteCall(otherplayer, "action", ["taxation",1])
		else:
			if fplay(1) == me:taxationendreaction(1)
			else: remoteCall(players[1], "taxationendreaction", [1])

def taxationendreaction(count):
	mute()
	global reactionattach
	
	if len(reactionattach) > 0:setGlobalVariable("taxationend", "1")
	if count == 1:remoteCall(players[1], "taxationendreaction", [2])
	else:
		if getGlobalVariable("taxationend") == "1":
			setGlobalVariable("taxationend", "2")
			if fplay(1) == me:reaction("taxationend",1)
			else: remoteCall(players[1], "reaction", ["taxationend",1])
		else:
			if fplay(1) == me:taxationphaseend(table)
			else:remoteCall(players[1], "taxationphaseend", [table])

def taxationphaseend(group, x=0, y=0):
	mute()
	me.setGlobalVariable("finished","0")
	if me.isInverted:table.create("cb48782b-3bdd-4024-af85-fb0eb65a8f51",-320,-215)
	else:table.create("cb48782b-3bdd-4024-af85-fb0eb65a8f51",-320,125)

def startnextphase(count):
	mute()
	# for c in table: 
	# 	if c.Type == "Plot" and c.controller == me:
	# 		if len(me.piles['Plot Deck']) > 0:
	# 			c.filter = "#0099ffff"
	# 			x, y = c.position
	# 			if me.isInverted:c.moveToTable(x, y-20)
	# 			else:c.moveToTable(x, y+20)
	# 		else:
	# 			if c.filter == usedplotcolor:
	# 				c.moveTo(me.piles['Plot Deck'])
	# 			else:
	# 				c.filter = "#0099ffff"
	
	me.counters['Reserve'].value = 0
	me.counters['Initiative'].value = 0
	me.counters['Str'].value = 0
	me.setGlobalVariable("inmarshal","1")
	me.setGlobalVariable("firstevent", "0")
	me.setGlobalVariable("firstcharacter", "0")
	me.setGlobalVariable("firstll", "0")#A Noble Cause
	me.setGlobalVariable("turn", "0")
	me.setGlobalVariable("firstevent", "0")	
	me.setGlobalVariable("milcount","0")
	me.setGlobalVariable("milcountmax","1")	
	me.setGlobalVariable("intcount","0")
	me.setGlobalVariable("intcountmax","1")
	me.setGlobalVariable("powcount","0")
	me.setGlobalVariable("powcountmax","1")
	me.setGlobalVariable("active","0")
	me.setGlobalVariable("reduceloyal_turn", "0")
	me.setGlobalVariable("intwin", "0")
	me.setGlobalVariable("submilclaim", "0")
	me.setGlobalVariable("subintclaim", "0")
	me.setGlobalVariable("subpowclaim", "0")
	me.setGlobalVariable("limitchallenge", "0")
	me.setGlobalVariable("cantuseevent", "0")
	me.setGlobalVariable("cantuselocation", "0")
	me.setGlobalVariable("cantuseattach", "0")
	me.setGlobalVariable("plotOk","")
	me.setGlobalVariable("drawOk","")
	me.setGlobalVariable("setupOk","")
	me.setGlobalVariable("firstlimit","0")
	me.setGlobalVariable("firstnobaratheonplayer","0")
	me.setGlobalVariable("firstdraw","0")
	me.setGlobalVariable("firstlocation","0")
	

	if count == 1:remoteCall(players[1], "startnextphase", 2)
	if count == 2:
		setGlobalVariable("tableTargets", "")
		setGlobalVariable("insertre", "")
		setGlobalVariable("cantchallenge", "0")
		setGlobalVariable("bedefend", "")
		setGlobalVariable("aftcr", "")
		setGlobalVariable("aftcu", "")
		setGlobalVariable("dominancestart", "")
		setGlobalVariable("dominancewin", "")
		setGlobalVariable("dominancewinplayer","")
		setGlobalVariable("dominanceend", "")
		setGlobalVariable("standingstart", "")
		setGlobalVariable("standingover", "")
		setGlobalVariable("standingend", "")
		setGlobalVariable("taxationstart", "")
		setGlobalVariable("taxationreturn", "")
		setGlobalVariable("taxationrcheckhand", "")
		setGlobalVariable("taxationend", "")
		setGlobalVariable("aftcuevent", "-1")
		setGlobalVariable("chaevent", "-1")
		setGlobalVariable("attachmodify", "{}")
		setGlobalVariable("mainstep", "0")
		setGlobalVariable("ambush", "0")
		setGlobalVariable("aftercalculatestand", "[]")
		setGlobalVariable("aftercalculatedraw", "[]")
		setGlobalVariable("ignorestr", "[]")
		setGlobalVariable("addclaim","0")
		setGlobalVariable("addclaimall","0")
		setGlobalVariable("reavelplot","1")
		setGlobalVariable("drawphase","0")
		setGlobalVariable("marshalphase","0")
		setGlobalVariable("firstreveal", "")
		setGlobalVariable("challengephase","0")
		setGlobalVariable("dominancephase","0")
		setGlobalVariable("standingphase","0")
		setGlobalVariable("taxationphase","0")
		setGlobalVariable("action","0")
		setGlobalVariable("activeplayer","")
		setGlobalVariable("winint","0")
		setGlobalVariable("challengeplayer","0")
		setGlobalVariable("Kingdomgold0","0")
		setGlobalVariable("Edictgold0","0")
		setGlobalVariable("plotdisc","0")
		setGlobalVariable("plotkill","0")
		setGlobalVariable("generalaction", "0")
		setGlobalVariable("dominanceaction", "0")
		setGlobalVariable("standingaction", "0")
		setGlobalVariable("actiontaxation", "0")
		notify("Taxation phase over")
		notify("A new turn start")
		notify("Plot phase start")
		remoteCall(fplay(1), "plotphasestart", [1])

def plotphasestart(count):
	mute()
	if me.isInverted:table.create("62bad042-fbb0-4121-85d2-92149576308b",-375,-250)
	else:table.create("62bad042-fbb0-4121-85d2-92149576308b",-375,200)

def resetperturn():
	mute()
	global reactionattach
	global addiconmil_turn
	global addiconint_turn
	global addiconpow_turn
	global subiconmil_turn
	global subiconint_turn
	global subiconpow_turn
	global returntohand_turn
	global disc_turn
	global noprint_turn
	for addmil in addiconmil_turn:
		cardmarkers(addmil,"milicon",-1)
	for addint in addiconint_turn:
		cardmarkers(addint,"inticon",-1)
	for addpow in addiconpow_turn:
		cardmarkers(addpow,"powicon",-1)
	for submil in subiconmil_turn:
		cardmarkers(addmil,"milicon",1)
	for subint in subiconint_turn:
		cardmarkers(addint,"inticon",1)
	for subpow in subiconpow_turn:
		cardmarkers(addpow,"powicon",1)
	for cardreturn in returntohand_turn:
		remoteCall(cardreturn.controller,"returncard",[cardreturn])
	for carddisc in disc_turn:
		remoteCall(carddisc.controller,"disc",[carddisc])
	for card in noprint_turn:
		restoreprintcard(card)
		card.markers[TokenRed] -= 1
	reactionattach = {}
	addiconmil_turn = []
	addiconint_turn = []
	addiconpow_turn = []
	subiconmil_turn = []
	subiconint_turn = []
	subiconpow_turn = []
	returntohand_turn = []
	noprint_turn = []
	disc_turn = []
	me.setGlobalVariable("reduceloyal_turn", "0")
	me.setGlobalVariable("reduce_character_turn", "0")
	me.setGlobalVariable("reduce_Baratheon_character_turn", "0")
	me.setGlobalVariable("reduce_Baratheon_card_turn", "0")
	me.setGlobalVariable("reduce_Greyjoy_character_turn", "0")
	me.setGlobalVariable("reduce_Greyjoy_card_turn", "0")
	me.setGlobalVariable("reduce_Lannister_character_turn", "0")
	me.setGlobalVariable("reduce_Lannister_card_turn", "0")
	me.setGlobalVariable("reduce_Martell_character_turn", "0")
	me.setGlobalVariable("reduce_Martell_card_turn", "0")
	me.setGlobalVariable("reduce_NW_character_turn", "0")
	me.setGlobalVariable("reduce_NW_card_turn", "0")
	me.setGlobalVariable("reduce_Stark_character_turn", "0")
	me.setGlobalVariable("reduce_Stark_card_turn", "0")
	me.setGlobalVariable("reduce_Targaryen_character_turn", "0")
	me.setGlobalVariable("reduce_Targaryen_card_turn", "0")
	me.setGlobalVariable("reduce_Tyrell_character_turn", "0") 
	me.setGlobalVariable("reduce_Tyrell_card_turn", "0")
	
def checkcounter(args):
	mute()
	if args.counter == me.counters['Gold']:
		i = 0 
		for card in table:
			if card.controller == me and card.model == "390a8cf7-8bc4-45c1-bea5-e6a694e9f2d5":card.markers[STR_Up] = me.counters['Gold'].value#Tywin Lannister
			if card.type == "Plot" and card.controller == me:
				if card  not in usedplot:card.markers[Gold] = me.counters['Gold'].value

def onsmoved(args):
	index = 0
	global aryaduplicate
	for card in args.cards:
		if args.cards[index].model == "fdf1989a-ee7d-4972-9d12-b299bfe3ba6d" and args.toGroups[index].name == "Table" and args.fromGroups[index].name != "Table" and args.cards[index].controller == me and args.cards[index].filter != WaitColor:
			for cardadd in table:
				if cardadd.controller == me and "Knight." in cardadd.traits and cardadd.filter != WaitColor and cardadd._id != args.cards[index]._id:
					cardmarkers(args.cards[index],"str",1)
					cardmarkers(args.cards[index],"powicon",1)
					break
		if "Knight." in args.cards[index].traits and args.toGroups[index].name == "Table" and args.fromGroups[index].name != "Table" and args.cards[index].controller == me and args.cards[index].filter != WaitColor:
			i = 0
			for cardadd in table:
				if cardadd.controller == me and "Knight." in cardadd.traits and cardadd.filter != WaitColor and cardadd._id != args.cards[index]._id:
					i += 1
			if i == 1:
				for cardaddd in table:
					if cardaddd.controller == me and cardaddd.model == "fdf1989a-ee7d-4972-9d12-b299bfe3ba6d" and cardaddd._id != args.cards[index]._id and cardaddd not in noprint_turn:
						cardmarkers(cardaddd,"str",1)
						cardmarkers(cardaddd,"powicon",1)
		if "Knight." in args.cards[index].traits and args.toGroups[index].name != "Table" and args.fromGroups[index].name == "Table" and args.cards[index].controller == me and args.cards[index].filter != WaitColor:
			i = 0
			for cardadd in table:
				if cardadd.controller == me and "Knight." in cardadd.traits and cardadd.filter != WaitColor and cardadd._id != args.cards[index]._id:
					i += 1
			if i == 1:
				for cardaddd in table:
					if cardaddd.controller == me and cardaddd.model == "fdf1989a-ee7d-4972-9d12-b299bfe3ba6d" and cardaddd not in noprint_turn:
						cardmarkers(cardaddd,"str",-1)
						cardmarkers(cardaddd,"powicon",-1)
		if args.cards[index].model == "91b7190f-d0ba-4c3b-b9e2-5e7d2c872acb" and args.toGroups[index].name == "Table" and args.fromGroups[index].name != "Table" and args.cards[index].controller == me and args.cards[index].filter != WaitColor:
			for cardadd in table:
				if cardadd.controller == me and "Drowned God." in cardadd.traits and cardadd.filter != WaitColor and cardadd._id != args.cards[index]._id:
					cardmarkers(cardadd,"str",1)
				elif cardadd._id == args.cards[index]._id:
					for cardaddd in table:
						if cardaddd.model == "91b7190f-d0ba-4c3b-b9e2-5e7d2c872acb" and cardaddd.controller == me:
							cardmarkers(cardadd,"str",1)
		if args.cards[index].model != "91b7190f-d0ba-4c3b-b9e2-5e7d2c872acb" and args.toGroups[index].name == "Table" and args.fromGroups[index].name != "Table" and args.cards[index].controller == me and args.cards[index].filter != WaitColor:
			if "Drowned God." in args.cards[index].traits:
				for cardadd in table:
					if cardadd.model == "91b7190f-d0ba-4c3b-b9e2-5e7d2c872acb" and cardadd.controller == me:
						cardmarkers(args.cards[index],"str",1)
		if args.cards[index].model == "91b7190f-d0ba-4c3b-b9e2-5e7d2c872acb" and args.toGroups[index].name != "Table" and args.fromGroups[index].name == "Table" and args.cards[index].controller == me and args.cards[index].filter != WaitColor and args.cards[index] not in noprint_turn:
				for cardaddd in table:
					if "Drowned God." in cardaddd.traits and cardaddd.controller == me:
						cardmarkers(cardaddd,"str",-1)
		if args.cards[index].model == "a5512893-cf5c-4e54-a8a7-87114492a50b" and args.toGroups[index].name == "Table" and args.fromGroups[index].name != "Table" and args.cards[index].controller == me and args.cards[index].filter != WaitColor:
			for cardaddd in table:
				if cardaddd.model == "597acd7c-3424-4e8c-82e6-d6682d662c8c" and cardaddd.controller == me and cardaddd.filter != WaitColor:
					for cardadd in table:
						if cardadd.controller == me and cardadd.model == "a5512893-cf5c-4e54-a8a7-87114492a50b" and cardadd.filter != WaitColor and cardadd not in noprint_turn:
							cardmarkers(cardadd,"str",1)
							cardmarkers(cardadd,"inticon",1)
						if cardadd.controller == me and cardadd.model == "597acd7c-3424-4e8c-82e6-d6682d662c8c" and cardadd.filter != WaitColor and cardadd not in noprint_turn:
							cardmarkers(cardadd,"str",1)
							cardmarkers(cardadd,"powicon",1)

		if args.cards[index].model == "597acd7c-3424-4e8c-82e6-d6682d662c8c" and args.toGroups[index].name == "Table" and args.fromGroups[index].name != "Table" and args.cards[index].controller == me and args.cards[index].filter != WaitColor:
			for cardaddd in table:
				if cardaddd.model == "a5512893-cf5c-4e54-a8a7-87114492a50b" and cardaddd.controller == me and cardaddd.filter != WaitColor:
					for cardadd in table:
						if cardadd.controller == me and cardadd.model == "a5512893-cf5c-4e54-a8a7-87114492a50b" and cardadd.filter != WaitColor and cardadd not in noprint_turn:
							cardmarkers(cardadd,"inticon",1)
						if cardadd.controller == me and cardadd.model == "597acd7c-3424-4e8c-82e6-d6682d662c8c" and cardadd.filter != WaitColor and cardadd not in noprint_turn:
							cardmarkers(cardadd,"str",1)
							cardmarkers(cardadd,"powicon",1)

		if args.cards[index].model in ("597acd7c-3424-4e8c-82e6-d6682d662c8c","a5512893-cf5c-4e54-a8a7-87114492a50b") and args.toGroups[index].name != "Table" and args.fromGroups[index].name == "Table" and args.cards[index].controller == me and args.cards[index].filter != WaitColor:
				for cardadd in table:
					if cardadd.controller == me and cardadd.model == "a5512893-cf5c-4e54-a8a7-87114492a50b" and cardadd.filter != WaitColor and cardadd not in noprint_turn:
						cardmarkers(cardadd,"str",-1)
						cardmarkers(cardadd,"inticon",-1)
					if cardadd.controller == me and cardadd.model == "597acd7c-3424-4e8c-82e6-d6682d662c8c" and cardadd.filter != WaitColor and cardadd not in noprint_turn:
						cardmarkers(cardadd,"str",-1)
						cardmarkers(cardadd,"powicon",-1)

		if args.cards[index].model == "cbeb3a37-d4c1-4697-b8d2-e366b4569002" and args.toGroups[index].name == "Table" and args.fromGroups[index].name != "Table" and args.cards[index].controller == me and args.cards[index].filter != WaitColor and args.cards[index] not in noprint_turn:
			for cardadd in table:
				if cardadd.controller == me and "Warship" in cardadd.traits:cardmarkers(args.cards[index],"str",1)
		if args.cards[index].model == "3e1a5952-f5d1-4bca-9226-2b94531cfa54" and args.toGroups[index].name == "Table" and args.fromGroups[index].name != "Table" and args.cards[index].controller == me and args.cards[index].filter != WaitColor and args.cards[index] not in noprint_turn:
			for cardadd in table:
				if cardadd.controller == me and "The Reach" in cardadd.traits:cardmarkers(args.cards[index],"str",1)
		if args.cards[index].Faction == "Night's Watch." and args.cards[index].type == "Character" and args.toGroups[index].name == "Table" and args.fromGroups[index].name != "Table" and args.cards[index].controller == me and args.cards[index].filter != WaitColor:
			for cardadd in table:
				if cardadd.controller == me and cardadd.model == "5d20e021-5d12-4338-8bdd-42d008bff919" and cardadd.filter != WaitColor and cardadd not in noprint_turn:cardmarkers(args.cards[index],"str",1)
		if args.cards[index].model == "390a8cf7-8bc4-45c1-bea5-e6a694e9f2d5" and args.toGroups[index].name == "Table" and args.fromGroups[index].name != "Table" and args.cards[index].controller == me and args.cards[index].filter != WaitColor:args.cards[index].markers[STR_Up] += me.counters['Gold'].value
		if args.cards[index].model == "c41d4a72-6919-4e32-97ef-a4b0f1acb281" and args.toGroups[index].name == "Table" and args.fromGroups[index].name != "Table" and args.cards[index].controller == me and args.cards[index].filter != WaitColor and args.cards[index] not in noprint_turn:
			for cardadd in table:
				if cardadd.controller == me and cardadd.model != "c41d4a72-6919-4e32-97ef-a4b0f1acb281" and "Direwolf" in cardadd.traits:cardmarkers(args.cards[index],"str",1)
				if cardadd.controller == me and cardadd.model == "c41d4a72-6919-4e32-97ef-a4b0f1acb281" and args.cards[index]._id != cardadd._id:
					for cardadd2 in table:
						if cardadd2.model == "c41d4a72-6919-4e32-97ef-a4b0f1acb281" and cardadd2._id != cardadd._id and cardadd2._id != args.cards[index]._id and cardadd2 not in noprint_turn:cardmarkers(cardadd2,"str",-1)
				if cardadd.controller == me and cardadd.model == "c41d4a72-6919-4e32-97ef-a4b0f1acb281":
					for cardadd2 in table:
						if cardadd2.model == "c41d4a72-6919-4e32-97ef-a4b0f1acb281" and cardadd2._id != cardadd._id and cardadd2 not in noprint_turn:cardmarkers(cardadd2,"str",1)
		if args.cards[index].model == "c41d4a72-6919-4e32-97ef-a4b0f1acb281" and args.toGroups[index].name != "Table" and args.fromGroups[index].name == "Table" and args.cards[index].controller == me and args.cards[index].filter != WaitColor:
			for cardadd in table:
				if cardadd.controller == me and cardadd.model == "c41d4a72-6919-4e32-97ef-a4b0f1acb281" and args.cards[index]._id != cardadd._id:cardmarkers(cardadd,"str",-1)
		if args.cards[index].model != "c41d4a72-6919-4e32-97ef-a4b0f1acb281" and args.toGroups[index].name == "Table" and args.fromGroups[index].name != "Table" and args.cards[index].controller == me and args.cards[index].filter != WaitColor:
			if "Direwolf" in args.cards[index].traits:
				for cardadd in table:
					if cardadd.controller == me and cardadd.model == "c41d4a72-6919-4e32-97ef-a4b0f1acb281" and cardadd not in noprint_turn:cardadd.markers[STR_Up] += 1
		if args.cards[index].model == "c41d4a72-6919-4e32-97ef-a4b0f1acb281" and args.toGroups[index].name == "Table" and args.fromGroups[index].name != "Table" and args.cards[index].controller == me and args.cards[index].filter != WaitColor and args.cards[index] in noprint_turn:
			if "Direwolf" in args.cards[index].traits:
				for cardadd in table:
					if cardadd.controller == me and cardadd.model == "c41d4a72-6919-4e32-97ef-a4b0f1acb281" and cardadd not in noprint_turn:cardadd.markers[STR_Up] += 1
		if args.cards[index].model != "c41d4a72-6919-4e32-97ef-a4b0f1acb281" and args.toGroups[index].name != "Table" and args.fromGroups[index].name == "Table" and args.cards[index].controller == me and args.cards[index].filter != WaitColor:
			if "Direwolf" in args.cards[index].traits:
				for cardadd in table:
					if cardadd.controller == me and cardadd.model == "c41d4a72-6919-4e32-97ef-a4b0f1acb281" and cardadd not in noprint_turn:cardmarkers(cardadd,"str",-1)
		if args.cards[index].type == "Location" and args.toGroups[index].name == "Table" and args.fromGroups[index].name != "Table" and args.cards[index].controller == me and args.cards[index].filter != WaitColor:
			if "Warship" in args.cards[index].traits:
				for cardadd in table:
					if cardadd.controller == me and cardadd.model == "cbeb3a37-d4c1-4697-b8d2-e366b4569002" and cardadd not in noprint_turn:cardmarkers(cardadd,"str",1)
			if "The Reach" in args.cards[index].traits:
				for cardadd in table:
					if cardadd.controller == me and cardadd.model == "3e1a5952-f5d1-4bca-9226-2b94531cfa54" and cardadd not in noprint_turn:cardmarkers(cardadd,"str",1)
			if args.cards[index].model == "5d20e021-5d12-4338-8bdd-42d008bff919" :
				for cardadd in table:
					if cardadd.controller == me and cardadd.Faction == "Night's Watch." and cardadd.type == "Character" and cardadd.filter != WaitColor:cardmarkers(cardadd,"str",1)
		if args.cards[index].type == "Location" and args.toGroups[index].name != "Table" and args.fromGroups[index].name == "Table" and args.cards[index].controller == me and args.cards[index].filter != WaitColor:
			if "Warship" in args.cards[index].traits:
				for cardadd in table:
					if cardadd.controller == me and cardadd.model == "cbeb3a37-d4c1-4697-b8d2-e366b4569002" and cardadd not in noprint_turn:cardmarkers(cardadd,"str",-1)
			if "The Reach" in args.cards[index].traits:
				for cardadd in table:
					if cardadd.controller == me and cardadd.model == "3e1a5952-f5d1-4bca-9226-2b94531cfa54" and cardadd not in noprint_turn:cardmarkers(cardadd,"str",-1)
			if args.cards[index].model == "5d20e021-5d12-4338-8bdd-42d008bff919" and args.cards[index] in noprint_turn:
				for cardadd in table:
					if cardadd.controller == me and cardadd.Faction == "Night's Watch."and cardadd.type == "Character" and cardadd.filter != WaitColor:cardmarkers(cardadd,"str",-1)


		if args.cards[index].model == "abf9c701-f480-4576-a5c0-44b4e9b04e6c" and args.toGroups[index].name == "Table" and args.fromGroups[index].name != "Table" and args.cards[index].controller == me and args.cards[index].filter != WaitColor:
			if not confirm("place the top card of your deck on her facedown as arya's duplicate?"):return
			if len(me.deck) > 1:
				for cardatt in me.Deck.top(1):
					x,y = args.cards[index].position
					if me.isInverted: 
						cardatt.moveToTable(x-12,y-12,True)
					else:
						cardatt.moveToTable(x+12,y+12,True)
					cardatt.peek()
					cardatt.filter = "#005c3521"
					cardatt.sendToBack()
					aryaduplicate.append(cardatt)
				cardmarkers(args.cards[index],"milicon",1)
				return
		if card in aryaduplicate and args.toGroups[index].name != "Table" and args.fromGroups[index].name == "Table" and card.controller == me:
			aryaduplicate.remove(card)
			if len(aryaduplicate) == 0:
				for card in table:
					if card.model == "abf9c701-f480-4576-a5c0-44b4e9b04e6c" and card.controller == me and card not in noprint_turn:cardmarkers(card,"milicon",-1)
	index += 1
def movecardp(card,x,y,back):
	mute()
	card.moveToTable(x,y)
	if back == 1:card.sendToBack()

def actionmarshal(count):
	mute()
	me.setGlobalVariable("setupOk","")
	if count < 3:actiongeneral(3)
	global actionattach
	for card in me.hand:
		for d in marshalaction:
			if card.model == marshalaction[d][1] and card.controller == me and marshalaction[d][3] == "Hand":
				if marshalaction[d][2] == "kneel4cadd1power" and checkcardstatus(deck = table,cardtype = "Character",cost = 4,stand = 0):
					if not actionattach.has_key(card._id):
						actionattach[card._id] = 1
					else:actionattach[card._id] += 1

	for card in table:
		for d in marshalaction:
			if card.model == marshalaction[d][1] and card.controller == me and marshalaction[d][3] == "table" and card.filter != WaitColor:
				if card.type == "Character" and check511():continue
				if card.type in ("Character","Location") and checknoprint(card):continue
				if marshalaction[d][2] == "reduce3s" and card.orientation == 0:
					if not actionattach.has_key(card._id):
						actionattach[card._id] = 1
					else:actionattach[card._id] += 1
				if marshalaction[d][2] == "controllb" and card.orientation == 0:
					if not actionattach.has_key(card._id):
						actionattach[card._id] = 1
					else:actionattach[card._id] += 1
				if marshalaction[d][2] == "discattachmentc" and card.orientation == 0 and checkcardstatus(cardtype = "Attachment",traits = "Condition"):
					if not actionattach.has_key(card._id):
						actionattach[card._id] = 1
					else:actionattach[card._id] += 1
				if marshalaction[d][2] == "reduce1Baratheoncharacter" and card.orientation == 0:
					if not actionattach.has_key(card._id):
						actionattach[card._id] = 1
					else:actionattach[card._id] += 1
				if marshalaction[d][2] == "reduce1Baratheoncard" and card.orientation == 0:
					if not actionattach.has_key(card._id):
						actionattach[card._id] = 1
					else:actionattach[card._id] += 1
				if marshalaction[d][2] == "reduce1Greyjoycharacter" and card.orientation == 0:
					if not actionattach.has_key(card._id):
						actionattach[card._id] = 1
					else:actionattach[card._id] += 1
				if marshalaction[d][2] == "kneel2location" and card.orientation == 0:
					if fplay(1) == me and checkcardstatus(cardtype = "Location",cost = 3):
						if not actionattach.has_key(card._id):
							actionattach[card._id] = 1
						else:actionattach[card._id] += 1
					elif fplay(1) != me and checkcardstatus(cardtype = "Location",cost = 2):
						if not actionattach.has_key(card._id):
							actionattach[card._id] = 1
						else:actionattach[card._id] += 1
				if marshalaction[d][2] == "reduce1Greyjoycard" and card.orientation == 0:
					if not actionattach.has_key(card._id):
						actionattach[card._id] = 1
					else:actionattach[card._id] += 1
				if marshalaction[d][2] == "reduce1Lannistercharacter" and card.orientation == 0:
					if not actionattach.has_key(card._id):
						actionattach[card._id] = 1
					else:actionattach[card._id] += 1
				if marshalaction[d][2] == "reduce1Lannistercard" and card.orientation == 0:
					if not actionattach.has_key(card._id):
						actionattach[card._id] = 1
					else:actionattach[card._id] += 1
				if marshalaction[d][2] == "reduce1Martellcharacter" and card.orientation == 0:
					if not actionattach.has_key(card._id):
						actionattach[card._id] = 1
					else:actionattach[card._id] += 1
				if marshalaction[d][2] == "reduce1Martellcard" and card.orientation == 0:
					if not actionattach.has_key(card._id):
						actionattach[card._id] = 1
					else:actionattach[card._id] += 1
				if marshalaction[d][2] == "reduce1NWcharacter" and card.orientation == 0:
					if not actionattach.has_key(card._id):
						actionattach[card._id] = 1
					else:actionattach[card._id] += 1
				if marshalaction[d][2] == "reduce1Starkcharacter" and card.orientation == 0:
					if not actionattach.has_key(card._id):
						actionattach[card._id] = 1
					else:actionattach[card._id] += 1
				if marshalaction[d][2] == "reduce1Starkcard" and card.orientation == 0:
					if not actionattach.has_key(card._id):
						actionattach[card._id] = 1
					else:actionattach[card._id] += 1
				if marshalaction[d][2] == "reduce1Targaryencharacter" and card.orientation == 0:
					if not actionattach.has_key(card._id):
						actionattach[card._id] = 1
					else:actionattach[card._id] += 1
				if marshalaction[d][2] == "reduce1Targaryencard" and card.orientation == 0:
					if not actionattach.has_key(card._id):
						actionattach[card._id] = 1
					else:actionattach[card._id] += 1
				if marshalaction[d][2] == "reduce1Tyrellcharacter" and card.orientation == 0:
					if not actionattach.has_key(card._id):
						actionattach[card._id] = 1
					else:actionattach[card._id] += 1
				if marshalaction[d][2] == "reduce1Tyrellcard" and card.orientation == 0:
					if not actionattach.has_key(card._id):
						actionattach[card._id] = 1
					else:actionattach[card._id] += 1
			if card.model == marshalaction[d][1] and card.controller != me and marshalaction[d][3] == "table" and card.filter != WaitColor:
				if marshalaction[d][2] == "controllb":
					if not actionattach.has_key(card._id):
						actionattach[card._id] = 1
					else:actionattach[card._id] += 1
	debug(actionattach)
	# if len(actionattach) > 0 and count < 3:setGlobalVariable("dominanceaction", "1")
	if count < 3:action("marshal",1)
	# if count == 1:remoteCall(players[1], "actionmarshal", [2])
	# if count == 2:

	# 	if getGlobalVariable("dominanceaction") == "1":
	# 		setGlobalVariable("dominanceaction", "2")
	# 		debug("dominanceaction")
	# 		debug(getGlobalVariable("dominanceaction"))
	# 		if fplay(1) == me:action("dominance",1)
	# 		else:remoteCall(otherplayer, "action", ["dominance",1])
	# 	else:
	# 		if fplay(1) == me:dominanceendreaction(1)
	# 		else: remoteCall(players[1], "dominanceendreaction", [1])

def reactionmarshal(card):
	mute()
	debug(card)
	global reactionattach
	global sessionpass
	sessionpass = ""
	if "R'hllor" in card.traits and checkcardstatus(cardtype = "Character",stand = 0):
		for cardre in table:
			if cardre.model == "6ab37ed8-df99-410d-a9ff-7afe98f7ee22" and cardre.controller == me and cardre.filter != WaitColor:reactionattach[cardre._id] = 1#Melisandre
	
	if card.model == "499ed82d-cc0e-43a5-89ba-a748b388f528" and len(me.deck) > 0:reactioncard = reactionattach[card._id] = 1#Littlefinger

	if card.model == "47f94d62-7d83-4e36-80c6-0062d56aa820":
		for disccard in players[1].piles['Discard pile']:
			if disccard.type == "Character" and int(disccard.cost) <= 3:
				reactioncard = reactionattach[card._id] = 1#Yoren
				break
	if card.model == "8f2b58df-649e-4793-bd4c-bbf701cd57c5" and me.getGlobalVariable("firstdraw") == "0":reactionattach[card._id] = 1#Pleasure Barge
	if "Builder" in card.traits:
		for cardre in table:
			if cardre.model == "5347c5c6-a2cf-48e3-b851-7d4c68ffafc5" and cardre.controller == me and cardre.filter != WaitColor:
				debug(cardre)
				if not reactioncardlimit.has_key(cardre._id):
					reactionattach[cardre._id] = 1#Brandon's Gift
				else:
					if reactioncardlimit[cardre._id] <= 3:
						reactionattach[cardre._id] = 1#Brandon's Gift
	if card.model == "f88dd3c7-cae8-4e52-b810-8fbd8f70fd23":reactionattach[card._id] = 1#Northern Rookery
	debug(reactionattach)

	if len(reactionattach) > 0:reaction("reactionmarshal",1)
	else:remoteCall(players[1], "action", ["marshal",1])

def noprintcard(card, x = 0, y = 0,ntype = 0):
	mute()
	debug(card)
	global noprint_turn
	if ntype == 0:noprint_turn.append(card)
	if ntype == 1:noprint_turn.append(card)
	if card.type == "Location":
		if card.model == "5d20e021-5d12-4338-8bdd-42d008bff919":
			for cardadd in table:
				if cardadd.controller == me and cardadd.Faction == "Night's Watch."and cardadd.type == "Character" and cardadd.filter != WaitColor:cardmarkers(cardadd,"str",-1)
	if card.model == "fdf1989a-ee7d-4972-9d12-b299bfe3ba6d":
		for cardadd in table:
			if cardadd.controller == me and "Knight" in cardadd.traits and cardadd != card:
				cardmarkers(card,"str",-1)
				cardmarkers(card,"powicon",-1)
				break
	if card.model == "cbeb3a37-d4c1-4697-b8d2-e366b4569002":
		for cardadd in table:
			if cardadd.controller == me and "Warship" in cardadd.traits:cardmarkers(card,"str",-1)
	if card.model == "3e1a5952-f5d1-4bca-9226-2b94531cfa54":
		for cardadd in table:
			if cardadd.controller == me and "The Reach" in cardadd.traits:cardmarkers(card,"str",-1)
	if card.model == "91b7190f-d0ba-4c3b-b9e2-5e7d2c872acb":
		for cardaddd in table:
			if "Drowned God." in cardaddd.traits and cardaddd.controller == me:
				cardmarkers(cardaddd,"str",-1)
	if card.model == "a5512893-cf5c-4e54-a8a7-87114492a50b":
		for cardadd in table:
			if cardadd.controller == me and cardadd.model == "597acd7c-3424-4e8c-82e6-d6682d662c8c" and cardadd.filter != WaitColor:
				cardmarkers(card,"str",-1)
				cardmarkers(card,"inticon",-1)
	if card.model == "597acd7c-3424-4e8c-82e6-d6682d662c8c":
		for cardadd in table:
			if cardadd.controller == me and cardadd.model == "a5512893-cf5c-4e54-a8a7-87114492a50b" and cardadd.filter != WaitColor:
				cardmarkers(card,"str",-1)
				cardmarkers(card,"powicon",-1)

	if card.model == "abf9c701-f480-4576-a5c0-44b4e9b04e6c" and card.controller == me:
		if len(aryaduplicate) > 0:cardmarkers(card,"milicon",-1)
	if card.model == "c41d4a72-6919-4e32-97ef-a4b0f1acb281":
		i = 0
		for cardadd in table:
			if cardadd.controller == me and cardadd.model == "c41d4a72-6919-4e32-97ef-a4b0f1acb281" and cardadd != card:
				i += 1
			if cardadd.model != "c41d4a72-6919-4e32-97ef-a4b0f1acb281":
				if "Direwolf" in cardadd.traits:i += 1
		cardmarkers(card,"str",-i)

def restoreprintcard(card, x = 0, y = 0):
	mute()
	global noprint_turn
	#noprint_turn.remove(card)
	if card.type == "Location":
		if card.model == "5d20e021-5d12-4338-8bdd-42d008bff919":
			for cardadd in table:
				if cardadd.controller == me and cardadd.Faction == "Night's Watch."and cardadd.type == "Character" and cardadd.filter != WaitColor:cardmarkers(cardadd,"str",1)
	if card.model == "fdf1989a-ee7d-4972-9d12-b299bfe3ba6d":
		for cardadd in table:
			if cardadd.controller == me and "Knight" in cardadd.traits and cardadd != card and cardadd.filter != WaitColor:
				cardmarkers(card,"str",1)
				cardmarkers(card,"powicon",1)
				break
	if card.model == "cbeb3a37-d4c1-4697-b8d2-e366b4569002":
		for cardadd in table:
			if cardadd.controller == me and "Warship" in cardadd.traits and cardadd.filter != WaitColor:cardmarkers(card,"str",1)
	if card.model == "3e1a5952-f5d1-4bca-9226-2b94531cfa54":
		for cardadd in table:
			if cardadd.controller == me and "The Reach" in cardadd.traits and cardadd.filter != WaitColor:cardmarkers(card,"str",1)
	if card.model == "91b7190f-d0ba-4c3b-b9e2-5e7d2c872acb":
		for cardaddd in table:
			if "Drowned God." in cardaddd.traits and cardaddd.controller == me and cardaddd.filter != WaitColor:
				cardmarkers(cardaddd,"str",1)
	if card.model == "a5512893-cf5c-4e54-a8a7-87114492a50b":
		for cardadd in table:
			if cardadd.controller == me and cardadd.model == "597acd7c-3424-4e8c-82e6-d6682d662c8c" and cardadd.filter != WaitColor:
				cardmarkers(card,"str",1)
				cardmarkers(card,"inticon",1)
	if card.model == "597acd7c-3424-4e8c-82e6-d6682d662c8c":
		for cardadd in table:
			if cardadd.controller == me and cardadd.model == "a5512893-cf5c-4e54-a8a7-87114492a50b" and cardadd.filter != WaitColor:
				cardmarkers(card,"str",1)
				cardmarkers(card,"powicon",1)

	if card.model == "abf9c701-f480-4576-a5c0-44b4e9b04e6c" and card.controller == me:
		if len(aryaduplicate) > 0:cardmarkers(card,"milicon",1)
	if card.model == "c41d4a72-6919-4e32-97ef-a4b0f1acb281":
		i = 0
		for cardadd in table:
			if cardadd.controller == me and cardadd.model == "c41d4a72-6919-4e32-97ef-a4b0f1acb281" and cardadd != card:
				i += 1
			if cardadd.model != "c41d4a72-6919-4e32-97ef-a4b0f1acb281":
				if "Direwolf" in cardadd.traits:i += 1
		cardmarkers(card,"str",i)
