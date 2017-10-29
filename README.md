# Inferno

# A RESTful interface for the DPMI Consumer Bitrate 

About DPMI MP:  
  
     --> The MP application taps one or more links and does packet capturing, packet filtering & distribute
     	 measurement data. It then transfers the captured data to the consumers attached to measuring
	 area network(MArN).
  
  
About DPMI BITRATE:  
  
     --> DPMI Bitrate is an consumer application that interfaces with the DPMI MP streams and monitors the 
     	 traffic on different links and interfaces.
     --> By using interface and stream name as arguments, DPMI Bitrate calculates the bits per time sample 
     	 on the interface.
  

About Inferno:
  
     --> Inferno is a RESTful interface which is accessible to the user through a web interface(CURL/Browser) 
     	 to control the measurement streams on bit rate application and be able to store this to a
	 	database and have a data visualization.
 
	Exception: User should have authorized credentials to access the Inferno interface.  
      
Functionalities provided to the user by Inferno RESTful Interface:
  
     The user is able to;
     --> Start a stream: Start a stream to monitor the bitrate traffic on the interface.
     --> Add streams: Add multiple streams to monitor the bitrate traffic on the interface.
     --> Change to another stream: Change to another stream to monitor the bitrate traffic on the interface.
     --> Delete streams: Delete multiple streams to monitor the rest of bitrate traffic on the interface.
     --> Show running streams: Show all streams currently monitoring the bitrate traffic on the interface.
     --> Stop all the streams: Stop all the streams on the interface.
     --> Visualize data of the bitrate traffic in Grafana.

About Design of Inferno:
   
     The Inferno Interface is designed in a way that;
     --> It is easily accessible through a web interface.
     --> Easily control the measurement streams using the control functions.
     --> Provide response messages to the user every time a control function is used to perform some action.
     --> View all the controlled measurement streams at particular point of time.
     --> Provide unique tag for each stream to make data Visualization easy.

REQUIREMENTS:

     1. DPMI REQUIREMENTS:
		a. mp (DPMI Measurement Point)
		b. libcap_utils (DPMI capture utilities)
		c. consumer-bitrate (Bitrate, packetrate, timescale consumers) 
				
     2. SYSTEM REQUIREMENTS:
		a. automake
		b. autoconf
		c. pkg-config
		d. build-essential
		e. libtool
		f. libpcap-dev
		g. libmysqlclient-dev
		h. librrd-dev
		i. libqd-dev
		j. pip
		k. Influxdb 
		l. Influxdb python module
		m. Flask python module 
		n. Grafana
		
INSTALLATIONS:

     Note: First login as root user in order to avoid 'Permission denied' interruptions, at any point of the
     		installation process.	
     
     1. DPMI INSTALLATIONS: 
	
		a. Clone 'mp' from git:
			git clone https://github.com/DPMI/mp.git
			cd mp
			autoreconf -si
			mkdir build && cd build 
			../configure
			make && make install


   		b. Clone 'libcap_utils' from git:
			git clone https://github.com/DPMI/libcap_utils.git
			cd libcap_utils
			autoreconf -si
			mkdir build && cd build
			../configure
			make && make install


   		c. Clone 'consumer-bitrate' from git:
			git clone https://github.com/DPMI/consumer-bitrate.git
			cd consumer-bitrate
			make
	
     2. SYSTEM REQUIREMENT INSTALLATIONS:
   
		a. Install 'automake', 'autoconf', 'pkg-config', 'build-essential', 'libtool', 'libpcap-dev', 
		   'libmysqlclient-dev', 'librrd-dev', 'libqd-dev' packages from APT repository.
	
			Use 'sudo apt-get <package-name>'

		b. Install pip:
	
			sudo apt-get install python-pip python-dev
			sudo pip install --upgrade pip 
	
		c. Install Influxdb:	('https://portal.influxdata.com/downloads')
	
		   	Installing on ubuntu:
	
			wget https://dl.influxdata.com/influxdb/releases/influxdb_1.3.6_amd64.deb
			sudo dpkg -i influxdb_1.3.6_amd64.deb
			sudo service influxdb start
	
		d. Install Influxdb python module:	(InfluxDB-Python)
	
			sudo pip install influxdb
	
		e. Install Flask python module:
	
			sudo pip install Flask
	
		f. Install Grafana:	('http://docs.grafana.org/installation/')
	
			Add the following line to your /etc/apt/sources.list file:
			deb https://packagecloud.io/grafana/stable/debian/ jessie main
	
			Then add the Package Cloud key from terminal:
			curl https://packagecloud.io/gpg.key | sudo apt-key add -

			Update and install grafana:
			sudo apt-get update
			sudo apt-get install grafana
	
			Start grafana server:
			sudo service grafana-server start
     	
INFERNO RESTful Interface:

     The server runs on the default port 5000. The clients can access the server from terminal (using CURL) 
     or the web browser with authorized credentials.
     
     The authorized credentials to access the API are:
		a. username --> dpmi
		b. password --> dpmi
         
     The services provided by the INFERNO:
	
		a. Start stream:	[ Used to start only one stream, use 'addstream' to start multiple]

			curl -u dpmi http://localhost:5000/startstream/<stream>


		b. Add stream:		[ Used to add single/multiple streams ]

			curl -u dpmi http://localhost:5000/addstream/<streams>


		c. Change stream: 	[ Used to change to one stream ]

			curl -u dpmi http://localhost:5000/changestream/<stream>


		d. Delete stream:	[ Used to delete single/multiple streams ]

			curl -u dpmi http://localhost:5000/deletestream/<streams>


		e. Show stream:		[ Used to show all the running streams ]

			curl -u dpmi http://localhost:5000/showstream


		f. stop service:	[ Used to stop all running streams at once]

			curl -u dpmi http://localhost:5000/stop
