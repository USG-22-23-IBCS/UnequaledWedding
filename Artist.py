import turtle

class Artist:

    def __init__(self, t):
        self.t = t
    
    def triangle(self, size = 100):
        ts = input("set size for triangle\n")
        for i in range(3):
            self.t.right(120)
            self.t.forward(int(ts))

    def square(self, size = 150):
        sqs = input("set size for square\n")
        for i in range(4):
            self.t.right(90)
            self.t.forward(int(sqs))

    def circle(self):
        cs = input("set size for circle\n")
        for i in range (40):
            self.t.right(10)
            self.t.forward(int(cs))

    def star(self):
        for i in range(5):
            self.t.forward(38)
            self.t.penup()
            self.t.forward(24)
            self.t.pendown()
            self.t.forward(38)
            self.t.left(144)

    def polygon(self):
        p = input("type any number for polygon\n")
        for i in range(int(p)):
            self.t.forward(100)
            self.t.right(360/int(p))

    def diamond(self):
        for i in range(2):
            self.t.right(60)
            self.t.forward(100)
            self.t.right(120)
            self.t.forward(100)

    def secondStar(self):
        for i in range(10):
            self.t.forward(100)
            self.t.right(160)
            

    def move(self, x, y):
        self.t.penup()
        self.t.goto(x, y)
        self.t.pendown()

def main():

    canvas = turtle.Screen()
    canvas.bgcolor("green")
    canvas.title("stupid art thing")
    t = turtle.Turtle()
    t.shape("turtle")
    t.speed(0)
    art = Artist(t)
    art.polygon()
    art.move(50,200)
    art.triangle(50)
    art.move(150,200)
    art.square(100)
    art.move(-150,200)
    art.circle()
    art.move(-150,-100)
    art.move(150,-200)
    art.star()
    art.move(100,-200)
    art.diamond()
    art.secondStar()

    
    
    
    


if __name__ == "__main__":
    main()
