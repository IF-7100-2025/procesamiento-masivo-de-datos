# Sending Emails Massively

## Architecture Characteristics to prioritize

- Performance
- Scalability
- Reliability
- Maintainability

## Context

Daily Planet is a news company that has a large number of subscribers. The company receives a lot of emails from all people around the world. People send email for many different reasons, such as to subscribe to the newsletter, to ask for information, to send news tips, and to send complaints. The company needs to process all of them and analyze the content to understand the user's intention. Thus, it classifies the email into different categories and sends a response to the user. The idea is don't lose any email and give an appropriate response to the user. The intention is to send an acknowledgment email in less than 5 minutes after the user sends the email. Then the company will send a response in less than 24 hours. This time is considering human interaction given that some of the answers are not automatic. So it wants to build a system to automate the process of classifying the emails and sending the acknowledgment email.

## Problem

It's necessary to build a service who was constantly checking emails evaluating it and proceed with the acknowledgement email (before 5 min). The service should be able to handle a large number of emails and be able to scale up if the number of emails increases. Then process the email using some mechanism to read automatically the content of the email and then identify it needs to generate an automatic response or redirect to human intervention. In order to obtain metrics, it's to required to generate metrics about how often emails arrive and how long it takes to process them.

## Preconditions

- Generate a small apps who send emails massively.
- For this case, database doesn't matter. The idea is to focus on the email processing.
- Consider to have to respond massively a large number of emails.
- The human intervention is not necessary for this task. It will be enough just to place the email in a queue for further processing.
- Ignore attachments for this task.

## Scoring Parameters

| Characteristic  | Description                                                                          | Scoring Criteria                                                                                                                                                                                      |
|-----------------|--------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Performance     | Measure of the time taken to process and respond to an email.                        | \- Less than ~5 minutes: 5 points<br>\- 5-10 minutes: 3 points<br>\- More than 10 minutes: 1 point                                                                                                    |
| Scalability     | Ability of the system to handle a growing number of emails.                          | \- Easily scalable to accommodate increased emails: 3 points<br>\- Some scalability features, but with limitations: 2 points<br>\- Limited scalability, potential issues with increased load: 1 point |
| Reliability     | The system's ability to process all emails without losing any.                       | \- No emails lost: 3 points<br>\- Few emails lost: 2 points<br>\- Many emails lost: 1 point                                                                                                           |
| Maintainability | Ease of maintaining and updating the email processing and responding implementation. | \- Well-documented code: 3 points<br>\- Modularity and clear structure(Single Responsibility pattern): 2 points<br>\- Lack of documentation or unclear structure: 1 point                             |