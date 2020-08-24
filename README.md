# Trade Tracker

![GitHub repo size](https://img.shields.io/github/repo-size/chaixinzhe2000/trade-tracker)
![GitHub contributors](https://img.shields.io/github/contributors/chaixinzhe2000/trade-tracker)
![GitHub stars](https://img.shields.io/github/stars/chaixinzhe2000/trade-tracker?style=social)
![GitHub forks](https://img.shields.io/github/forks/chaixinzhe2000/trade-tracker?style=social)

## Description
Trade Tracker is a simple command line interface that helps users to log and analyse their tradings. The motivation of building this tool derives from my own wish to see my realized profits (or sometimes losses) after I execute a SELL order. The broker that I currently use, Robinhood, does not support this feature.

## Progress
The logging function (along with data validation) is completed. The next step is to write the data into the excel file.

## How to Use this Tool
### Getting Started
First, clone this repository to your local computer:
```
git clone https://github.com/chaixinzhe2000/trade-tracker.git
```
Second, make it a Python executable (you will need Python 3.x and pip installed)

Note: if you have both python 2.x and 3.x on your computer, please use `pip3` instead of `pip` to ensure the correct installation:
```
pip install -e /path/to/script/folder
```
At last, install the dependencies:
```
pip install -r requirements.txt
```
The tool should be able to run by now, by typing the command below:
```
trade -h
```
for a brief usage instruction for the CLI tool.
