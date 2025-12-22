---
data: |-
  verifier = raw_input('Type in the generated PIN: ').strip()
  auth.get_access_token(verifier)
tags:
  - oauth
  - token-exchange
type: command
output: Access token and secret retrieved
executor: python
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:35.513Z'
id: 126625c2-ee41-4634-aa7e-1c1f03de7a92
verified: false
validated: true
submitted: true
---
# exchange-verifier-for-token

## Command

```python
verifier = raw_input('Type in the generated PIN: ').strip()
auth.get_access_token(verifier)
```

## Description

Prompts for the OAuth verifier PIN and exchanges it for access tokens using a pre-initialized Tweepy auth handler. Essential for completing OAuth after user authorization in Twitter API exploits.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| verifier | 7-digit PIN from Twitter authorization page | Yes |
| auth | Pre-existing Tweepy OAuthHandler instance | Yes |

## Examples

### Basic Usage

```python
verifier = raw_input('Type in the generated PIN: ').strip()
auth.get_access_token(verifier)
print(auth.access_token, auth.access_token_secret)
```

### Advanced Usage

With validation:

```python
verifier = raw_input('Type in the generated PIN: ').strip()
if verifier:
    auth.get_access_token(verifier)
else:
    print('Invalid PIN')
```

## Expected Output

Access token: 12345-abcDEF...
Access token secret: xyz789...

## Related

- [[commands/setup-oauth-handler]]
- [[procedures/Exchange-Verifier-PIN-for-Access-Token]]
