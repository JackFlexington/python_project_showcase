# Webscraping
## Video
[webscrape gif]()

## Libraries used
* pandas
* selenium

## How it works
Though it shows the browser, this is purely for illustrative purposes (and testing)... however everything runs better when the browser is ran in "headless" mode. Meaning the graphical porition of the web browser doesn't render but still exists.

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