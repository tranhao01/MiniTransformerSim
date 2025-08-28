from setuptools import setup

setup(
    name='mini-transformer-sim',
    version='0.1.0',
    description='Minimal Transformer simulation demonstrating encoder, decoder and cross-attention',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    author='tranhao01',
    url='https://github.com/tranhao01/MiniTransformerSim',
    license='MIT',
    py_modules=['mini_transformer_simulation'],
    install_requires=[
        'numpy',
        'matplotlib',
    ],
    python_requires='>=3.8',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
