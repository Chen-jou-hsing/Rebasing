class Person:  #定義名為 Person 的類別
    def __init__(self):  #初始化方法，建立類別的實例
        self._age = None  # 建立私有變數 _age，用於存放年齡資訊
        self._name = None  # 建立私有變數 _name，用於存放姓名資訊
        self._height = None  # 建立私有變數 _height，用於存放身高資訊
    
    def age(self):
        return self._age  # 回傳 _age 的值

    def age(self, value):
        self._age = value  # 設定 _age 的值為傳入的 value

    def name(self):
        return self._name  # 回傳 _name 的值

    def name(self, value):
        self._name = value  # 設定 _name 的值為傳入的 value
        
    def height(self):
        return self._height  # 回傳 _height 的值

    def height(self, value):
        self._height = value  # 設定 _height 的值為傳入的 value