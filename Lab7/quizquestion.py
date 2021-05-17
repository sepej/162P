class Box:
    def __init__(self, numSides=6, material="cardboard"):
        self.numSides = numSides
        self.material = material

    def aboutBox(self):
        print("This box has " + str(self.numSides) + " sides and is made of " + self.material)

class TriangleBox(Box):
    def __init__(self, material):
            super().__init__(3, material)

def main():
        tri = TriangleBox("wood")
        # call aboutBox through tri
        tri.aboutBox()

if __name__ == '__main__':
    main()