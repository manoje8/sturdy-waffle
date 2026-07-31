class A:
    def ping(self):
        print("ping A: ", self)


class B(A):
    def pong(self):
        print("Pong B: ", self)


class C(A):
    def pong(self):
        print("PONG C: ", self)


class D(B, C):
    def ping(self):
        super().ping()
        print("Post-ping D", self)

    def pingpong(self):
        self.ping()
        super().ping()
        self.pong()
        super().pong()
        C.pong(self)


if __name__ == "__main__":
    d = D()
    d.ping()
    print("----------------")
    d.pong()
    print("----------------")
    d.pingpong()
    print(D.__mro__)
