from .engine import Game, Player
from . import minmaxwrapper

class Morpx:
	def __init__(self, p1, p2):
		self.p1=p1
		self.p2=p2
		self.even=False
	
	def play(self):
		game=Game()
		if self.even:
			(first, second)=(self.p1, self.p2)
		else:
			(first, second)=(self.p2, self.p1)
		
		minmaxwrapper.install(game, Player.P1, 4, first.intelligence)
		minmaxwrapper.install(game, Player.P2, 4, second.intelligence)
		
		game.reset()
		
		if game.board.state==Player.P1:
			self.results=self.even and 1 or 2
		elif game.board.state==Player.P2:
			self.results=self.even and 2 or 1
		else:
			self.results=0
		
		self.even=not self.even
