#Brian Chan, Isaac Wang, Somin Kim
from Summoner import Summoner
import urllib, json

class Summoner_set:
	
	def __init__(self, name):
		self.key = ["4e125fd6-a393-4bff-a348-8bbffdf96c76", "3ee70df8-1421-4834-a5c3-153995295808", "591292ec-a2b1-48c7-82dc-d366c559c0df", "bcca9eb7-2e8c-4947-b140-cbb6a20ae044"]

		self.originalSummonerName = name
		self.originalSummonerURL = "https://na.api.pvp.net/api/lol/na/v1.4/summoner/by-name/" + name + "?api_key=" + self.key[0]
		self.key = self.key[1:] + [self.key[0]]

		self.originalSummonerResponse = urllib.urlopen(self.originalSummonerURL);
		self.originalSummonerData = json.loads(self.originalSummonerResponse.read())
		self.originalSummonerID = self.originalSummonerData[name]["id"]

		self.matchURL = "https://na.api.pvp.net/api/lol/na/v1.3/game/by-summoner/" + str(self.originalSummonerID) + "/recent?api_key=" + self.key[0]
		self.key = self.key[1:] + [self.key[0]]

		self.matchResponse = urllib.urlopen(self.matchURL);
		self.game = json.loads(self.matchResponse.read())['games'][0]
		self.originalChampionId = self.game['championId']

		self.originalSummoner = Summoner(self.originalSummonerID, self.originalChampionId)
		self.originalSummonerSide = 100

		self.fellowPlayers = self.game['fellowPlayers']

		self.blueSummoners = []
		self.redSummoners = []

		for dic in self.fellowPlayers:
			if dic["teamId"] == 100:
				self.blueSummoners.append(Summoner(dic["summonerId"], dic["championId"]))
			else:
				self.redSummoners.append(Summoner(dic["summonerId"], dic["championId"]))
			

		if len(self.blueSummoners) == 4:
			self.blueSummoners.append(self.originalSummoner)
		else:
			self.redSummoners.append(self.originalSummoner)
			self.originalSummonerSide = 200

	def averageWinRate(self, team):
		total = 0
		for player in team:
			total += player.getWinRate()
		return total / 5

	def determineChances(self):
		blue = self.averageWinRate(self.blueSummoners)
		red = self.averageWinRate(self.redSummoners)
		if self.originalSummonerSide == 100:
			return blue / (blue+red)
		else:
			return red / (blue+red)

	def won(self):
		self.game['stats']['win']
		
name = input('Enter summoner name: ')

A = Summoner_set(name)

def test(users):
	correct = 0
	for user in users:
		S = Summoner_set(user)
		prediction = S.determineChances() > .50
		if prediction == S.won():
			correct += 1
	print (str(correct) + " of " (str(len(users))) + " correctly predicted")

#Friends = ["bciscool", "coolguypat", "mikeypwnsall", "d0ny", "waddlingpenguins"]
#test(Friends)

print(A.determineChances())
