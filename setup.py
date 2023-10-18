from setuptools import find_packages, setup

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='nextdnsapi',
    packages=find_packages(include=['nextdnsapi']),
    version = '1.7.3',      # Start with a small number and increase it with every change you make
    license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description="I was getting increasingly frustrated with NextDNS's lack of API. I wanted to manage things on the fly. So, I did the most logical thing. I built a python script (library-to-be) to control my NextDNS account. I decided to make it public because why not?",
    author_email = 'contact_NAPI@imx.anonaddy.io',      # Type in your E-Mail
    url = 'https://github.com/IMXEren/nextdnsapi',   # Provide either the link to your github or to your website
    keywords = ['NEXTDNS', 'API', 'REQUESTS'],   # Keywords that define your package best
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=[            # I get to this in a second
           'requests',
           'pyotp'
       ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',      # Define that your audience are developers
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',   # Again, pick a license
        'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    )