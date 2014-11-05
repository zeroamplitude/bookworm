DROP TABLE IF EXISTS Members;
DROP TABLE IF EXISTS Books;
DROP TABLE IF EXISTS Schools;
DROP TABLE IF EXISTS Auctions;
DROP TABLE IF EXISTS Bids;

CREATE TABLE Members(
	member_id	SERIAL 		NOT NULL,
	firstName	VARCHAR(40)	NOT NULL,
	lastName	VARCHAR(40) NOT NULL,
	school_id	INTEGER		NOT NULL,
-- Basic Table
--	email		VARCHAR(70) NOT NULL,
--	address		VARCHAR(70) NOT NULL,
--	city		VARCHAR(30) NOT NULL,
--	province	VARCHAR(30) NOT NULL,
--	postal_code	VARCHAR(6) 	NOT NULL,
--	phone		VARCHAR(10)	NOT NULL,
--	subject		VARCHAR(30)	NOT NULL,
--	facebook	VARCHAR(99) NOT NULL,
--	twitter		VARCHAR(99)	NOT NULL,
PRIMARY KEY(member_id)
);

CREATE TABLE Books(
	book_id		SERIAL		NOT NULL,
	title		VARCHAR(90)	NOT NULL,
	author		VARCHAR(90)	NOT NULL,
	publisher	VARCHAR(90)	NOT NULL,
--	year		INTEGER 	NOT	NULL,
--	subject		VARCHAR(90)	NOT NULL,
PRIMARY KEY(book_id)
);

CREATE TABLE Schools(
	school_id	SERIAL 		NOT NULL,
	name		VARCHAR(99)	NOT NULL,
--	address		VARCHAR(99) NOT NULL,
--	city		VARCHAR(30)	NOT NULL,
--	province	VARCHAR(30)	NOT NULL,
--	postal_code	VARCHAR(6 )	NOT NULL,
PRIMARY KEY(school_id)
);

CREATE TABLE Auctions(
	auction_id	SERIAL  NOT NULL,
	book_id		INTEGER UNIQUE 	NOT NULL,
	start_time 	TIME	NOT NULL,
	end_time 	TIME	NOT NULL,
	member_id	INTEGER UNIQUE	NOT NULL,
	min_price	FLOAT	NOT NULL,
	bid_id 		INTEGER UNIQUE 	NOT NULL,
	PRIMARY KEY(auction_id)
);

CREATE TABLE Bids(
	bid_id		INTEGER NOT NULL,
	auction_id	INTEGER NOT NULL,
	bdPrice 	float	NOT NULL,
	member_id	INTEGER	NOT NULL,
	PRIMARY KEY(bid_id)
);

ALTER TABLE Members
ADD FOREIGN KEY (school_id) 	REFERENCES Schools(school_id);

ALTER TABLE Auctions
ADD FOREIGN KEY (book_id) 	REFERENCES Books(book_id);

ALTER TABLE Bids
ADD FOREIGN KEY (auction_id) 	REFERENCES Auctions(auction_id),
ADD FOREIGN KEY (member_id) 	REFERENCES Members(member_id);