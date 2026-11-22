# Serverless Visitor Counter + Contact Form

A serverless website feature that counts visitors and sends contact form messages without any server.

## How It Works
Visitor opens website -> API Gateway -> Lambda -> DynamoDB (counter +1)
Visitor fills form -> API Gateway -> Lambda -> SES (sends email to me)

## AWS Services Used
- S3 - Hosts website
- CloudFront - Delivers website fast
- Lambda - 2 functions (counter + contact)
- API Gateway - REST API for website to call
- DynamoDB - Stores visitor count
- SES - Sends contact form email

## Files
- index.html - Website with counter + form
- lambda-counter.py - Increments counter in DynamoDB
- lambda-contact.py - Sends form data via SES

## What I Learned
How to build serverless apps, connect frontend to backend with API Gateway, and use DynamoDB + SES without managing servers.
