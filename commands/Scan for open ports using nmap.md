---
id: 420fcf59-2b61-4b63-8680-d7853aa8ff19
name: Scan for open ports using nmap
type: command
executor: bash
data: '$ nmap -sCV 10.10.10.10 -p 2376

  2376/tcp open  docker  Docker 19.03.5

  | docker-version:

  |   Version: 19.03.5

  |   MinAPIVersion: 1.12'
output: null
created_at: '2023-04-06T03:56:16.968339+00:00'
updated_at: '2023-04-10T20:33:46.886185+00:00'
---

# Scan for open ports using nmap

```bash
$ nmap -sCV 10.10.10.10 -p 2376
2376/tcp open  docker  Docker 19.03.5
| docker-version:
|   Version: 19.03.5
|   MinAPIVersion: 1.12
```


