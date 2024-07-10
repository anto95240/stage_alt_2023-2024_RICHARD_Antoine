-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3308
-- Généré le : ven. 05 juil. 2024 à 13:24
-- Version du serveur : 8.2.0
-- Version de PHP : 8.2.13

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `educational_platform`
--

-- --------------------------------------------------------

--
-- Structure de la table `admin_table`
--

DROP TABLE IF EXISTS `admin_table`;
CREATE TABLE IF NOT EXISTS `admin_table` (
  `AdminId` int NOT NULL AUTO_INCREMENT,
  `UserId` int NOT NULL,
  PRIMARY KEY (`AdminId`),
  KEY `FK_admin_user` (`UserId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Structure de la table `document_table`
--

DROP TABLE IF EXISTS `document_table`;
CREATE TABLE IF NOT EXISTS `document_table` (
  `DocumentId` int NOT NULL AUTO_INCREMENT,
  `UserId` int NOT NULL,
  `TeacherId` int NOT NULL,
  `Name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `Description` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `FilePath` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `CreatedAt` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`DocumentId`),
  KEY `FK_document_user` (`UserId`),
  KEY `FK_document_teacher` (`TeacherId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Structure de la table `note_table`
--

DROP TABLE IF EXISTS `note_table`;
CREATE TABLE IF NOT EXISTS `note_table` (
  `NoteId` int NOT NULL AUTO_INCREMENT,
  `UserId` int NOT NULL,
  `TeacherId` int NOT NULL,
  `appreciation` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `Note` decimal(2,2) NOT NULL,
  `Coefficient` decimal(2,2) NOT NULL,
  `Label` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `TotalScore` decimal(2,2) NOT NULL,
  PRIMARY KEY (`NoteId`),
  KEY `FK_note_user` (`UserId`),
  KEY `FK_note_teacher` (`TeacherId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Structure de la table `notification_table`
--

DROP TABLE IF EXISTS `notification_table`;
CREATE TABLE IF NOT EXISTS `notification_table` (
  `NotificationId` int NOT NULL AUTO_INCREMENT,
  `UserId` int NOT NULL,
  `Type` enum('cours_a_venir','changement_planning','absence_retard') CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `Message` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `DateSent` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `IsRead` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`NotificationId`),
  KEY `FK_notification_user` (`UserId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Structure de la table `planning_table`
--

DROP TABLE IF EXISTS `planning_table`;
CREATE TABLE IF NOT EXISTS `planning_table` (
  `PlanningId` int NOT NULL AUTO_INCREMENT,
  `Date` date NOT NULL,
  `StartTime` time NOT NULL,
  `EndTime` time NOT NULL,
  `Subject` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `Class` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `ClassLevel` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `Comment` text COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`PlanningId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Structure de la table `presence_table`
--

DROP TABLE IF EXISTS `presence_table`;
CREATE TABLE IF NOT EXISTS `presence_table` (
  `PresenceId` int NOT NULL AUTO_INCREMENT,
  `UserId` int NOT NULL,
  `TeacherId` int NOT NULL,
  `IsAbsence` tinyint(1) NOT NULL DEFAULT '0',
  `IsLate` tinyint(1) NOT NULL DEFAULT '0',
  `Date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`PresenceId`),
  KEY `FK_presence_teacher` (`TeacherId`),
  KEY `FK_presence_user` (`UserId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Structure de la table `teacher_table`
--

DROP TABLE IF EXISTS `teacher_table`;
CREATE TABLE IF NOT EXISTS `teacher_table` (
  `TeacherId` int NOT NULL AUTO_INCREMENT,
  `UserId` int NOT NULL,
  `Specialization` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`TeacherId`),
  KEY `FK_teacher_user` (`UserId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Structure de la table `user_table`
--

DROP TABLE IF EXISTS `user_table`;
CREATE TABLE IF NOT EXISTS `user_table` (
  `UserId` int NOT NULL AUTO_INCREMENT,
  `FirstName` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `LastName` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `Email` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `Age` int NOT NULL,
  `Password` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `Photo` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `Role` enum('student','teacher','admin') COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`UserId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `admin_table`
--
ALTER TABLE `admin_table`
  ADD CONSTRAINT `FK_admin_user` FOREIGN KEY (`UserId`) REFERENCES `user_table` (`UserId`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Contraintes pour la table `document_table`
--
ALTER TABLE `document_table`
  ADD CONSTRAINT `FK_document_teacher` FOREIGN KEY (`TeacherId`) REFERENCES `teacher_table` (`TeacherId`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_document_user` FOREIGN KEY (`UserId`) REFERENCES `user_table` (`UserId`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Contraintes pour la table `note_table`
--
ALTER TABLE `note_table`
  ADD CONSTRAINT `FK_note_teacher` FOREIGN KEY (`TeacherId`) REFERENCES `teacher_table` (`TeacherId`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_note_user` FOREIGN KEY (`UserId`) REFERENCES `user_table` (`UserId`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Contraintes pour la table `notification_table`
--
ALTER TABLE `notification_table`
  ADD CONSTRAINT `FK_notification_user` FOREIGN KEY (`UserId`) REFERENCES `user_table` (`UserId`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Contraintes pour la table `presence_table`
--
ALTER TABLE `presence_table`
  ADD CONSTRAINT `FK_presence_teacher` FOREIGN KEY (`TeacherId`) REFERENCES `teacher_table` (`TeacherId`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_presence_user` FOREIGN KEY (`UserId`) REFERENCES `user_table` (`UserId`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Contraintes pour la table `teacher_table`
--
ALTER TABLE `teacher_table`
  ADD CONSTRAINT `FK_teacher_user` FOREIGN KEY (`UserId`) REFERENCES `user_table` (`UserId`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
