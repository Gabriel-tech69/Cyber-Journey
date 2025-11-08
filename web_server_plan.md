=== BASIC INFRASTRUCTURE DOCUMENTATION ===

Scenario: Document the setup for a web server accessible from the internet.

Port forwarding is needed in web servers so it is accessible for external devices to connect to a network, since we are trying to access web server which is on port 443 (https), we use port forwarding. 

I would use a stateful firewall so all connection are throughly scanned to deny or allow any connection and packets, since speed is not a rewuirement in connecting to web servers, i use stateful.
