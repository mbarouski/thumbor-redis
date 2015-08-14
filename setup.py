import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="tc_redis",
    version="1.0.0",
    author="Thumbor Community",
    description=("Thumbor redis storage adapters"),
    license="MIT",
    keywords="thumbor redis",
    url="https://github.com/thumbor-community/redis",
    packages=['tc_redis'],
    package_dir={'tc_redis': 'tc_redis'},
    long_description=read('README.md'),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
    ],
    install_requires=[
        'thumbor>=5.0.0',
        'redis'
    ]
)