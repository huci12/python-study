#클래스
#파이썬 클래스에 속한 것들은 self 라고 한다.

#더블언더스코어 꼭 지킬건 아니지만 클래스 외부에서 접근 하지 못하게 할때


class FishCakeMaker:
    def __init__(self,**kwargs):
        self._size = 10
        self._flaver = "팥"
        self._price = 100
        if "size" in kwargs:
            self._size = kwargs.get("size")
        if "flavor" in kwargs:
            self._flaver = kwargs.get("flavor")
        if "price" in kwargs:
            self._price = kwargs.get("price")
        pass
    def __del__(self):
        print("삭제되었습니다.")
    def __le__(self,other):
        return self._price < other._price
    def __lt__(self,other):
        return self._price <= other._price
    def __gt__(self , other):
        return self._price > other._price
    def __ge__(self,other):
        return self._price >= other._price
    def __eq__(self,other):
        return self._price == other._price
    def __ne__(self,other):
        return self._price != other._price
    def __str__(self):
        return("<class FishCakeMaker (size={},price={},flavor={})>".format(self._flaver,self._price,self._flaver))

    def show(self):
        print("붕어빵 종류 {}".format(self._flaver))
        print("붕어빵 크기 {}".format(self._size))
        print("붕어빵 가격 {}".format(self._price))




fish1 = FishCakeMaker()
fish2 = FishCakeMaker(size=20,price=300)
fish3 = FishCakeMaker(size=20,price=500,flavor="초코")

fish1.show()
fish2.show()
fish3.show()

print(fish1)
#del fish1

if fish1 < fish2 :
    print("fish2가 비싸요")
else :
    print("fish1이 비싸요")


class MarkertGoods(FishCakeMaker):
    def __init__(self,margin=1000,**kwargs):
        super().__init__(**kwargs)
        self._market_price = self._price + margin
    def show(self):
        print(self._flaver,self._market_price)

fish1 = MarkertGoods(size=20 , price=500)

fish1.show()
