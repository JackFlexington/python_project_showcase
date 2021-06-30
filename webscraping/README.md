# Web Scraping
## Video
![GIF webscrape](https://github.com/JackFlexington/python_project_showcase/blob/master/webscraping/webscraping.gif)

## Libraries used
* Pandas
* Selenium
* Requests

## How it works
Stitching together to two above Python libraries enables "data scrapeing" with beautiful formatting of table-like datasets. When executing this script, it'll initialize a robot that navigates to "auction.com". Keys in the desired state then iterates through every single listing, compiling information along the way. At the end it spits out the results into a local comma-separated file for review.

### Procedures:
* Start Firefox browser.
* Make a list of hyperlinks displayed on the web page.
  * Loop through said list to grab house specific records.
  * Take these records then append them to the growing list of information.
* Once the script has finished looping through every single house on at the website, commit information to CSV file.
* Quit the browser.

### Notes:
* Had to open up the target website to identify "key" HTML elements.
* Program is less than 100 lines of code.
* Though it shows the browser, this is purely for illustrative purposes (and testing)... things run much better when the browser is executed in "headless" mode. Meaning the graphical porition of the web browser doesn't render but still is able to function.

## Installation:
```bash
pip3 install pandas;
pip3 install selenium;
pip3 install requests;
# Change "headless mode" to "false", so that we can watch the application run
vi webscrape.py;
```

Install geckodriver [Source](https://askubuntu.com/questions/870530/how-to-install-geckodriver-in-ubuntu#871077)
Add gecko drivers to PATH Source: [Using geckodriver - Stack overflow](https://stackoverflow.com/questions/40208051/selenium-using-python-geckodriver-executable-needs-to-be-in-path)
```bash

```
What is headless mode? The application will run without displaying any GUI. (Which means it'll run much faster, as HTML elements don't need to render in like they would in graphical displays).
