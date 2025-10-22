---
id: 783a7a2a-44e3-4431-a8e9-65971e931a21
name: Take Screenshots of a List of URLs
type: command
executor: bash
data: aquatone < $_URL_LIST.txt
output: 'root@kali:~/dump# aquatone < hosts.txt

  aquatone v1.7.0 started at 2020-03-06T03:02:34-05:00

  Targets    : 15

  Threads    : 3

  Ports      : 80, 443, 8000, 8080, 8443

  Output dir : .

  http://megabank.com: 200 OK

  http://superfriends.com: 200 OK

  http://cows.com: 200 OK

  ...'
created_at: '2020-03-23T21:07:34.528153+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Take Screenshots of a List of URLs

```bash
aquatone < $_URL_LIST.txt
```

## Expected Output

```
root@kali:~/dump# aquatone < hosts.txt
aquatone v1.7.0 started at 2020-03-06T03:02:34-05:00

Targets    : 15
Threads    : 3
Ports      : 80, 443, 8000, 8080, 8443
Output dir : .

http://megabank.com: 200 OK
http://superfriends.com: 200 OK
http://cows.com: 200 OK
...
```
