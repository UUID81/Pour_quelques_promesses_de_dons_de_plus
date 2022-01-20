-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: localhost:8081
-- Generation Time: Jan 20, 2022 at 04:11 PM
-- Server version: 5.7.24
-- PHP Version: 7.4.16

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `datas_dons`
--

-- --------------------------------------------------------

--
-- Table structure for table `donnateurs`
--

CREATE TABLE `donnateurs` (
  `id_nom` int(11) NOT NULL,
  `nom` varchar(30) NOT NULL,
  `prenom` varchar(30) NOT NULL,
  `don` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `donnateurs`
--

INSERT INTO `donnateurs` (`id_nom`, `nom`, `prenom`, `don`) VALUES
(1, 'corlay', 'morgan', 23),
(2, 'babar', 'mickey', 144000),
(3, 'babar', 'morgan', 123),
(4, 'gege', 'gaga', 1234),
(5, 'bob', 'bill', 456);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `donnateurs`
--
ALTER TABLE `donnateurs`
  ADD PRIMARY KEY (`id_nom`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `donnateurs`
--
ALTER TABLE `donnateurs`
  MODIFY `id_nom` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
