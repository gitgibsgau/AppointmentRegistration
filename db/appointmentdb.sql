-- phpMyAdmin SQL Dump
-- version 4.6.5.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 25, 2017 at 08:50 PM
-- Server version: 5.7.17-log
-- PHP Version: 7.1.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


--
-- Database: `appointmentPerldb`
--

-- --------------------------------------------------------

--
-- Table structure for table `appointmentMaster`
--

CREATE TABLE `appointmentMaster` (
  `appointment_date` varchar(45) DEFAULT NULL,
  `appointment_time` varchar(45) DEFAULT NULL,
  `description` varchar(250) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `appointmentMaster`
--

INSERT INTO `appointmentMaster` (`appointment_date`, `appointment_time`, `description`) VALUES
('25/10/2017', '9:30pm', 'Physio: Gaurav Shinde'),
('26/10/2017', '7:30am', 'Psychotherapist: Shweta Bhagwat');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
