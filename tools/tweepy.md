---
url: 'https://www.tweepy.org/'
tags:
  - twitter-api
  - oauth
  - python-library
type: tool
verified: false
platforms:
  - Web
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:35.484Z'
id: c2e22f80-3345-4655-b254-aaa04e7f9de1
validated: true
submitted: true
---
# tweepy

**Status**: Unverified

## Overview

Tweepy is a Python library for accessing the Twitter API, simplifying OAuth authentication, tweeting, and data retrieval like Direct Messages. Commonly used in security testing for API abuse and credential exploitation scenarios.

## Description

Tweepy handles Twitter's REST and Streaming APIs, supporting OAuth 1.0a for app/user authentication. In offensive security, it's used to script interactions with leaked keys, automate DM fetching, and exploit permission misconfigurations. Features include easy handler setup, token management, and endpoint wrappers.

## Features

- Feature 1: OAuth 1.0a support for consumer and access tokens
- Feature 2: API wrappers for timelines, DMs, users, and searches
- Feature 3: Streaming API for real-time data

## Installation

### Requirements

- Python 2.7+ or 3.5+
- requests library (auto-installed)

### Install Commands

```bash
pip install tweepy
```

## Basic Usage

```python
import tweepy
# See command examples for auth and API calls
```

### Common Options

| Option | Description |
|--------|-------------|
| N/A | Tweepy is a library; options via API methods (e.g., wait_on_rate_limit=True) |
| N/A | Verbose logging via Python logging module |

## Examples

### Example 1: Basic Usage

```python
import tweepy
consumer_key = 'key'
consumer_secret = 'secret'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth)
```

### Example 2: Advanced Usage

```python
# Auth with tokens and fetch DMs
full_auth.set_access_token(token, secret)
api = tweepy.API(full_auth)
print(api.direct_messages())
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Valid Accounts]] Valid Accounts
- [[Use Alternate Authentication Material]] Use Alternate Authentication Material
- [[Data from Information Repositories]] Data from Information Repositories

### Tactics

- [[Initial Access]] Initial Access
- [[Collection]] Collection

## Detection

Indicators and methods for detecting this tool's usage:

- Python processes importing tweepy with suspicious consumer keys
- API logs showing requests from Tweepy user-agent
- Network traffic to api.twitter.com with OAuth patterns

## Related Procedures

- [[procedures/Setup-OAuth-Authentication-with-Leaked-Twitter-Keys]]
- [[procedures/Fetch-Direct-Messages-via-Authenticated-API]]

## Related Tools

- [[requests]] (HTTP library)
- [[twarc]] (Twitter CLI tool)

## References

- Official documentation: https://docs.tweepy.org/
- Twitter API docs: https://developer.twitter.com/en/docs/twitter-api
