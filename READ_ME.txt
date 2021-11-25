How to Run with Python(version >= 3.6):
    
    1) Open a terminal in /home/andreas/Documents/CSD/hy583/project/unnamed_project/lib

	2) Run:
	    
	    source hy583/bin/activate
	    
	    // It will activate virtual environment
	    
    3) Run:
    
        python app.py
        
    4) Insert a Measurement ID in textbox and press Generate graph.

How to Run with Docker (You have to istall Docker first):

	1) Open a terminal in /home/andreas/Documents/CSD/hy583/project/unnamed_project

	2) Run:
		
		docker build -t unnamed_project .	

		// It will take some time. Grab a coffee. :)

	3) Run:

		docker run unnamed_project

		// It will run forever, so we need to open a new terminal

	4) Open new terminal wherever we want

	5) Run:

		docker ps

		// In order to find our container

	6) Run:

		docker exec -it <CONTAINER-ID> /bin/bash

		// <CONTAINER-ID> can be found from the output of previous command.
		// This will open a bash in our container

	7) Run:

		python test_hier.py

	8) Run:

		exit

		// To exit this session


How to close docker container:
	
	1) Run in the second terminal that we opened:

		docker stop <CONTAINER-ID>

		// <CONTAINER-ID> is the one that we used before

	2) Run:

		docker ps -as

	3) Run:

		sudo docker rm <CONTAINER-ID>

		// <CONTAINER-ID> can be found from the output of previous command.

	4) Run:

		docker images

	5) Run:

		sudo docker rmi <IMAGE-ID>

		// <IMAGE-ID> can be found from the output of previous command.

	6) Close both terminals and the system is fresh clean.
