from setuptools import find_packages,setup
from typing import List

HYPEN_E = "-e ."

def get_requirements(file_name:str)->List[str]:
    '''This function will return all the packages from requirement.txt'''
    requirements=[]
    with open(file_name) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        
        if HYPEN_E in requirements:
            requirements.remove(HYPEN_E)

    return requirements
setup(
    name='mlproject',
    version='0.0.1',
    author='Rushi',
    author_email='rsalvi1814@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)