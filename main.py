import play
class Cell():
  def __init__(self,x,y,color):
    self.x=x
    self.y=y
    self.color=color
    self.sprite = play.new_box(color=self.color,x=self.x,y=self.y,width=24,height=24)
  def move(self,x,y):
    self.x=x
    self.y=y
    self.sprite.go_to(self.x,self.y)
  def getPos(self):
    return {
      'x':self.x,
      'y':self.y
    }
class Snake():
  def __init__(self,x,y,size):
    self.x=x
    self.y=y
    self.size = size
    self.d = 'up'
    self.cells = []
    self.addCell = False
    for i in range(size):
      newC = Cell(self.x,self.y-(i*25),'black')
      self.cells.append(newC)
  def update(self,food,game):
    nextPos = self.cells[0].getPos()
    for c in self.cells[1:]:
      newPos = c.getPos()
      c.move(nextPos['x'],nextPos['y'])
      nextPos = newPos
    if self.addCell:
      self.addCell = False
      self.cells.append(Cell(nextPos['x'],nextPos['y'],'black'))
    oldPos=self.cells[0].getPos()
    if self.d == 'up':
      self.cells[0].move(oldPos['x'],oldPos['y']+25)
    if self.d == 'down':
      self.cells[0].move(oldPos['x'],oldPos['y']-25)
    if self.d == 'left':
      self.cells[0].move(oldPos['x']-25,oldPos['y'])
    if self.d == 'right':
      self.cells[0].move(oldPos['x']+25,oldPos['y'])
    for c in self.cells:
      for cc in self.cells:
        if c.sprite.is_touching(cc.sprite) and c != cc:
          print('touching')
  def setDirection(self,d):
    self.d = d
s = Snake(0,0,7)
@play.when_any_key_pressed
def do(key):
  s.setDirection(key)
@play.repeat_forever
async def game():
  s.update(None,None)
  await play.timer(0.2)
play.start_program()