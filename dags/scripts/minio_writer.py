import os
from minio import Minio

def main():
    # Retrieve credentials from environment variables
    minio_endpoint = os.getenv("MINIO_ENDPOINT")
    minio_access_key = os.getenv("MINIO_ACCESS_KEY")
    minio_secret_key = os.getenv("MINIO_SECRET_KEY")

    client = Minio(
        minio_endpoint,
        access_key=minio_access_key,
        secret_key=minio_secret_key,
        secure=False
    )

    # Create bucket if it does not exist
    if not client.bucket_exists("my-bucket"):
        client.make_bucket("my-bucket")

    # Upload a file
    client.put_object(
        "my-bucket", "dummy.txt", data=b"Hello, world!", length=13,
    )

if __name__ == "__main__":
    main()
