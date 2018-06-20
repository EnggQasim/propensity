-- phpMyAdmin SQL Dump
-- version 4.7.7
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 13, 2018 at 07:04 AM
-- Server version: 10.1.30-MariaDB
-- PHP Version: 7.2.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ubl`
--

-- --------------------------------------------------------

--
-- Table structure for table `calls`
--

CREATE TABLE `calls` (
  `id` int(255) NOT NULL,
  `Customers_lists` varchar(5000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `calls`
--

INSERT INTO `calls` (`id`, `Customers_lists`) VALUES
(1, '50');

-- --------------------------------------------------------

--
-- Table structure for table `customers`
--

CREATE TABLE `customers` (
  `id` int(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `cnic` varchar(255) NOT NULL,
  `acc_no` varchar(255) NOT NULL,
  `branch_code` varchar(255) NOT NULL,
  `call_status` int(255) NOT NULL DEFAULT '0',
  `intrest_level` varchar(255) NOT NULL,
  `comments` varchar(255) NOT NULL,
  `phone` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `score` float NOT NULL,
  `predict_intrest_level` tinyint(1) NOT NULL,
  `g1` varchar(255) NOT NULL,
  `g2` varchar(255) NOT NULL,
  `m1` varchar(255) NOT NULL,
  `m2` varchar(255) NOT NULL,
  `c1` varchar(255) NOT NULL,
  `c2` varchar(255) NOT NULL,
  `c3` varchar(255) NOT NULL,
  `c4` varchar(255) NOT NULL,
  `c5` varchar(255) NOT NULL,
  `c6` varchar(255) NOT NULL,
  `c7` varchar(255) NOT NULL,
  `c8` varchar(255) NOT NULL,
  `tenor` varchar(255) NOT NULL,
  `no_of_bills` int(255) NOT NULL,
  `no_of_funds_transfer` int(255) NOT NULL,
  `no_of_ibft` int(255) NOT NULL,
  `credit_card` varchar(255) NOT NULL,
  `priority_banking` varchar(255) NOT NULL,
  `average_advance` int(255) NOT NULL,
  `average_deposit` int(255) NOT NULL,
  `gross_revenue` int(255) NOT NULL,
  `non_fund_income` int(255) NOT NULL,
  `turnor` varchar(255) NOT NULL,
  `tranaction_count` int(11) NOT NULL,
  `caller_id` int(255) NOT NULL DEFAULT '0',
  `time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `customers`
--

INSERT INTO `customers` (`id`, `name`, `cnic`, `acc_no`, `branch_code`, `call_status`, `intrest_level`, `comments`, `phone`, `email`, `score`, `predict_intrest_level`, `g1`, `g2`, `m1`, `m2`, `c1`, `c2`, `c3`, `c4`, `c5`, `c6`, `c7`, `c8`, `tenor`, `no_of_bills`, `no_of_funds_transfer`, `no_of_ibft`, `credit_card`, `priority_banking`, `average_advance`, `average_deposit`, `gross_revenue`, `non_fund_income`, `turnor`, `tranaction_count`, `caller_id`, `time`) VALUES
(1, 'Salah Uddin', '12345-1234567-1', '12345678912', '0057', 1, '1', 'aa', '0314-1234567', 'salah.uddin@ubl.com.pk', 0.78, 1, 'g1', 'g2', 'm2', 'm2', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'tenor', 1, 2, 3, 'abc', 'abcd', 4, 5, 6, 7, 'aa', 25, 2, '2018-06-12 04:11:40'),
(2, 'Muhammad qasim', '42201-7578760-3', '12345678912', '00357', 1, '1', '123', '0315-2968211', 'mohammad.qasim@ubl.com.pk', 0.95, 1, 'g1', 'g2', 'm1', 'm2', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'tenorvalue', 5, 6, 7, '8', 'aaa', 9, 10, 11, 12, 'cc', 50, 2, '2018-06-12 04:11:40'),
(3, 'Aziz', '', '', '', 1, '0', '555', '', '', 0.85, 0, '', '', '', '', '', '', '', '', '', '', '', '', '', 0, 0, 0, '', '', 0, 0, 0, 0, '', 0, 1, '2018-06-12 04:11:40'),
(4, 'Asif Khan', '', '', '', 0, '1', 'asdgadsf', '', '', 0.6, 0, '', '', '', '', '', '', '', '', '', '', '', '', '', 0, 0, 0, '', '', 0, 0, 0, 0, '', 0, 1, '2018-06-12 04:11:40');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(255) NOT NULL,
  `user` varchar(255) NOT NULL,
  `pass` varchar(255) NOT NULL,
  `type` varchar(255) NOT NULL,
  `time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `user`, `pass`, `type`, `time`) VALUES
(1, 'mohammad.qasim', '123', 'admin', '2018-05-29 04:46:21'),
(2, 'rafy', '123', 'user', '2018-05-29 04:46:21'),
(3, 'salah.uddin', '123', 'admin', '2018-05-29 06:54:37');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `calls`
--
ALTER TABLE `calls`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `customers`
--
ALTER TABLE `customers`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `calls`
--
ALTER TABLE `calls`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `customers`
--
ALTER TABLE `customers`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
