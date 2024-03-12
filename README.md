# Reservation Zicare
For the Zicare Backend test

## My assumption about this test
My assumption is simple, create an app (Backend services) to reserve or booking an appointment with doctor in some clinic. Of course after you booked the doctor, you get some queue number so the patient can just come and wait in the clinic without creating an appointment on site (the clinic).
I create 6 tables to achieve this feature, below attached the ERD
![zicare_erd](https://github.com/Hyrdie/zicare/assets/33867561/03409042-7fe0-4e57-a90f-11a82f9bb66e)
3 main entities:
1. Clinic
2. Doctor
3. Patient

## Explanation of the project structure
Im using mvc structure (Model View Controller) for this project, inspired when im using java in my 1st company as a backend dev
i think it's easy to read the structure and can be traced easily if there some error

Build with python 3.8 + FastAPI

Docker
====================
to run the project using docker : 
1. create .env file inside the app folder
2. fill the .env file with value from sample.env
3. run the command below
```docker-compose up```

Without Docker
====================
To run the project, you must create and activate the virtual environment first.

Windows : 
```
python3 -m venv env
cd env/Script/activate
```

Linux : 
```
python3 -m venv env
source ./env/bin/activate
```
install dependencies from requirements.txt (file is inside the app folder)
```
pip3 install -r requirements.txt
```

after that, you must create .env file with the value from sample.env
.env is located inside app folder 
app/.env
create folder named "logs" before you run the app
and then you can run it by:
```
make run
```

Documentation
===================
after you run the application, you can hit ```/docs``` to see the swagger documentation generated by fastapi
or you can import the postman collection inside this repo
