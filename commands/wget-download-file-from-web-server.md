---
id: 0fee6e18-062c-4e13-983b-fdbb1a4a6f54
type: command
executor: bash
data: 'wget http://$_TARGET_IP/$_FILE'
output: >-
  root@kali:~/# wget http://10.10.10.10/secrets.txt

  --2020-02-19 20:07:45--  http://10.10.10.10/secrets.txt

  Connecting to 10.10.10.10:80... connected.

  HTTP request sent, awaiting response... 200 OK

  Length: 26325 (26K) [text/plain]

  Saving to: ‘secrets.txt’


  secrets.txt                               
  100%[=====================================================================================>] 
  25.71K  --.-KB/s    in 0s      


  2020-02-19 20:07:45 (155 MB/s) - ‘secrets.txt’ saved [26325/26325]
created_at: '2020-03-23T19:45:50.957965+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - Network
  - Download
verified: true
validated: true
---

# wget-download-file-from-web-server

## Command

```bash
wget http://$_TARGET_IP/$_FILE
```

## Description

This command uses Wget to download a specific file from a web server over HTTP. It is useful in security testing for retrieving sensitive files, payloads, or reconnaissance data from a target IP address.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_IP | The IP address or hostname of the target web server | Yes |
| $_FILE | The path to the file to download on the target server | Yes |

## Examples

### Basic Usage

Download a file named 'secrets.txt' from a target at 10.10.10.10.

```bash
wget http://10.10.10.10/secrets.txt
```

### Advanced Usage

Download with output to a specific directory and verbose logging.

```bash
wget -v -P /tmp http://$_TARGET_IP/$_FILE
```

## Expected Output

Description of what output to expect when the command runs successfully.

```
root@kali:~/# wget http://10.10.10.10/secrets.txt
--2020-02-19 20:07:45--  http://10.10.10.10/secrets.txt
Connecting to 10.10.10.10:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 26325 (26K) [text/plain]
Saving to: ‘secrets.txt’

secrets.txt                                100%[=====================================================================================>]  25.71K  --.-KB/s    in 0s      

2020-02-19 20:07:45 (155 MB/s) - ‘secrets.txt’ saved [26325/26325]
```

The file is saved locally with the same name as the remote file, and progress is shown with connection details and transfer speed.

## Related

- [[Related Procedure: Download-Payload-From-Remote-Server]]
- [[commands/curl-download-file]]
