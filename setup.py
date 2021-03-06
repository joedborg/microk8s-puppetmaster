from setuptools import setup


setup(
    name="joule",
    version="0.1.0",
    url="https://github.com/joedborg/joule",
    license="Apache License 2.0",
    author="Joe Borg",
    author_email="joseph.borg@canonical.com",
    description="Drive applications inside auto scale groups",
    packages=[
        "joule",
        "joule.applications",
        "joule.events",
        "joule.providers",
    ],
    install_requires=[
        "backoff",
        "boto3",
        "boto3-stubs[autoscaling,ec2,sqs]",
        "click",
        "ec2-metadata",
        "pyyaml",
    ],
    entry_points={
        "console_scripts": [
            "joule=joule.daemon:main",
        ],
    },
)
