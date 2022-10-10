class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        min_dist = math.inf
        ans = -1
        for i in range(len(points)):
            if points[i][0]==x or points[i][1]==y:
                manh_dist = abs(points[i][0]-x) + abs(points[i][1]-y)
                if manh_dist < min_dist:
                    ans =i
                    min_dist = manh_dist
        return ans