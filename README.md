# Jublia Send Email Flask

The applicant is to program a simple web application that is able to serve a POST endpoint. The main function of the endpoint is to store in the database an email for a particular group of recipients. The emails are then to be sent automatically at a later time. There are several features that needs to be completed:
- The endpoint should be a POST endpoint with these specs:
    - It should be called ‘/save_emails
    - It should take 4 parameters:
        - event_id (Integer): id of the event. E.g: 1, 2, 12, 24
        - email_subject (String): subject of the email. E.g: “Email Subject”.
        - email_content (String): body of the email. E.g: “Email Body”.
        - timestamp (Timestamp): date and time of which the email should be sent. To be stored as a timestamp object in the database that you are using. E.g: “15 Dec 2015 23:12”
    - Emails of the recipients should be saved in a database, for which you can come up with your own table schema
- Emails saved should be executed according to the timestamp saved. Several hints on how you can do this:
    - A script that constantly check for the time and sends the necessary email
    - Having a queue task that sends the necessary email (bonus points for this approach will be given)
- You can assume the timestamp of the event is UTC+8 (Asia / Singapore).

Optional Criteria
These are some extra features that you could implement to obtain more points:
- Using an ORM to manage your database
- Having your emails saved Unicode compliant
- Building a GUI to manage all this
- Building tests for it
- Packaging the web app
Code consideration:
- Usage and constructions of the Endpoint
- Code quality and maintainability
- Source control familiarity
Extra notes
- The web app must be built in Python 3+, Flask Microframework
- The web app’s source code must be uploaded to a source control environment (Github, Gitlab or Bitbucket)
- Usage of Python libraries is encouraged