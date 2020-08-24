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
Second, make it a Python executable (you will need Python 3.x and pip installed). In this step, you need to find the absolute path to the CLI tool, and replace the `/path/to/script/folder` in the following command.

Note: if you have both python 2.x and 3.x on your computer, please use `pip3` instead of `pip` to ensure the correct installation:
```
pip install -e /path/to/script/folder
```
At last, install the dependencies:
```
pip install -r requirements.txt
```
The tool should be able to run by now, try typing the command below:
```
trade -h
```
for a brief usage instruction for the CLI tool.

### Currently Supported Features
This tool is still in development stage, and currently we support the following commands:
`trade log` is used to log the trade data
`trade show` is used to show the summary of your trade (most recent for each ticker)
`trade profit` will output your total profit across all trade up-to-date
