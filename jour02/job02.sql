CREATE TABLE `etage`(`id_etage` INT NOT NULL AUTO_INCREMENT,
    `nom` VARCHAR(255) NOT NULL,
    `numero` INT NOT NULL,
    `superficie` INT NOT NULL,
    PRIMARY KEY(`id_etage`))ENGINE = InnoDB;

CREATE TABLE `salles`(`id_salle` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `nom` VARCHAR(255) NOT NULL,
    `id_etage` INT NOT NULL,
    `capacite` INT NOT NULL,
    FOREIGN KEY (`id_etage`) REFERENCES etage(`id_etage`))ENGINE =InnoDB;