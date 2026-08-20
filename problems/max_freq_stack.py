"""
Maximum Frequency Stack

Design a stack-like data structure to push elements to the stack and pop the most
frequent element from the stack.

Implement the FreqStack class:

    FreqStack() constructs an empty frequency stack.
    void push(int val) pushes an integer val onto the top of the stack.
    int pop() removes and returns the most frequent element in the stack.

    If there is a tie for the most frequent element, the element closest
    to the stack's top is removed and returned.

"""


class FreqStack:
    def __init__(self):
        self.freq = {}
        self.group = {}
        self.maxFreq = -1

    def push(self, val: int) -> None:
        if val not in self.freq:
            self.freq[val] = 0
        self.freq[val] += 1

        f = self.freq[val]

        if f not in self.group:
            self.group[f] = []
        self.group[f].append(val)

        self.maxFreq = max(self.maxFreq, f)

    def pop(self) -> int:
        val = self.group[self.maxFreq].pop()

        self.freq[val] -= 1

        if not self.group[self.maxFreq]:
            self.maxFreq -= 1

        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
