# Elastic Stack - Ingesting Browser History

<em>**Make Browser History More Useful**</em>

If you search for "Browser History", you'll find more post about Privacy, VPNs and other ways to protect your search history. Very few will discuss better ways to use or analyze your browser history. If you do find a solution, it usually show you how to export history to a cvs.

This project's goal is improve the "history search problem" of the major Chromium based browsers.



<img src="./images/brave-logo.png" width="50">&nbsp;&nbsp;&nbsp;&nbsp;<img src="./images/chrome-logo.png" width="50">&nbsp;&nbsp;&nbsp;&nbsp;<img src="./images/edge-logo.png" width="85">&nbsp;&nbsp;&nbsp;&nbsp; <img src="./images/firefox-logo.png" width="50">&nbsp;&nbsp;&nbsp;&nbsp; <img src="./images/safari-logo.png" width="50"> 


Within 10 minutes:


## Instead of that...
![](./images/BrowserHistory.png)

## You can have this...
![](./images/BrowserHistoryDashboard.png)

**Get the most out of three fields!!**
- last_visit_time
- url
- title


#### Prerequisites

Example has been tested on Mac with the following versions:
- Elasticsearch 7.8.0
- Logstash 7.8.0
- Kibana 7.8.0
- Docker 19.03.0
- Docker Compose 1.25.5
