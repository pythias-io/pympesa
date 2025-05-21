from setuptools import setup

setup(name='pympesa',
      version='1.0.2',
      description='Daraja (Mpesa REST API) python library',
      url='https://github.com/pythias-io/pympesa',
      author='Andrew Kamau',
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
