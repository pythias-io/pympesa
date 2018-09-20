from setuptools import setup

setup(name='pympesa',
      version='1.0.2',
      description='Daraja (Mpesa REST API) python library',
      url='https://github.com/pythias-io/pympesa',
      author='Andrew Kamau',
      author_email='andrew@pythias.io',
      license='MIT',
      packages=['pympesa'],
      install_requires=[
          'requests',
      ],
      zip_safe=False)
