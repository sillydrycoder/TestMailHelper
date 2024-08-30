from setuptools import setup, find_packages

setup(
    name='tmclient',
    version='0.1.0',
    author='Your Name',
    author_email='youremail@example.com',
    description='A simple client for the testmail.app API',
    # long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/tmclient',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
