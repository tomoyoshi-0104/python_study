class TestClass:

    # インスタンスメソッド
    def sample_instancemethod(self, arg_1):
        print('sample_instancemethod')

    # クラスメソッド
    @classmethod
    def sample_classmethod(cls, arg_1):
        print('sample_classmethod')

    # スタティックメソッド
    @staticmethod
    def sample_staticmethod(arg_1, arg_2):
        print('sample_staticmethod')
