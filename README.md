# Cloud Integration Framework<br>

### This is a cloud agnostic framework for easy integration and experimentation between Amazon Web Services (AWS), Azure, and Google Cloud Platform (GCP) using Python.  This cloud integration framework can be useful for building proof of concept (PoC) applications and concepts that need cross cloud platform integration.  Its is an excellent way to speed up your learning in other cloud environments with actual hands on learning and experimentation.<br><br>

# Structure of Files:<br>

### The _'helpers'_ folder has Python class files for GCP, AWS, and Azure functionality.  These frameworks need to be extended with more examples and useful integration code.  The code you write should be built out using object oriented programming (OOP) in Python, and a sepecific class should be written for each specific cloud functionality you want to unit test or integration test between clouds.<br>

### Any code you contribute to the _'helpers'_ folder should have an associated unit or integration test in the _'examples'_ folder.  Helpful generic functions can be found in the _'helpers'_ folder _'generic_helpers.py'_ Python file.  Sample data your unit or integration test creates can be stored in the _'data'_ folder.  Please create a subfolder under the _'data'_ folder so we can better organize the sample data if we get more contributors.<br><br>

# How to Contribute Example:<br>

### If you learn how to use Amazon Lamda Functions, you can come to this repository and add in Lamda API logic for connecting and running a Lamda function in Python in the _'helpers'_ folder and _'aws_helpers.py'_ Python file.  Then you can create a corresponding unit test in the _'examples'_ folder.  If your unit test creates data of any kind sample data can be written to the _'data'_ folder.<br><br>