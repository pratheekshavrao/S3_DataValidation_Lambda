import csv
import boto3
from datetime import datetime



def lambda_handler(event, context):
    s3 = boto3.resource('s3')

# to get input bucket name and objetc name and also initialize output bucket name    
    billing_bucket = event['Records'][0]['s3']['bucket']['name']
    csv_file = event['Records'][0]['s3']['object']['key']
    error_bucket = 'pra-billing-errors'
    
#to read the contents of object, decode from bytes to string and then split the content by lines 
    obj = s3.Object(billing_bucket, csv_file)
    data = obj.get()['Body'].read().decode('utf-8').splitlines()
    
    
#initialize error flag
    error_flag = False

#set valid product lines and valid currencies from the csv file
    valid_product_lines = ['Bakery','Meat','Dairy']
    valid_currencies = ['USD','MXN','CAD']

#read csv file line by line skipping the header, then extract values of date,product line,currency and bill amount for each row
    for row in csv.reader(data[1:], delimiter = ','):
        date = row[6]
        product_line = row[4]
        currency = row[7]
        bill_amount = float(row[8])
        
#verify if date is in correct format
        try:
            datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            error_flag = True
            print(f"Error in record {row[0]} , incorrect date format {date}")
            break
   
#verify if product line is valid
        if product_line not in valid_product_lines:
            error_flag = True
            print(f"Error in record {row[0]} , invalid product line {product_line}")
            break
        
#verify if currency is valid
        if currency not in valid_currencies:
            error_flag = True
            print(f"Error in record {row[0]} , invalid currency {currency}")
            break
        
#verify if bill amount is negative
        if bill_amount < 0:
            error_flag = True
            print(f"Error in record {row[0]} , invalid bill amount {bill_amount}")
            break


#if any errors in CSV file, copy it to error bucket and delete from billing bucket        
    if error_flag:
        copy_source = {
            'Bucket':  billing_bucket,
            'Key': csv_file
        }
        s3.meta.client.copy(copy_source, error_bucket, csv_file)
        print("Errenous file copied to error bucket")
        s3.Object(billing_bucket,csv_file).delete()
        print("Deleted file from source bucket")
    else:
        print("No errors in CSV file")
        return {
            'statusCode': 200,
            'body': 'No errors in CSV file',
            
    }
