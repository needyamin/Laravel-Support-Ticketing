-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: otithee-aurora-0.cvkeq0gyqlh4.ap-southeast-1.rds.amazonaws.com
-- Generation Time: Sep 08, 2024 at 11:16 AM
-- Server version: 8.0.32
-- PHP Version: 8.2.22

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `otithee_administrator`
--

-- --------------------------------------------------------

--
-- Table structure for table `agent_rank`
--

CREATE TABLE `agent_rank` (
  `id` int NOT NULL,
  `user_id` bigint NOT NULL,
  `agents` varchar(50) NOT NULL,
  `users` varchar(50) NOT NULL,
  `properties` varchar(50) NOT NULL,
  `apartment` int DEFAULT '0',
  `hotel` int DEFAULT '0',
  `resort` int DEFAULT '0',
  `sharedroom` int DEFAULT '0',
  `conventionhall` int DEFAULT '0',
  `transport` int DEFAULT '0',
  `club_rank_id` int NOT NULL,
  `club_rank_name` varchar(256) DEFAULT NULL,
  `entry_by` int NOT NULL DEFAULT '1',
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `agent_rank`
--
ALTER TABLE `agent_rank`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`,`agents`,`users`,`properties`,`club_rank_name`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `agent_rank`
--
ALTER TABLE `agent_rank`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
