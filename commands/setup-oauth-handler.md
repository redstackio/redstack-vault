---
data: >-
  auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

  auth.secure = True

  auth_url = auth.get_authorization_url()

  print 'Visit this URL and authorise the app to use your Twitter account: ' +
  auth_url
tags:
  - oauth
  - twitter
type: command
output: Printed authorization URL
executor: python
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:35.517Z'
id: 62089d73-1b9f-44e1-b102-1951fb86c025
verified: false
validated: true
submitted: true
---
# setup-oauth-handler

## Command

```python
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.secure = True
auth_url = auth.get_authorization_url()
print 'Visit this URL and authorise the app to use your Twitter account: ' + auth_url
```

## Description

Sets up a Tweepy OAuth handler using Twitter consumer keys and generates an authorization URL for user approval. Use this in scripts exploiting leaked official keys to initiate misleading OAuth flows.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| consumer_key | Official Twitter API consumer key (e.g., 'IQKbtAYlXLripLGPWd0HUA') | Yes |
| consumer_secret | Corresponding consumer secret (e.g., 'GgDYlkSvaPxGxC4X8liwpUoqKwwr3lCADbz8A7ADU') | Yes |
| secure | Enables HTTPS for OAuth (set to True) | No |

## Examples

### Basic Usage

```python
auth = tweepy.OAuthHandler('IQKbtAYlXLripLGPWd0HUA', 'GgDYlkSvaPxGxC4X8liwpUoqKwwr3lCADbz8A7ADU')
auth.secure = True
auth_url = auth.get_authorization_url()
print 'Visit: ' + auth_url
```

### Advanced Usage

Integrate into a full script with error handling:

```python
import tweepy
consumer_key = 'IQKbtAYlXLripLGPWd0HUA'
consumer_secret = 'GgDYlkSvaPxGxC4X8liwpUoqKwwr3lCADbz8A7ADU'
# ... (rest of command)
```

## Expected Output

Visit this URL and authorise the app to use your Twitter account: https://api.twitter.com/oauth/authorize?oauth_token=ABC123...

## Related

- [[commands/exchange-verifier-for-token]]
- [[procedures/Setup-OAuth-Authentication-with-Leaked-Twitter-Keys]]
