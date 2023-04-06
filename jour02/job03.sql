INSERT INTO `etage`(`nom`,`numero`,`superficie`) VALUES
    ("RDC",0,500),
    ("R+1",1,500);

CREATE TABLE `salles`(`id_salle` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `nom` VARCHAR(255) NOT NULL,
    `id_etage` INT NOT NULL,
    `capacite` INT NOT NULL,
    FOREIGN KEY (`id_etage`) REFERENCES etage(`id_etage`))ENGINE =InnoDB;