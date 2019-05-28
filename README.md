# FreshWorks-CRD

1.  **Initializing 'mydatastore.txt'**\
      The program will create a file named 'mydatastore.txt' in the present working directory.\
      If you want to create the file in any specific location, press 'y' when prompted. \
      Please provide the Absolute Path of the directory in which you want to create the 'mydatastore.txt'\

2.  **Operations and their arguments**\
      There are 4 operations that you can perform\
      - create(key,value,time_to_live)\
        
        This operation creates a new record in the datastore.\
        The key and value arguments are **required**, whereas time_to_live is **optional**,which takes a default value of 1.\
        The key is a string of upto 32 characters.\
        The value is a JSON object which can be upto 16KB. I was confused if the user will be wants to provide a path to the JSON file. However I have written the code assuming that the contents of the JSON file will be passed.\
        The time_to_live is an integer denoting the number of seconds the record has to be stored.\
        
        *Example*
        ```
        create(Mark,{Id: 7, Company: Facebook Inc, Occupation: CEO},10)
        Record created successfully!      #o/p
        ```
        This will create a record in mydatastore.txt as 
        ```
        Mark - {Id: 7, Company: Facebook Inc, Occupation: CEO}
        ```
        This record will be deleted after 10 seconds. If no time_to_live was provided, the record will be permanent unless deleted by the user.\
        Other responses provided by this operation are as follows
        ```
        Parameter(s) exceed limit                 #When either key or value argument breaches limit
        Record with '"+key+"' already exists.     #When the user tries to create another record with the existing key
        Data Store exceeds 1 GB                   #When the size of datastore exceed 1 GB
        ```
        
       - read(key)
       
         This operation retrieves a particular record based on the key provided.\
         Key is passed as an argument.\
         
         *Example*
         ```
         read(Mark)
         Mark - {Id: 7, Company: Facebook Inc, Occupation: CEO} #o/p
         ```
       - delete(key)
       
         This operation deletes a particular record from the datastore.\
         Key is passed as an argument.\
         
         *Example*
         ```
         delete(Mark)
         Record 'Mark' Deleted successfully! #o/p
         ```
         
       - exit()
         This operation is used end the program. No argument is needed.\
         
