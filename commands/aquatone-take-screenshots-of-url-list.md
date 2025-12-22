---
type: command
executor: bash
data: aquatone < $_URL_LIST
output: |-
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
platforms:
  - Linux
tags:
  - web-enumeration
  - screenshot
verified: true
validated: true
---

# aquatone-take-screenshots-of-url-list

## Command

```bash
aquatone < $_URL_LIST
```

## Description

This command takes screenshots of a list of URLs provided via standard input, scanning common ports and generating visual reports of the HTTP-based attack surface. It uses a headless browser to capture page renders and outputs results to the current directory.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_URL_LIST | Path to a text file containing one URL per line (piped via stdin) | Yes |

## Examples

### Basic Usage

```bash
aquatone < hosts.txt
```

### Advanced Usage

```bash
echo -e "http://example.com\nhttps://test.com" | aquatone --ports 80,443,8080
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

## Related

- [[tools/Aquatone]]
- [[procedures/web-application-enumeration]]
