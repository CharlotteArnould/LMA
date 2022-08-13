from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep

class Wamiz :
    def reject_cookie(self, driver):
        try :
            driver.find_element(By.CLASS_NAME, "didomi-continue-without-agreeing").click()
            sleep(5)
        except :
            pass

    def __init__(self, publication):
        # Ouverture du site Wamiz
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        driver.get("https://wamiz.com/")
        sleep(3)

        # Rejet des cookies
        self.reject_cookie(driver)

        # Connexion
        driver.find_element(By.LINK_TEXT, "Se connecter").click()
        sleep(3)
        element = driver.find_element(By.ID, "signin_username")
        element.send_keys("gestion.lamaisondesanimaux77@gmail.com")

        element = driver.find_element(By.ID, "signin_password")
        element.send_keys("antiloened")

        element.send_keys(Keys.RETURN)
        sleep(5)

        # Accéder à l'espace adoption
        driver.get("https://wamiz.com/adoption/membre")
        sleep(5)

        # Ajouter un animal
        driver.find_element(By.LINK_TEXT, "Ajouter un animal").click()
        sleep(5)

        # Mettre en forme la descritpion
        description = publication.animal.description

        # Remplir le formulaire
        if publication.animal.type.lower() == "chat":
            driver.find_element(By.XPATH, "//label[@for=\'adoption_pet_parent_cat_2\']").click()

            #race1
            elements = driver.find_elements(By.ID, "select2-adoption_pet_fiche_chat_adoption_list-container")
            elt = elements[0]
            sleep(2)
            #elt.select_by_visible_text ("Européen")

            #print(elements.) #.send_keys(publication.animal.race)

            # race2
            #print(elements[1]) #.send_keys(publication.animal.race2)

        elif publication.animal.type.lower() == "chien":
            driver.find_element(By.XPATH, "//label[@for=\'adoption_pet_parent_cat_1\']").click()
            element = driver.find_element(By.ID, "adoption_pet_height")
            element.send_keys(publication.animal.taille)

            # race1
            element = driver.find_element(By.ID, "select2-adoption_pet_fiche_chat_adoption_list-container")
            element.send_keys(publication.animal.race)
            # race2
            # element = driver.find_element(By.ID, "select2-selection select2-selection--single")
            # element.send_keys(publication.animal.race2)

        else :
            driver.find_element(By.XPATH, "//label[@for=\'adoption_pet_parent_cat_3\']").click()

            # espece
            # element = driver.find_element(By.ID, "select2-btig-container")
            # element.send_keys(publication.animal.type)

        #nom
        element = driver.find_element(By.ID, "adoption_pet_name")
        element.send_keys(publication.animal.nom)

        #date de naissance
        jour, mois, annee = publication.animal.dateDeNaissance.split('/')
        element = driver.find_element(By.ID, "adoption_pet_birthdate_day")
        element.send_keys(jour)
        element = driver.find_element(By.ID, "adoption_pet_birthdate_month")
        element.send_keys(mois)
        element = driver.find_element(By.ID, "adoption_pet_birthdate_year")
        element.send_keys(annee)

        #numero identification
        element = driver.find_element(By.ID, "adoption_pet_puce")
        element.send_keys(publication.animal.numeroIdentification)

        #descriptions
        element = driver.find_element(By.ID, "adoption_pet_description")
        element.send_keys(description)

        #sexe
        element = driver.find_element(By.ID, "adoption_pet_gender")
        element.send_keys(publication.animal.sexe)

test = True
if test :
    from Parser import Publication
    publication = Publication("./Description.ini")
    wamiz = Wamiz(publication)