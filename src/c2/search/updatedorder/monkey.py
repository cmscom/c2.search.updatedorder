from Products.ZCTextIndex import ZCTextIndex
from c2.search.updatedorder.okapi_updated_index import OkapiUpdatedIndex
from logging import getLogger

logger = getLogger(__name__)
info = logger.info


add_index_types = {'Okapi BM25 Updated Rank': OkapiUpdatedIndex}

ZCTextIndex.index_types.update(add_index_types)
info("patched %s", str(ZCTextIndex.index_types))
