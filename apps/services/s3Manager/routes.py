from apps.services.s3Manager import blueprint
from flask import request
from apps import AWS_ACCESS_KEY, AWS_SECRET_KEY
import boto3

@blueprint.route('/',methods=['GET'])
# Display an HTML list of all s3 buckets.
def s3_list():
    # Let's use Amazon S3
    # s3 = boto3.resource('s3')
    # # Print out bucket names
    # buckets = s3.buckets.all()

    # for b in buckets:
    #     name = b.name

    # buckets = s3.buckets.all()

    return "s3_list1"

    # return render_template("s3_examples/list.html",title="s3 Instances",buckets=buckets)


@blueprint.route('/<id>',methods=['GET'])
#Display details about a specific bucket.
def s3_view(id):
    # s3 = boto3.resource('s3')

    # bucket = s3.Bucket(id)

    # for key in bucket.objects.all():
    #     k = key

    # keys =  bucket.objects.all()

    return "s3_list2"
    # return render_template("s3_examples/view.html",title="S3 Bucket Contents",id=id,keys=keys)


@blueprint.route('/upload',methods=['POST'])
#Upload a new file to an existing bucket
def s3_upload(bucket=None, file=None, filename=None):
    bucketData = bucket or request.form.get('bucket')
    filenameData = filename or request.form.get('filename')
    fileData = file or request.files['file']
    print(bucketData, filenameData, fileData)
    s3 = boto3.client('s3',
        aws_access_key_id=AWS_ACCESS_KEY,
        aws_secret_access_key=AWS_SECRET_KEY,
        region_name='us-east-1')

    s3.upload_fileobj(fileData, bucketData, filenameData)

    return {
        "data": filenameData
    }


@blueprint.route('/delete_images',methods=['POST'])
#Upload a new file to an existing bucket
def s3_delete_all(bucket=None, file=None, filename=None):
    bucketData = bucket or request.form.get('bucket')
    
    s3 = boto3.resource('s3',
        aws_access_key_id=AWS_ACCESS_KEY,
        aws_secret_access_key=AWS_SECRET_KEY,
        region_name='us-east-1')

    bucket = s3.Bucket(bucketData)
    # suggested by Jordon Philips 
    response = bucket.objects.all().delete()

    if response:
        return {"msg": "All object are deleted"}
    else:
        print(response)
        return {"msg": "Something went wrong"}
