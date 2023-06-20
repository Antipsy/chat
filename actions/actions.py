import requests
from typing import Any, Dict, List, Text
from rasa_sdk import Action, Tracker
from rasa_sdk.forms import FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
class ActionHelloWorld(Action):

     def name(self) -> Text:
         return "validate_form"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         cin = tracker.get_slot("cin")
         datenaissance = tracker.get_slot("datenaissance")
         pension = tracker.get_slot("pension")
         if cin == None & pension == None & datenaissance == None:
            dispatcher.utter_message(response="utter_cin")
         if cin & pension == None & datenaissance == None:
            dispatcher.utter_message(response="utter_pension")
         if cin & pension & datenaissance == None:
            dispatcher.utter_message(response="utter_datenaissance")

         return []

class LoginAction(FormValidationAction):

    def name(self) -> Text:
        return "form_log"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ['cin', 'pension', 'datenaissance']

    def submit(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Get the item ID from the tracker
        cin = tracker.get_slot("cin")
        datenaissance = tracker.get_slot("datenaissance")
        pension = tracker.get_slot("pension")
        data = None
        if cin & pension & datenaissance:
            # Set the API endpoint URL with the item ID
            url = f"http://localhost:8080/User/{cin}/{pension}/{datenaissance}"

            # Send a GET request to the API
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()  # Extract JSON response data
                # Process the data as needed
                dispatcher.utter_message(text=f"Received item: {data}")
            else:
                dispatcher.utter_message(text=f"Failed to retrieve the item with Cin {cin}.")
        else:
            dispatcher.utter_message(text=f"Item CIN not provided.")

        return [data]

class ActionHelloWorld(Action):

     def name(self) -> Text:
         return "getuser"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         cin = tracker.get_slot("AE255393")


         if cin:
             # Set the API endpoint URL with the item ID
             url = "http://localhost:8080/User/{cin}"

             # Send a GET request to the API
             response = requests.get(url)

             if response.status_code == 200:
                 data = response.json()  # Extract JSON response data
                 # Process the data as needed
                 dispatcher.utter_message(text="Received item: {data}")
             else:
                 dispatcher.utter_message(text="Failed to retrieve the item with Cin {cin}.")
         else:
             dispatcher.utter_message(text="Item CIN not provided.")

         return []
