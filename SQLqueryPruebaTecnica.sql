CREATE DATABASE foodCom;

USE foodCom;

CREATE TABLE interactions_test (
	user_id BIGINT PRIMARY KEY NOT NULL,
    recipe_id INT NOT NULL,
    `date` DATE NOT NULL,
    rating DOUBLE NOT NULL,
    u INT NOT NULL,
    i INT NOT NULL
    
);

USE foodCom;

CREATE TABLE pp_users (
	u INT PRIMARY KEY NOT NULL,
    techniques VARCHAR(255) NOT NULL,
    items VARCHAR(255) NOT NULL,
    n_items INT NOT NULL,
    ratings VARCHAR(255) NOT NULL,
    n_ratings INT NOT NULL
    
);

USE foodCom;

CREATE TABLE pp_recipes (
    id INT PRIMARY KEY NOT NULL,
    i INT NOT NULL,
    name_tokens VARCHAR(255) NOT NULL,
    ingredient_tokens VARCHAR(255) NOT NULL,
    steps_tokens VARCHAR(255) NOT NULL,
    techniques VARCHAR(255) NOT NULL,
    calorie_level INT NOT NULL
);


