---
id: e7a1400b-d67d-4170-be3f-a6bbe007db23
type: command
executor: bash
data: >-
  aws cognito-idp get-user --region us-east-1 --access-token
  eyJraWQiOiJPVjBKWGljSCtpUDAzWTQ2aGdsMWxENG96Z1BZdWZTVFg2aXNKRGlXaHprPSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiIxYjIxOWFkNS05OWMyLTQwNjItYjBiOC1mMDkzNGI3YTdlNmEiLCJldmVudF9pZCI6ImE2N2U5NzUyLWNhZDYtNGRjZS1hZTg0LWIwZjczNjI1OWM4ZiIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoiYXdzLmNvZ25pdG8uc2lnbmluLnVzZXIuYWRtaW4iLCJhdXRoX3RpbWUiOjE2MzY2NTQ3NjUsImlzcyI6Imh0dHBzOlwvXC9jb2duaXRvLWlkcC51cy1lYXN0LTEuYW1hem9uYXdzLmNvbVwvdXMtZWFzdC0xX2dCaWVDd01jMSIsImV4cCI6MTYzNjY1ODM2NSwiaWF0IjoxNjM2NjU0NzY1LCJqdGkiOiI1NTg1NmIyNi02ZTFjLTQxNmYtODk4Ni03YzY0NGFhZTA0NzYiLCJjbGllbnRfaWQiOiIzY2sxNWExb3Y0ZjBkM285N3ZzM3RiamI1MiIsInVzZXJuYW1lIjoiMWIyMTlhZDUtOTljMi00MDYyLWIwYjgtZjA5MzRiN2E3ZTZhIn0.d_Y2H0qKGkJBCcFkSE6HFWpPT2MuY0yR3ULL29HI_NPG128JAdcZ3PhA6gBzFobQDS0Jx9OjJhHWmtFuJDCggvjiuB9AQoRnokgqSNgtewbXF8LRf3d-P6qFHhgn_kpYSKApqBnElOD_iZvnyyWQ2iim10E-mnOECdJ0k_BTG1a4_uHE1ql4rKkI44eyIKUmTP2Z0K0SvRYcy_8YptIe11o_M5evkYYcN1bUGEPh82hr5rSyIz3nfuKbl94LsM4dFXma6qlixVDIghIsHtsqjT8H5z9dR3L6HCDvH7fgcjXyhqa9KmW7xjaODBFryHYcK71MDyPon0A1t2LXnEn7_Q
output: null
created_at: '2025-12-11T06:10:15.720Z'
updated_at: '2025-12-11T06:10:15.721Z'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - aws
  - cognito
  - error-handling
verified: false
validated: true
submitted: true
---

# aws-cognito-get-user-failure

## Command

```bash
aws cognito-idp get-user --region us-east-1 --access-token eyJraWQiOiJPVjBKWGljSCtpUDAzWTQ2aGdsMWxENG96Z1BZdWZTVFg2aXNKRGlXaHprPSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiIxYjIxOWFkNS05OWMyLTQwNjItYjBiOC1mMDkzNGI3YTdlNmEiLCJldmVudF9pZCI6ImE2N2U5NzUyLWNhZDYtNGRjZS1hZTg0LWIwZjczNjI1OWM4ZiIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoiYXdzLmNvZ25pdG8uc2lnbmluLnVzZXIuYWRtaW4iLCJhdXRoX3RpbWUiOjE2MzY2NTQ3NjUsImlzcyI6Imh0dHBzOlwvXC9jb2duaXRvLWlkcC51cy1lYXN0LTEuYW1hem9uYXdzLmNvbVwvdXMtZWFzdC0xX2dCaWVDd01jMSIsImV4cCI6MTYzNjY1ODM2NSwiaWF0IjoxNjM2NjU0NzY1LCJqdGkiOiI1NTg1NmIyNi02ZTFjLTQxNmYtODk4Ni03YzY0NGFhZTA0NzYiLCJjbGllbnRfaWQiOiIzY2sxNWExb3Y0ZjBkM285N3ZzM3RiamI1MiIsInVzZXJuYW1lIjoiMWIyMTlhZDUtOTljMi00MDYyLWIwYjgtZjA5MzRiN2E3ZTZhIn0.d_Y2H0qKGkJBCcFkSE6HFWpPT2MuY0yR3ULL29HI_NPG128JAdcZ3PhA6gBzFobQDS0Jx9OjJhHWmtFuJDCggvjiuB9AQoRnokgqSNgtewbXF8LRf3d-P6qFHhgn_kpYSKApqBnElOD_iZvnyyWQ2iim10E-mnOECdJ0k_BTG1a4_uHE1ql4rKkI44eyIKUmTP2Z0K0SvRYcy_8YptIe11o_M5evkYYcN1bUGEPh82hr5rSyIz3nfuKbl94LsM4dFXma6qlixVDIghIsHtsqjT8H5z9dR3L6HCDvH7fgcjXyhqa9KmW7xjaODBFryHYcK71MDyPon0A1t2LXnEn7_Q
```

## Description

Attempts to retrieve user attributes in AWS Cognito but fails if the user is not registered, used to demonstrate issues after fixes.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--region` | Specifies the AWS region (us-east-1) | Yes |
| `--access-token` | The Cognito access token for authentication | Yes |

## Examples

### Basic Usage

```bash
aws cognito-idp get-user --region us-east-1 --access-token [full_token]
```

### Advanced Usage

```bash
aws cognito-idp get-user --region us-east-1 --access-token [full_token] --output text
```

## Expected Output

Error: UserNotFoundException - User does not exist.

## Related

- [[commands/aws-cognito-get-user]]
- [[procedures/Retrieve-User-Details-via-AWS-CLI]]
