-- TO DO : implement an index search

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
  `id` INT(11) NOT NULL ,
  `name` VARCHAR(45) NOT NULL ,
  `gender` ENUM('Male', 'Female', 'Other') NULL DEFAULT NULL,
  `popularity` FLOAT NULL DEFAULT NULL,
   PRIMARY KEY (`id`),
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
-- Table `DbMysql36`.`IMDB_ratings` 3
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `DbMysql36`.'IMDB_ratings' (
  `imdb_id` INT(11) NOT NULL,
   'rating' FLOAT,
   PRIMARY KEY (`imdb_id`),
   )
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

-- -----------------------------------------------------
-- Table `DbMysql36`.`Movies` 4
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `DbMysql36`.`Movies` (
 `id` INT(11) NOT NULL,
 `imdb_id`  INT(11) NOT NULL,
  `title` VARCHAR(150) NULL DEFAULT NULL,
  'language' VARCHAR(10),
  `popularity` FLOAT NULL DEFAULT NULL,
  `release_date` DATE NULL DEFAULT NULL,
  `profit` DOUBLE(12,2) NULL DEFAULT NULL, 
   PRIMARY KEY (`id`, 'imdb_id'),
   CONSTRAINT `imdb_id`
   FOREIGN KEY (`imdb_id`)
   REFERENCES `DbMysql36`.`IMDB_ratings` (`imdb_id`),
)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

-- -----------------------------------------------------
-- Table `DbMysql36`.`Movie_actors` 5
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `DbMysql36`.`Movie_actors` (
  `movie_id` INT(11) NOT NULL,
  `actor_id` INT(11) NOT NULL,
  PRIMARY KEY (`movie_id`, `actor_id`),
  CONSTRAINT `actor_id`
    FOREIGN KEY (`actor_id`)
    REFERENCES `DbMysql36`.`actors` (`id`),
  CONSTRAINT `movie_id`
    FOREIGN KEY (`movie_id`)
    REFERENCES `DbMysql36`.`movies` (`id`))
)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

-- -----------------------------------------------------
-- Table `DbMysql36`.`Movie_genres` 6
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `DbMysql36`.`Movie_genres` (
  `movie_id` INT(11) NOT NULL,
  `genre_id` INT(11) NOT NULL,
  PRIMARY KEY (`movie_id`, `genre_id`),
  CONSTRAINT `genre_id`
    FOREIGN KEY (`genre_id`)
    REFERENCES `DbMysql36`.`Genres` (`id`),
  CONSTRAINT `movie_id_FK`
    FOREIGN KEY (`movie_id`)
    REFERENCES `DbMysql36`.`Movies` (`id`)
)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


