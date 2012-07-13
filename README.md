Scrape OS Data
=============
My first python script!

I built this to enable me to easily pull down csv files of ODS data from the Connecting For Health website. Requires the pymssql module for connecting to SQL  R2Server 2008

The following is the header information for the ODS csv files repoduced from http://www.connectingforhealth.nhs.uk/systemsandservices/data/ods/datafiles

Ref.No. Field 	                    Max length 	  Notes
1. 	    Organisation Code 	        8 	
2. 	    Organisation Name 	        100
3. 	    National Grouping Code 	    3 	          = Field 1 of Regional Directorate file
4. 	    High Level Health Authority 3 	          = Field 1 of SHA file
5. 	    Address Line 1 	            35 	
6. 	    Address Line 2 	            35
7. 	    Address Line 3 	            35
8. 	    Address Line 4 	            35
9. 	    Address Line 5 	            35
10.   	Postcode 	                  8
11. 	  Open Date 	                ccyymmdd
12. 	  Close Date 	                ccyymmdd

Basic table schema (Sql Server):

CREATE TABLE [dbo].[ODSdata](
  [OrganisationCode] [nvarchar](8) NULL,
	[OrganisationName] [nvarchar](100) NULL,
	[NationalGroupingCode] [nvarchar](3) NULL,
	[HighLevelHealthAuthority] [nvarchar](3) NULL,
	[AddressLine1] [nvarchar](35) NULL,
	[AddressLine2] [nvarchar](35) NULL,
	[AddressLine3] [nvarchar](35) NULL,
	[AddressLine4] [nvarchar](35) NULL,
	[AddressLine5] [nvarchar](35) NULL,
	[Postcode] [nvarchar](8) NULL,
	[OpenDate] [date] NULL,
	[CloseDate] [date] NULL
) ON [PRIMARY]