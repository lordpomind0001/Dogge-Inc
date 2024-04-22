from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
long_description = "DICord: 0.6.1dev AI: 2.1.5"
setup(
  name='Doggel_Inc',
  version='1.5.1',
  description='Doggeł Inc packages',
  long_description=long_description,
  url='',  
  author='Lordpomind',
  author_email='lordpomind@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='Doggeł Inc packages', 
  packages=find_packages(),
  install_requires=['aiohttp','websockets'] 
)
