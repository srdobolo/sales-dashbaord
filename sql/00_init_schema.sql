IF DB_ID(N'SalesDW') IS NULL
BEGIN
    PRINT 'Creating database SalesDW...';
    CREATE DATABASE [SalesDW];
END;
GO

USE [SalesDW];
GO

IF NOT EXISTS (SELECT 1 FROM sys.schemas WHERE name = 'staging')
    EXEC ('CREATE SCHEMA staging;');

IF NOT EXISTS (SELECT 1 FROM sys.schemas WHERE name = 'dw')
    EXEC ('CREATE SCHEMA dw;');
GO