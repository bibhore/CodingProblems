from Helper.ConfigHelper import configsectionmap
import boto3


class Problem1:
    # take local file and upload to s3
    @staticmethod
    def problem1(localfilename, s3bucket):
        s3Config = configsectionmap('S3Config')
        if not localfilename or not s3bucket:
            return
        s3 = boto3.resource('s3',
                            aws_access_key_id=s3Config['aws_access_key_id'],
                            aws_secret_access_key=s3Config['aws_secret_access_key']
                            )
        data = open(localfilename, 'rb')
        s3.Bucket(s3bucket).put_object(Key='test.jpg', Body=data)