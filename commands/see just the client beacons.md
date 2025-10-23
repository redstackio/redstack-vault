---
id: db407a45-637f-4d09-9c26-1283f9b2f0d8
name: see just the client beacons
type: command
executor: bash
data: 'cat sb2-01.csv| cut -d'','' -f7 | sort

  '
output: null
created_at: '2020-07-14T18:14:34.051400+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# see just the client beacons

```bash
cat sb2-01.csv| cut -d',' -f7 | sort

```


