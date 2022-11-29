# Chunk Slice
Chunk Slice is based on https://www.plotz.co.uk/ but allows the user to upload any .STL file. A desired object height can then be set before viewing the object as built with cubes. The, by specifying a layer, the user can view the neccesary blocks to place in that layer. 

## Technologies Used
Flask <br/>
PyMongo <br/>
GridFS 

## Install Locally
A full list of dependencies is found in the requirements.txt file in the root directory. Place the files in a local directory and navigate to the directory containing the requirements.txt file. Run the command below in the terminal to install all dependencies.

     pip3 install -r requirements.txt

Then, naviagte to the bin directory and run the below to start the app

     python3 -m flask run
     
You can view the landing page by going to http://localhost:5000/home

# Planning

## User Stories
As a common user, I want to easily be able to easily upload a file and see the results so that time is not wasted <br/>
As a common user, I want to have an accurate number of blocks needed to construct a build so that I can properly prepare <br/>
As a common user, I want to see what other people have done so that I can build inspiration for my own projects <br/>
As a common user, I want to see the final 3D object along with the cross section so that I can get an understanding of where I am in the progression of the build <br/>
As a common user, I want to change the size of the model so that I can scale the project to my needs <br/>

Home page
![image](https://user-images.githubusercontent.com/92054622/204640449-2a380bd6-6a48-42cd-936a-7b3b7af3b174.png)

List page
![image](https://user-images.githubusercontent.com/92054622/204640489-ac45c2b7-b47e-4066-914b-63620b16d677.png)

View part page
![image](https://user-images.githubusercontent.com/92054622/204640508-e5d336c5-f7e2-4ade-acfb-d4289b215fb4.png)
