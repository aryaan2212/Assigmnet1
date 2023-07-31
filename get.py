import boto3
def get_csv_from_s3(bucket_name,s3_key,file_name):
    s3 = boto3.client('s3')
    try:
        s3.download_file(bucket_name,s3_key,file_name)
        print("file download succefully from s3")
    except Exception as e:
        print(f"an error occurred:{str(e)}")
bucket_name = 'fintech5-7722'
file_name = 'test_12.py'
s3_key = 'test_1.py'

get_csv_from_s3(bucket_name,s3_key,file_name)