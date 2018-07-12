import boto3

client = boto3.client('inspector')

response = client.create_exclusions_preview(
    assessmentTemplateArn='arn:aws:inspector:ap-south-1:878611794755:target/0-C4iTLBsR/template/0-1QPmE8E7'
)

print(response)
