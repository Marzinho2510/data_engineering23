import boto3

# Define MinIO server configuration
minio_endpoint = "http://localhost:9000"
access_key = "minio_user"
secret_key = "minio_password"
bucket_name = "de-assessment-3"
csv_file_to_upload = r"random_data.csv" 

def create_minio_bucket(s3, bucket_name):
    try:
        s3.create_bucket(Bucket=bucket_name)
        print(f"MinIO bucket '{bucket_name}' created successfully.")
    except Exception as e:
        print(f"Error creating MinIO bucket '{bucket_name}': {str(e)}")

def upload_to_minio(file_name, bucket_name):
    try:
        s3 = boto3.client('s3',
                          endpoint_url=minio_endpoint,
                          aws_access_key_id=access_key,
                          aws_secret_access_key=secret_key,
                          region_name='us-east-1',  # Use a region that your MinIO server is configured with
                          )

        # Check if the bucket exists, and create it if not
        try:
            s3.head_bucket(Bucket=bucket_name)
        except Exception as e:
            if "404" in str(e):
                create_minio_bucket(s3, bucket_name)

        # Upload the file
        s3.upload_file(file_name, bucket_name, file_name)
        print(f"{file_name} uploaded to MinIO bucket: {bucket_name}")

    except Exception as e:
        print(f"Error uploading {file_name} to MinIO: {str(e)}")

if __name__ == '__main__':
    upload_to_minio(csv_file_to_upload, bucket_name)