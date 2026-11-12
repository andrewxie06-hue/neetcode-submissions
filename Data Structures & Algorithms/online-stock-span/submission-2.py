class StockSpanner:

    def __init__(self):
        self.__stack = []
        self.__left = []
        self.__arr = []
        self.__i = -1

    def next(self, price: int) -> int:
       
        self.__arr.append(price)
        self.__i += 1
        while self.__stack and self.__arr[self.__stack[-1]] <= self.__arr[self.__i]:
            self.__stack.pop()
        if self.__stack:
            #print(self.__i, self.__stack[-1])
            self.__left.append(self.__stack[-1])
        else:
            self.__left.append(-1)
        self.__stack.append(self.__i)
        #print(self.__i, self.__stack, self.__arr, self.__left)
        #print(self.__left)
        return self.__i - self.__left[self.__i]


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)