class A:
    def y(self):
        return "A"

class B(A):
    def y(self):
        return super().y() + "B"

class C(A):
    def y(self):
        return super().y() + "C"

class D(B, C):
    def y(self):
        return super().y() + "D"

print(D().y())
