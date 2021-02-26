A series of AWS webinars
========================

Three goals
-----------

- Walk through the basic configuration of a significant number of AWS services over 4-5 webinars.

	+ Each webinar building on the previous ones.

- Provide an opportunity for attendees to develop **hands-on-literacy** with AWS services (in three steps):

	+ **See** - Expose attendees to AWS services/components/concepts using the AWS console (**webinar**).

	+ **Do** - Allow attendees to recreate the steps from the webinar using the awscli (**goingCmdO**).

	+ **Explore** - Allow attendees to become familiar with using the AWS APIs directly (**code samples**)

- **NO SLIDES** - content is publicly available on GitHub.

	+ This session is available at **https://github.com/addr2data/webinar-02**.


|

**UNDER CONSTRUCTION**

|

Webinar-02
==========




Identity and Access Management (IAM)
------------------------------------

- Create user named **webserver**

- Create user named **worker**


Simple Queue Service (SQS)
--------------------------

- Create a queue named **jobs** with the following settings:

    + Visibility timeout: **15 mins**

    + Delivery delay: **0 seconds**

    + Receive message wait time: **20 seconds**

    + Message retention period: **7 days**

    + Maximum message size: **256 KB**

    + Access policy

        Choose method: **Basic**

        Define who can send messages to the queue

            Only the specified AWS accounts, IAM users and roles: 

                Add **webserver**

        Define who can receive messages from the queue

            Only the specified AWS accounts, IAM users and roles:

                Add **worker**
