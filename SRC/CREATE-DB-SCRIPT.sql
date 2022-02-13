SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema DbMysql36
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `DbMysql36` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `DbMysql36` ;

-- -----------------------------------------------------
-- Table `DbMysql36`.`Actors` 1
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `DbMysql36`.`Actors` (
  `imdb_id` INT(11) NOT NULL ,
  `name` VARCHAR(45) NOT NULL ,
  `sex` ENUM('Male', 'Female', 'Other') NULL NOT NULL,
  `popularity` FLOAT NULL DEFAULT NULL,
  'adult' INT(11) DEFAULT NULL,
  'deathday'DATE NULL DEFAULT NULL,
  'birthday' DATE NULL DEFAULT NULL, 
  'place_of_birth' VARCHAR(50) NOT NULL,
   PRIMARY KEY (`imdb_id`),
)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

-- -----------------------------------------------------
-- Table `DbMysql36`.`Genres` 2
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `DbMysql36`.`Genres` (
  `id` INT(11) NOT NULL,
  `name` VARCHAR(255) NOT NULL, 
  PRIMARY KEY (`id`)
)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

-- -----------------------------------------------------
-- Table `DbMysql36`.`Movies` 3
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `DbMysql36`.`Movies` (
 `imdb_id`  INT(11) NOT NULL,
  `title` VARCHAR(150) NULL DEFAULT NULL,
  `rating` FLOAT NULL DEFAULT NULL,
  `release_date` DATE NULL DEFAULT NULL,
  `profit` DOUBLE(12,2) NULL DEFAULT NULL, 
  'run_time' INT(11) NULL DEFAULT NULL,
   PRIMARY KEY ('imdb_id'),
)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

-- -----------------------------------------------------
-- Table `DbMysql36`.`Movie_actors` 4
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `DbMysql36`.`Movie_actors` (
  `movie_id` INT(11) NOT NULL,
  `actor_id` INT(11) NOT NULL,
  PRIMARY KEY (`movie_id`, `actor_id`),
  CONSTRAINT `actor_id`
    FOREIGN KEY (`actor_id`)
    REFERENCES `DbMysql36`.`Actors` (`imdb_id`),
  CONSTRAINT `movie_id`
    FOREIGN KEY (`movie_id`)
    REFERENCES `DbMysql36`.`Movies` (`imdb_id`))
)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

-- -----------------------------------------------------
-- Table `DbMysql36`.`Movie_genres` 5
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `DbMysql36`.`Movie_genres` (
  `movie_id` INT(11) NOT NULL,
  `genre_id` INT(11) NOT NULL,
  PRIMARY KEY (`movie_id`, `genre_id`),
  CONSTRAINT `genre_id`
    FOREIGN KEY (`genre_id`)
    REFERENCES `DbMysql36`.`Genres` (`id`),
  CONSTRAINT `movie_id`
    FOREIGN KEY (`movie_id`)
    REFERENCES `DbMysql36`.`Movies` (`imdb_id`)
)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

-- -----------------------------------------------------
-- INDEXING
-- -----------------------------------------------------
CREATE FULLTEXT INDEX title_index ON Movies(title);
CREATE INDEX rating_index ON Movies(rating);
CREATE INDEX profit_index ON Movies(profit);

-- -----------------------------------------------------
-- VIEW
-- -----------------------------------------------------
CREATE VIEW amount_movies_in_db AS
SELECT count(distinct Movies.imdb_id) as amount
FROM Movies
