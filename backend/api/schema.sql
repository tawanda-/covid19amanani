CREATE TABLE IF NOT EXISTS country
(
    iso character(2) COLLATE pg_catalog."default" NOT NULL,
    country character(100) COLLATE pg_catalog."default" NOT NULL,
    population integer,
    life_expectancy character(10) COLLATE pg_catalog."default",
    continent character(10) COLLATE pg_catalog."default",
    location character(25) COLLATE pg_catalog."default",
    capital_city character(100) COLLATE pg_catalog."default",
    CONSTRAINT country_pkey PRIMARY KEY (iso)
);

CREATE TABLE IF NOT EXISTS current_data
(
    iso character(2) COLLATE pg_catalog."default" NOT NULL,
    confirmed integer,
    deaths integer,
    administered integer,
    people_vaccinated integer,
    people_partially_vaccinated integer,
    CONSTRAINT current_data_pkey PRIMARY KEY (iso),
    CONSTRAINT iso_fk FOREIGN KEY (iso)
        REFERENCES country (iso) MATCH SIMPLE
        ON DELETE CASCADE
);
