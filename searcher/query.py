
from .models import QueryParam


class QueryHandler:
    def __init__(self, search_query: dict):
        self.search_query = search_query

    def get_query_param_from_db(self):
        db_query_params = [qp for qp in QueryParam.objects.all()]

        for qp in db_query_params:
            if self._matches_to_search_query(qp):
                return qp

        return None

    def _matches_to_search_query(self, qp: QueryParam):
        try:
            if self.search_query.get("answers") != None:
                self.search_query["answers"] = int(
                    self.search_query["answers"])
            if self.search_query.get("views") != None:
                self.search_query["views"] = int(self.search_query["views"])
            if self.search_query.get("user") != None:
                self.search_query["user"] = int(self.search_query["user"])

            return qp.q == self.search_query.get("q") \
                and qp.body == self.search_query.get("body") \
                and qp.title == self.search_query.get("title") \
                and qp.url == self.search_query.get("url") \
                and qp.tagged == self.search_query.get("tagged") \
                and qp.nottagged == self.search_query.get("nottagged") \
                and qp.order == self.search_query.get("order") \
                and qp.sort == self.search_query.get("sort") \
                and qp.accepted == bool(self.search_query.get("accepted")) \
                and qp.closed == bool(self.search_query.get("closed")) \
                and qp.migrated == bool(self.search_query.get("migrated")) \
                and qp.wiki == bool(self.search_query.get("wiki")) \
                and qp.notice == bool(self.search_query.get("notice")) \
                and qp.answers == self.search_query.get("answers") \
                and qp.views == self.search_query.get("views") \
                and qp.user == self.search_query.get("user")
        except:
            return False
