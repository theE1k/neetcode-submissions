class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list) 
        self.follows = defaultdict(set)
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.timestamp,tweetId))
        self.timestamp += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        userIds = self.follows[userId] | {userId}
        for uid in userIds:
            tweets = self.tweets[uid]
            if tweets:
                idx = len(tweets) - 1
                timestamp, tweetId = tweets[idx]
                heapq.heappush(heap,(-timestamp,tweetId,uid,idx))
        result = []
        while heap and len(result) < 10:
            timestamp,tweetId,uid,idx = heapq.heappop(heap)
            result.append(tweetId)
            if idx > 0:
                idx -= 1
                t,tid = self.tweets[uid][idx]
                heapq.heappush(heap,(-t,tid,uid,idx))
            
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)
