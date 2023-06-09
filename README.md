# Grain Saver #

_______________________________________________________________________________________________________________________________________________

## What is Grain Saver? ##
Grain Saver is a mobile application that opens up the channel between crop producers and consumers, forming a closed loop of food production and consumption, making information more open and transparent, helping food supply and demand to achieve a relative balance, and reducing waste of resources. In some parts of the world, it is hard for people to obtain sufficient and sustainable food because of economic shocks, regional conflicts, extreme weather and so on. Due to lack of food, the safety of their lives and property cannot be guaranteed. Grain Saver uses artificial intelligence to help residents in these areas obtain grain planting information in time and grasp weather change in advance, so as to take active measures to ensure grain growth. The steps for users to get assistance are as follows. In the seed selection stage, in view of the harsh environment and technical reasons, we use IBM Watson Studio, GeoJSON, Node-Red to create a smart agricultural assistant: consumers choose the desired crops and yield, combined with the current global land conditions ,such as area, soil quality, climate and other factors, to build a model and recommend a suitable location. In the planting stage, if there is a lack of funds to purchase raw materials such as seeds, we use IBM Watson Studio to build a loan assistant which provides loan strategies and start-up funds according to the user's credit rating in the Bank of China, carbon account status, etc.. After planting , we use Watson IoT Platform to manage soil testing equipment, collect land moisture content and trace element content and  also obtain weather change data through IBM The Weather Company. Based on the  above data, we build models to formulate crop growth and planting strategy models, and reminds farmers to apply fertilizer, weed and irrigate during critical growth stages  to increase food production. When determining planting strategies, carbon emissions are the primary factor under the premise of normal crop growth, and the planting process is recorded under the carbon footprint account. When harvesting crops, consumers can sell grain or process it at their own discretion. If they choose to sell raw materials, the transportation route with the least cost and carbon emissions according to the distance would be planned by models. If they choose to process, the best factory would be recommended based on the size, cost, and carbon emissions of transportation. We use Watson Assistant to train robot assistants, providing knowledge about planting skills and carbon emission to bring technology to the hands of small farmers. In the trading session, we use IBM GeoJSON and Node-Red to build an aggregation platform which provides real-time display of global current food reserves, grain shortage, crop acreage, expected production and other information, to fill in the information gap between food producers and consumers, and opening up the global food trading chain. Users can also see the imbalance between regional production and demand, real-time trading volume and other information, to help a deeper understanding of the world's food insecurity situation, encourage people to start from their own to contribute to global food security. Water Assistant provides solutions for residents in water-poor areas to improve the quality of users’ life. With diverse, advanced AI tools from IBM, Grain Saver opens up the channel between crop producers and consumers, forming a closed loop of food production and consumption, making information more open and transparent, helping food supply and demand to achieve a relative balance, and reducing waste of resources. Each user creates a carbon footprint account, and preferential loan policies and financial assistance are provided for users with excellent carbon footprint to encourage the reduction of carbon emissions, thereby deepening conservation awareness, advocating low-carbon living, and enhancing global sustainability and food security.

## Contents

