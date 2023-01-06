# Cyber-Tools
Tool to disable an electric generator via ICS/SCADA server


Python command-line tool that utilizes the PyModBus library to disable an electric generator via the power bit on an ICS/SCADA registry.  

The tool takes the ip, port, and power registry bit of a ICS/SCADA server in order to cycle the power at 7 second increments. 

I was inspired to write this tool after completing the ICS/SCADA rooms on TryHackMe.
