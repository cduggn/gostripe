import setuptools


with open("README.md") as fp:
    long_description = fp.read()


setuptools.setup(
    name="eventbridge_stripe_go",
    version="0.0.1",

    description="A sample CDK Python app",
    long_description=long_description,
    long_description_content_type="text/markdown",

    author="author",

    package_dir={"": "eventbridge_stripe_go"},
    packages=setuptools.find_packages(where="eventbridge_stripe_go"),

    install_requires=[
        "aws-cdk.core==1.64.1",
        "aws-cdk.core==1.62.0",
        "aws-cdk.aws_iam==1.64.1",
        "aws-cdk.aws_sqs==1.64.1",
        "aws-cdk.aws_sns==1.64.1",
        "aws-cdk.aws_sns_subscriptions==1.64.1",
        "aws-cdk.aws_s3==1.64.1",
        "aws-cdk.aws_dynamodb==1.64.1",
        "aws-cdk.aws_apigateway==1.64.1",
        "aws-cdk.aws_lambda==1.64.1",
        "aws-cdk.aws-events==1.64.1",
        "aws-cdk.aws-events-targets==1.64.1",
        "aws-cdk.aws-lambda-destinations==1.64.1",
    ],

    python_requires=">=3.6",

    classifiers=[
        "Development Status :: 4 - Beta",

        "Intended Audience :: Developers",

        "License :: OSI Approved :: Apache Software License",

        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",

        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",

        "Typing :: Typed",
    ],
)
