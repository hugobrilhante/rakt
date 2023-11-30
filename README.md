# 👋 Hi, I'm Rakt Food Truck App 🍔🚚

Welcome to the Rakt Food Truck App repository! Follow these tasty steps to get your food truck up and running using Docker Compose.

## What You Need Before Ordering

- A hungry appetite 🍴
- Docker installed on your device. Need it? Get it fresh from [Docker's official website](https://www.docker.com/get-started).

## Placing Your Order

1. Open your "food truck window" aka terminal.

2. Place your order with the chef by cloning the repository using this command:
    ```bash
    git clone https://github.com/hugobrilhante/rakt.git
    ```

3. Let's head to the food truck window:
    ```bash
    cd rakt
    ```

## Customizing Your Meal

1. Spice up your dish by finding the secret recipe book named `.env.example` in the food truck's main pantry.

2. Whisper to the chef: "Hey chef, I want to customize my meal!" Rename `.env.example` to `.env` using this magic spell:
    ```bash
    mv .env.example .env
    ```

3. Mix and match ingredients in the `.env` file to personalize your meal just the way you like it.

## Preparing Your Food Truck Kitchen

1. To prepare your food truck, build the Docker containers by running:
    ```bash
    docker compose build
    ```

2. Before starting your food truck, let's set up the kitchen! Execute the following command to perform database migrations:
    ```bash
    docker compose run --rm server python manage.py migrate
    ```

3. Now, it's time to stock up your food truck! Use this command to populate the food trucks in your database using a CSV file:
    ```bash
    docker compose run --rm server python manage.py populate_food_trucks food-truck-data.csv

## Serving Your Order from the Food Truck

1. Check if the food truck is open (aka Docker is running).

2. Now, let's serve your order! Shout out your request to the chef using this command:
    ```bash
    docker compose up -d
    ```

3. Watch the kitchen heat up and the aromas fill the air as your meal gets ready. You'll see [logs](logs) showing the progress.

4. Once your meal is prepared, taste it at [http://localhost:port/nearest-food-trucks/?latitude={latitude}&longitude={longitude}](http://127.0.0.1:8000/nearest-food-trucks/?latitude=37.7749&longitude=-122.4194), where `port` is your food truck's special serving number.

## Closing Time at the Food Truck

1. To close up and rest the food truck, say goodbye with this command:

    ```bash
    docker compose down --volumes
    ```
## Setting Up Your Developer Kitchen

1. Open your terminal.

2. Install `pre-commit` to keep your code tasty and fresh:
    ```bash
    pip install pre-commit
    ```

3. Set up `pre-commit` hooks by navigating to your project directory and running:
    ```bash
    pre-commit install
    ```

## Executing the Taste Tests with Docker Compose

1. Ensure Docker is running on your machine.

2. Run the following command to execute the tests using Docker Compose:
    ```bash
    docker compose run --rm server python manage.py test
    ```
   
## Decisions Made for Production-Ready Application

This Rakt Food Truck App has been crafted with decisions tailored for production:

- Utilization of `django-configurations` library for streamlined configuration management, including URL-based cache, database, email, and search settings.
- Prepared for production with robust logging, containerization, and served using a well-configured Gunicorn server.
- Integration of GeoDjango to efficiently handle geographic coordinates within the application.

## Embracing Learning and Collaboration

I might not be a programming genius, but I'm always eager to learn! Consultation of documentation and forums has been instrumental in resolving challenges faced during development, especially the part regarding GeoDjango, which was something I was familiar with but hadn't yet applied. It's a simple application, but I aimed to cover all areas of real-world application.

That's it! You've successfully set up `pre-commit` hooks, executed tests using Docker Compose after building the containers, and ensured the deliciousness of your Rakt Food Truck App in the development environment. Bon appétit! 🍔🍟🥤
