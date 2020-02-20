##Super easy question about dictionaries
##https://leetcode.com/problems/logger-rate-limiter/submissions/
##don't forget to import lmao
from _collections import *


class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        ##YMU because when they initiate this, you need to do SELF.time
        self.time = defaultdict(int)

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        ##Either it's not in the list yet, or it is, and it's not within last 10 seconds
        ##so you're looking at like 11-1 = 10, that's good so >=
        ##else return false
        ##YMU because you forgot to do self.time, it doesn't know what the object is if you don't ping it
        if message not in self.time or (timestamp - self.time[message]) >= 10:
            self.time[message] = timestamp
            return True
        return False

    # Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)