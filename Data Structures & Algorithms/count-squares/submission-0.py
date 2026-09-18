class CountSquares:

    def __init__(self):
        self.points = {}

    def add(self, point: List[int]) -> None:
        x,y = tuple(point)
        self.points[(x,y)] = self.points.get((x,y), 0)+1
        

    def count(self, point: List[int]) -> int:
        result = 0
        x,y = point
        for (x2,y2),freq in self.points.items():
            if abs(x2 - x) == abs(y2 - y) and x2 != x:
                result += freq*self.points.get((x2,y),0)*self.points.get((x,y2),0)
        return result