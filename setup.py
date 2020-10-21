from setuptools import setup, find_packages

setup(name='c_lasso',
      version='0.3.1.50',
      license='MIT',
      author='Leo Simpson',
      url='https://github.com/Leo-Simpson/CLasso',
      author_email='leo.bill.simpson@gmail.com',
      description='Algorithms for constrained Lasso problems',
      packages=['classo'],
      install_requires = [
                          'numpy',
                          'matplotlib',
                          'pandas',
                          'h5py',
                          'scipy',
                    ],
      long_description_content_type = 'text/markdown',
      long_description=open('README.md').read(),
      zip_safe=False)
