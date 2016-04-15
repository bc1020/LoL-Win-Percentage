#Brian Chan, Isaac Wang, Somin Kim
import urllib, json, time

class Summoner:
	
	def __init__(self, Id, champId):
		self.key = ["4e125fd6-a393-4bff-a348-8bbffdf96c76", "3ee70df8-1421-4834-a5c3-153995295808", "591292ec-a2b1-48c7-82dc-d366c559c0df", "bcca9eb7-2e8c-4947-b140-cbb6a20ae044"]

		self.summonerID = Id

		self.statsURL = "https://na.api.pvp.net/api/lol/na/v1.3/stats/by-summoner/" + str(self.summonerID) + "/ranked?season=SEASON2014&api_key=" + self.key[0]
		self.key = self.key[1:] + [self.key[0]]
		time.sleep(1)

		self.statsResponse = urllib.urlopen(self.statsURL)

		self.statsChampions = json.loads(self.statsResponse.read())['champions']
		self.champion = champId

	def getID(self):
		return self.summonerID 

	def getGame(self):
		return self.game

	def getFellowPlayers(self):
		return self.fellowPlayers

	def getChampion(self):
		return self.champion

	def getWinRate(self):
		for dic in self.statsChampions:
			if dic['id'] == self.champion:
				if dic['stats']['totalSessionsPlayed'] == None:
					return .50
				return float(dic['stats']['totalSessionsWon']) / dic['stats']['totalSessionsPlayed']
		return .50

