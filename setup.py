from setuptools import setup

setup(name='pympesa',
      version='0.3',
      description='Mpesa rest api library',
      url='https://bitbucket.org/pythias_io/pympesa',
      author='Andrew Kamau',
      license='MIT',
      packages=['pympesa'],
      install_requires=[
          'requests',
      ],
      zip_safe=False)
