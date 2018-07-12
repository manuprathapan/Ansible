import boto3

client = boto3.client('inspector')

response = client.start_assessment_run(
    assessmentTemplateArn='arn:aws:inspector:ap-south-1:878611794755:target/0-C4iTLBsR/template/0-1QPmE8E7',
    assessmentRunName='someName'
)

print(response)
