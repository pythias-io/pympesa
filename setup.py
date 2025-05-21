from setuptools import setup

setup(name='pympesa',
      version='0.3',
      description='Mpesa rest api library',
      url='https://bitbucket.org/pythias_io/pympesa',
      author='Andrew Kamau',
      author_email='andrew@pythias.io',
      license='MIT',
      packages=['pympesa'],
      install_requires=[
          'requests',
      ],
      python_requires='>=3.6',
      classifiers=[
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3.9',
          'Programming Language :: Python :: 3.10',
          'Programming Language :: Python :: 3.11',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
      ],
      zip_safe=False)
