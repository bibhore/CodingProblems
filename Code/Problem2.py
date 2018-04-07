from Helper.ConfigHelper import configsectionmap
import boto3
import psycopg2


class Problem2:
    # take local file and upload to s3
    @staticmethod
    def problem2(s3File, redshiftTable):
        s3Config = configsectionmap('S3Config')
        if not s3File or not redshiftTable:
            return
        redshift = boto3.resource('redshift',
                            aws_access_key_id=s3Config['aws_access_key_id'],
                            aws_secret_access_key=s3Config['aws_secret_access_key']
                            )
        con = psycopg2.connect(s3Config['redshift_connect_string']);
        sql = """COPY %s FROM '%s' credentials 
              'aws_access_key_id=%s; aws_secret_access_key=%s'
               delimiter '%s' FORMAT CSV commit;""",
        (redshiftTable, s3File, s3Config['aws_access_key_id'], s3Config['aws_secret_access_key'], ',')
        cursor = con.cursor()
        cursor.execute(sql)
        con.close()