from setuptools import setup, find_packages

try:
    with open('README.md', 'r') as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = ""


setup(
    name='slackbot-queue',
    packages=find_packages(),
    version='0.3.5',
    license='MIT',
    description='Slackbot with a celery queue for long running tasks',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Eddy Hintze',
    author_email="eddy@hintze.co",
    url="https://github.com/xtream1101/slackbot-queue",
    install_requires=['celery==5.0.5',
                      'slackclient==2.9.3'],
)
