
class QuotaValidator:
    daily_quota = 100
    minute_quota = 5

    def has_quota(self):
        if self._has_minute_quota and self._has_daily_quota:
            return True
        return False

    def _has_minute_quota(self):
        # TODO
        return True

    def _has_daily_quota(self):
        # TODO
        return True

    def get_remaining_quota(self):
        # TODO
        return {
            "daily_quota": self.daily_quota,
            "minute_quota": self.minute_quota
        }
