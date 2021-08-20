-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 20, 2021 at 12:57 AM
-- Server version: 10.4.17-MariaDB
-- PHP Version: 8.0.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `port`
--

-- --------------------------------------------------------

--
-- Table structure for table `contact`
--

CREATE TABLE `contact` (
  `Name` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `subject` varchar(70) NOT NULL,
  `message` varchar(1500) NOT NULL,
  `date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `contact`
--

INSERT INTO `contact` (`Name`, `email`, `subject`, `message`, `date`) VALUES
('John doe', 'test1@gmail.com', 'new subject', 'An inspiring message', '2021-08-19'),
('John doe', 'test1@gmail.com', 'new subject', 'An inspiring message', '2021-08-19'),
('John doe', 'test1@gmail.com', 'new subject', 'An inspiring message', '2021-08-19'),
('Big Ben', 'trex@email.com', 'How far', 'Hey, how are you doing?', '2021-08-19'),
('bagwell', 'akorneth16@gmail.com', 'new subject', 'i\"m bagwell', '2021-08-19'),
('Jide1che', 'test1@gmail.com', 'Business', 'lets do business', '2021-08-19');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
