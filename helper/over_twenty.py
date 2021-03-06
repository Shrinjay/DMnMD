from google.cloud import language_v1
from data.db_functions import create_new_symptom, get_user
from helper.word_search import word_search
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = f"{os.getcwd()}/auth.json"
client = language_v1.LanguageServiceClient()


def over_twenty(phone_num, message):
    text = message
    document = {"content": text, "type_": language_v1.Document.Type.PLAIN_TEXT}
    response = client.classify_text(request={'document': document})
    result = {}

    user = get_user(phone=phone_num)[0]
    userID = user["_id"]

    print(text)
    symptomMessage = ""

    for category in response.categories:
        # Turn the categories into a dictionary of the form: {category.name: category.confidence}
        result[category.name] = category.confidence
        print(f"Category name: {category.name}")
        print(f"Category Confidence: {category.confidence}")
        if "Health" in category.name and category.confidence > 0.3:
            symptoms = word_search(message)
            for symptom in symptoms:
                create_new_symptom(userID, symptom, message)
                if len(symptomMessage) == 0:
                    symptomMessage += symptom
                else:
                    symptomMessage = f"{symptomMessage}, {symptom}"

    if not result:  # checks if the dictionary is empty to see if no categories were returned
        symptoms = word_search(message)

        for symptom in symptoms:
            create_new_symptom(userID, symptom, message)
            if len(symptomMessage) == 0:
                symptomMessage += symptom
            else:
                symptomMessage = f"{symptomMessage}, {symptom}"

    txtResponse = {
        'status': True,
        'message': "BEEP BOOP I'M A BOT. DMnMD recorded these symptoms: " + symptomMessage
    }

    return txtResponse

