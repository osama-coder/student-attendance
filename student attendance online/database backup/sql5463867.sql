-- phpMyAdmin SQL Dump
-- version 4.7.1
-- https://www.phpmyadmin.net/
--
-- Host: sql5.freemysqlhosting.net
-- Generation Time: Jan 12, 2022 at 10:20 PM
-- Server version: 5.5.62-0ubuntu0.14.04.1
-- PHP Version: 7.0.33-0ubuntu0.16.04.16

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `sql5463867`
--

-- --------------------------------------------------------

--
-- Table structure for table `attendance`
--

CREATE TABLE `attendance` (
  `Full_name` text NOT NULL,
  `Level` text NOT NULL,
  `Class` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `attendance`
--

INSERT INTO `attendance` (`Full_name`, `Level`, `Class`) VALUES
('osama mohammed', '6', 'A'),
('kali linux', '6', 'A'),
('ibrahem hassan', '6', 'A');

-- --------------------------------------------------------

--
-- Table structure for table `staccounts`
--

CREATE TABLE `staccounts` (
  `name` text NOT NULL,
  `password` text NOT NULL,
  `level` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `staccounts`
--

INSERT INTO `staccounts` (`name`, `password`, `level`) VALUES
('kalios', 'kali', '6'),
('osama', 'adfagdgad', '9');

-- --------------------------------------------------------

--
-- Table structure for table `students`
--

CREATE TABLE `students` (
  `Full_name` text NOT NULL,
  `Birth_date` text NOT NULL,
  `Phone` text NOT NULL,
  `Email` text NOT NULL,
  `Payment` text NOT NULL,
  `Register_date` text NOT NULL,
  `Level` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `students`
--

INSERT INTO `students` (`Full_name`, `Birth_date`, `Phone`, `Email`, `Payment`, `Register_date`, `Level`) VALUES
('gjdfghdfg', '2/2/1997', '0362645274235', 'osamakort63@gmail.com', 'yes', '2/6/2012', '7'),
('hgd', 'sfsf', 'sf', 'sf', 'dsfsdf', 'sfd', 'sfs'),
('fdsf', 'fsd', 'sdfsf', 'sdfsd', 'fs', 'sfds', 'sfd'),
('fdsfs', 'dfsdf', 'fdsfsdf', 'df', 'ds', 'sdfds', 'sdfds'),
('dsf', 'dfs', 'sfdd', 'fsdsd', 'dfs', 'sdfs', 'sdfs'),
('sdfs', 'sdsd', 'sdsdf', 'sdf', 'sdfds', 'sdf', 'sdfs'),
('sdfd', 'sd', 'sdfs', 'sdf', 'sdfds', 'sdf', 'sdf'),
('dfsfd', 'sdfd', 'dfsf', 'dsfs', 'sdf', 'sdf', 'sdf'),
('dfdsf', 'sdf', 'sdf', 'sfdsdf', 'dfs', 'sdf', 'sdf'),
('hfgdfg', 'dsfs', 'sdfs', 'sdfs', 'df', 'sdf', 'sdfs'),
('hsf', 'fsf', 'f', 'fsffsd', 'dsdf', 'fsdfs', 'dsfs'),
('rrrrr', 'asd', 'asdas', 'asda', 'asd', 'asd', 'asd');

-- --------------------------------------------------------

--
-- Table structure for table `teachers`
--

CREATE TABLE `teachers` (
  `name` text NOT NULL,
  `password` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `teachers`
--

INSERT INTO `teachers` (`name`, `password`) VALUES
('abcde', '3242343');

-- --------------------------------------------------------

--
-- Table structure for table `weeklytable`
--

CREATE TABLE `weeklytable` (
  `id` int(11) NOT NULL,
  `Level` text NOT NULL,
  `Subject_name` text NOT NULL,
  `Teacher_name` text NOT NULL,
  `Day` text NOT NULL,
  `Date` text NOT NULL,
  `From_1` text NOT NULL,
  `To_1` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `weeklytable`
--

INSERT INTO `weeklytable` (`id`, `Level`, `Subject_name`, `Teacher_name`, `Day`, `Date`, `From_1`, `To_1`) VALUES
(1, '4', 'dssdsfds', 'ddsdfsdf', 'saturday', '2/3/1997', '4:30', '7:30'),
(3, '6', 'jjjjjjj', 'bv', 'ghg', 'cf', 'ds', 'rd'),
(4, 'dad', 'asda', '', '', '', '', ''),
(5, '10', 'wewr', 'werew', 'wer', '', '', ''),
(8, '8', 'dfgd', 'dgdf', 'dgdf', '', '', ''),
(10, '3', 'fsfsdfssd', 'fsd', 'dfs', '', '', ''),
(11, '54', 'dfsd', 'sfs', 'fs', 'fsfsd', '', ''),
(12, 'ewfwe', 'wefw', 'fwee', 'fs', 'sfsf', 'fsss', ''),
(13, '33', 'fsfss', 'fsfdf', 'fsf', 'fsfdfs', 'fsdffsd', 'fsfsd'),
(14, '5', 'ada', 'dad', 'dad', 'asdad', 'sda', 'add'),
(15, '6', 'fsdfsd', 'sdfsdf', 'sdfsf', 'sdfsd', 'sdfsdfs', '111111'),
(17, '6', 'dfsdfs', 'dfsdf', 'fsd', 'dfsfd', '1:11', '3:44');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `weeklytable`
--
ALTER TABLE `weeklytable`
  ADD PRIMARY KEY (`id`) USING BTREE;

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `weeklytable`
--
ALTER TABLE `weeklytable`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
