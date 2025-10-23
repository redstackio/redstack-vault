---
id: 73ec73b1-4b81-405c-af96-8f59f8d2af04
type: code
language: Bash
verified: false
created_at: '2020-07-14T18:21:25.723103+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet 73ec73b1

**Language**: Bash

```bash

function start_sshtunnel() {
  ssh -A -t -p22 -L 8800:localhost:8800 james@123.001.123 -t ssh -L 8800:localhost:80 james@124.125.123
}

```


