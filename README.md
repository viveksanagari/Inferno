# Inferno

# A RESTful interface for the DPMI Consumer Bitrate 

About DPMI MP:  
  --> The MP application taps one or more links and does packet capturing, packet filtering and distribute measurement data. It then transfers the captured data to the consumers attached to measuring area network(MArN).
  
  
About DPMI BITRATE:  
  --> DPMI Bitrate is an consumer application that interfaces with the DPMI MP streams and monitors the traffic on different links and interfaces.
  --> By using interface and stream name as arguments, DPMI Bitrate calculates the bits per time sample on the interface.
  

About Inferno:
  --> Inferno is a RESTful interface which is accessible to the user through a web interface (CURL / Browser) to control the measurement streams on bit rate application and be able to store this to a database and have a data visualization.
 
    Exception: User should have authorized credentials to access the Inferno interface.  
      
Functionalities provided to the user by Inferno RESTful Interface:
  The user is able to;
  --> Start a stream: Start a stream to monitor the bitrate traffic on the interface.
	--> Add streams: Add multiple streams to monitor the bitrate traffic on the interface.
	--> Change to another stream: Change to another stream to monitor the bitrate traffic on the interface.
	--> Delete streams: Delete multiple streams to monitor the rest of the bitrate traffic on the interface.
	--> Show running streams: Show all the streams currently monitoring the bitrate traffic on the interface.
	--> Stop all the streams: Stop all the streams on the interface.
	--> Visualize data of the bitrate traffic in Grafana.

About Design of Inferno:
   The Inferno Interface is designed in a way that;
   --> It is easily accessible through a web interface.
   --> Easily control the measurement streams using the control functions.
   --> Provide response messages to the user every time a control function is used to perform some action.
   --> View all the controlled measurement streams at particular point of time.
   --> Provide unique tag for each stream to make data Visualization easy.
