# actions.py

from rasa_sdk import Action
from rasa_sdk.events import SlotSet

class ActionConfirmBooking(Action):
    def name(self):
        return "action_confirm_booking"

    def run(self, dispatcher, tracker, domain):
        date = tracker.get_slot("date")
        city = tracker.get_slot("city")

        if date and city:
            dispatcher.utter_message(
                text=f"Je résume. Vous voulez un hôtel pour {date} à {city}. C’est ça ?"
            )
        else:
            dispatcher.utter_message(text="Je n'ai pas assez d'informations.")
        
        return []
