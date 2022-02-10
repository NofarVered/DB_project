SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

CREATE SCHEMA IF NOT EXISTS `DbMysql36` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `DbMysql36` ;

CREATE TABLE IF NOT EXISTS `DbMysql36`.`Actors` (
  `id` INT(11) NOT NULL ,
  `name` VARCHAR(45) NOT NULL ,
  `sex` ENUM('Male', 'Female', 'Other') NULL DEFAULT NULL,
  `birthday` VARCHAR(10) NULL DEFAULT NULL,
  `deathday` VARCHAR(10) NULL DEFAULT NULL,
  `biography` TEXT NULL DEFAULT NULL,
  `popularity` NUMERIC NOT NULL, 
  `imdb_id` VARCHAR(10) NOT NULL,
  `adult` TINYINT(1) DEFAULT 0,
  `homepage` TEXT NULL DEFAULT NULL,
  `profile_path` TEXT NULL DEFAULT NULL,
  `place_of_birth` TEXT NULL DEFAULT NULL,
   primary key (`id`)
  
)
 
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `DbMysql36`.`Genres` (
  `id` INT(11) NOT NULL,
  `name` VARCHAR(45) NOT NULL, 
  
  PRIMARY KEY (`id`)
)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


CREATE TABLE IF NOT EXISTS `DbMysql36`.`Movies` (
 `id` INT(11) NOT NULL PRIMARY KEY,
 `imdbid` VARCHAR(10) NULL DEFAULT NULL,
  `title` VARCHAR(150) NULL DEFAULT NULL,
  `runtime` INT(11) NULL DEFAULT NULL,
  `popularity` FLOAT NULL DEFAULT NULL,
  `poster_path` VARCHAR(64) NULL DEFAULT NULL,
  `release_date` DATE NULL DEFAULT NULL,
  `boxOffice_dollars` DOUBLE(12,2) NULL DEFAULT NULL
)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


CREATE TABLE IF NOT EXISTS `DbMysql36`.`Movie_actors` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `movie_id` INT(11) NOT NULL,
  `actor_id` INT(11) NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `actor_id`
    FOREIGN KEY (`actor_id`)
    REFERENCES `DbMysql36`.`Actors` (`id`),
  CONSTRAINT `movie_id`
    FOREIGN KEY (`movie_id`)
    REFERENCES `DbMysql36`.`Movies` (`id`)
)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `DbMysql36`.`Movie_genres` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `movie_id` INT(11) NOT NULL,
  `genre_id` INT(11) NOT NULL,
  PRIMARY KEY (`id`),
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

CREATE TABLE IF NOT EXISTS `DbMysql36`.`Companies` (
  `company_id` INT(11) NOT NULL, 
  `name` VARCHAR(45) NOT NULL, 
  `description` TEXT NULL DEFAULT NULL, 
  `headquarters` TEXT NULL DEFAULT NULL, 
  `origin_country` VARCHAR(20) NULL DEFAULT NULL, 
  `homepage` TEXT NULL DEFAULT NULL, 
  `logo_path` TEXT NULL DEFAULT NULL,
   PRIMARY KEY (`company_id`)
   
)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `DbMysql36`.`Movie_companies` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `movie_id` INT(11) NOT NULL,
  `company_id` INT(11) NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `company_id`
    FOREIGN KEY (`company_id`)
    REFERENCES `DbMysql36`.`Companies` (`company_id`),
  CONSTRAINT `movie_id_w_company`
    FOREIGN KEY (`movie_id`)
    REFERENCES `DbMysql36`.`Movies` (`id`)
)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

CREATE VIEW Yearly_Revenues AS 
SELECT Companies.company_id, Companies.name, YEAR(x.release_date) AS 'Year', SUM(y.boxOffice_dollars) AS 'revenues'
FROM Companies, Movies x, Movies y, Movie_companies
WHERE Companies.company_id= Movie_companies.company_id AND x.id= Movie_companies.movie_id
AND x.id= y.id
GROUP BY Companies.name, 'Year'
ORDER BY 'revenues';








  



