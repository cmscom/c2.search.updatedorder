from BTrees.IIBTree import IIBucket
from Products.ZCTextIndex.OkapiIndex import OkapiIndex
from Products.ZCTextIndex.CosineIndex import CosineIndex
from Products.ZCTextIndex.interfaces import IIndex
from zope.interface import implementer
from logging import getLogger

logger = getLogger(__name__)
info = logger.info


def custom_score(original, custom):
    return abs(int(original * 0.5 + custom * -0.5))


@implementer(IIndex)
class OkapiUpdatedIndex(OkapiIndex):
    def __init__(self, lexicon):
        super().__init__(lexicon)
    
    def index_doc(self, docid, text):
        count = super().index_doc(docid, text)
        info("index_doc docid: %s, count: %s", str(docid), str(count))
        return count

    def _search_wids(self, wids):
        info("_search_wids wids: %s", str(wids))
        L = super()._search_wids(wids)
        data = []
        # info("_search_wids L: %s", str(L))
        for doc, score in L:
            result = IIBucket()
            for d, i in doc.items():
                info("doc: %s, i: %s", str(d), str(i))
                result[d] = custom_score(i, d)
            data.append((result, score))
            # info("docid: %s, score: %s", str(docid), str(score))
        info("_search_wids data: %s", str(data))
        info("_search_wids L: %s", str(L))
        return data

    def query_weight(self, tearms):
        info("I don't know what this is ++++++++++++++++++++++ ")
        info("query_weight tearms: %s", str(tearms))
        sum = super().query_weight(tearms)
        info("query_weight sum: %s", str(sum))
        return sum
