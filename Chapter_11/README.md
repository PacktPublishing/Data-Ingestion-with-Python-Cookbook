## Structure of the chapter code

The decision to create this structure is to organize the DAGs and configuration scrips accordingly wit the recipe it is approached.

- /airflow-local
    - This folder contains the base configuration for the Airflow. You can copy the DAGs and other configurations inside here to test the scripts.

- /recipe-names 
    - Inside each recipe folder you will find the respective code approached. If you try to run it alone, it wont work.
    - You need to put the files in the same folder as the airflow-local in order to make it run properly.
