
def checkdbclickselectcard(card):
	mute()
	if confirm("You will marshal [{}],reduced cost by [{}],finally marshal for cost [{}], after marshal you have [{}] gold".format(card.name,int(card.cost)-checkreduce(card),checkreduce(card),me.counters['Gold'].value-checkreduce(card))):
		return True