-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: ecommy
-- ------------------------------------------------------
-- Server version	8.0.36

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `additem`
--

DROP TABLE IF EXISTS `additem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `additem` (
  `item_id` binary(16) NOT NULL,
  `item_name` longtext NOT NULL,
  `discription` longtext,
  `quantity` int DEFAULT NULL,
  `category` enum('Electronics','Grocery','Fashion','Home') DEFAULT NULL,
  `price` int DEFAULT NULL,
  `addedby` varchar(100) DEFAULT NULL,
  `imgid` varchar(200) DEFAULT NULL,
  `p_link` text,
  PRIMARY KEY (`item_id`),
  KEY `addedby` (`addedby`),
  CONSTRAINT `additem_ibfk_1` FOREIGN KEY (`addedby`) REFERENCES `vendor` (`email`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `additem`
--

LOCK TABLES `additem` WRITE;
/*!40000 ALTER TABLE `additem` DISABLE KEYS */;
INSERT INTO `additem` VALUES (_binary 'x\Ëc\Z¿ÔΩée0\Z\À','0278e863-1ac0-11ef-bd8e-106530151acb','sportz',3,'Fashion',900,'palaabhilash9640@gmail.com','9Id8Dt.jpeg',NULL),(_binary 'Ñ{∫0ÔΩée0\Z\À','0c847bba-1b30-11ef-bd8e-106530151acb','liquid',1,'Grocery',430,'palaabhilash9640@gmail.com','9Vl8Bu.jpeg',NULL),(_binary '\rúç}*7\Ô¥e0\Z\À','LED lights','Most Famous lights',1,'Electronics',496,'palaabhilash9640@gmail.com','1Um9Jx.jpg',NULL),(_binary '$\'1ÔΩée0\Z\À','Keyboard','Dell',1,'Electronics',800,'palaabhilash9640@gmail.com','5Az8Tr.jpeg',NULL),(_binary '€©l\Z¿ÔΩée0\Z\À','15dba96c-1ac0-11ef-bd8e-106530151acb','Women shirts',4,'Fashion',1500,'palaabhilash9640@gmail.com','0Ie1Mo.jpeg',NULL),(_binary '!ch1ÔΩée0\Z\À','Keyboard','hp',1,'Electronics',900,'palaabhilash9640@gmail.com','1Xr9Oo.jpeg',NULL),(_binary '#ˇ}°*ÔΩée0\Z\À','23ff7da1-192a-11ef-bd8e-106530151acb','sport',3,'Fashion',550,'palaabhilash9640@gmail.com','1Ux4Gs.jpeg',NULL),(_binary '*\ﬁM¯\Z¿ÔΩée0\Z\À','2ade4df8-1ac0-11ef-bd8e-106530151acb','sportz',4,'Fashion',950,'palaabhilash9640@gmail.com','7Kq5Tg.jpeg',NULL),(_binary '<cy.ÔΩée0\Z\À','printer','High quality',1,'Electronics',15000,'palaabhilash9640@gmail.com','6Bq7Zv.jpeg',NULL),(_binary '<)\ˆ3èÔΩée0\Z\À','Sports','Men shirts',3,'Fashion',900,'palaabhilash9640@gmail.com','4Gr8Kn.jpeg',NULL),(_binary '>362\Z¿ÔΩée0\Z\À','3e333632-1ac0-11ef-bd8e-106530151acb','sportz',5,'Fashion',1800,'palaabhilash9640@gmail.com','3Me4Tt.jpeg',NULL),(_binary 'L´+\Î*)\Ô¥e0\Z\À','Air Conditioner','Super Cooling Feel Free',1,'Electronics',30000,'palaabhilash9640@gmail.com','9Ir0Bt.jpg',NULL),(_binary 'U\ƒ\Œ1-ÔΩée0\Z\À','Tide  Surf','Fast Wash',1,'Grocery',250,'palaabhilash9640@gmail.com','8Hh6Rx.jpeg',NULL),(_binary 'XlZf1ÔΩée0\Z\À','printer','super  quality',1,'Electronics',14000,'palaabhilash9640@gmail.com','8Dc5Oz.jpeg',NULL),(_binary '`æígèÔΩée0\Z\À','Raymond','Men Shirts',4,'Fashion',1800,'palaabhilash9640@gmail.com','2Ra2Zi.webp',NULL),(_binary 'púH1ÔΩée0\Z\À','Mouse','Easy move1',1,'Electronics',130,'palaabhilash9640@gmail.com','9Ed5Xa.jpeg',NULL),(_binary 'q‹∑≠*6\Ô¥e0\Z\À','Table Lamp','Using for study in any stream',1,'Electronics',5000,'palaabhilash9640@gmail.com','7Ub9Aj.jpg',NULL),(_binary 'à*\“\ÏèÔΩée0\Z\À','882ad2ec-198f-11ef-bd8e-106530151acb','sportz',5,'Fashion',3000,'palaabhilash9640@gmail.com','1Ex0Ny.webp',NULL),(_binary 'àjâl1ÔΩée0\Z\À','Mouse','Fast Move',1,'Electronics',250,'palaabhilash9640@gmail.com','3Hi2Jc.jpeg',NULL),(_binary 'ä*6\Ô¥e0\Z\À','Table Lamp','Using for study in any stream',2,'Electronics',6000,'palaabhilash9640@gmail.com','3Uv4Kj.jpeg',NULL),(_binary 'ù$\Î/ÔΩée0\Z\À','surf','Dust Cleaner',2,'Grocery',300,'palaabhilash9640@gmail.com','2Rb4Er.jpeg',NULL),(_binary '≠	\nT*6\Ô¥e0\Z\À','Cieling Lights','High quality Product',1,'Electronics',20000,'palaabhilash9640@gmail.com','0Hu6Wi.jpg',NULL),(_binary '∑|\ÿ\ZøÔΩée0\Z\À','b77cd801-1abf-11ef-bd8e-106530151acb','Alankar',1,'Fashion',1200,'palaabhilash9640@gmail.com','4Vo6Rn.jpeg',NULL),(_binary '∏\ÔVk1ÔΩée0\Z\À','Dryyer','Hair Dryyer',1,'Electronics',800,'palaabhilash9640@gmail.com','5Zy0Wg.jpeg',NULL),(_binary 'ºÆ\’/ÔΩée0\Z\À','surf','Best cleaner',1,'Grocery',210,'palaabhilash9640@gmail.com','8Wc4Pi.jpeg',NULL),(_binary '\—\Úg*6\Ô¥e0\Z\À','Cieling Lights','super  quality',1,'Electronics',12000,'palaabhilash9640@gmail.com','6Gd3Mf.jpg',NULL),(_binary '\’\Ï\’¿/ÔΩée0\Z\À','surf','Best cleaner',1,'Grocery',400,'palaabhilash9640@gmail.com','9Au7Fd.jpeg',NULL),(_binary '\⁄e\Ï©1ÔΩée0\Z\À','See','varitey ',1,'Electronics',250,'palaabhilash9640@gmail.com','8Ie1Jw.jpeg',NULL),(_binary '\‹lkèÔΩée0\Z\À','dc6c6b05-198f-11ef-bd8e-106530151acb','sportz',6,'Fashion',800,'palaabhilash9640@gmail.com','8Bj8Jo.jpeg',NULL),(_binary '\‚ê*tˇÔΩée0\Z\À','Sports','Men shirts',6,'Fashion',900,'palaabhilash9640@gmail.com','9Gt8Co.jpeg',NULL),(_binary '\Ì\\±\Ô*6\Ô¥e0\Z\À','LED lights','Most Famous lights',1,'Electronics',4000,'palaabhilash9640@gmail.com','5Bh9Pq.webp',NULL),(_binary '\Ô/b/\ZøÔΩée0\Z\À','ef2f622f-1abf-11ef-bd8e-106530151acb','sportz',2,'Fashion',1000,'palaabhilash9640@gmail.com','8Ac9Uv.jpeg',NULL),(_binary '\Ûü\ı/ÔΩée0\Z\À','soap','100% clean',1,'Grocery',100,'palaabhilash9640@gmail.com','3Oj0Ob.jpeg',NULL);
/*!40000 ALTER TABLE `additem` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `notes`
--

DROP TABLE IF EXISTS `notes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `notes` (
  `nid` int NOT NULL AUTO_INCREMENT,
  `discription` text NOT NULL,
  `username` varchar(25) DEFAULT NULL,
  PRIMARY KEY (`nid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `notes`
--

LOCK TABLES `notes` WRITE;
/*!40000 ALTER TABLE `notes` DISABLE KEYS */;
/*!40000 ALTER TABLE `notes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `one`
--

DROP TABLE IF EXISTS `one`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `one` (
  `date` datetime DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `one`
--

LOCK TABLES `one` WRITE;
/*!40000 ALTER TABLE `one` DISABLE KEYS */;
/*!40000 ALTER TABLE `one` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orders` (
  `ordid` binary(16) NOT NULL,
  `itemid` binary(16) NOT NULL,
  `item_name` varchar(255) DEFAULT NULL,
  `qty` int DEFAULT NULL,
  `total_price` decimal(20,4) DEFAULT NULL,
  `user` varchar(255) DEFAULT NULL,
  `category` varchar(255) DEFAULT NULL,
  `imgid` varchar(255) DEFAULT NULL,
  `dis` longtext,
  PRIMARY KEY (`ordid`),
  KEY `itemid` (`itemid`),
  KEY `user` (`user`),
  CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`itemid`) REFERENCES `additem` (`item_id`) ON DELETE CASCADE,
  CONSTRAINT `orders_ibfk_2` FOREIGN KEY (`user`) REFERENCES `user` (`email`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders`
--

LOCK TABLES `orders` WRITE;
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
INSERT INTO `orders` VALUES (_binary '#ì*(\Ô¥e0\Z\À',_binary '\‚ê*tˇÔΩée0\Z\À','Sports',1,900.0000,'palaabhilash9640@gmail.com','Fashion','9Gt8Co.jpeg','Men shirts'),(_binary '\»>ì6 ÔΩée0\Z\À',_binary '€©l\Z¿ÔΩée0\Z\À','15dba96c-1ac0-11ef-bd8e-106530151acb',1,1500.0000,'palaabhilash9640@gmail.com','Fashion','0Ie1Mo.jpeg','Women shirts'),(_binary '\›jL†$ù\Ôöve0\Z\À',_binary '`æígèÔΩée0\Z\À','Raymond',1,1800.0000,'palaabhilash9640@gmail.com','Fashion','2Ra2Zi.webp','Men Shirts');
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reviews`
--

DROP TABLE IF EXISTS `reviews`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reviews` (
  `email` varchar(255) DEFAULT NULL,
  `item_id` binary(16) DEFAULT NULL,
  `title` tinytext,
  `review` text,
  `rating` int DEFAULT NULL,
  `date` datetime DEFAULT CURRENT_TIMESTAMP,
  KEY `email` (`email`),
  KEY `item_id` (`item_id`),
  CONSTRAINT `reviews_ibfk_1` FOREIGN KEY (`email`) REFERENCES `user` (`email`),
  CONSTRAINT `reviews_ibfk_2` FOREIGN KEY (`item_id`) REFERENCES `additem` (`item_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reviews`
--

LOCK TABLES `reviews` WRITE;
/*!40000 ALTER TABLE `reviews` DISABLE KEYS */;
INSERT INTO `reviews` VALUES ('palaabhilash9640@gmail.com',_binary '<cy.ÔΩée0\Z\À','Mamuluga vundadhu mari','super goood',5,'2024-06-14 21:07:07'),('palaabhilash9640@gmail.com',_binary '<)\ˆ3èÔΩée0\Z\À','Wonderful','this is very  wonderful T-shirt i feel comfortable.This brand is very famous and good company ',5,'2024-06-14 21:22:45'),('palaabhilash9640@gmail.com',_binary '<)\ˆ3èÔΩée0\Z\À','Excellent','This is the wonderful T-shirt and every person has like this \r\nT-shirt because of it is famous and incridible brand',10,'2024-06-14 21:59:53'),('palaabhilash9640@gmail.com',_binary '€©l\Z¿ÔΩée0\Z\À','qwweewwwwwww','lhsdljflkkjsdflksdflksdf2',2,'2024-06-14 22:20:28'),('palaabhilash9640@gmail.com',_binary '\Ì\\±\Ô*6\Ô¥e0\Z\À','Lamp','EXcellent work super work',5,'2024-06-15 10:58:54');
/*!40000 ALTER TABLE `reviews` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `username` varchar(255) NOT NULL,
  `mobile_no` bigint NOT NULL,
  `email` varchar(255) NOT NULL,
  `address` text NOT NULL,
  `password` varbinary(255) DEFAULT NULL,
  PRIMARY KEY (`email`),
  UNIQUE KEY `mobile_no` (`mobile_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES ('abhi',9705170789,'abhiyo7675@gmail.com','casa colony',_binary '$2b$12$tz.gqBlaTHZXwEJCALPdwuGznr4.31G0eP/YaYbP.vCz.l7XlbsYK'),('PALA ABHILASH',9640585057,'palaabhilash9640@gmail.com','vanukuru,casa colony',_binary '$2b$12$.JCFTw4Qghme0aDgOhNRpuS8zdn/d.xmolGsrJ0IhC6A0kpqMJEEG');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vendor`
--

DROP TABLE IF EXISTS `vendor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vendor` (
  `email` varchar(50) NOT NULL,
  `name` varchar(150) NOT NULL,
  `mobile_no` bigint DEFAULT NULL,
  `address` text NOT NULL,
  `password` varbinary(255) DEFAULT NULL,
  PRIMARY KEY (`email`),
  UNIQUE KEY `mobile_no` (`mobile_no`),
  UNIQUE KEY `mobile_no_2` (`mobile_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vendor`
--

LOCK TABLES `vendor` WRITE;
/*!40000 ALTER TABLE `vendor` DISABLE KEYS */;
INSERT INTO `vendor` VALUES ('palaabhilash9640@gmail.com','PALA ABHILASH',9640585057,'vanukuru,casa colony',_binary '$2b$12$HiIEqrpDfKLwOVpznbKCDuuQGRhknkU/efGELncLxKKsmnxS1YJcu');
/*!40000 ALTER TABLE `vendor` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-06-15 13:22:23
