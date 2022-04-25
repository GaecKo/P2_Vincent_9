CREATE TABLE animaux (
    id INT PRIMARY KEY NOT NULL,
    famille_id INT NOT NULL,
    sexe TEXT NOT NULL,
    presence INT NOT NULL,
    apprivoise INT NOT NULL,
    mort_ne INT NOT NULL,
    decede INT NOT NULL,
    FOREIGN KEY (famille_id) REFERENCES familles(id)
);

CREATE TABLE velages (
    id INT PRIMARY KEY NOT NULL,
    mere_id INT NOT NULL,
    pere_id INT NOT NULL,
    date TEXT NOT NULL,
    FOREIGN KEY (mere_id) REFERENCES animaux(id),
    FOREIGN KEY (pere_id) REFERENCES animaux(id)
);

CREATE TABLE velages_complications (
    velage_id INT NOT NULL,
    complication_id INT NOT NULL,
    FOREIGN KEY (complication_id) REFERENCES complications(id),
    FOREIGN KEY (velage_id) REFERENCES velages(id),
    CONSTRAINT PK_velcompl PRIMARY KEY (velage_id,complication_id)
);

CREATE TABLE types (
    id INT PRIMARY KEY NOT NULL,
    type TEXT NOT NULL
);

CREATE TABLE familles (
    id INT PRIMARY KEY NOT NULL,
    nom TEXT NOT NULL
);

CREATE TABLE complications (
    id INT PRIMARY KEY NOT NULL,
    complication TEXT NOT NULL
);

CREATE TABLE animaux_velages (
    animal_id INT NOT NULL,
    velage_id INT NOT NULL,
    FOREIGN KEY (animal_id) REFERENCES animaux(id),
    FOREIGN KEY (velage_id) REFERENCES velages(id),
    CONSTRAINT PK_animvel PRIMARY KEY (animal_id,velage_id)
);

CREATE TABLE animaux_types (
    animal_id INT NOT NULL,
    type_id INT NOT NULL,
    pourcentage REAL NOT NULL,
    FOREIGN KEY (type_id) REFERENCES types(id),
    FOREIGN KEY (animal_id) REFERENCES animaux(id),
    CONSTRAINT PK_animtyp PRIMARY KEY (animal_id,type_id)
);