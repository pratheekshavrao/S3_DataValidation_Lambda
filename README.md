# Automate real-time data validation of files uploaded into S3

Amazon S3 event triggers enable the automatic initiation of AWS Lambda functions or other AWS services in response to events within an Amazon S3 bucket. These events include actions such as object creation, deletion, or modification. S3 event triggers facilitate real-time processing and automation, allowing developers to build scalable and event-driven architectures.

Within this project, our focus is on activating S3 events, specifically those associated with object creation, to trigger a Lambda function. The Lambda function is designed to validate the data within files uploaded to an S3 bucket. Should the data validation process encounter issues, the file is promptly removed from the original bucket and relocated to an error bucket.

## Steps to execute

1.	Access the AWS console, navigate to S3, and create two buckets using default configurations. Designate one as the origin bucket and the other as the error bucket, ensuring that the names align with their respective purposes.

   ![alt text](https://github.com/pratheekshavrao/S3_DataValidation_Lambda/blob/master/images/Buckets_created.jpg)

2.	Next to create a Lambda function,  navigate to Lambda console. Click on "Create function."Choose a meaningful name for your Lambda function, specify the runtime as Python 3.9, and create a new role.

   ![alt text](https://github.com/pratheekshavrao/S3_DataValidation_Lambda/blob/master/images/Lambda_created.jpg)

3.	For local testing of Lambda functions, download the functions to Cloud9 environment, create event.json and template .yaml files. Use below code from terminal to test the functions.Upon successful local testing, upload the Lambda function code from Cloud9 to AWS Lambda.

   ![alt text](https://github.com/pratheekshavrao/S3_DataValidation_Lambda/blob/master/images/Local_invoke_command.jpeg)

4.	Grant Permissions to Lambda for S3 Access. Attach an IAM policy to the Lambda Execution Role to permit access to S3 buckets.

   ![alt text](https://github.com/pratheekshavrao/S3_DataValidation_Lambda/blob/master/images/Lambda_permissions.jpg)

5.	Create a trigger from the Lambda console by clicking on ‘Add Trigger’. Select S3 as source and also select appropriate origin S3 bucket from which trigger has to be created.Select the Event type as ‘PUT’.

    ![alt text](https://github.com/pratheekshavrao/S3_DataValidation_Lambda/blob/master/images/Create_trigger.jpg)

6.	Upload the file into origin S3 bucket which will trigger the lambda function.

    ![alt text](https://github.com/pratheekshavrao/S3_DataValidation_Lambda/blob/master/images/Input_file_uploaded.jpg)

## Result

The input file is validated and upon failed validation, file is deleted from origin bucket and uploaded into error bucket.

![alt text](https://github.com/pratheekshavrao/S3_DataValidation_Lambda/blob/master/images/file_deleted_origin.jpg)

![alt text](https://github.com/pratheekshavrao/S3_DataValidation_Lambda/blob/master/images/file_copied_error_bucket.jpg)