01. [Short Description](#Short-Description)
02. [Demo Video](#Demo-Video)
02. [Demo APP](#Demo-APP)
03. [How it works](#How-it-works)
06. [Project Roadmap](#Project-Roadmap)
07. [Getting Started](#Getting-Started)
08. [IBM Cloud Services](#IBM-Cloud-Services)
10. [Authors](#Authors)

## Short Description <a name="Short-Description"></a>

### What's the problem?
According to the definition of the Food and Agriculture Organization of the United Nations, food security refers to people's inability to obtain sufficient, safe and nutritious food on a regular basis. The report released by the agency on May 3 pointed out that in 2022, affected by economic shocks, regional conflicts, extreme weather, etc., the global food crisis situation and severe food insecurity will further intensify, and about 258 million people in 58 countries and regions will be severely affected by food crisis.

### How can technology help?

* Planting area recommendation models allowing users to choose a suitable location that is likely to obtain higher yields
* An agricultural assistant helping farmers take action at critical stages of crop growth
* Planning transportation routes based on the distance between producers and consumers and carbon emissions
* Displaying grain information on the aggregation platform in real time, promoting grain transactions to make up for food imbalances 
* Chatting with expert tools through artificial intelligence robots to share knowledge and skills related to  planting skills, carbon emission, food access, etc.

Obtaining real-time planting data, changes in growing conditions for a period of time in the future, and responding to these changes in time are essential to get a good harvest. Transparency in global food information is equally important to alleviating food insecurity. Grain Saver brings advanced Internet of Things technology and artificial intelligence to underdeveloped areas, lowering the threshold of technology use, so that enables everyone in the world get sufficient and sustainable food as well as enjoy the improvement of the quality of life bringing by technological development. With Watson IoT Platform, Cloud Pak for Data, Machine Learning, Watson Assistant and other services provided by IBM, Water Assistant uses PHP, AngularJS, NodeJS, Python, iOS and other technologies to dynamically display real-time grain data and thus help users to know where to buy grain they need. Grain Saver alleviates food insecurity for users from the source by means of early warning and popularization of skills.


## Demo Video <a name="Demo-Video"></a>
[![Demo Video](https://github.com/yaoyao06/Grain-Saver/blob/master/cover.png?raw=ture)](https://www.youtube.com/watch?v=GGQBY8lymJI "DEMO VIDEO")

## Demo APP <a name="Demo-APP"></a>
![picture alt](https://github.com/yaoyao06/Grain-Saver/blob/master/app_1.gif?raw=true)
![picture alt](https://github.com/yaoyao06/Grain-Saver/blob/master/app_2.gif?raw=true)
![picture alt](https://github.com/yaoyao06/Grain-Saver/blob/master/app_3.gif?raw=true)
![picture alt](https://github.com/yaoyao06/Grain-Saver/blob/master/app_4.gif?raw=true)
![picture alt](https://github.com/yaoyao06/Grain-Saver/blob/master/app_5.gif?raw=true)
![picture alt](https://github.com/yaoyao06/Grain-Saver/blob/master/app_6.gif?raw=true)
![picture alt](https://github.com/yaoyao06/Grain-Saver/blob/master/AggregationPlatform.jpg?raw=true)

## How it works <a name="How-it-works"></a>
![picture alt](https://github.com/yaoyao06/Grain-Saver/blob/master/Architecture.png?raw=true)
1. We use IoT soil quality monitoring equipment to monitor water source information, and then store the data in the Cloudant database. IoT Plantform manages these devices so as to gather data,together with weather data from The Weather Company to build which recommend suitable planting locations.
2. In order to eliminate obstacles in the production, harvesting, and sales of food, we train several machine learning models to provide assistance in loans, planting strategies, and sales plan planning. In addition, we have also built a matching platform to make global food information transparent and open, helping users who are food insecure to obtain food with more favorable policies.
3. Constructing a chatting rebot based on Watson Assistant to provide users with self-service inquiries about planting skills and carbon emission knowledge.

## Project Roadmap <a name="Project-Roadmap"></a>
<div  align="center">    
<img src="https://github.com//yaoyao06/Grain-Saver/blob/master/Roadmap.png?raw=true" width="50%" height="50%">
</div>

* In the first stage, we focused on using the Internet of Things technology to monitor soil quality and weather data, build a machine learning model, and provide users with suitable planting locations.
* In the second stage, we pay attention to train models to provide assistance in loans, planting strategies, and sales plan planning. In addition, we have also built a matching platform to make global food information transparent and open, helping users who are food insecure to obtain food with more favorable policies.
* In the third stage, we improve the chatting robot to realize self-service query of planting skills and carbon emission, and thus users would improve their ability to cope with harsh external environments.
## Getting Started <a name="Getting-Started"></a>

#### Prerequisite
* Register for an [IBM Cloud account](https://www.ibm.com/account/reg/us-en/signup?formid=urx-42793&eventid=cfc-2020).
* Request a [Weather Company API key](https://callforcode.weather.com/)
* Register for an [Apple ID](https://appleid.apple.com/account)

#### Run it
* Download the Github code
* Install node.js
* After deploying the nodejs service, start from server.js
* Use Xcode to build an iOS package

## IBM Cloud Services <a name="IBM-Cloud-Services"></a>
* [IBM Cloud Object Storage](https://www.ibm.com/cloud/object-storage)
* [IBM Watson Studio](https://www.ibm.com/cloud/watson-studio)
* [IBM Watson Assistant](https://www.ibm.com/cloud/watson-assistant/)
* [The Weather Company API](https://callforcode.weather.com/)


## Authors <a name="Authors"></a>
* Yao Yao - Product and software developers, system designer
* Jun Ling - Artificial intelligence engineer
* Shen Zhang - Web developer
* Zhouqin Yang - Software developer
* Lu Cheng – UI designer

## License <a name="License"></a>
This project is licensed under the Apache 2 License - see the [ LICENSE ](https://github.com/yaoyao06/Grain-Saver/blob/master/LICENSE)
for details.
