CREATE DATABASE  IF NOT EXISTS `sql_ssis` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `sql_ssis`;
-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: sql_ssis
-- ------------------------------------------------------
-- Server version	8.0.36

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `course`
--

DROP TABLE IF EXISTS `course`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `course` (
  `course_code` varchar(10) NOT NULL,
  `course_name` varchar(60) DEFAULT NULL,
  PRIMARY KEY (`course_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `course`
--

LOCK TABLES `course` WRITE;
/*!40000 ALTER TABLE `course` DISABLE KEYS */;
INSERT INTO `course` VALUES ('BAH','Bachelor of Arts in Helena'),('BSA','Bachelor of Science in Accountancy'),('BSB','bachelors of science in bogart'),('BSBM','Bachelor of Science in Business Management'),('BSCA','Bachelor of Science in Computer Application'),('BSCE','Bachelor of Science in Civil Engineering'),('bsco','bachelors in blah'),('BSComEng','Bachelor of Science in Computer Engineering'),('BSCS','Bachelor of Science in Computer Science'),('BSE','Bachelor of Science in Economics'),('BSEE','Bachelor of Science in Electrical Engineering'),('BSIS','Bachelor of Science in Information System'),('BSIT','Bachelor of Science in Information Technology'),('BSjk','bushyy'),('BSME','Bachelor of Science in Mechanical Engineering'),('BSN','Bachelor of Science in Nursing'),('BSPhy','Bachelor of Science in Physics'),('BSPsych','Bachelor of Science in Pyschology'),('BSStats','Bachelor of Science in Statistics'),('bushy','bachelors bogart');
/*!40000 ALTER TABLE `course` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student` (
  `ID_number` varchar(9) NOT NULL,
  `student_name` varchar(50) DEFAULT NULL,
  `gender` varchar(30) NOT NULL,
  `year_lvl` varchar(50) DEFAULT NULL,
  `course_code` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`ID_number`),
  KEY `fk_course_code` (`course_code`),
  CONSTRAINT `fk_course_code` FOREIGN KEY (`course_code`) REFERENCES `course` (`course_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student`
--

LOCK TABLES `student` WRITE;
/*!40000 ALTER TABLE `student` DISABLE KEYS */;
INSERT INTO `student` VALUES ('1989-1313','Taylor Sheesh','female','2nd year','BSA'),('2019-3423','Leonardo Dicaprio','male','2nd year',NULL),('2020-0006','Selena Marie L. Gomez','female','3rd year','BSCS'),('2021-3134','Karen G. Smith','female','2nd year','BSCE'),('2021-5736','Merlia P. Summers','female','2nd year','BSCE'),('2021-7823','Sabrina Y. Yap','female','3rd year','BSN'),('2021-7879','Sabrina Y. Yap','female','3rd year','BSN'),('2023-0001','Kevin D. Mcdonald','male','1st year','BSME'),('2023-0003','Devon D. Mcdonald','male','1st year','BSEE'),('2023-1112','Eli Y. Jong','male','1st year','BSIT'),('2023-1235','John Doe','male','1st year','BSN'),('2023-1236','Michael Davis','male','3rd year','BSCS'),('2023-1237','James Evans','male','1st year','BSIS'),('2023-1238','William Roberts','male','3rd year','BSN'),('2023-1239','John Reyes','male','1st year','BSCS'),('2023-1240','Michael Reed','male','3rd year','BSIS'),('2023-1241','James Ford','male','1st year','BSN'),('2023-1242','William Carr','male','3rd year','BSCS'),('2023-1243','John Peters','male','1st year','BSIS'),('2023-1327','Lou Grace R. Yanong','female','1st year','BSComEng'),('2023-2133','Lance T. Elliot','male','1st year','BSEE'),('2023-2173','Lance T. Elliot','male','1st year','BSEE'),('2023-2346','John Lee','male','1st year','BSPhy'),('2023-2347','Michael Hall','male','3rd year','BSCE'),('2023-2348','James Parker','male','1st year','BSBM'),('2023-2349','William Nelson','male','3rd year','BSPhy'),('2023-2350','John Bell','male','1st year','BSCE'),('2023-2351','Michael Kelley','male','3rd year','BSBM'),('2023-2352','James Grant','male','1st year','BSPhy'),('2023-2353','William Gilbert','male','3rd year','BSCE'),('2023-3457','William Taylor','male','3rd year','BSME'),('2023-3458','John Harris','male','1st year','BSComEng'),('2023-3459','Michael Hill','male','3rd year','BSIT'),('2023-3460','James Morris','male','1st year','BSME'),('2023-3461','William Hoffman','male','3rd year','BSComEng'),('2023-3462','John Diaz','male','1st year','BSIT'),('2023-3463','Michael Kennedy','male','3rd year','BSME'),('2023-3464','James Ferguson','male','1st year','BSComEng'),('2023-3465','William Bradley','male','3rd year','BSIT'),('2023-4273','Brad F. Evans','male','1st year','BSEE'),('2023-4279','Brad F. Evans','male','1st year','BSEE'),('2023-4322','Olivia Martinez','female','2nd year','BSIS'),('2023-4323','Jane Moore','female','4th year','BSN'),('2023-4324','Emily Lewis','female','2nd year','BSCS'),('2023-4325','Sophia Diaz','female','4th year','BSIS'),('2023-4326','Olivia Griffin','female','2nd year','BSN'),('2023-4327','Jane Russell','female','4th year','BSCS'),('2023-4328','Emily Dixon','female','2nd year','BSIS'),('2023-4329','Sophia Hart','female','4th year','BSN'),('2023-4330','Olivia Schmidt','female','2nd year','BSCS'),('2023-5433','Sophia Brown','female','4th year','BSCE'),('2023-5434','Olivia White','female','2nd year','BSBM'),('2023-5435','Jane Young','female','4th year','BSPhy'),('2023-5436','Emily Carter','female','2nd year','BSCE'),('2023-5437','Sophia Coleman','female','4th year','BSBM'),('2023-5438','Olivia Powell','female','2nd year','BSPhy'),('2023-5439','Jane Fisher','female','4th year','BSCE'),('2023-5440','Emily Jacobs','female','2nd year','BSBM'),('2023-5441','Sophia Simmons','female','4th year','BSPhy'),('2023-5670','Sophia Smith','female','4th year','BSIT'),('2023-5671','Olivia Baker','female','2nd year','BSME'),('2023-5672','Jane Morgan','female','4th year','BSComEng'),('2023-5673','Emily Foster','female','2nd year','BSIT'),('2023-5674','Sophia Richardson','female','4th year','BSME'),('2023-5675','Olivia Warren','female','2nd year','BSComEng'),('2023-5676','Jane Rose','female','4th year','BSIT'),('2023-5677','Emily Chambers','female','2nd year','BSME'),('2023-5679','Emily Johnson','female','2nd year','BSComEng'),('2023-6744','Lou Grace R. Yanong','female','1st year','BSCS'),('2023-6780','Emily Brown','female','2nd year','BSStats'),('2023-6781','Sophia King','female','4th year','BSPsych'),('2023-6782','Olivia Wright','female','2nd year','BSE'),('2023-6783','Jane Rivera','female','4th year','BSStats'),('2023-6784','Emily Cooper','female','2nd year','BSPsych'),('2023-6785','Sophia Hayes','female','4th year','BSE'),('2023-6786','Olivia Castillo','female','2nd year','BSStats'),('2023-6787','Jane Burns','female','4th year','BSPsych'),('2023-7891','Jane Anderson','female','4th year','BAH'),('2023-7892','Emily Thompson','female','2nd year','BSEE'),('2023-7893','Sophia Moore','female','4th year','BSA'),('2023-7894','Olivia Adams','female','2nd year','BAH'),('2023-7895','Jane Ramirez','female','4th year','BSEE'),('2023-7896','Emily Myers','female','2nd year','BSA'),('2023-7897','Sophia Alvarez','female','4th year','BAH'),('2023-7898','Olivia Dean','female','2nd year','BSEE'),('2023-7899','Jane Chapman','female','4th year','BSA'),('2023-8766','James Wilson','male','1st year','BSPsych'),('2023-8767','William Clark','male','3rd year','BSE'),('2023-8768','John Cooper','male','1st year','BSStats'),('2023-8769','Michael Scott','male','3rd year','BSPsych'),('2023-8770','James Jenkins','male','1st year','BSE'),('2023-8771','William Hughes','male','3rd year','BSStats'),('2023-8772','John Mason','male','1st year','BSPsych'),('2023-8773','Michael Watts','male','3rd year','BSE'),('2023-8774','James Hunt','female','1st year','BSStats'),('2023-9089','Eli Y. Jang','male','1st year','BSCS'),('2023-9877','Michael Williams','male','3rd year','BSEE'),('2023-9878','James Johnson','male','1st year','BSA'),('2023-9879','William Allen','male','3rd year','BAH'),('2023-9880','John Brown','male','1st year','BSEE'),('2023-9881','Michael Ward','male','3rd year','BSA'),('2023-9882','James Long','male','1st year','BAH'),('2023-9883','William Barnes','male','3rd year','BSEE'),('2023-9884','John Webb','male','1st year','BSA'),('2023-9885','Michael Fisher','male','3rd year','BAH');
/*!40000 ALTER TABLE `student` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-04-21 23:55:51
