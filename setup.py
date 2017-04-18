from setuptools import setup

setup(name="data_recover",
      version="0.1",
      description="dataRecover",
      url="",
      author="Wen-ting, Chang",
      author_email="wen-ting.chang@ucdconnect.ie",
      licence="GPL3",
      packages=['dataRecover'],
      entry_points={
        'console_scripts':['data_recover=dataRecover.main:main']
        },
      )