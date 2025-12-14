---
data: |-
  full_auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  full_auth.set_access_token(auth.access_token, auth.access_token_secret)
  api = tweepy.API(full_auth)
tags:
  - api-auth
  - twitter
type: command
output: Authenticated API instance
executor: python
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:35.508Z'
id: bf6a7a3c-cb16-43fb-bedd-085e7da2fbb7
verified: false
validated: true
submitted: true
---
# create-authenticated-api

## Command

```python
full_auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
full_auth.set_access_token(auth.access_token, auth.access_token_secret)
api = tweepy.API(full_auth)
```

## Description

Creates a fully authenticated Tweepy API instance using consumer keys and obtained access tokens, allowing calls to protected Twitter endpoints like Direct Messages.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| consumer_key | Official Twitter consumer key | Yes |
| consumer_secret | Official Twitter consumer secret | Yes |
| access_token | User's access token from exchange | Yes |
| access_token_secret | User's access token secret | Yes |

## Examples

### Basic Usage

```python
full_auth = tweepy.OAuthHandler('IQKbtAYlXLripLGPWd0HUA', 'GgDYlkSvaPxGxC4X8liwpUoqKwwr3lCADbz8A7ADU')
full_auth.set_access_token('12345-abc', 'xyz789')
api = tweepy.API(full_auth)
```

### Advanced Usage

With error checking:

```python
try:
    api = tweepy.API(full_auth)
    if not api.verify_credentials():
        print('Authentication failed')
except:
    print('Error creating API')
```

## Expected Output

tweepy.api.API object created successfully.

## Related

- [[commands/fetch-direct-messages]]
- [[procedures/Fetch-Direct-Messages-via-Authenticated-API]]
