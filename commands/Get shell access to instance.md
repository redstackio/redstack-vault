---
id: c59fd7ba-a22d-4948-a925-1c0778dd07a1
name: Get shell access to instance
type: command
executor: bash
data: 'gcloud beta compute ssh --zone "<region>" "<instance name>" --project "<project
  name>"

  '
output: null
created_at: '2020-07-14T19:08:34.229762+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Get shell access to instance

```bash
gcloud beta compute ssh --zone "<region>" "<instance name>" --project "<project name>"

```


