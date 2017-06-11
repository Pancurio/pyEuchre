import sys, pygame
pygame.init()

size = width, height = 720, 720
green = 70, 150, 80
white = 255, 255, 255
red = 255, 0, 0

screen = pygame.display.set_mode(size)

	#Creating class for cards
class Card(pygame.sprite.Sprite):

	def __init__(self, suit, number):
		pygame.sprite.Sprite.__init__(self)
		strSuit = str(suit)
		strNumber = str(number)
		cardPath = strSuit + strNumber + ".png"
		self.image = pygame.image.load(cardPath)
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


	#Card Objects
for i in 

	#Cards on Table
cardSpaceUp = cardSpace(green, 100, 100)
cardSpaceUp.rect.center=(360, 150)
cardSpaceRight = cardSpace(green, 100, 100)
cardSpaceRight.rect.center=(540, 300)
cardSpaceDown = cardSpace(green, 100, 100)
cardSpaceDown.rect.center=(360, 450)
cardSpaceLeft = cardSpace(green, 100, 100)
cardSpaceLeft.rect.center=(180, 300)
cardSpaceDiscard = cardSpace(green, 100, 100)
cardSpaceDiscard.rect.center=(640, 100)

	#Cards in Hand
cardHand1 = cardSpace(green, 100, 100)
cardHand1.rect.center=(120, 620)
cardHand2 = cardSpace(green, 100, 100)
cardHand2.rect.center=(240, 620)
cardHand3 = cardSpace(green, 100, 100)
cardHand3.rect.center=(360, 620)
cardHand4 = cardSpace(green, 100, 100)
cardHand4.rect.center=(480, 620)
cardHand5 = cardSpace(green, 100, 100)
cardHand5.rect.center=(600, 620)


	#Creating Sprite Group
cardSpaces = pygame.sprite.RenderPlain([cardSpaceUp, cardSpaceRight, cardSpaceDown, cardSpaceLeft, cardSpaceDiscard, cardHand1, cardHand2, cardHand3, cardHand4, cardHand5])


	#Main Game Loop
while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()
	
	
	screen.fill(green)
	cardSpaces.update
	cardSpaces.draw(screen)
	pygame.display.flip()