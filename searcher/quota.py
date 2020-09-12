
class QuotaValidator:
    def has_quota(self):
        if self._has_minute_quota and self._has_daily_quota:
            return True
        return False

    def _has_minute_quota(self):
        # TODO
        return False

    def _has_daily_quota(self):
        # TODO
        return False
