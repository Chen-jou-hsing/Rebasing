class Person:  #定義名為 Person 的類別
    def __init__(self):  #初始化方法，建立類別的實例
        self._age = None  # 建立私有變數 _age，用於存放年齡資訊
    
    def age(self):
        return self._age  # 回傳 _age 的值

    def age(self, value):
        self._age = value  # 設定 _age 的值為傳入的 value