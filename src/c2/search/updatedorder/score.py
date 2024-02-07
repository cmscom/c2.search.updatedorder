import math
from datetime import datetime


def _calc_score(pub_date: datetime, score: int) -> int:
    """Calculation score from now

    bonus point:
      if diff days from now < 2: return 5
      else 1 / math.log({diff days from now}, 30)  it means 1/log(days, 30)
    
    return score * bonus point
    """
    now_timestamp = datetime.now().timestamp()
    pub_timestamp = pub_date.timestamp()
    diff_days = (now_timestamp - pub_timestamp) / (24 * 60 * 60)
    if diff_days < 2:
        bonus_point = 5.0
    else:
        bonus_point = 1 / math.log(diff_days, 30)
    new_score = int(score * bonus_point)
    print(f"{score=}, {new_score=}, {pub_date=}, {diff_days=}, {bonus_point=:.2f}")
    return new_score


def _sort_limit_arguments(query):
    """
    refer form https://github.com/zopefoundation/Products.ZCatalog/blob/master/src/Products/ZCatalog/Catalog.py#L497
    """

    b_start = int(query.get('b_start', 0))
    b_size = query.get('b_size', None)
    if b_size is not None:
        limit = b_start + b_size
    else:
        limit = None
    return b_start, limit


def get_sorted_result(items, query=None):
    """
    検索結果のイテラブルオブジェクトを受取、ソート結果を出力する
    """
    if query is not None:
        if query.get("sort_on", None):
            return items  # maybe already sorted
        b_start, limit = _sort_limit_arguments(query)
    else:
        b_start, limit = None, None
    scored_items = []
    for score, data, item_gettier in items:
        item = item_gettier(data)
        new_score = _calc_score(item.Date, score)
        scored_items.append((new_score, item))
    scored_items.sort()  # TODO:
    if b_start is not None and limit is not None:
        limited_items = scored_items[b_start:limit]
    elif b_start is not None:
        limited_items = scored_items[b_start:]
    elif limit is not None:
        limited_items = scored_items[:limit]
    else:
        limited_items = scored_items
    return [i[1] for i in limited_items]
