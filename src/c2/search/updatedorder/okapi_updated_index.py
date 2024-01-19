from Products.ZCTextIndex.OkapiIndex import OkapiIndex


class OkapiUpdatedIndex(OkapiIndex):
    def query_weight(self, tearms):
        sum = super().query_weight(tearms)
        print(sum)
        return sum
