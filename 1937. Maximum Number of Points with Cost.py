class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        m=len(points)
        n=len(points[0])
        dp=[[0 for x in range(n)] for y in range(m)] 
        for j in range(n):
            dp[0][j]=points[0][j]
        for i in range(1,m):
            for j in range(n):
                for k in range(j,-1,-1):
                    if points[i][j] - abs(j-k) < 0:
                        break
                    if dp[i][j] < dp[i-1][k] + points[i][j] - abs(j-k):
                        dp[i][j] = dp[i-1][k] + points[i][j] - abs(j-k)
                for k in range(j,n):
                    if points[i][j] - abs(k-j) < 0:
                        break
                    if dp[i][j] < dp[i-1][k] + points[i][j] - abs(k-j):
                        dp[i][j] = dp[i-1][k] + points[i][j] - abs(k-j)
        return max(dp[-1])

sln=Solution()
assert 9==sln.maxPoints(points = [[1,2,3],[1,5,1],[3,1,1]])
assert 11==sln.maxPoints(points = [[1,5],[2,3],[4,2]])
assert 85==sln.maxPoints(points = [[1,77,2,3],[5,1,5,1],[3,5,1,1]])
assert 9==sln.maxPoints(points = [[3],[4],[2],[0]])
