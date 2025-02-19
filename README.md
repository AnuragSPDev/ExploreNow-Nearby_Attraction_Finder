ExploreNow App


ExploreNow App is a user-friendly web application designed to help you find exciting attractions around any city, state, or province. Whether you're planning a trip or just exploring new places, this app makes it easy to discover interesting spots near your chosen location.

Purpose
-------
The main goal of ExploreNow App is to provide users with a convenient way to search for and explore attractions in various locations. Simply enter the name of the place you're interested in, and the app will provide you with a list of nearby attractions.

How It Works
------------
- Search by Place Name: Enter the name of a city, state, or province you're interested in.

- Immediate Results: The app checks its database for existing data. If found, it displays the attractions immediately.

- Fallback Search: If no data is found for the place name, the app performs a search within a 100 km radius around the location to ensure more comprehensive results.

- User-Friendly Interface: The results are displayed in an easy-to-read format with detailed information about each attraction.

Features
--------
- Simple Search: Just enter the name of any city, state, or province.

- Fallback Mechanism: If no direct results are found, the app expands the search radius to find nearby attractions.

- Real-Time Data: Uses third-party APIs to fetch up-to-date information about attractions.

- Loading Spinner: Provides visual feedback during data retrieval to enhance user experience.

- Beautiful Design: Utilizes Bootstrap for a modern and responsive user interface.

Getting Started
---------------
Frontend:

  o The frontend is built using ReactJS.

  o Allows users to enter a place name and view the search results.

Backend:

  o The backend is powered by FastAPI.

  o Handles the search logic, data retrieval, and database storage.

Installation
------------
To run this project locally, follow these steps:

- Clone the repository:

  o bash
    git clone https://github.com/AnuragSPDev/ExploreNow-Nearby_Attraction_Finder.git

- Navigate to the project directory:

  o bash
    cd ExploreNow-App

- Install the required dependencies for the frontend:

  o bash
    cd frontend
    npm install
    npm start

- Install the required dependencies for the backend:

  o bash
    cd backend
    pip install -r requirements.txt
    uvicorn main:app --reload

Contributing
------------
We welcome contributions! If you'd like to contribute to the project, please fork the repository and submit a pull request.

License
-------
This project is licensed under the MIT License.
