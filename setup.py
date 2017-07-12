from setuptools import setup

setup(
    name='tweetreader',
    packages=['tweetreader'],
    include_package_data=True,
    install_requires=[
        'flask',
        'tweepy'
    ]
)
