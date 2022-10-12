class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        # From slope Eqn
        (x0,y0),(x1,y1) = coordinates[0],coordinates[1]
        for x,y in coordinates[2:]:
            if (x0-x1)*(y1-y) != (x1-x) * (y0-y1):
                return False
        return True
            