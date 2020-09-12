# stackoverflow-searcher-api

API for searching questions on StackOverflow.

### Rough

search view pseudocode

```
quota not left for quota_minute or quota_daily?
  return error
does request.query_params exists in QueryParam table?
yes:
  find the corresponding SearchResult
  return SearchResult
no:
  fetch SearchResult from stackoverflow
  save (QueryParam, Question[], SearchResult) to DB
  return SearchResult
```
