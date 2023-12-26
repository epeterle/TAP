import xml.etree.ElementTree as ET

def case_import(file_path):
    # Parse the XML file
    tree = ET.parse(file_path)
    root = tree.getroot()

    # Extracting required elements
    code_juridiction = root.find('.//Code_Juridiction').text if root.find('.//Code_Juridiction') is not None else None
    nom_juridiction = root.find('.//Nom_Juridiction').text if root.find('.//Nom_Juridiction') is not None else None
    numero_dossier = root.find('.//Numero_Dossier').text if root.find('.//Numero_Dossier') is not None else None
    date_lecture = root.find('.//Date_Lecture').text if root.find('.//Date_Lecture') is not None else None
    type_decision = root.find('.//Type_Decision').text if root.find('.//Type_Decision') is not None else None
    type_recours = root.find('.//Type_Recours').text if root.find('.//Type_Recours') is not None else None

    # Return the data as a dictionary
    return {
        'Code_Juridiction': code_juridiction,
        'Nom_Juridiction': nom_juridiction,
        'Numero_Dossier': numero_dossier,
        'Date_Lecture': date_lecture,
        'Type_Decision': type_decision,
        'Type_Recours': type_recours
    }

# Example usage
file_path = 'C:/Users/Emmanuel Peterle/TAP/Data/Raw/TA_202208/TA25/DTA_2001337_20220817.xml'
case_data = case_import(file_path)
print(case_data)