import boto3

client = boto3.client('inspector')

'''
response = client.create_assessment_target(
    assessmentTargetName='my-test-target',
    resourceGroupArn='string'
)
'''

response = client.create_assessment_template(
    assessmentTargetArn='arn:aws:inspector:ap-south-1:878611794755:target/0-C4iTLBsR',
    assessmentTemplateName='second-template',
    durationInSeconds=3600,
    rulesPackageArns=[
        "arn:aws:inspector:ap-south-1:162588757376:rulespackage/0-EhMQZy6C", 
        "arn:aws:inspector:ap-south-1:162588757376:rulespackage/0-LqnJE9dO", 
        "arn:aws:inspector:ap-south-1:162588757376:rulespackage/0-PSUlX14m", 
        "arn:aws:inspector:ap-south-1:162588757376:rulespackage/0-fs0IZZBj"
    ],
    userAttributesForFindings=[
        {
            'key': 'Example',
            'value': 'example'
        },
    ]
)

print(response)
