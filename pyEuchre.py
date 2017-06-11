import sys, pygame
pygame.init()

size = width, height = 720, 720
green = 70, 150, 80
white = 255, 255, 255
red = 255, 0, 0
black = 0, 0, 0
h = "h"
c = "c"
s = "s"
d = "d"
font = pygame.font.SysFont("monospace", 16)

screen = pygame.display.set_mode(size)

	#Creating class for cards
class Card(pygame.sprite.Sprite):

	def __init__(self, suit, number):
		pygame.sprite.Sprite.__init__(self)
		cardValue = number
		strSuit = str(suit)
		if number == 9:
			strNumber = "0" + str(number)
		else:
			strNumber = str(number)
		cardPath = strSuit + strNumber + ".png"
		self.image = pygame.transform.scale(pygame.image.load(cardPath), (100, 140))
		self.rect = self.image.get_rect()

	#Creating spaces for cards to fill on table
class cardSpace(pygame.sprite.Sprite):
	
	def __init__(self, color, width, height):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface([width, height])
		self.image.fill(color)
		
		# Fetch the rectangle object that has the dimensions of the image
		# Update the position of this object by setting the values of rect.x and rect.y
		self.rect = self.image.get_rect()

class thumbnail(pygame.sprite.Sprite):

	def __init__(self, suit):
		pygame.sprite.Sprite.__init__(self)
		if suit == c:
			thumbnailPath = "Club.png"
		elif suit == h:
			thumbnailPath = "Heart.png"
		elif suit == d:
			thumbnailPath = "Diamond.png"
		elif suit == s:
			thumbnailPath = "Spade.png"
		self.image = pygame.transform.scale(pygame.image.load(thumbnailPath), (10, 10))
		self.rect = self.image.get_rect()
		
	#Thumbnails
ThumbHeart = thumbnail(h)
ThumbClub = thumbnail(c)
ThumbDiamond = thumbnail(d)
ThumbSpade = thumbnail(s)
		
	#Card Objects
cardH09 = Card(h, 9)
cardH10 = Card(h, 10)
cardH11 = Card(h, 11)
cardH12 = Card(h, 12)
cardH13 = Card(h, 13)
cardH14 = Card(h, 14)
cardS09 = Card(s, 9)
cardS10 = Card(s, 10)
cardS11 = Card(s, 11)
cardS12 = Card(s, 12)
cardS13 = Card(s, 13)
cardS14 = Card(s, 14)
cardD09 = Card(d, 9)
cardD10 = Card(d, 10)
cardD11 = Card(d, 11)
cardD12 = Card(d, 12)
cardD13 = Card(d, 13)
cardD14 = Card(d, 14)
cardC09 = Card(c, 9)
cardC10 = Card(c, 10)
cardC11 = Card(c, 11)
cardC12 = Card(c, 12)
cardC13 = Card(c, 13)
cardC14 = Card(c, 14)

		
		

	#Cards on Table
cardSpaceUp = cardSpace(white, 100, 100)
cardSpaceUp.rect.center=(435, 150)
cardSpaceRight = cardSpace(white, 100, 100)
cardSpaceRight.rect.center=(585, 300)
cardSpaceDown = cardSpace(white, 100, 100)
cardSpaceDown.rect.center=(435, 450)
cardSpaceLeft = cardSpace(white, 100, 100)
cardSpaceLeft.rect.center=(285, 300)
cardSpaceDiscard = cardSpace(white, 100, 100)
cardSpaceDiscard.rect.center=(640, 100)

	#Cards in Hand
cardHand1 = cardSpace(white, 100, 100)
cardHand1.rect.center=(120, 620)
cardHand2 = cardSpace(white, 100, 100)
cardHand2.rect.center=(240, 620)
cardHand3 = cardSpace(white, 100, 100)
cardHand3.rect.center=(360, 620)
cardHand4 = cardSpace(white, 100, 100)
cardHand4.rect.center=(480, 620)
cardHand5 = cardSpace(white, 100, 100)
cardHand5.rect.center=(600, 620)


	#Creating Sprite Group
cardSpaces = pygame.sprite.RenderPlain([cardSpaceUp, cardSpaceRight, cardSpaceDown, cardSpaceLeft, cardSpaceDiscard, cardHand1, cardHand2, cardHand3, cardHand4, cardHand5])
	#Creating Deck Group
Deck = pygame.sprite.RenderPlain([cardH09, cardH10, cardH11, cardH12, cardH13, cardH14, cardS09, cardS10, cardS11, cardS12, cardS13, cardS14, cardD09, cardD10, cardD11, cardD12, cardD13, cardD14, cardC09, cardC10, cardC11, cardC12, cardC13, cardC14])

labelYT = font.render("Your Tricks: ", 1, black)
labelTT = font.render("Their Tricks: ", 1, black)
labelTI = font.render("Trump is: ", 1, black)
	#Main Game Loop
while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()
	
	
	screen.fill(green)
	screen.blit(labelYT, (25,100))
	screen.blit(labelTT, (25,275))
	screen.blit(labelTI, (580, 15))
	cardSpaces.update
	cardSpaces.draw(screen)
	pygame.display.flip()