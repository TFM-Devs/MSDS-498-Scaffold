# MSDS-498-Scaffold
Construct a Command Line Tool to Pull Sports Card Pricing Information Using AWS

The purpose of this application is to build a minimum viable product (MVP) of a serverless application that tracks sports card prices. The technologies used were MarketMovers for sports card prices, AWS S3 for cloud storage, AWS lambda for data flow and transformations, AWS DynamoDB for a lightweight cloud database, AWS Cloud 9 for a cloud IDE, Click for a command line tool, and GitHub for source control and CI/CD. 

Here is a quick diagram of how I glued these different technologies together. 

![Indiv Pic 1](https://user-images.githubusercontent.com/67444022/119280432-3f12c900-bbe6-11eb-8286-ed4bab7b8a60.PNG)

All the way on the left is the ultimate source of data for this application. Market movers is a platform that I use to track sports card prices. This platform provides up to date pricing for Basketball, Football, Soccer, and Baseball cards. It provides .csv data download capabilities. This .csv is the starting point file for the rest of the data flow. 
Once a .csv has been downloaded it is manually uploaded to Amazon S3 storage. This manual process could potentially be automated, but for simplicity’s sake it makes sense to keep that manual. Automating this would require website calls that are out of scope. 

Once the .csv is uploaded to S3 this triggers the AWS lambda function that takes the data from the .csv and loads it into AWS Dynamo DB. Here is a sample of the Lambda function code.

![Indiv Pic 2](https://user-images.githubusercontent.com/67444022/119280437-45a14080-bbe6-11eb-83d2-d62e93151929.PNG)

After the function loads the S3 data to DynamoDB it becomes available for use. The front end for the application is a command line tool (CLI) built using the Click python package. With Click I can write flexible command line tools that I can expand, or contract based on changes that I make to the underlying data. Since this is a minimum viable product, I decided to keep it simple and create a command line tool I can use to pull the price information for a given player. Meaning, that when I enter a player’s name into the CLI all the cards that exist in the database will be returned for that player. 

The CLI is built using the boto3 three python package to establish a connection between the python interpreter and the DynamoDB table that holds the pricing information. Using the DynamoDB table scan syntax, the command line tool searches through the database for any card that matches the name that you enter. 
Below is a sample of the code and a sample output from the CLI that shows all the cards in the database for Barry Sanders (my favorite running back).

![Indiv Pic 4](https://user-images.githubusercontent.com/67444022/119280449-5487f300-bbe6-11eb-841e-94557f296e76.PNG)

![Indiv Pic 3](https://user-images.githubusercontent.com/67444022/119280450-5651b680-bbe6-11eb-9f2f-71baab9ad51d.PNG)

[![Python application test with Gihub Actions](https://github.com/TFM-Devs/MSDS-434-Scaffold/actions/workflows/main.yml/badge.svg)](https://github.com/TFM-Devs/MSDS-434-Scaffold/actions/workflows/main.yml)
