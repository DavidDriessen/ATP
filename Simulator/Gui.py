import pygame


class color:
    black = (0, 0, 0)
    white = (255, 255, 255)
    red = (255, 0, 0)
    blue = (0, 0, 255)
    green = (0, 255, 0)
    yellow = (255, 255, 0)
    dark_red = (100, 0, 0)
    dark_blue = (0, 0, 100)
    dark_green = (0, 100, 0)
    dark_yellow = (100, 100, 0)


class button:
    func = None
    font = None
    text = None
    color = color.blue

    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def setFunction(self, func):
        self.func = func
        return self

    def setColor(self, color):
        self.color = color
        return self

    def setText(self, text):
        if self.font:
            self.text = self.font.render(text, True, color.white)
        return self

    def setFont(self, font):
        self.font = font
        return self

    def draw(self, gameDisplay):
        pygame.draw.rect(gameDisplay, self.color, (self.x, self.y, self.w, self.h))
        if self.text:
            gameDisplay.blit(self.text, (
                self.x + self.w / 2 - self.text.get_width() // 2,
                self.y + self.h / 2 - self.text.get_height() // 2))

    def check(self, mousPos):
        if self.x < mousPos[0] < self.x + self.w and self.y < mousPos[1] < self.y + self.h:
            if self.func:
                self.func()


class keypad:
    def __init__(self, x, y, w, h):
        self.buttons = {
            '1': button(x, y, w / 4, h / 4).setColor(color.blue),
            '2': button(x + w / 4, y, w / 4, h / 4).setColor(color.blue),
            '3': button(x + w / 4 * 2, y, w / 4, h / 4).setColor(color.blue),
            'A': button(x + w / 4 * 3, y, w / 4, h / 4).setColor(color.red),
            '4': button(x, y + h / 4, w / 4, h / 4).setColor(color.blue),
            '5': button(x + w / 4, y + h / 4, w / 4, h / 4).setColor(color.blue),
            '6': button(x + w / 4 * 2, y + h / 4, w / 4, h / 4).setColor(color.blue),
            'B': button(x + w / 4 * 3, y + h / 4, w / 4, h / 4).setColor(color.red),
            '7': button(x, y + h / 4 * 2, w / 4, h / 4).setColor(color.blue),
            '8': button(x + w / 4, y + h / 4 * 2, w / 4, h / 4).setColor(color.blue),
            '9': button(x + w / 4 * 2, y + h / 4 * 2, w / 4, h / 4).setColor(color.blue),
            'C': button(x + w / 4 * 3, y + h / 4 * 2, w / 4, h / 4).setColor(color.red),
            '*': button(x, y + h / 4 * 3, w / 4, h / 4).setColor(color.red),
            '0': button(x + w / 4, y + h / 4 * 3, w / 4, h / 4).setColor(color.blue),
            '#': button(x + w / 4 * 2, y + h / 4 * 3, w / 4, h / 4).setColor(color.red),
            'D': button(x + w / 4 * 3, y + h / 4 * 3, w / 4, h / 4).setColor(color.red),
        }

    def draw(self, gameDisplay):
        for key, btn in self.buttons.items():
            btn.draw(gameDisplay)

    def check(self, mousPos):
        for key, btn in self.buttons.items():
            btn.check(mousPos)

    def setFont(self, font):
        for key, btn in self.buttons.items():
            btn.setFont(font).setText(key)
        return self

    def setFunction(self, key, func):
        self.buttons.get(key).setFunction(func)
        return self


class Led:
    status = False

    def __init__(self, x, y, activeColor, inactiveColor):
        self.x = x
        self.y = y
        self.activeColor = activeColor
        self.inactiveColor = inactiveColor

    def on(self):
        self.status = True
        return self

    def off(self):
        self.status = False
        return self

    def set(self, val):
        self.status = val
        return self

    def toggle(self):
        self.status = not self.status
        return self

    def draw(self, gameDisplay):
        if self.status:
            c = self.activeColor
        else:
            c = self.inactiveColor
        pygame.draw.circle(gameDisplay, c, (self.x, self.y), 10)
        pygame.draw.circle(gameDisplay, color.black, (self.x, self.y), 12, 2)


class Containers:
    def __init__(self, x, y, max=2000):
        self.x = x
        self.y = y
        self.max = max
        self.leds = [
            Led(x - 20, y + 50, color.red, color.dark_red),
            Led(x + 430, y + 50, color.red, color.dark_red),
            Led(x - 20, y, color.green, color.dark_green),
            Led(x + 430, y, color.green, color.dark_green),
        ]

    def cup(self, x, y, c, amount, max, gameDisplay):
        pygame.draw.rect(gameDisplay, c, (x + 5, y + 150 - 140 * (amount / max), 100, 140 * (amount / max)))
        pygame.draw.line(gameDisplay, color.black, (x, y), (x, y + 155), 4)
        pygame.draw.line(gameDisplay, color.black, (x, y + 155), (x + 110, y + 155), 4)
        pygame.draw.line(gameDisplay, color.black, (x + 108, y), (x + 108, y + 155), 4)

    def draw(self, gameDisplay, cup1, cup2, cup3):
        self.cup(self.x, self.y + 30, color.blue, cup1, self.max, gameDisplay)
        self.cup(self.x + 150, self.y + 130, color.blue, cup2, self.max, gameDisplay)
        self.cup(self.x + 300, self.y + 30, color.blue, cup3, self.max, gameDisplay)
        pygame.draw.line(gameDisplay, color.black, (self.x + 50, self.y + 40), (self.x + 50, self.y), 4)
        pygame.draw.line(gameDisplay, color.black, (self.x + 350, self.y + 40), (self.x + 350, self.y), 4)
        pygame.draw.line(gameDisplay, color.black, (self.x + 350, self.y), (self.x + 50, self.y), 4)
        pygame.draw.line(gameDisplay, color.black, (self.x + 200, self.y + 140), (self.x + 200, self.y), 4)
        for l in self.leds:
            l.draw(gameDisplay)

    def pump(self, n):
        if n is 1:
            return self.leds[0]
        if n is 2:
            return self.leds[1]

    def valve(self, n):
        if n is 1:
            return self.leds[2]
        if n is 2:
            return self.leds[3]


class GUI:
    display_width = 800
    display_height = 700

    def __init__(self, plant, controller, monitor):
        self.plant = plant
        self.controller = controller
        self.monitor = monitor

        pygame.init()
        self.gameDisplay = pygame.display.set_mode((self.display_width, self.display_height))
        pygame.display.set_caption('A bit Racey')
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("arial", 40)

    def run(self):
        gameExit = False
        containers = Containers(180, 370)
        led = Led(250, 130, color.yellow, color.white)
        pad = keypad(280, 100, 200, 200).setFont(self.font).setFunction('A', self.plant._effectors['pumpA'].switchOn)
        pad.setFunction('B', self.plant._effectors['pumpB'].switchOn )
        pad.setFunction('C', self.plant._effectors['valveA'].switchOn)
        pad.setFunction('D', self.plant._effectors['valveB'].switchOn)
        pad.setFunction('*', self.plant._effectors['ledY'].switchOn)
        pad.setFunction('#', self.plant._effectors['ledY'].switchOff)

        '''
        pad.setFunction('0', )
        pad.setFunction('1', )
        pad.setFunction('2', )
        pad.setFunction('3', )
        pad.setFunction('4', )
        pad.setFunction('5', )
        pad.setFunction('6', )
        pad.setFunction('7', )
        pad.setFunction('8', )
        pad.setFunction('9', )
        '''
        while not gameExit:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pad.check(pygame.mouse.get_pos())

            self.plant.update()
            #self.controller.update()
            #self.monitor.update()

            # gui update
            self.gameDisplay.fill(color.white)

            self.gameDisplay.blit(self.font.render(self.plant._effectors['lcd']._text, True, color.black), (200, 20))

            containers.pump(1).set(self.plant._effectors['pumpA'].isOn())
            containers.pump(2).set(self.plant._effectors['pumpB'].isOn())
            containers.valve(1).set(self.plant._effectors['valveA'].isOn())
            containers.valve(2).set(self.plant._effectors['valveB'].isOn())
            led.set(self.plant._effectors['ledY'].isOn())

            containers.draw(self.gameDisplay, self.plant._vessels['a'].getFluidAmount(),
                            self.plant._vessels['mix'].getFluidAmount(), self.plant._vessels['b'].getFluidAmount())
            pad.draw(self.gameDisplay)
            led.draw(self.gameDisplay)


            pygame.display.update()
            self.clock.tick(60)

        pygame.quit()
        quit()
