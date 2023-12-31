USE [master]
GO
/****** Object:  Database [Takvim]    Script Date: 15.06.2023 16:56:14 ******/
CREATE DATABASE [Takvim]
 CONTAINMENT = NONE
 ON  PRIMARY 
( NAME = N'Takvim', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL16.MSSQLSERVER\MSSQL\DATA\Takvim.mdf' , SIZE = 8192KB , MAXSIZE = UNLIMITED, FILEGROWTH = 65536KB )
 LOG ON 
( NAME = N'Takvim_log', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL16.MSSQLSERVER\MSSQL\DATA\Takvim_log.ldf' , SIZE = 8192KB , MAXSIZE = 2048GB , FILEGROWTH = 65536KB )
 WITH CATALOG_COLLATION = DATABASE_DEFAULT, LEDGER = OFF
GO
ALTER DATABASE [Takvim] SET COMPATIBILITY_LEVEL = 160
GO
IF (1 = FULLTEXTSERVICEPROPERTY('IsFullTextInstalled'))
begin
EXEC [Takvim].[dbo].[sp_fulltext_database] @action = 'enable'
end
GO
ALTER DATABASE [Takvim] SET ANSI_NULL_DEFAULT OFF 
GO
ALTER DATABASE [Takvim] SET ANSI_NULLS OFF 
GO
ALTER DATABASE [Takvim] SET ANSI_PADDING OFF 
GO
ALTER DATABASE [Takvim] SET ANSI_WARNINGS OFF 
GO
ALTER DATABASE [Takvim] SET ARITHABORT OFF 
GO
ALTER DATABASE [Takvim] SET AUTO_CLOSE OFF 
GO
ALTER DATABASE [Takvim] SET AUTO_SHRINK OFF 
GO
ALTER DATABASE [Takvim] SET AUTO_UPDATE_STATISTICS ON 
GO
ALTER DATABASE [Takvim] SET CURSOR_CLOSE_ON_COMMIT OFF 
GO
ALTER DATABASE [Takvim] SET CURSOR_DEFAULT  GLOBAL 
GO
ALTER DATABASE [Takvim] SET CONCAT_NULL_YIELDS_NULL OFF 
GO
ALTER DATABASE [Takvim] SET NUMERIC_ROUNDABORT OFF 
GO
ALTER DATABASE [Takvim] SET QUOTED_IDENTIFIER OFF 
GO
ALTER DATABASE [Takvim] SET RECURSIVE_TRIGGERS OFF 
GO
ALTER DATABASE [Takvim] SET  ENABLE_BROKER 
GO
ALTER DATABASE [Takvim] SET AUTO_UPDATE_STATISTICS_ASYNC OFF 
GO
ALTER DATABASE [Takvim] SET DATE_CORRELATION_OPTIMIZATION OFF 
GO
ALTER DATABASE [Takvim] SET TRUSTWORTHY OFF 
GO
ALTER DATABASE [Takvim] SET ALLOW_SNAPSHOT_ISOLATION OFF 
GO
ALTER DATABASE [Takvim] SET PARAMETERIZATION SIMPLE 
GO
ALTER DATABASE [Takvim] SET READ_COMMITTED_SNAPSHOT OFF 
GO
ALTER DATABASE [Takvim] SET HONOR_BROKER_PRIORITY OFF 
GO
ALTER DATABASE [Takvim] SET RECOVERY FULL 
GO
ALTER DATABASE [Takvim] SET  MULTI_USER 
GO
ALTER DATABASE [Takvim] SET PAGE_VERIFY CHECKSUM  
GO
ALTER DATABASE [Takvim] SET DB_CHAINING OFF 
GO
ALTER DATABASE [Takvim] SET FILESTREAM( NON_TRANSACTED_ACCESS = OFF ) 
GO
ALTER DATABASE [Takvim] SET TARGET_RECOVERY_TIME = 60 SECONDS 
GO
ALTER DATABASE [Takvim] SET DELAYED_DURABILITY = DISABLED 
GO
ALTER DATABASE [Takvim] SET ACCELERATED_DATABASE_RECOVERY = OFF  
GO
EXEC sys.sp_db_vardecimal_storage_format N'Takvim', N'ON'
GO
ALTER DATABASE [Takvim] SET QUERY_STORE = ON
GO
ALTER DATABASE [Takvim] SET QUERY_STORE (OPERATION_MODE = READ_WRITE, CLEANUP_POLICY = (STALE_QUERY_THRESHOLD_DAYS = 30), DATA_FLUSH_INTERVAL_SECONDS = 900, INTERVAL_LENGTH_MINUTES = 60, MAX_STORAGE_SIZE_MB = 1000, QUERY_CAPTURE_MODE = AUTO, SIZE_BASED_CLEANUP_MODE = AUTO, MAX_PLANS_PER_QUERY = 200, WAIT_STATS_CAPTURE_MODE = ON)
GO
USE [Takvim]
GO
/****** Object:  Table [dbo].[Kullanicilar]    Script Date: 15.06.2023 16:56:14 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Kullanicilar](
	[KullaniciId] [int] IDENTITY(1,1) NOT NULL,
	[Ad] [varchar](15) NOT NULL,
	[Soyad] [varchar](15) NOT NULL,
	[KullaniciAdi] [varchar](25) NOT NULL,
	[Parola] [varchar](25) NOT NULL,
	[KimlikNo] [varchar](11) NOT NULL,
	[Telefon] [varchar](11) NOT NULL,
	[Email] [varchar](50) NOT NULL,
	[Adres] [varchar](150) NOT NULL,
	[KullaniciTuru] [bit] NOT NULL,
 CONSTRAINT [PK_Kullanicilar] PRIMARY KEY CLUSTERED 
(
	[KullaniciId] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Olaylar]    Script Date: 15.06.2023 16:56:14 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Olaylar](
	[KullaniciId] [int] NOT NULL,
	[Tarih] [datetime] NOT NULL,
	[BaslangicZamani] [time](7) NOT NULL,
	[OlayinTanimlamasi] [time](7) NULL,
	[OlayTipi] [nchar](10) NULL,
	[OlayAciklamasi] [nchar](10) NULL,
 CONSTRAINT [PK_Olaylar] PRIMARY KEY CLUSTERED 
(
	[KullaniciId] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
SET IDENTITY_INSERT [dbo].[Kullanicilar] ON 

INSERT [dbo].[Kullanicilar] ([KullaniciId], [Ad], [Soyad], [KullaniciAdi], [Parola], [KimlikNo], [Telefon], [Email], [Adres], [KullaniciTuru]) VALUES (2, N'baturay', N'incekara', N'bat123', N'1234', N'451551', N'42542452', N'baturayincekara@gmail.com', N'asdasdf', 0)
INSERT [dbo].[Kullanicilar] ([KullaniciId], [Ad], [Soyad], [KullaniciAdi], [Parola], [KimlikNo], [Telefon], [Email], [Adres], [KullaniciTuru]) VALUES (4, N'sezen melis', N'oktay', N'sezen123', N'1234', N'542425', N'24524524', N'sezenmelisoktay@gmail.com', N'254254254', 0)
INSERT [dbo].[Kullanicilar] ([KullaniciId], [Ad], [Soyad], [KullaniciAdi], [Parola], [KimlikNo], [Telefon], [Email], [Adres], [KullaniciTuru]) VALUES (6, N'sezen melis', N'oktay', N'sezen1234', N'1234', N'5424252', N'24524524', N'sezenmelisoktay@gmail.com', N'254254254', 0)
SET IDENTITY_INSERT [dbo].[Kullanicilar] OFF
GO
INSERT [dbo].[Olaylar] ([KullaniciId], [Tarih], [BaslangicZamani], [OlayinTanimlamasi], [OlayTipi], [OlayAciklamasi]) VALUES (2, CAST(N'2023-06-15T00:00:00.000' AS DateTime), CAST(N'00:00:00' AS Time), CAST(N'16:48:00' AS Time), N'          ', N'          ')
GO
SET ANSI_PADDING ON
GO
/****** Object:  Index [UK_KullaniciAdi]    Script Date: 15.06.2023 16:56:15 ******/
ALTER TABLE [dbo].[Kullanicilar] ADD  CONSTRAINT [UK_KullaniciAdi] UNIQUE NONCLUSTERED 
(
	[KullaniciAdi] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO
ALTER TABLE [dbo].[Olaylar]  WITH CHECK ADD  CONSTRAINT [FK_Olaylar_Kullanicilar] FOREIGN KEY([KullaniciId])
REFERENCES [dbo].[Kullanicilar] ([KullaniciId])
GO
ALTER TABLE [dbo].[Olaylar] CHECK CONSTRAINT [FK_Olaylar_Kullanicilar]
GO
USE [master]
GO
ALTER DATABASE [Takvim] SET  READ_WRITE 
GO
