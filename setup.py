import setuptools

with open("README.md", "r") as fh:

    long_description = fh.read()

setuptools.setup(

     name='rrev',  

     version='0.2',

     scripts=['rrev'] ,

     author="Ahmed",

     author_email="ricksy@mailbox.org",

     description="A reverse text utility package",

     long_description=long_description,

   long_description_content_type="text/markdown",

     url="https://github.com/ricksy",

     packages=setuptools.find_packages(),

     classifiers=[

         "Programming Language :: Python :: 3",

         "License :: OSI Approved :: MIT License",

         "Operating System :: OS Independent",

     ],
     project_urls={  
         'Bug Reports': 'https://github.com/ricksy/my_1st_pip_package/issues',
         'Source': 'https://github.com/ricksy/my_1st_pip_package/',
     },
 )

