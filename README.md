# Automate real-time data validation of files uploaded into S3

Amazon S3 event triggers enable the automatic initiation of AWS Lambda functions or other AWS services in response to events within an Amazon S3 bucket. These events include actions such as object creation, deletion, or modification. S3 event triggers facilitate real-time processing and automation, allowing developers to build scalable and event-driven architectures.

Within this project, our focus is on activating S3 events, specifically those associated with object creation, to trigger a Lambda function. The Lambda function is designed to validate the data within files uploaded to an S3 bucket. Should the data validation process encounter issues, the file is promptly removed from the original bucket and relocated to an error bucket.
